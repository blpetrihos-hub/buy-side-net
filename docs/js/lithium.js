"use strict";

const SIDE_COLORS = { us: "#2f5d73", prc: "#8c3a2b", allied: "#6b7c3c" };
const SIDE_LABEL = { us: "U.S.", prc: "PRC", allied: "Allied / other" };
const SIDE_ORDER = { prc: 0, us: 1, allied: 2 };

const LAYER_LABEL = {
  infrastructure: "Infrastructure",
  resources: "Scarce Natural Resources",
  energy: "Energy",
};
const LAYER_SHAPE = { infrastructure: "square", resources: "circle", energy: "triangle" };

const SUB_LABEL = {
  port_ownership: "Port ownership and concessions",
  port_cranes: "Port cranes and terminal equipment",
  rail: "Rail",
  bridges_roads: "Bridges and roads",
  engineering_epc: "Engineering, design, and EPC firms",
  lithium: "Lithium",
  solar: "Solar",
  power_plants_grid: "Power plants and grid",
  other_renewables: "Other renewables",
};

const GOLD = "#c9a24a";

// China is stored at lon - 360 so every route crosses the Pacific on a
// Pacific-centered map instead of wrapping over Africa.
function cn(lat, lon) {
  return [lat, lon - 360];
}

const HUBS = {
  cauchari: {
    label: "Cauchari-Olaroz",
    latlng: [-23.45, -66.75],
    tip: "Minera Exar brine operation, Jujuy. Ganfeng 46.7%, Lithium Argentina 44.8%, JEMSE 8.5%.",
  },
  chile_ports: {
    label: "Northern Chile ports",
    latlng: [-23.4, -70.42],
    labelLeft: true,
    tip: "Antofagasta and Mejillones. Since February 2025 Exar trucks part of its output over Paso de Jama to ship to China across the Pacific.",
  },
  buenos_aires: {
    label: "Port of Buenos Aires",
    latlng: [-34.6, -58.37],
    tip: "Exar's main export gateway: more than 28,000 t of lithium carbonate left through Buenos Aires in 2024.",
  },
  cn_port: {
    label: "Chinese entry port (illustrative)",
    latlng: cn(31.23, 121.47),
    tip: "Shown at Shanghai. The specific Chinese port of entry is not disclosed; Chinese-operated ports receive the cargo.",
  },
  xinyu: {
    label: "Xinyu, Jiangxi (Ganfeng)",
    latlng: cn(27.82, 114.92),
    labelLeft: true,
    tip: "Ganfeng headquarters and its Basic Lithium and Xinyu Ganfeng refining plants.",
  },
  shenzhen: {
    label: "Shenzhen (BYD)",
    latlng: cn(22.69, 114.35),
    labelLeft: true,
    tip: "BYD headquarters. Chinese manufacturers make 98% of the world's LFP cathodes.",
  },
  camacari: {
    label: "Camaçari, Bahia (BYD)",
    latlng: [-12.7, -38.32],
    tip: "BYD's Camaçari EV complex on the former Ford site, inaugurated October 2025: its largest plant outside China.",
  },
};

