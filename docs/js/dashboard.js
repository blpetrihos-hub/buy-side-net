const LAYER_SHAPE = {
  infrastructure: "square",
  resources: "circle",
  energy: "triangle",
};

const LAYER_LABEL = {
  infrastructure: "Infrastructure",
  resources: "Scarce Natural Resources",
  energy: "Energy",
};

let DATA = null;
let ROWS = null;
let COLORS = { us: "#2f5d73", prc: "#8c3a2b", allied: "#6b7c3c" };
const SHAPE_SWATCH = "#8a9096";
const PLAY_MS = 700;
let map = null;
let layerGroup = null;
let markersById = {};
let activeLayers = { infrastructure: true, resources: true, energy: true };
const timeState = {
  year: null,
  playing: false,
  years: [],
  timer: null,
  ready: false,
};

function $(id) {
  return document.getElementById(id);
}

function selected() {
  return {
    subcategory: $("subcategory").value,
    country: $("country").value,
    evidence: $("evidence").value,
    side: $("side").value,
  };
}

function sideBucket(side) {
  if (side === "us") return "us";
  if (side === "prc") return "prc";
  if (side === "allied" || side === "other") return "allied";
  return "other";
}

function pinColor(row) {
  const b = sideBucket(row.side);
  if (b === "us") return COLORS.us;
  if (b === "prc") return COLORS.prc;
  return COLORS.allied;
}

function isHunt(row) {
  return row.status === "hunt" || row.evidence === "hunt";
}

function rowYear(r) {
  const y = Number(r.year);
  return Number.isFinite(y) ? y : null;
}

function isMappable(r) {
  return r.on_map && r.lat != null && r.lon != null && !isHunt(r);
}

function filterRowsBase() {
  const s = selected();
  return ROWS.filter((r) => {
    if (r.status === "archived") return false;
    if (r.evidence === "exclude") return false;
    if (r.layer === "archived") return false;
    if (isHunt(r)) return false;
    if (!activeLayers[r.layer]) return false;
    if (s.subcategory !== "all" && r.subcategory !== s.subcategory) return false;
    if (s.country !== "all" && (r.country || "(unspecified)") !== s.country) return false;
    if (s.evidence !== "all" && r.evidence !== s.evidence) return false;
    if (s.side !== "all") {
      const b = sideBucket(r.side);
      if (s.side === "us_prc") {
        if (b !== "us" && b !== "prc") return false;
      } else if (s.side === "allied") {
        if (b !== "allied") return false;
      } else if (b !== s.side) return false;
    }
    return true;
  });
}

function filterRows() {
  const rows = filterRowsBase();
  if (timeState.year == null) return rows;
  return rows.filter((r) => {
    const y = rowYear(r);
    return y != null && y <= timeState.year;
  });
}

function yearsFromRows(rows) {
  let min = Infinity;
  let max = -Infinity;
  rows.forEach((r) => {
    if (!isMappable(r)) return;
    const y = rowYear(r);
    if (y == null) return;
    if (y < min) min = y;
    if (y > max) max = y;
  });
  if (!Number.isFinite(min)) return [];
  const out = [];
  for (let y = min; y <= max; y++) out.push(y);
  return out;
}

function syncTimeDomain(baseRows) {
  const years = yearsFromRows(baseRows);
  timeState.years = years;
  if (!years.length) {
    timeState.year = null;
    stopPlay();
    return;
  }
  const minY = years[0];
  const maxY = years[years.length - 1];
  if (!timeState.ready || timeState.year == null) {
    timeState.year = maxY;
    timeState.ready = true;
  } else if (timeState.year < minY) {
    timeState.year = minY;
  } else if (timeState.year > maxY) {
    timeState.year = maxY;
  }
}

function stopPlay() {
  if (timeState.timer != null) {
    clearInterval(timeState.timer);
    timeState.timer = null;
  }
  timeState.playing = false;
  const btn = $("timePlay");
  if (btn) {
    btn.textContent = "Play";
    btn.setAttribute("aria-pressed", "false");
  }
}

