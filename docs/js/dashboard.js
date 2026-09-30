const COLORS = {
  prc_cheaper: "#8c3a2b",
  us_cheaper: "#2f5d73",
  tie: "#1b3a4b",
  unscored: "#8a9096",
};

const LANE_LABEL = {
  commanding_heights: "Commanding heights",
  niobium: "Niobium",
  ai_chips: "AI chips",
  icbc_finance: "ICBC finance",
};

let DATA = null;
let ROWS = null;
let map = null;
let layer = null;
let markersById = {};

function $(id) {
  return document.getElementById(id);
}

function selected() {
  return {
    lane: $("lane").value,
    country: $("country").value,
    evidence: $("evidence").value,
  };
}

function filterRows() {
  const s = selected();
  return ROWS.filter((r) => {
    if (s.lane !== "all" && r.lane !== s.lane) return false;
    if (s.country !== "all" && (r.country || "(unspecified)") !== s.country) return false;
    if (s.evidence !== "all" && r.evidence !== s.evidence) return false;
    return true;
  });
}

function fmtPct(gap) {
  if (gap == null || Number.isNaN(gap)) return "—";
  const pct = gap * 100;
  const sign = pct > 0 ? "+" : "";
  return sign + pct.toFixed(1) + "%";
}

function fmtMoney(n, unit) {
  if (n == null || Number.isNaN(n)) return "—";
  const abs = Math.abs(n);
  let s;
  if (abs >= 1e9) s = (n / 1e9).toFixed(2) + "B";
  else if (abs >= 1e6) s = (n / 1e6).toFixed(2) + "M";
  else if (abs >= 1e3) s = (n / 1e3).toFixed(2) + "k";
  else s = Number.isInteger(n) ? String(n) : n.toFixed(4).replace(/\.?0+$/, "");
  return unit ? s + " " + unit : s;
}

function pinColor(row) {
  if (!row.on_scoreboard || row.gap == null) return COLORS.unscored;
  if (row.gap > 0) return COLORS.prc_cheaper;
  if (row.gap < 0) return COLORS.us_cheaper;
  return COLORS.tie;
}

function popupHtml(row) {
  const src = row.evidence_url
    ? `<a href="${row.evidence_url}" rel="noopener" target="_blank">source</a>`
    : "no source URL yet";
  return (
    `<strong>${row.spec || row.spec_class || row.id}</strong><br>` +
    `Buyer: ${row.buyer || "—"}<br>` +
    `U.S./allied: ${row.seller_us || "—"} · PRC: ${row.seller_prc || "—"}<br>` +
    `Price year: ${row.price_year || "—"} · Unit: ${row.unit || "—"} · ${row.currency || ""}<br>` +
    `Original: U.S. ${fmtMoney(row.us_price)} / PRC ${fmtMoney(row.prc_price)}<br>` +
    `USD: ${fmtMoney(row.us_price_usd)} / ${fmtMoney(row.prc_price_usd)}<br>` +
    `<span class="popup-gap">Gap: ${fmtPct(row.gap)}</span><br>` +
    `Evidence: ${row.evidence}` +
    (row.on_scoreboard ? " (on median)" : " (off median)") +
    `<br>${src}<br>` +
    `<em>${row.note || ""}</em>`
  );
}

function renderScoreboards() {
  const goods = (DATA.scoreboards && DATA.scoreboards.goods) || [];
  const finance = (DATA.scoreboards && DATA.scoreboards.finance) || [];
  const counts = (DATA.meta && DATA.meta.counts) || {};

  if (!goods.length) {
    $("scoreGoods").innerHTML = '<p class="empty">No scored goods pairs yet.</p>';
  } else {
    $("scoreGoods").innerHTML = goods
      .map(
        (g) =>
          `<div class="score goods"><b>${fmtPct(g.median_gap)}</b>` +
          `<span>${LANE_LABEL[g.lane] || g.lane} · ${g.spec_class}</span>` +
          `<small>n = ${g.n}</small></div>`
      )
      .join("");
  }

  if (!finance.length) {
    $("scoreFinance").innerHTML = '<p class="empty">No scored finance pairs yet.</p>';
  } else {
    $("scoreFinance").innerHTML = finance
      .map(
        (g) =>
          `<div class="score finance"><b>${fmtPct(g.median_gap)}</b>` +
          `<span>${LANE_LABEL[g.lane] || g.lane} · ${g.spec_class}</span>` +
          `<small>n = ${g.n}</small></div>`
      )
      .join("");
  }

  const keys = [
    ["paired", "Paired"],
    ["proxy", "Proxy"],
    ["one_sided", "One-sided"],
    ["hunt", "Hunt"],
    ["scored", "Scored"],
  ];
  $("scoreCounts").innerHTML = keys
    .map(
      ([k, label]) =>
        `<div class="score count"><b>${counts[k] != null ? counts[k] : 0}</b><span>${label}</span></div>`
    )
    .join("");
}