const STEPS = [
  {
    n: 1,
    kicker: "Mining",
    title: "Cauchari-Olaroz",
    layer: "resources",
    color: "#2a8c86",
    body:
      "Chinese firm Ganfeng is the largest owner of the Argentine Cauchari-Olaroz brine operation, which produced about 34,100 tons of lithium carbonate in 2025. The region it sits in, the Lithium Triangle, provides about a third of global supply.",
    stats: [
      { v: "46.7%", l: "Ganfeng stake, the largest" },
      { v: "34,100 t", l: "lithium carbonate, 2025" },
      { v: "~1/3", l: "of global supply from the Lithium Triangle" },
    ],
    note: "Pins are lithium plots in Argentina, Chile, and Bolivia. PRC plots are drawn strong and linked to the hub; U.S. and allied plots are faded for contrast.",
    sources: [
      {
        label: "Lithium Argentina, FY2025 results",
        url: "https://investors.lithium-argentina.com/news-releases/news-release-details/lithium-argentina-reports-fourth-quarter-and-full-year-2025",
      },
    ],
    hubs: ["cauchari"],
    flows: [],
    pins: { hub: "cauchari", dir: "in", match: { sub: ["lithium"], country: ["Argentina", "Chile", "Bolivia"] } },
  },
  {
    n: 2,
    kicker: "Refinement",
    title: "Xinyu",
    layer: "infrastructure",
    color: "#4b5d9c",
    body:
      "The same company, Ganfeng, imports the material to Xinyu, Jiangxi, through Chinese-operated ports, where it is refined. China's refining share is 75% and rising year over year.",
    stats: [
      { v: "75%", l: "China's share of lithium refining" },
      { v: "530 km", l: "by road to Chile's Pacific ports" },
    ],
    note: "Since February 2025 Exar trucks part of its output over Paso de Jama to northern Chilean ports for the Pacific crossing; the rest still leaves through Buenos Aires (dashed). The Chinese entry port is shown at Shanghai for illustration.",
    sources: [
      { label: "EXAR, March 2025", url: "https://www.exar.com.ar/exar-comenzara-a-exportar-desde-el-norte-de-chile-pacifico/" },
      { label: "Ganfeng annual report", url: "https://www.hkexnews.hk/listedco/listconews/sehk/2019/0424/ltn201904241477.pdf" },
    ],
    hubs: ["cauchari", "chile_ports", "buenos_aires", "cn_port", "xinyu"],
    flows: [
      { from: "cauchari", to: "chile_ports", bend: 0.3, label: "Trucked over Paso de Jama to Antofagasta and Mejillones" },
      { from: "chile_ports", to: "cn_port", bend: 0.1, label: "Across the Pacific to China" },
      { from: "cn_port", to: "xinyu", bend: 0.25, label: "Inland to Ganfeng's refineries in Xinyu" },
      { from: "cauchari", to: "buenos_aires", bend: -0.2, alt: true, label: "Main 2024 route: more than 28,000 t exported via Buenos Aires" },
    ],
  },
  {
    n: 3,
    kicker: "Export/Manufacturing",
    title: "BYD Company",
    layer: "energy",
    color: "#c2571a",
    body:
      "BYD and other Chinese domestic manufacturers make 98% of the world's LFP (lithium iron phosphate) cathodes, the key component of lithium-ion cells, which China manufactures 80% of.",
    stats: [
      { v: "98%", l: "of LFP cathodes made in China" },
      { v: "80%", l: "of lithium-ion cells made in China" },
    ],
    note: "The chain loops back: BYD opened its Camaçari EV complex in Brazil in October 2025 and supplies grid batteries across Chile and Brazil. Pins are energy plots that name BYD.",
    sources: [],
    hubs: ["xinyu", "shenzhen", "camacari"],
    flows: [
      { from: "xinyu", to: "shenzhen", bend: 0.3, label: "Refined lithium to BYD cathode and cell lines" },
      { from: "shenzhen", to: "camacari", bend: 0.14, label: "BYD builds back into Latin America: Camaçari EV complex (October 2025)" },
    ],
    pins: { hub: "shenzhen", dir: "out", match: { layer: ["energy"], head: /\bbyd\b/i } },
  },
];

const STEP_BY_N = Object.fromEntries(STEPS.map((s) => [s.n, s]));

const CARTO_BASEMAP_KEY = "cb1_32m3_1_44dc754e68375e8ab5208497";

let ROW_BY_ID = {};
let map = null;
let webLayer = null;
const state = { on: new Set(), fresh: null, plot: null };

function $(id) {
  return document.getElementById(id);
}