function setPlayhead(year, opts) {
  const options = opts || {};
  if (!timeState.years.length) {
    timeState.year = null;
  } else {
    const minY = timeState.years[0];
    const maxY = timeState.years[timeState.years.length - 1];
    timeState.year = Math.max(minY, Math.min(maxY, year));
  }
  if (options.pause) stopPlay();
  if (!options.skipRender) render();
}

function advancePlay() {
  if (!timeState.years.length || timeState.year == null) {
    stopPlay();
    return;
  }
  const maxY = timeState.years[timeState.years.length - 1];
  if (timeState.year >= maxY) {
    stopPlay();
    return;
  }
  setPlayhead(timeState.year + 1);
}

function togglePlay() {
  if (timeState.playing) {
    stopPlay();
    return;
  }
  if (!timeState.years.length) return;
  const minY = timeState.years[0];
  const maxY = timeState.years[timeState.years.length - 1];
  if (timeState.year == null || timeState.year >= maxY) {
    timeState.year = minY;
  }
  timeState.playing = true;
  const btn = $("timePlay");
  if (btn) {
    btn.textContent = "Pause";
    btn.setAttribute("aria-pressed", "true");
  }
  render();
  timeState.timer = setInterval(advancePlay, PLAY_MS);
}

function sparkSvg(seriesUs, seriesPrc, years, playhead) {
  const n = years.length;
  if (!n) return "";
  const w = 280;
  const h = 28;
  const gap = 1;
  const pairW = Math.max(2, (w - gap * (n - 1)) / n);
  const barW = Math.max(1, (pairW - 1) / 2);
  let peak = 1;
  for (let i = 0; i < n; i++) {
    peak = Math.max(peak, seriesUs[i] || 0, seriesPrc[i] || 0);
  }
  const bars = [];
  years.forEach((y, i) => {
    const x0 = i * (pairW + gap);
    const usH = Math.max(0, ((seriesUs[i] || 0) / peak) * (h - 2));
    const prcH = Math.max(0, ((seriesPrc[i] || 0) / peak) * (h - 2));
    bars.push(
      `<rect class="us" x="${x0.toFixed(2)}" y="${(h - usH).toFixed(2)}" width="${barW.toFixed(
        2
      )}" height="${usH.toFixed(2)}"></rect>`
    );
    bars.push(
      `<rect class="prc" x="${(x0 + barW + 1).toFixed(2)}" y="${(h - prcH).toFixed(
        2
      )}" width="${barW.toFixed(2)}" height="${prcH.toFixed(2)}"></rect>`
    );
  });
  let cursor = "";
  const idx = years.indexOf(playhead);
  if (idx >= 0) {
    const x = idx * (pairW + gap) + pairW / 2;
    cursor = `<line class="spark-now" x1="${x.toFixed(2)}" y1="0" x2="${x.toFixed(2)}" y2="${h}"></line>`;
  }
  return (
    `<svg class="time-spark" viewBox="0 0 ${w} ${h}" role="img" aria-label="Observation rate by year, U.S. and PRC">` +
    bars.join("") +
    cursor +
    "</svg>"
  );
}

function updateTimeControls() {
  const bar = $("timeBar");
  const scrubber = $("timeScrubber");
  const label = $("timeYearLabel");
  if (!bar || !scrubber || !label) return;
  const years = timeState.years;
  if (!years.length || timeState.year == null) {
    bar.hidden = true;
    return;
  }
  bar.hidden = false;
  scrubber.min = String(years[0]);
  scrubber.max = String(years[years.length - 1]);
  scrubber.value = String(timeState.year);
  label.textContent = String(timeState.year);
}