function renderCountryStrip(rows) {
  // Rebuild from filtered scored rows so controls matter; never blend lanes.
  const bucket = {};
  rows
    .filter((r) => r.on_scoreboard && r.gap != null)
    .forEach((r) => {
      const c = r.country || "(unspecified)";
      if (!bucket[c]) bucket[c] = {};
      if (!bucket[c][r.lane]) bucket[c][r.lane] = [];
      bucket[c][r.lane].push(r.gap);
    });
  const countries = Object.keys(bucket).sort();
  if (!countries.length) {
    $("countryLines").innerHTML = '<p class="empty">No scored country lines yet.</p>';
    return;
  }
  const laneOrder = ["commanding_heights", "niobium", "ai_chips", "icbc_finance"];
  $("countryLines").innerHTML = countries
    .map((c) => {
      const lines = laneOrder
        .filter((lane) => bucket[c][lane] && bucket[c][lane].length)
        .map((lane) => {
          const vals = bucket[c][lane].slice().sort((a, b) => a - b);
          const mid = vals[Math.floor(vals.length / 2)];
          return `<p class="country-line">${LANE_LABEL[lane] || lane}: median gap ${fmtPct(mid)} (n = ${vals.length})</p>`;
        })
        .join("");
      return `<div class="country-block"><strong>${c}</strong>${lines}</div>`;
    })
    .join("");
}

function listItem(row) {
  const gapBit = row.gap != null ? ` · ${fmtPct(row.gap)}` : "";
  return (
    `<li><button type="button" data-id="${row.id}">` +
    `<strong>${row.id}</strong>` +
    `<span class="meta">${LANE_LABEL[row.lane] || row.lane} · ${row.evidence}${gapBit}` +
    (row.country ? ` · ${row.country}` : "") +
    `</span></button></li>`
  );
}

function renderLists(rows) {
  const scored = rows.filter((r) => r.on_scoreboard);
  const proxy = rows.filter((r) => r.evidence === "proxy" || r.evidence === "one_sided");
  const hunt = rows.filter((r) => r.evidence === "hunt");
  $("listScored").innerHTML = scored.length
    ? scored.map(listItem).join("")
    : '<li class="empty">None yet.</li>';
  $("listProxy").innerHTML = proxy.length
    ? proxy.map(listItem).join("")
    : '<li class="empty">None yet.</li>';
  $("listHunt").innerHTML = hunt.length
    ? hunt.map(listItem).join("")
    : '<li class="empty">None yet.</li>';

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
      " has no coordinates. " +
      (row.note || "It stays on the list until a project or HQ is named.");
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

function renderMap(rows) {
  if (!map) {
    map = L.map("map").setView([-15, -50], 3);
    L.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png", {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: "abcd",
      maxZoom: 20,
    }).addTo(map);
    addFullscreenControl(map);
  }
  if (layer) layer.remove();
  markersById = {};
  layer = L.layerGroup();
  rows.forEach((r) => {
    if (r.lat == null || r.lon == null) return;
    const color = pinColor(r);
    const m = L.circleMarker([r.lat, r.lon], {
      radius: 8,
      color: color,
      fillColor: color,
      fillOpacity: 0.7,
      weight: 1,
    });
    m.bindPopup(popupHtml(r));
    layer.addLayer(m);
    markersById[r.id] = m;
  });
  layer.addTo(map);
}

function fillCountrySelect() {
  const sel = $("country");
  const current = sel.value;
  const countries = Array.from(
    new Set(ROWS.map((r) => r.country || "(unspecified)").filter(Boolean))
  ).sort();
  sel.innerHTML =
    '<option value="all">All countries</option>' +
    countries.map((c) => `<option value="${c}">${c}</option>`).join("");
  if ([...sel.options].some((o) => o.value === current)) sel.value = current;
}

function render() {
  if (!DATA || !ROWS) return;
  const rows = filterRows();
  renderScoreboards();
  renderCountryStrip(rows);
  renderLists(rows);
  renderMap(rows);
  if (map) setTimeout(() => map.invalidateSize(), 80);
  const counts = DATA.meta.counts || {};
  $("note").textContent =
    `${rows.length} row(s) with current filters. ` +
    `${counts.scored || 0} scored on the median across the full codebook. ` +
    `A lower matched PRC buy-side price is the asymmetry.`;
}

async function boot() {
  const [dash, rows] = await Promise.all([
    fetch("data/dashboard.json").then((r) => r.json()),
    fetch("data/observations.json").then((r) => r.json()),
  ]);
  DATA = dash;
  ROWS = rows;
  fillCountrySelect();
  ["lane", "country", "evidence"].forEach((id) => $(id).addEventListener("change", render));
  render();
}

boot().catch((err) => {
  $("note").textContent = "Could not load the data files. Rebuild with process/build_site_data.py.";
  console.error(err);
});