function esc(s) {
  return String(s == null ? "" : s).replace(
    /[&<>"']/g,
    (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]
  );
}

function sideBucket(side) {
  if (side === "us") return "us";
  if (side === "prc") return "prc";
  return "allied";
}

function fmtMoney(n) {
  if (n == null || Number.isNaN(n)) return "";
  const abs = Math.abs(n);
  if (abs >= 1e9) return "$" + (n / 1e9).toFixed(2) + "B";
  if (abs >= 1e6) return "$" + (n / 1e6).toFixed(1) + "M";
  if (abs >= 1e3) return "$" + (n / 1e3).toFixed(0) + "k";
  return "$" + Math.round(n);
}

function isPlot(r) {
  return (
    r.status === "active" &&
    r.evidence !== "exclude" &&
    r.layer !== "archived" &&
    r.on_map &&
    r.lat != null &&
    r.lon != null
  );
}

function matchRow(m, r) {
  if (m.layer && !m.layer.includes(r.layer)) return false;
  if (m.sub && !m.sub.includes(r.subcategory)) return false;
  if (m.country && !m.country.includes(r.country)) return false;
  if (m.head) {
    const head = [r.id, r.asset, r.counterpart, r.counterpart_actor].filter(Boolean).join(" ");
    if (!m.head.test(head)) return false;
  }
  return true;
}

function indexRows(rows) {
  const plots = rows.filter(isPlot);
  STEPS.forEach((step) => {
    step.rows = [];
    if (!step.pins) return;
    step.rows = plots
      .filter((r) => matchRow(step.pins.match, r))
      .sort(
        (a, b) =>
          SIDE_ORDER[sideBucket(a.side)] - SIDE_ORDER[sideBucket(b.side)] ||
          (b.value_usd || 0) - (a.value_usd || 0)
      );
  });
}

function activeSteps() {
  return STEPS.filter((s) => state.on.has(s.n));
}

function isAchieved() {
  return state.on.size === STEPS.length;
}

function plotMeta(r) {
  return [r.country, SIDE_LABEL[sideBucket(r.side)], r.year, fmtMoney(r.value_usd), r.evidence]
    .filter(Boolean)
    .join(" · ");
}

// ---------- Map geometry ----------

// Quadratic arc drawn in zoom-0 Web Mercator pixels so the curve and its
// arrow angle stay the same at every zoom level.
function arc(fromLatLng, toLatLng, bend) {
  const p0 = map.project(L.latLng(fromLatLng), 0);
  const p2 = map.project(L.latLng(toLatLng), 0);
  const dx = p2.x - p0.x;
  const dy = p2.y - p0.y;
  const c = L.point((p0.x + p2.x) / 2 - dy * bend, (p0.y + p2.y) / 2 + dx * bend);
  const at = (t) =>
    L.point(
      (1 - t) * (1 - t) * p0.x + 2 * (1 - t) * t * c.x + t * t * p2.x,
      (1 - t) * (1 - t) * p0.y + 2 * (1 - t) * t * c.y + t * t * p2.y
    );
  const latlngs = [];
  for (let i = 0; i <= 48; i++) latlngs.push(map.unproject(at(i / 48), 0));
  const t = 0.55;
  const tx = 2 * (1 - t) * (c.x - p0.x) + 2 * t * (p2.x - c.x);
  const ty = 2 * (1 - t) * (c.y - p0.y) + 2 * t * (p2.y - c.y);
  return {
    latlngs,
    mid: map.unproject(at(t), 0),
    angle: (Math.atan2(ty, tx) * 180) / Math.PI,
    length: Math.hypot(dx, dy),
  };
}

function arrowIcon(color, angle, size) {
  const s = size;
  return L.divIcon({
    className: "flow-arrow",
    html:
      `<svg width="${s}" height="${s}" viewBox="-6 -6 12 12" style="transform:rotate(${angle.toFixed(1)}deg)">` +
      `<path d="M6,0 L-5,-4.6 L-2.6,0 L-5,4.6 Z" fill="${color}"/></svg>`,
    iconSize: [s, s],
    iconAnchor: [s / 2, s / 2],
  });
}

function pinIcon(row, picked) {
  const color = SIDE_COLORS[sideBucket(row.side)];
  const shape = LAYER_SHAPE[row.layer] || "circle";
  const html =
    shape === "triangle"
      ? `<span class="ch-shape triangle" style="border-bottom-color:${color}"></span>`
      : `<span class="ch-shape ${shape}" style="background:${color}"></span>`;
  const s = picked ? 22 : 16;
  return L.divIcon({
    className: "ch-marker li-pin" + (picked ? " picked" : ""),
    html,
    iconSize: [s, s],
    iconAnchor: [s / 2, s / 2],
  });
}

function hubIcon(hub, colors) {
  const bar = colors.map((c) => `<span style="background:${c}"></span>`).join("");
  return L.divIcon({
    className: "hub-icon" + (hub.labelLeft ? " label-left" : ""),
    html: `<span class="hub-square"></span><span class="hub-label">${esc(hub.label)}<span class="hub-bar">${bar}</span></span>`,
    iconSize: [14, 14],
    iconAnchor: [7, 7],
  });
}

// ---------- Commanding-heights lights ----------

const BULB_SVG =
  '<svg class="li-bulb-svg" viewBox="0 0 24 32" aria-hidden="true">' +
  '<circle class="li-bulb-glass" cx="12" cy="11" r="9"/>' +
  '<path class="li-bulb-filament" d="M8.5 12l1.2 2.6 1.2-2.6 1.2 2.6 1.2-2.6 1.2 2.6"/>' +
  '<path class="li-bulb-base" d="M8 20h8v2.5H8zM8.5 23.5h7v2h-7zM9.5 26.5h5v2h-5z"/>' +
  "</svg>";
let lightsBox = null;
let litBefore = new Set();
let achievedBefore = false;

function addLightsControl() {
  const Lights = L.Control.extend({
    options: { position: "topright" },
    onAdd() {
      lightsBox = L.DomUtil.create("div", "leaflet-control li-lights");
      lightsBox.setAttribute("aria-live", "polite");
      L.DomEvent.disableClickPropagation(lightsBox);
      return lightsBox;
    },
  });
  map.addControl(new Lights());
}

// Bulbs that just switched on (and the sign, on first reaching 3 of 3) flicker once.
function renderLights() {
  if (!lightsBox) return;
  const achieved = isAchieved();
  const bulbs = STEPS.map((s) => {
    const on = state.on.has(s.n);
    const cls = "li-bulb" + (on ? " on" : "") + (on && !litBefore.has(s.n) ? " flick" : "");
    return (
      `<div class="${cls}" style="--glow:${s.color}">${BULB_SVG}` +
      `<span class="li-bulb-label">${esc(LAYER_LABEL[s.layer].replace("Scarce Natural ", ""))}</span></div>`
    );
  }).join("");
  const signCls = "li-lights-sign" + (achieved ? " on" : "") + (achieved && !achievedBefore ? " flick" : "");
  lightsBox.className = "leaflet-control li-lights" + (achieved ? " achieved" : "");
  lightsBox.innerHTML = `<div class="li-bulbs">${bulbs}</div><div class="${signCls}">Commanding heights</div>`;
  litBefore = new Set(state.on);
  achievedBefore = achieved;
}

// ---------- Map rendering ----------

function initMap() {
  map = L.map("lithiumMap", {
    scrollWheelZoom: true,
    zoomControl: false,
    worldCopyJump: false,
    minZoom: 2,
    zoomSnap: 0.25,
  }).setView([-5, -150], 2);
  L.control.zoom({ position: "topleft" }).addTo(map);
  L.tileLayer(
    "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png?key=" +
      encodeURIComponent(CARTO_BASEMAP_KEY),
    {
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: "abcd",
      maxZoom: 20,
    }
  ).addTo(map);
  addFullscreenControl();
  addLightsControl();
  map.createPane("strands").style.zIndex = 410;
  map.createPane("flows").style.zIndex = 420;
  map.createPane("arrows").style.zIndex = 615;
  map.createPane("hubs").style.zIndex = 640;
  map.getPane("tooltipPane").style.zIndex = 680;
}

// ---------- Full screen ----------

const FS_EXPAND =
  '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3H3v5M16 3h5v5M8 21H3v-5M16 21h5v-5"/></svg>';
const FS_COLLAPSE =
  '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3v5H3M16 3v5h5M8 21v-5H3M16 21v-5h5"/></svg>';
let fsButton = null;

// The whole dashboard (step bar, map, panel) goes full screen so the steps stay clickable.
function isFullscreen() {
  const page = $("lithiumPage");
  const fs = document.fullscreenElement || document.webkitFullscreenElement;
  return fs === page || page.classList.contains("li-windowed-full");
}

function updateFullscreenButton() {
  const on = isFullscreen();
  fsButton.innerHTML = on ? FS_COLLAPSE : FS_EXPAND;
  fsButton.title = on ? "Exit full screen (F)" : "Full screen (F)";
  fsButton.setAttribute("aria-label", fsButton.title);
  fsButton.setAttribute("aria-pressed", on ? "true" : "false");
}

function syncFullscreen() {
  $("lithiumPage").classList.toggle("is-fullscreen", isFullscreen());
  updateFullscreenButton();
  setTimeout(() => renderMap(true), 120);
}

function toggleFullscreen() {
  const page = $("lithiumPage");
  if (isFullscreen()) {
    const cur = document.fullscreenElement || document.webkitFullscreenElement;
    const exit = document.exitFullscreen || document.webkitExitFullscreen;
    if (cur === page && exit) {
      Promise.resolve(exit.call(document)).catch(() => {}).then(syncFullscreen);
      return;
    }
    page.classList.remove("li-windowed-full");
    syncFullscreen();
    return;
  }
  const req = page.requestFullscreen || page.webkitRequestFullscreen;
  if (!req) {
    page.classList.add("li-windowed-full");
    syncFullscreen();
    return;
  }
  Promise.resolve(req.call(page))
    .catch(() => page.classList.add("li-windowed-full"))
    .then(syncFullscreen);
}

function addFullscreenControl() {
  const Fullscreen = L.Control.extend({
    options: { position: "topleft" },
    onAdd() {
      const bar = L.DomUtil.create("div", "leaflet-bar leaflet-control");
      fsButton = L.DomUtil.create("a", "map-fs-btn", bar);
      fsButton.href = "#";
      fsButton.setAttribute("role", "button");
      L.DomEvent.disableClickPropagation(bar);
      L.DomEvent.on(fsButton, "click", L.DomEvent.stop).on(fsButton, "click", toggleFullscreen);
      return bar;
    },
  });
  map.addControl(new Fullscreen());
  document.addEventListener("fullscreenchange", syncFullscreen);
  document.addEventListener("webkitfullscreenchange", syncFullscreen);
  updateFullscreenButton();
}

function drawFlow(step, fl, achieved) {
  const color = achieved ? GOLD : step.color;
  const g = arc(HUBS[fl.from].latlng, HUBS[fl.to].latlng, fl.bend);
  const tip = `<strong>${step.n} · ${esc(step.kicker)}</strong><br>${esc(fl.label)}`;
  if (achieved && !fl.alt) {
    webLayer.addLayer(
      L.polyline(g.latlngs, { pane: "flows", color: GOLD, weight: 13, opacity: 0.22, lineCap: "round", interactive: false })
    );
  }
  const drawIn = state.fresh === step.n && !fl.alt && !achieved;
  const cls = ["li-flow"];
  if (achieved && !fl.alt) cls.push("li-flow-gold");
  if (drawIn) cls.push("li-draw");
  const line = L.polyline(g.latlngs, {
    pane: "flows",
    color,
    weight: fl.alt ? 3 : 5,
    opacity: fl.alt ? 0.75 : 0.92,
    dashArray: fl.alt ? "6 8" : null,
    lineCap: "round",
    className: cls.join(" "),
  }).bindTooltip(tip, { sticky: true });
  webLayer.addLayer(line);
  if (drawIn) {
    const el = line.getElement();
    if (el) el.setAttribute("pathLength", "1");
  }
  webLayer.addLayer(
    L.marker(g.mid, {
      pane: "arrows",
      icon: arrowIcon(color, g.angle, fl.alt ? 14 : 20),
      interactive: false,
    })
  );
}

function renderMap(fit) {
  if (webLayer) webLayer.remove();
  webLayer = L.layerGroup().addTo(map);
  const achieved = isAchieved();
  const steps = activeSteps();
  const hubColors = {};
  const bounds = [];

  steps.forEach((step) => {
    step.flows.forEach((fl) => drawFlow(step, fl, achieved));
    step.hubs.forEach((h) => (hubColors[h] = hubColors[h] || []).push(step.color));
  });

  steps.forEach((step) => {
    if (!step.pins) return;
    const hub = HUBS[step.pins.hub];
    step.rows.forEach((r) => {
      const prc = sideBucket(r.side) === "prc";
      const picked = state.plot === r.id;
      bounds.push([r.lat, r.lon]);
      if (prc) {
        const from = step.pins.dir === "out" ? hub.latlng : [r.lat, r.lon];
        const to = step.pins.dir === "out" ? [r.lat, r.lon] : hub.latlng;
        const g = arc(from, to, 0.18);
        if (g.length >= 0.25) {
          webLayer.addLayer(
            L.polyline(g.latlngs, {
              pane: "strands",
              color: achieved ? GOLD : step.color,
              weight: 1.2,
              opacity: 0.7,
              dashArray: "3 5",
              lineCap: "butt",
              interactive: false,
            })
          );
        }
      }
      const m = L.marker([r.lat, r.lon], {
        icon: pinIcon(r, picked),
        opacity: prc || picked ? 1 : 0.45,
        zIndexOffset: picked ? 1000 : prc ? 100 : 0,
      });
      m.bindTooltip(`<strong>${esc((r.asset || r.id).slice(0, 110))}</strong><br>${esc(plotMeta(r))}`, {
        direction: "top",
        offset: [0, -6],
      });
      m.on("click", () => setPlot(r.id));
      webLayer.addLayer(m);
    });
  });

  Object.entries(hubColors).forEach(([id, colors]) => {
    const hub = HUBS[id];
    const marker = L.marker(hub.latlng, {
      pane: "hubs",
      icon: hubIcon(hub, achieved ? [GOLD] : [...new Set(colors)]),
      keyboard: false,
    });
    marker.bindTooltip(`<strong>${esc(hub.label)}</strong><br>${esc(hub.tip)}`, {
      direction: "right",
      offset: [10, 0],
    });
    webLayer.addLayer(marker);
    bounds.push(hub.latlng);
  });

  if (fit) {
    const pts = bounds.length ? bounds : Object.values(HUBS).map((h) => h.latlng);
    // Side padding leaves room for hub nameplates; bottom clears the banner.
    map.invalidateSize(false);
    map.fitBounds(L.latLngBounds(pts), {
      paddingTopLeft: [200, 40],
      paddingBottomRight: [200, achieved ? 120 : 40],
      maxZoom: 6,
    });
  }
}

// ---------- Step bar, meter, panel ----------

function renderSteps() {
  const parts = [];
  STEPS.forEach((s, i) => {
    if (i) parts.push('<span class="li-step-arrow" aria-hidden="true">&#9654;</span>');
    const on = state.on.has(s.n);
    parts.push(
      `<button type="button" class="li-step${on ? " on" : ""}" data-step="${s.n}" aria-pressed="${on}" style="--step:${s.color}">` +
        `<span class="li-step-kicker">${s.n} · ${esc(s.kicker)}</span>` +
        `<span class="li-step-title">${esc(s.title)}</span>` +
        `<span class="li-step-layer"><span class="li-shape ${LAYER_SHAPE[s.layer]}"></span>${esc(LAYER_LABEL[s.layer])}</span>` +
        `</button>`
    );
  });
  $("liSteps").innerHTML = parts.join("");
}

function renderMeter() {
  const achieved = isAchieved();
  const segs = STEPS.map(
    (s) =>
      `<span class="li-seg${state.on.has(s.n) ? " on" : ""}" style="--seg:${s.color}" title="${esc(LAYER_LABEL[s.layer])}">` +
      `${esc(LAYER_LABEL[s.layer].replace("Scarce Natural ", ""))}</span>`
  ).join("");
  const label = achieved
    ? "Commanding heights achieved"
    : `${state.on.size} of 3 commanding heights`;
  const meter = $("liMeter");
  meter.className = "li-meter" + (achieved ? " achieved" : "");
  meter.innerHTML = `<span class="li-meter-label">${label}</span><span class="li-segs">${segs}</span>`;
}

function sideCounts(rows) {
  const c = { prc: 0, us: 0, allied: 0 };
  rows.forEach((r) => (c[sideBucket(r.side)] += 1));
  return c;
}

function stepCard(s) {
  if (!state.on.has(s.n)) {
    return (
      `<button type="button" class="li-card-off" data-step="${s.n}" style="--step:${s.color}">` +
      `<span class="li-step-kicker">${s.n} · ${esc(s.kicker)}</span> ${esc(s.title)}` +
      `<span class="li-card-off-hint">Click to add ${esc(LAYER_LABEL[s.layer])}</span></button>`
    );
  }
  const stats = s.stats
    .map((x) => `<div class="li-stat"><strong>${esc(x.v)}</strong><span>${esc(x.l)}</span></div>`)
    .join("");
  const sources = s.sources.length
    ? `<p class="li-sources">Sources: ${s.sources
        .map((x) => `<a href="${esc(x.url)}" target="_blank" rel="noopener">${esc(x.label)}</a>`)
        .join(" · ")}</p>`
    : "";
  let plots = "";
  if (s.pins) {
    const c = sideCounts(s.rows);
    const items = s.rows
      .map(
        (r) =>
          `<li><button type="button" class="plot-item${state.plot === r.id ? " on" : ""}" data-plot="${esc(r.id)}">` +
          `<span class="plot-swatch" style="background:${SIDE_COLORS[sideBucket(r.side)]}"></span>` +
          `<span class="plot-text"><span class="plot-asset">${esc((r.asset || r.id).slice(0, 110))}</span>` +
          `<span class="meta">${esc(plotMeta(r))}</span></span></button></li>`
      )
      .join("");
    plots =
      `<p class="layer-line">${s.rows.length} mapped plots: <span class="side-prc">PRC ${c.prc}</span> · ` +
      `<span class="side-us">U.S. ${c.us}</span> · <span class="side-allied">Allied / other ${c.allied}</span></p>` +
      `<details class="li-plots"><summary>List plots</summary><ul>${items}</ul></details>`;
  } else {
    plots = `<p class="layer-line">Route hubs, not codebook plots: this leg runs through ports and plants outside the Latin America codebook.</p>`;
  }
  return (
    `<div class="summary-card li-card" style="border-top-color:${s.color}">` +
    `<p class="summary-kicker" style="color:${s.color}">${s.n} · ${esc(s.kicker)} · ${esc(LAYER_LABEL[s.layer])}</p>` +
    `<h2>${esc(s.title)}</h2>` +
    `<p>${esc(s.body)}</p>` +
    `<div class="li-stats">${stats}</div>` +
    `<p class="summary-note">${esc(s.note)}</p>` +
    sources +
    plots +
    `</div>`
  );
}

function renderCards() {
  const head = [];
  if (isAchieved()) {
    head.push(
      `<div class="summary-card li-card li-achieved-card">` +
        `<p class="summary-kicker">Commanding heights achieved</p>` +
        `<h2>One company chain, three layers</h2>` +
        `<p>The same Chinese firms hold the mine, the refining and the route into it, and the battery maker at the end. ` +
        `A pathway illustrative of Chinese diffuse international vertical integration. We're seeing this across products, sectors, and countries, and the process continues to accelerate.</p>` +
        `</div>`
    );
  } else if (!state.on.size) {
    head.push(
      `<div class="summary-card">` +
        `<p class="summary-kicker">Team 2 brief · Slide 10</p>` +
        `<h2>From mines to microchips</h2>` +
        `<p>Click steps 1, 2, and 3 (or press the 1, 2, 3 keys) to build the chain. Each step lights one commanding height: ` +
        `Scarce Natural Resources, Infrastructure, and Energy. Turn on all three to see the full chain. Press F for full screen.</p>` +
        `</div>`
    );
  }
  $("liCards").innerHTML = head.join("") + STEPS.map(stepCard).join("");
}

function renderDetail() {
  const box = $("liDetail");
  const r = state.plot ? ROW_BY_ID[state.plot] : null;
  if (!r) {
    box.hidden = true;
    box.innerHTML = "";
    return;
  }
  const fits = STEPS.filter((s) => (s.rows || []).some((x) => x.id === r.id))
    .map((s) => `Step ${s.n} · ${s.kicker}`)
    .join(", ");
  const note = (r.note || "").length > 420 ? r.note.slice(0, 420) + "…" : r.note || "";
  box.hidden = false;
  box.innerHTML =
    `<div class="detail-head"><p class="summary-kicker">${esc(LAYER_LABEL[r.layer] || r.layer)} · ${esc(
      SUB_LABEL[r.subcategory] || r.subcategory
    )}</p>` +
    `<button type="button" class="overlay-close" data-close-plot aria-label="Close plot">×</button></div>` +
    `<h3>${esc(r.asset || r.id)}</h3>` +
    `<p class="layer-line"><span class="plot-swatch" style="background:${SIDE_COLORS[sideBucket(r.side)]}"></span>${esc(
      plotMeta(r)
    )}</p>` +
    `<p class="detail-note">${esc(note)}</p>` +
    `<p class="detail-links">` +
    (r.evidence_url ? `<a href="${esc(r.evidence_url)}" target="_blank" rel="noopener">Source</a> · ` : "") +
    `<a href="index.html?focus=${encodeURIComponent(r.id)}">Open on the main map</a></p>` +
    `<p class="summary-note">Fits: ${esc(fits)} · <code>${esc(r.id)}</code></p>`;
}

function renderLegend() {
  const shapes = ["resources", "infrastructure", "energy"]
    .map(
      (l) =>
        `<span class="legend-item"><span class="li-shape ${LAYER_SHAPE[l]}" style="--shape:${STEP_BY_N[
          { resources: 1, infrastructure: 2, energy: 3 }[l]
        ].color}"></span>${esc(LAYER_LABEL[l])}</span>`
    )
    .join("");
  const sides = ["prc", "us", "allied"]
    .map(
      (k) =>
        `<span class="legend-item"><span class="legend-swatch circle" style="background:${SIDE_COLORS[k]}"></span>${SIDE_LABEL[k]} plot</span>`
    )
    .join("");
  $("liLegend").innerHTML =
    shapes +
    "<span>·</span>" +
    sides +
    "<span>·</span>" +
    `<span class="legend-item"><span class="hub-square legend-hub"></span>Hub</span>` +
    `<span class="legend-item"><span class="legend-flow" aria-hidden="true"></span>Chain route (stylized)</span>` +
    `<span class="legend-item"><span class="legend-dash" aria-hidden="true"></span>Alternate route or linked PRC plot</span>`;
}

function render(fit) {
  const achieved = isAchieved();
  $("lithiumPage").classList.toggle("is-achieved", achieved);
  $("liBanner").hidden = !achieved;
  renderSteps();
  renderMeter();
  renderLights();
  renderMap(fit);
  renderDetail();
  renderCards();
  state.fresh = null;
}

// ---------- State and events ----------

function toggleStep(n) {
  if (state.on.has(n)) {
    state.on.delete(n);
  } else {
    state.on.add(n);
    state.fresh = n;
  }
  render(true);
}

function showAll() {
  STEPS.forEach((s) => state.on.add(s.n));
  render(true);
}

function reset() {
  state.on.clear();
  state.plot = null;
  render(true);
}

function setPlot(id) {
  state.plot = id;
  render(false);
  $("liPanel").scrollTop = 0;
}

function bindEvents() {
  $("liSteps").addEventListener("click", (e) => {
    const b = e.target.closest("[data-step]");
    if (b) toggleStep(Number(b.getAttribute("data-step")));
  });
  $("liAll").addEventListener("click", showAll);
  $("liReset").addEventListener("click", reset);
  $("liPanel").addEventListener("click", (e) => {
    if (e.target.closest("[data-close-plot]")) {
      state.plot = null;
      render(false);
      return;
    }
    const plot = e.target.closest("[data-plot]");
    if (plot) {
      setPlot(plot.getAttribute("data-plot"));
      return;
    }
    const step = e.target.closest("[data-step]");
    if (step) toggleStep(Number(step.getAttribute("data-step")));
  });
  document.addEventListener("keydown", (e) => {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    if (e.target.closest && e.target.closest("input, textarea, select")) return;
    if (STEP_BY_N[Number(e.key)]) toggleStep(Number(e.key));
    else if (e.key === "a" || e.key === "A") showAll();
    else if (e.key === "r" || e.key === "R") reset();
    else if (e.key === "f" || e.key === "F") toggleFullscreen();
    else if (e.key === "Escape" && $("lithiumPage").classList.contains("li-windowed-full")) toggleFullscreen();
    else if (e.key === "Escape" && state.plot) {
      state.plot = null;
      render(false);
    }
  });
}

async function boot() {
  if (location.hash) history.replaceState(null, "", location.pathname + location.search);
  renderLegend();
  initMap();
  bindEvents();
  render(false);
  const rows = await fetch("data/observations.json").then((r) => r.json());
  ROW_BY_ID = Object.fromEntries(rows.map((r) => [r.id, r]));
  indexRows(rows);
  render(true);
}

STEPS.forEach((s) => (s.rows = []));
boot().catch((err) => {
  $("liCards").insertAdjacentHTML(
    "afterbegin",
    '<p class="empty">Could not load data/observations.json. Rebuild with process/build_site_data.py.</p>'
  );
  console.error(err);
});