function updateRatePanel(baseRows, playhead) {
  const box = $("timeRate");
  if (!box) return;
  if (playhead == null) {
    box.innerHTML = "";
    return;
  }
  const mapped = baseRows.filter(isMappable);
  let newUs = 0;
  let newPrc = 0;
  let usdUs = 0;
  let usdPrc = 0;
  const years = timeState.years;
  const seriesUs = years.map(() => 0);
  const seriesPrc = years.map(() => 0);
  const yearIndex = Object.fromEntries(years.map((y, i) => [y, i]));
  mapped.forEach((r) => {
    const y = rowYear(r);
    if (y == null) return;
    const b = sideBucket(r.side);
    const i = yearIndex[y];
    if (i != null) {
      if (b === "us") seriesUs[i] += 1;
      else if (b === "prc") seriesPrc[i] += 1;
    }
    if (y !== playhead) return;
    if (b === "us") {
      newUs += 1;
      if (r.on_usd_sum && r.value_usd != null) usdUs += r.value_usd;
    } else if (b === "prc") {
      newPrc += 1;
      if (r.on_usd_sum && r.value_usd != null) usdPrc += r.value_usd;
    }
  });
  box.innerHTML =
    `<div class="rate-title">Investment rate · ${playhead}</div>` +
    `<p class="rate-line">New plots: <span class="side-us">U.S. <strong>${newUs}</strong></span> · ` +
    `<span class="side-prc">PRC <strong>${newPrc}</strong></span></p>` +
    `<p class="rate-line">Documented USD: <span class="side-us">U.S. <strong>${fmtMoney(
      usdUs
    )}</strong></span> · ` +
    `<span class="side-prc">PRC <strong>${fmtMoney(usdPrc)}</strong></span></p>` +
    sparkSvg(seriesUs, seriesPrc, years, playhead) +
    '<p class="rate-caveat">Pin counts can reflect source coverage, not capital stock. USD uses documented codebook rows for that year only.</p>';
}

function setupTimeBar() {
  const play = $("timePlay");
  const scrubber = $("timeScrubber");
  if (!play || !scrubber) return;
  play.addEventListener("click", togglePlay);
  scrubber.addEventListener("input", () => {
    setPlayhead(Number(scrubber.value), { pause: true });
  });
}

function fmtPct(gap) {
  if (gap == null || Number.isNaN(gap)) return "—";
  const pct = gap * 100;
  const sign = pct > 0 ? "+" : "";
  return sign + pct.toFixed(1) + "%";
}

function fmtMoney(n) {
  if (n == null || Number.isNaN(n)) return "—";
  const abs = Math.abs(n);
  if (abs >= 1e9) return "$" + (n / 1e9).toFixed(2) + "B";
  if (abs >= 1e6) return "$" + (n / 1e6).toFixed(2) + "M";
  if (abs >= 1e3) return "$" + (n / 1e3).toFixed(2) + "k";
  return "$" + (Number.isInteger(n) ? String(n) : n.toFixed(2));
}

function subLabel(layer, sub) {
  const tax = (DATA && DATA.taxonomy && DATA.taxonomy[layer]) || {};
  const subs = tax.subcategories || {};
  return subs[sub] || sub;
}

function popupHtml(row) {
  const src = row.evidence_url
    ? `<a href="${row.evidence_url}" rel="noopener" target="_blank">source</a>`
    : "no source URL yet";
  const gapBit =
    row.evidence === "paired" && row.gap != null
      ? `<br><span class="popup-gap">Matched gap: ${fmtPct(row.gap)}</span>`
      : "";
  const counterpart =
    row.counterpart_actor
      ? `<br>Counterpart (${row.counterpart_side || "—"}): ${row.counterpart_actor}` +
        (row.counterpart_value_usd != null
          ? ` · ${fmtMoney(row.counterpart_value_usd)}`
          : "")
      : "";
  return (
    `<strong>${row.asset || row.id}</strong><br>` +
    `${LAYER_LABEL[row.layer] || row.layer} · ${subLabel(row.layer, row.subcategory)}<br>` +
    `Side: ${row.side} · ${row.investment_type || "—"}<br>` +
    `Host/counterpart: ${row.counterpart || "—"} · ${row.country || "—"}<br>` +
    `Year: ${row.year || "—"} · Value: ${fmtMoney(row.value_usd)} (${row.currency || ""})` +
    counterpart +
    gapBit +
    `<br>Evidence: ${row.evidence}<br>${src}<br>` +
    `<em>${row.note || ""}</em>`
  );
}

function markerIcon(row) {
  const shape = LAYER_SHAPE[row.layer] || "circle";
  const color = pinColor(row);
  let html;
  if (shape === "triangle") {
    html = `<span class="ch-shape triangle" style="border-bottom-color:${color}"></span>`;
  } else {
    html = `<span class="ch-shape ${shape}" style="background:${color}"></span>`;
  }
  return L.divIcon({
    className: "ch-marker",
    html,
    iconSize: [16, 16],
    iconAnchor: [8, 8],
    popupAnchor: [0, -8],
  });
}

function renderLegend() {
  const shapes = [
    ["square", "Infrastructure"],
    ["circle", "Scarce Natural Resources"],
    ["triangle", "Energy"],
  ];
  const sides = [
    ["us", "U.S."],
    ["prc", "PRC"],
    ["allied", "Allied / other"],
  ];
  const shapeHtml = shapes
    .map(([sh, label]) => {
      if (sh === "triangle") {
        return `<span class="legend-item"><span class="legend-swatch triangle" style="border-bottom-color:${SHAPE_SWATCH}"></span>${label}</span>`;
      }
      return `<span class="legend-item"><span class="legend-swatch ${sh}" style="background:${SHAPE_SWATCH}"></span>${label}</span>`;
    })
    .join("");
  const sideHtml = sides
    .map(
      ([k, label]) =>
        `<span class="legend-item"><span class="legend-swatch circle" style="background:${COLORS[k]}"></span>${label}</span>`
    )
    .join("");
  $("mapLegend").innerHTML = shapeHtml + "<span>·</span>" + sideHtml;
}

function renderLayerToggles() {
  const box = $("layerToggles");
  box.innerHTML = ["infrastructure", "resources", "energy"]
    .map(
      (k) =>
        `<label><input type="checkbox" data-layer="${k}" ${
          activeLayers[k] ? "checked" : ""
        }> ${LAYER_LABEL[k]}</label>`
    )
    .join("");
  box.querySelectorAll("input").forEach((input) => {
    input.addEventListener("change", () => {
      activeLayers[input.getAttribute("data-layer")] = input.checked;
      fillSubcategorySelect();
      render();
    });
  });
}

function fillSubcategorySelect() {
  const sel = $("subcategory");
  const current = sel.value;
  const opts = [];
  ["infrastructure", "resources", "energy"].forEach((layer) => {
    if (!activeLayers[layer]) return;
    const tax = (DATA.taxonomy && DATA.taxonomy[layer]) || {};
    const subs = tax.subcategories || {};
    Object.keys(subs).forEach((sk) => {
      opts.push({ value: sk, label: `${LAYER_LABEL[layer]} · ${subs[sk]}` });
    });
  });
  sel.innerHTML =
    '<option value="all">All subcategories</option>' +
    opts.map((o) => `<option value="${o.value}">${o.label}</option>`).join("");
  if ([...sel.options].some((o) => o.value === current)) sel.value = current;
}

function fillCountrySelect() {
  const sel = $("country");
  const current = sel.value;
  const allowed = new Set((DATA.geography && DATA.geography.countries) || []);
  const countries = Array.from(
    new Set(
      ROWS.filter((r) => r.status !== "archived" && r.country && allowed.has(r.country)).map(
        (r) => r.country
      )
    )
  ).sort();
  sel.innerHTML =
    '<option value="all">All countries</option>' +
    countries.map((c) => `<option value="${c}">${c}</option>`).join("");
  if ([...sel.options].some((o) => o.value === current)) sel.value = current;
}

function renderLayerReadouts(rows) {
  const layers = ["infrastructure", "resources", "energy"];
  const html = layers
    .filter((l) => activeLayers[l])
    .map((layer) => {
      const subset = rows.filter((r) => r.layer === layer && r.on_readouts);
      const counts = { us: 0, prc: 0, allied: 0 };
      const usd = { us: 0, prc: 0, allied: 0 };
      const usdN = { us: 0, prc: 0, allied: 0 };
      subset.forEach((r) => {
        const b = sideBucket(r.side);
        if (counts[b] == null) return;
        counts[b] += 1;
        if (r.on_usd_sum && r.value_usd != null) {
          usd[b] += r.value_usd;
          usdN[b] += 1;
        }
      });
      const n = counts.us + counts.prc + counts.allied;
      return (
        `<div class="layer-card"><strong>${LAYER_LABEL[layer]}</strong>` +
        `<p class="layer-line"><span class="side-us">U.S. ${counts.us}</span> · ` +
        `<span class="side-prc">PRC ${counts.prc}</span> · ` +
        `<span class="side-allied">Allied/other ${counts.allied}</span> · n = ${n}</p>` +
        `<p class="layer-line">USD: <span class="side-us">U.S. ${fmtMoney(usd.us)} (n=${usdN.us})</span> · ` +
        `<span class="side-prc">PRC ${fmtMoney(usd.prc)} (n=${usdN.prc})</span> · ` +
        `<span class="side-allied">Allied ${fmtMoney(usd.allied)} (n=${usdN.allied})</span></p></div>`
      );
    })
    .join("");
  $("layerReadouts").innerHTML = html || '<p class="empty">No active layer readouts.</p>';
}

function renderCountryReadouts(rows) {
  const bucket = {};
  rows
    .filter((r) => r.on_readouts)
    .forEach((r) => {
      const c = r.country || "(unspecified)";
      if (!bucket[c]) bucket[c] = { us: 0, prc: 0, allied: 0, usdUs: 0, usdPrc: 0, nUs: 0, nPrc: 0 };
      const b = sideBucket(r.side);
      if (bucket[c][b] != null) bucket[c][b] += 1;
      if (r.on_usd_sum && r.value_usd != null) {
        if (b === "us") {
          bucket[c].usdUs += r.value_usd;
          bucket[c].nUs += 1;
        }
        if (b === "prc") {
          bucket[c].usdPrc += r.value_usd;
          bucket[c].nPrc += 1;
        }
      }
    });
  const countries = Object.keys(bucket).sort();
  if (!countries.length) {
    $("countryReadouts").innerHTML = '<p class="empty">No country lines yet.</p>';
    return;
  }
  $("countryReadouts").innerHTML = countries
    .map((c) => {
      const x = bucket[c];
      return (
        `<div class="country-block"><strong>${c}</strong>` +
        `<p class="layer-line"><span class="side-us">U.S. ${x.us}</span> · ` +
        `<span class="side-prc">PRC ${x.prc}</span> · allied/other ${x.allied}</p>` +
        `<p class="layer-line">USD: <span class="side-us">${fmtMoney(x.usdUs)} (n=${x.nUs})</span> · ` +
        `<span class="side-prc">${fmtMoney(x.usdPrc)} (n=${x.nPrc})</span></p></div>`
      );
    })
    .join("");
}

function renderGapReadouts(rows) {
  const paired = rows.filter((r) => r.evidence === "paired" && r.gap != null);
  if (!paired.length) {
    $("gapReadouts").innerHTML = '<p class="empty">No matched pairs in the current filter.</p>';
    return;
  }
  $("gapReadouts").innerHTML = paired
    .map((r) => {
      return (
        `<div class="country-block"><strong>${r.id}</strong>` +
        `<p class="layer-line">${LAYER_LABEL[r.layer] || r.layer} · ${r.country || "—"} · gap ${fmtPct(
          r.gap
        )}</p></div>`
      );
    })
    .join("");
}

function renderLists(rows) {
  const show = rows.slice().sort((a, b) => (a.id < b.id ? -1 : 1));
  $("listRows").innerHTML = show.length
    ? show
        .map((row) => {
          const gapBit = row.gap != null ? ` · ${fmtPct(row.gap)}` : "";
          return (
            `<li><button type="button" data-id="${row.id}">` +
            `<strong>${row.id}</strong>` +
            `<span class="meta">${LAYER_LABEL[row.layer] || row.layer} · ${row.side} · ${
              row.evidence
            }${gapBit}` +
            (row.country ? ` · ${row.country}` : "") +
            `</span></button></li>`
          );
        })
        .join("")
    : '<li class="empty">None with current filters.</li>';

  document.querySelectorAll(".side-list button").forEach((btn) => {
    btn.addEventListener("click", () => focusRow(btn.getAttribute("data-id")));
  });
}

function focusRow(id) {
  const row = ROWS.find((r) => r.id === id);
  if (!row) return;
  if (markersById[id]) {
    markersById[id].openPopup();
    map.setView(markersById[id].getLatLng(), Math.max(map.getZoom(), 5));
  } else {
    $("note").textContent =
      row.id +
      " has no map pin (missing coordinates, blank country, or outside Latin America & the Caribbean). " +
      (row.note || "");
  }
}

const FS_EXPAND =
  '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3H3v5M16 3h5v5M8 21H3v-5M16 21h5v-5"/></svg>';
const FS_COLLAPSE =
  '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3v5H3M16 3v5h5M8 21v-5H3M16 21v-5h5"/></svg>';

function mapIsFullscreen(el) {
  const fs = document.fullscreenElement || document.webkitFullscreenElement;
  return fs === el || el.classList.contains("map-windowed-full");
}

function updateFullscreenButton(el, btn) {
  const on = mapIsFullscreen(el);
  btn.innerHTML = on ? FS_COLLAPSE : FS_EXPAND;
  btn.title = on ? "Exit full screen" : "Full screen";
  btn.setAttribute("aria-label", btn.title);
  btn.setAttribute("aria-pressed", on ? "true" : "false");
}

function enterMapFullscreen(el) {
  const req = el.requestFullscreen || el.webkitRequestFullscreen;
  if (req) {
    const p = req.call(el);
    if (p && typeof p.catch === "function") {
      p.catch(() => el.classList.add("map-windowed-full"));
    }
    return;
  }
  el.classList.add("map-windowed-full");
}

function exitMapFullscreen(el) {
  const cur = document.fullscreenElement || document.webkitFullscreenElement;
  if (cur === el) {
    const exit = document.exitFullscreen || document.webkitExitFullscreen;
    if (exit) exit.call(document);
    return;
  }
  el.classList.remove("map-windowed-full");
}

function addFullscreenControl(leafletMap) {
  const Fullscreen = L.Control.extend({
    options: { position: "topleft" },
    onAdd: function () {
      const bar = L.DomUtil.create("div", "leaflet-bar leaflet-control");
      const btn = L.DomUtil.create("a", "map-fs-btn", bar);
      btn.href = "#";
      btn.innerHTML = FS_EXPAND;
      btn.title = "Full screen";
      btn.setAttribute("role", "button");
      btn.setAttribute("aria-label", "Full screen");
      btn.setAttribute("aria-pressed", "false");
      L.DomEvent.disableClickPropagation(bar);
      L.DomEvent.disableScrollPropagation(bar);
      L.DomEvent.on(btn, "click", L.DomEvent.stop).on(btn, "click", function () {
        const el = leafletMap.getContainer();
        if (mapIsFullscreen(el)) exitMapFullscreen(el);
        else enterMapFullscreen(el);
      });
      const sync = function () {
        updateFullscreenButton(leafletMap.getContainer(), btn);
        setTimeout(function () {
          leafletMap.invalidateSize();
        }, 80);
      };
      document.addEventListener("fullscreenchange", sync);
      document.addEventListener("webkitfullscreenchange", sync);
      window.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && leafletMap.getContainer().classList.contains("map-windowed-full")) {
          exitMapFullscreen(leafletMap.getContainer());
          sync();
        }
      });
      const mo = new MutationObserver(sync);
      mo.observe(leafletMap.getContainer(), { attributes: true, attributeFilter: ["class"] });
      return bar;
    },
  });
  leafletMap.addControl(new Fullscreen());
}

const CARTO_BASEMAP_KEY = "cb1_32m3_1_44dc754e68375e8ab5208497";

let countBox = null;

function addCountControl(m) {
  const Count = L.Control.extend({
    options: { position: "topleft" },
    onAdd() {
      const div = L.DomUtil.create("div", "leaflet-control count-box");
      div.setAttribute("aria-live", "polite");
      L.DomEvent.disableClickPropagation(div);
      countBox = div;
      return div;
    },
  });
  new Count().addTo(m);
}

function updateCountBox(rows) {
  if (!countBox) return;
  let us = 0;
  let prc = 0;
  rows.forEach((r) => {
    if (!isMappable(r)) return;
    const b = sideBucket(r.side);
    if (b === "us") us += 1;
    else if (b === "prc") prc += 1;
  });
  const asOf =
    timeState.year != null
      ? `As of ${timeState.year} · updates with filters`
      : "Updates with filters";
  countBox.innerHTML =
    '<div class="count-title">LatAm observations</div>' +
    `<div class="count-row"><span class="count-swatch" style="background:${COLORS.us}"></span>U.S. <strong>${us.toLocaleString()}</strong></div>` +
    `<div class="count-row"><span class="count-swatch" style="background:${COLORS.prc}"></span>PRC <strong>${prc.toLocaleString()}</strong></div>` +
    `<div class="count-sub">${asOf}</div>`;
}

function renderMap(rows) {
  if (!map) {
    // Centered on Latin America & the Caribbean
    map = L.map("map", { scrollWheelZoom: true, zoomControl: false }).setView([-15, -60], 3.5);
    addCountControl(map);
    L.control.zoom({ position: "topleft" }).addTo(map);
    const tiles =
      "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png?key=" +
      encodeURIComponent(CARTO_BASEMAP_KEY);
    L.tileLayer(tiles, {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: "abcd",
      maxZoom: 20,
    }).addTo(map);
    addFullscreenControl(map);
  }
  if (layerGroup) layerGroup.remove();
  markersById = {};
  layerGroup = L.layerGroup();
  rows.forEach((r) => {
    if (isHunt(r)) return;
    if (r.lat == null || r.lon == null) return;
    if (!r.on_map) return;
    const m = L.marker([r.lat, r.lon], { icon: markerIcon(r) });
    m.bindPopup(popupHtml(r));
    layerGroup.addLayer(m);
    markersById[r.id] = m;
  });
  layerGroup.addTo(map);
  updateCountBox(rows);
}

function setupOverlay() {
  const toggle = $("panelToggle");
  const overlay = $("filterOverlay");
  const close = $("overlayClose");
  function open() {
    overlay.hidden = false;
    toggle.setAttribute("aria-expanded", "true");
  }
  function shut() {
    overlay.hidden = true;
    toggle.setAttribute("aria-expanded", "false");
  }
  toggle.addEventListener("click", () => {
    if (overlay.hidden) open();
    else shut();
  });
  close.addEventListener("click", shut);
  open();
}

function render() {
  if (!DATA || !ROWS) return;
  const baseRows = filterRowsBase();
  syncTimeDomain(baseRows);
  updateTimeControls();
  updateRatePanel(baseRows, timeState.year);
  const rows = filterRows();
  renderLayerReadouts(rows);
  renderCountryReadouts(rows);
  renderGapReadouts(rows);
  renderLists(rows);
  renderMap(rows);
  if (map) setTimeout(() => map.invalidateSize(), 80);
  const counts = DATA.meta.counts || {};
  const yearBit =
    timeState.year != null ? ` Cumulative through ${timeState.year}.` : "";
  $("note").textContent =
    `${rows.length} row(s) with current filters.${yearBit} ` +
    `${counts.on_map || 0} mapped across the codebook. ` +
    `${counts.archived || 0} archived (out of region or legacy lanes). ` +
    `Descriptive only — no recommendations.`;
}

async function boot() {
  const [dash, rows] = await Promise.all([
    fetch("data/dashboard.json").then((r) => r.json()),
    fetch("data/observations.json").then((r) => r.json()),
  ]);
  DATA = dash;
  ROWS = rows;
  if (DATA.colors) COLORS = Object.assign(COLORS, DATA.colors);
  if (DATA.caption) $("caption").textContent = DATA.caption;
  renderLegend();
  renderLayerToggles();
  fillSubcategorySelect();
  fillCountrySelect();
  setupOverlay();
  setupTimeBar();
  ["subcategory", "country", "evidence", "side"].forEach((id) =>
    $(id).addEventListener("change", render)
  );
  render();
  const focus = new URLSearchParams(window.location.search).get("focus");
  if (focus) focusRow(focus);
}

boot().catch((err) => {
  $("note").textContent =
    "Could not load the data files. Rebuild with process/build_site_data.py.";
  console.error(err);
});
