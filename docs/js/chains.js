"use strict";

const SIDE_COLORS = { us: "#2f5d73", prc: "#8c3a2b", allied: "#6b7c3c" };
const SIDE_LABEL = { us: "U.S.", prc: "PRC", allied: "Allied / other" };
const SIDE_ORDER = { prc: 0, us: 1, allied: 2 };

const LAYER_LABEL = {
  infrastructure: "Infrastructure",
  resources: "Scarce Natural Resources",
  energy: "Energy",
};

const SUB_LABEL = {
  port_ownership: "Port ownership and concessions",
  port_cranes: "Port cranes and terminal equipment",
  rail: "Rail",
  bridges_roads: "Bridges and roads",
  building_materials: "Construction and building materials",
  engineering_epc: "Engineering, design, and EPC firms",
  niobium: "Niobium",
  lithium: "Lithium",
  copper: "Copper",
  nickel: "Nickel",
  graphite: "Graphite",
  balsa: "Balsa wood",
  water: "Water",
  fission_smr: "Small modular and other fission reactors",
  solar: "Solar",
  wind: "Wind",
  power_plants_grid: "Power plants and grid",
  other_renewables: "Other renewables",
};

const CHAINS = [
  {
    id: "copper",
    title: "Copper",
    long: "Copper capture pathway",
    color: "#b5651d",
    stages: ["Copper concentrate", "Chancay port", "Power and solar"],
    tagline:
      "Copper is dug in Latin America, moved through a PRC-run Pacific port, and used to wire power systems.",
    read:
      "A PRC smelter sets the copper fee, a PRC shipper runs the Pacific gateway, a PRC firm builds the cranes, and that copper wires the power system.",
  },
  {
    id: "balsa",
    title: "Balsa",
    long: "Balsa capture pathway",
    color: "#b8901c",
    stages: ["Balsa wood", "Guayaquil to Chancay", "Wind blades"],
    tagline:
      "Soft wood cut in Ecuador, moved on a PRC Asia route through Chancay, and built into wind blades.",
    read:
      "Ecuador grows the blade wood, COSCO runs the Asia route through Chancay, and a PRC firm builds the turbines, including in a factory it bought from GE in Brazil.",
  },
  {
    id: "lithium",
    title: "Lithium",
    long: "Lithium capture pathway",
    color: "#2a8c86",
    stages: ["Mining", "Refinement", "Export and manufacturing"],
    tagline:
      "Lithium is mined, refined, and manufactured by Chinese companies in a process dominated by the Lithium Triangle.",
    read:
      "The chokepoint is upstream from Latin America, but it illustrates diffuse Chinese international vertical integration.",
  },
  {
    id: "marcona",
    title: "Marcona iron ore",
    long: "Marcona iron ore capture pathway",
    color: "#6e5a8a",
    stages: ["Marcona iron ore", "San Nicolás port", "Thermal energy plant"],
    tagline:
      "Iron ore is mined in Marcona, Peru, shipped through a PRC-run private port, and powered by a PRC-owned plant.",
    read:
      "One PRC state company owns the mine, the port the ore leaves from, and a power plant. An accident at the port cut output 10.6%, which shows the port is the choke point.",
  },
];

const CHAIN_BY_ID = Object.fromEntries(CHAINS.map((c) => [c.id, c]));

// Geographic anchors where a chain's strands converge. "prc" sits in the
// Pacific as a stand-in for steps that happen in China, off the LatAm map.
const HUBS = {
  chancay: { label: "Chancay port", latlng: [-11.58, -77.27] },
  guayaquil: { label: "Guayaquil", latlng: [-2.2, -79.9] },
  marcona: { label: "Marcona and San Nicolás", latlng: [-15.36, -75.17], labelLeft: true },
  cauchari: { label: "Cauchari-Olaroz", latlng: [-23.45, -66.75] },
  camacari: { label: "Camaçari, Bahia", latlng: [-12.7, -38.32], labelLeft: true },
  prc: { label: "PRC (off map, across the Pacific)", latlng: [-17, -112], offMap: true, labelLeft: true },
};

// Chain backbone: the thick arrows from the brief's slides.
const FLOWS = [
  { chain: "copper", from: "chancay", to: "prc", bend: 0.16, label: "Concentrate to PRC smelters, which set the processing fee" },
  { chain: "balsa", from: "guayaquil", to: "chancay", bend: 0.22, label: "COSCO Guayaquil to Asia sailing by way of Chancay (March 2025)" },
  { chain: "balsa", from: "chancay", to: "prc", bend: -0.16, label: "Balsa to PRC blade and turbine makers" },
  { chain: "balsa", from: "prc", to: "camacari", bend: -0.12, label: "Goldwind's first plant outside China, bought from GE (2024)" },
  { chain: "lithium", from: "cauchari", to: "prc", bend: 0.14, label: "Brine product to Ganfeng refining in China (75% global share)" },
  { chain: "marcona", from: "marcona", to: "prc", bend: 0.24, label: "Ore exports go almost entirely to China" },
];

const PANEL_RE =
  /jinko|longi|trina|ja solar|risen|astronergy|chint|tongwei|huasun|hanersun|canadian solar|seraphim|dah solar|module|panel/i;

// Each node is a step from the brief. `match` searches the live observation
// rows; `hub` and `dir` decide where its strands run on the map ("in" means
// plots feed the hub, "out" means the hub supplies the plots).
const NODES = [
  // Copper
  {
    id: "cu_ore",
    chains: ["copper"],
    stage: 1,
    hub: "chancay",
    dir: "in",
    label: "Copper concentrate",
    desc: "Chile and Peru dig the ore that becomes copper metal.",
    match: { sub: ["copper"], country: ["Chile", "Peru"] },
  },
  {
    id: "cu_prc_mines",
    chains: ["copper"],
    stage: 1,
    hub: "chancay",
    dir: "in",
    label: "PRC copper mines",
    desc: "PRC-controlled copper mines and stakes in the region (MMG Las Bambas, Chinalco Toromocho, Zijin, and others).",
    match: { sub: ["copper"], side: ["prc"] },
  },
  {
    id: "cu_smelter",
    chains: ["copper"],
    stage: 1,
    hub: "prc",
    label: "PRC smelter fee",
    desc: "A PRC smelter sets the fee to process a ton of that concentrate.",
    context: "Set in China, so there is no map plot by design.",
  },
  {
    id: "chancay",
    chains: ["copper", "balsa"],
    stage: 2,
    hub: "chancay",
    dir: "in",
    label: "Chancay port",
    desc: "The PRC state shipper COSCO owns 60% of the company that runs the port; Peru's Volcan owns the other 40%. Opened November 2024.",
    match: { layer: ["infrastructure"], head: /chancay/i },
  },
  {
    id: "zpmc",
    chains: ["copper"],
    stage: 2,
    hub: "prc",
    dir: "out",
    label: "ZPMC cranes",
    desc: "ZPMC, a PRC state firm, builds the cranes that lift the cargo at Chancay, and its cranes show up across Latin American yards.",
    match: { sub: ["port_cranes"], head: /zpmc|zhenhua/i },
  },
  {
    id: "cu_rail",
    chains: ["copper"],
    stage: 2,
    hub: "chancay",
    dir: "in",
    label: "Rail to Chancay",
    desc: "Brazil and a PRC railway office are planning a line to this port. PRC builders already hold rail and tunnel work tied to Chancay.",
    match: {
      sub: ["rail", "bridges_roads"],
      country: ["Peru", "Brazil"],
      head: /chancay|bioce[aâ]nic|transoce[aâ]nic/i,
    },
  },
  {
    id: "cu_grid",
    chains: ["copper"],
    stage: 3,
    hub: "prc",
    dir: "out",
    label: "PRC grid stakes",
    desc: "Refined copper wires grids. Chinese grid SOEs hold large distribution and transmission stakes in Chile and Peru.",
    match: { sub: ["power_plants_grid"], side: ["prc"], country: ["Chile", "Peru"] },
  },
  {
    id: "cu_solar",
    chains: ["copper"],
    stage: 3,
    hub: "prc",
    dir: "out",
    label: "PRC solar panels",
    desc: "Copper wires solar farms too, and Latin American buyers also buy solar panels made in the PRC.",
    match: { sub: ["solar"], side: ["prc"], head: PANEL_RE },
  },
  {
    id: "cu_tariff",
    chains: ["copper"],
    stage: 3,
    label: "Brazil panel import tax",
    desc: "Brazil's import tax on those panels is 25%, or 9.6% inside a quota. The copper fee and the solar panels are both PRC-side prices.",
    context: "A price, not a site, so there is no map plot.",
  },

  // Balsa
  {
    id: "balsa_wood",
    chains: ["balsa"],
    stage: 1,
    hub: "guayaquil",
    dir: "in",
    label: "Ecuador balsa",
    desc: "Ecuador grows about 90% of the world's balsa. From 2019 through August 2024, China took 79% of Ecuador's balsa exports; the United States took 5%. That light wood is the core inside a wind turbine blade.",
    match: { sub: ["balsa"] },
  },
  {
    id: "guayaquil",
    chains: ["balsa"],
    stage: 2,
    hub: "guayaquil",
    dir: "in",
    label: "Guayaquil gateway",
    desc: "Exporters ship the wood from Guayaquil, where Contecon (part of Philippine ICTSI) runs the terminal. In March 2025 COSCO opened a Guayaquil to Asia sailing by way of Chancay.",
    match: {
      sub: ["port_ownership", "port_cranes", "engineering_epc"],
      country: ["Ecuador"],
      head: /guayaquil|posorja|contecon/i,
      and: /port|puerto|terminal|crane|berth|muelle|multipurpose/i,
    },
  },
  {
    id: "wind_oem",
    chains: ["balsa"],
    stage: 3,
    hub: "camacari",
    dir: "out",
    label: "Goldwind and Mingyang",
    desc: "PRC turbine makers Goldwind and Mingyang have used Ecuadorian balsa, per EIA.",
    match: { layer: ["energy"], head: /goldwind|mingyang/i },
  },
  {
    id: "camacari",
    chains: ["balsa"],
    stage: 3,
    hub: "camacari",
    dir: "in",
    label: "Camaçari blade plant",
    desc: "On 26 April 2024 Goldwind bought GE's old turbine plant in Camaçari, Bahia, its first plant outside China. By late August 2024 it was running.",
    match: {
      layer: ["energy"],
      head: /cama[cç]ari/i,
      and: /goldwind|sinoma|blade|turbine|nacelle|wind/i,
    },
  },

  // Lithium
  {
    id: "cauchari",
    chains: ["lithium"],
    stage: 1,
    hub: "cauchari",
    dir: "in",
    label: "Cauchari-Olaroz",
    desc: "Ganfeng is majority owner of the Argentine Cauchari-Olaroz brine operation, which produced nearly 35,000 tons of lithium carbonate in 2025, over 2% of global output.",
    match: { sub: ["lithium"], re: /cauchari|olaroz|exar/i },
  },
  {
    id: "li_prc",
    chains: ["lithium"],
    stage: 1,
    hub: "cauchari",
    dir: "in",
    label: "PRC lithium triangle stakes",
    desc: "Ganfeng and other PRC firms hold mining stakes across Argentina, Chile, and Bolivia.",
    match: { sub: ["lithium"], side: ["prc"], country: ["Argentina", "Chile", "Bolivia"] },
  },
  {
    id: "li_refine",
    chains: ["lithium"],
    stage: 2,
    hub: "prc",
    label: "Refining in China",
    desc: "Ganfeng imports the material to China, through Chinese-operated ports, where it is refined. China's refining share is 75% and rising year over year.",
    context: "Happens in China, outside the LatAm map by design.",
  },
  {
    id: "li_solar",
    chains: ["lithium"],
    stage: 3,
    hub: "cauchari",
    dir: "in",
    label: "Power for the salars",
    desc: "PRC firms also build the solar power beside the brine operations, such as Ganfeng's Mariana park and the PowerChina-built Cauchari park.",
    match: {
      sub: ["solar"],
      country: ["Argentina", "Chile", "Bolivia"],
      head: /ganfeng|mariana|cauchari|olaroz|litio|salar|lithium(?![- ]ion)/i,
    },
  },
  {
    id: "byd",
    chains: ["lithium"],
    stage: 3,
    hub: "prc",
    dir: "out",
    label: "BYD and LFP batteries",
    desc: "BYD and other Chinese manufacturers make 98% of the world's LFP cathodes, the key part of lithium-ion cells, which China makes 80% of.",
    match: { layer: ["energy"], head: /\bbyd\b/i },
  },

  // Marcona
  {
    id: "marcona_mine",
    chains: ["marcona"],
    stage: 1,
    hub: "marcona",
    dir: "in",
    label: "Marcona iron mine",
    desc: "Shougang bought the Marcona mine in 1992, the first Chinese mining company in South America. It produces about 98% of Peru's iron, and exports go almost entirely to China.",
    match: { layer: ["resources"], re: /shougang|hierro per[uú]|marcona|iron ore/i },
  },
  {
    id: "san_nicolas",
    chains: ["marcona"],
    stage: 2,
    hub: "marcona",
    dir: "in",
    label: "San Nicolás port",
    desc: "Shougang runs this private port directly. It takes ships up to about 209,000 tonnes and handles roughly 80 bulk carriers a year.",
    match: { layer: ["infrastructure"], re: /san nicol[aá]s|shougang/i, not: /jinzhao|san juan/i },
  },
  {
    id: "san_juan",
    chains: ["marcona"],
    stage: 2,
    hub: "marcona",
    dir: "in",
    label: "San Juan de Marcona port",
    desc: "A second, public port at San Juan de Marcona, concessioned to a PRC Jinzhao Mining vehicle, is planned. Not built yet.",
    match: { layer: ["infrastructure"], country: ["Peru"], re: /jinzhao|san juan de marcona|marcona/i },
  },
  {
    id: "shougesa",
    chains: ["marcona"],
    stage: 3,
    hub: "marcona",
    dir: "in",
    label: "Shougesa thermal plant",
    desc: "Shougesa, split off from the miner in 1997, is a Shougang subsidiary running a thermal plant of about 63 MW. BNamericas describes it as diesel-fired, 65.75 MW, and supplying the national grid.",
    match: { layer: ["energy"], re: /shougesa|shougang/i },
  },
  {
    id: "marcona_wind",
    chains: ["marcona"],
    stage: 3,
    hub: "marcona",
    dir: "in",
    label: "Marcona wind and solar",
    desc: "A $348.78 million wind plan (50 turbines, a 220 kV line) has been filed but not built. PRC-owned power already operates around Marcona.",
    match: { layer: ["energy"], country: ["Peru"], re: /marcona|san nicol[aá]s/i },
  },
];

const NODE_BY_ID = Object.fromEntries(NODES.map((n) => [n.id, n]));

const CARTO_BASEMAP_KEY = "cb1_32m3_1_44dc754e68375e8ab5208497";

let ROWS = [];
let ROW_BY_ID = {};
let MEMBERSHIP = {};
let map = null;
let webLayer = null;
let pinById = {};
const state = { chain: "all", node: null, side: "us_prc", q: "", plot: null };

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

function headText(r) {
  return [r.id, r.asset, r.counterpart, r.counterpart_actor].filter(Boolean).join(" ");
}

// `head` tests names (id, asset, actors) only; `re`, `and`, `not` also read the
// opening of the note, where later cycle logs mention unrelated projects.
function matchRow(m, r, head, text) {
  if (m.layer && !m.layer.includes(r.layer)) return false;
  if (m.sub && !m.sub.includes(r.subcategory)) return false;
  if (m.country && !m.country.includes(r.country)) return false;
  if (m.side && !m.side.includes(r.side)) return false;
  if (m.head && !m.head.test(head)) return false;
  if (m.re && !m.re.test(text)) return false;
  if (m.and && !m.and.test(text)) return false;
  if (m.not && m.not.test(text)) return false;
  return true;
}

function indexRows(rows) {
  const plots = rows.filter(isPlot).map((r) => {
    const head = headText(r);
    return { row: r, head, text: head + " " + (r.note || "").slice(0, 320) };
  });
  const membership = {};
  NODES.forEach((node) => {
    node.rows = [];
    if (!node.match) return;
    plots.forEach(({ row, head, text }) => {
      if (!matchRow(node.match, row, head, text)) return;
      node.rows.push(row);
      (membership[row.id] = membership[row.id] || []).push(node.id);
    });
    node.rows.sort(
      (a, b) =>
        SIDE_ORDER[sideBucket(a.side)] - SIDE_ORDER[sideBucket(b.side)] ||
        (b.value_usd || 0) - (a.value_usd || 0)
    );
  });
  return membership;
}

function sideRows(node) {
  if (!node.rows) return [];
  if (state.side === "all") return node.rows;
  if (state.side === "us_prc") {
    return node.rows.filter((r) => {
      const b = sideBucket(r.side);
      return b === "us" || b === "prc";
    });
  }
  return node.rows.filter((r) => sideBucket(r.side) === state.side);
}

function searchHit(r) {
  if (!state.q) return true;
  const hay = [r.id, r.asset, r.country, r.counterpart, r.counterpart_actor, r.note]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();
  return state.q
    .toLowerCase()
    .split(/\s+/)
    .filter(Boolean)
    .every((w) => hay.includes(w));
}

function chainActive(chains) {
  return state.chain === "all" || chains.includes(state.chain);
}

function sideCounts(rows) {
  const c = { prc: 0, us: 0, allied: 0 };
  rows.forEach((r) => (c[sideBucket(r.side)] += 1));
  return c;
}

function uniqueRows(nodes) {
  const seen = new Map();
  nodes.forEach((n) => sideRows(n).forEach((r) => seen.set(r.id, r)));
  return [...seen.values()];
}

function nodeColor(node) {
  if (state.chain !== "all" && node.chains.includes(state.chain)) return CHAIN_BY_ID[state.chain].color;
  return CHAIN_BY_ID[node.chains[0]].color;
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
  for (let i = 0; i <= 32; i++) latlngs.push(map.unproject(at(i / 32), 0));
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
  return L.divIcon({
    className: "chain-pin" + (picked ? " picked" : ""),
    html: `<span class="pin-ring" style="--pin:${color}"><span class="pin-dot"></span></span>`,
    iconSize: picked ? [22, 22] : [16, 16],
    iconAnchor: picked ? [11, 11] : [8, 8],
  });
}

function hubIcon(hub, colors) {
  const bar = colors.map((c) => `<span style="background:${c}"></span>`).join("");
  return L.divIcon({
    className: "hub-icon" + (hub.offMap ? " off-map" : "") + (hub.labelLeft ? " label-left" : ""),
    html: `<span class="hub-square"></span><span class="hub-label">${esc(hub.label)}<span class="hub-bar">${bar}</span></span>`,
    iconSize: [14, 14],
    iconAnchor: [7, 7],
  });
}

// ---------- Map rendering ----------

function initMap() {
  map = L.map("chainMap", { scrollWheelZoom: true, zoomControl: false, worldCopyJump: false }).setView(
    [-12, -75],
    3
  );
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
  map.createPane("strands").style.zIndex = 410;
  map.createPane("flows").style.zIndex = 420;
  map.createPane("arrows").style.zIndex = 615;
  // Hubs above pins/arrows (600/615) but below Leaflet tooltips (default 650)
  // so hover boxes are never buried under hub nameplates.
  map.createPane("hubs").style.zIndex = 640;
  map.getPane("tooltipPane").style.zIndex = 680;
  map.getPane("popupPane").style.zIndex = 700;
}

function visibleNodes() {
  return NODES.filter((n) => chainActive(n.chains));
}

function renderMap(fit) {
  if (webLayer) webLayer.remove();
  webLayer = L.layerGroup().addTo(map);
  pinById = {};
  const nodes = visibleNodes();
  const usedHubs = {};
  const bounds = [];
  const drawnStrands = new Set();
  const pinState = {};

  const focusNode = state.node ? NODE_BY_ID[state.node] : null;

  FLOWS.forEach((fl) => {
    if (!chainActive([fl.chain])) return;
    const color = CHAIN_BY_ID[fl.chain].color;
    const dim = focusNode && !focusNode.chains.includes(fl.chain);
    const g = arc(HUBS[fl.from].latlng, HUBS[fl.to].latlng, fl.bend);
    const line = L.polyline(g.latlngs, {
      pane: "flows",
      color,
      weight: 4.5,
      opacity: dim ? 0.2 : 0.85,
      lineCap: "round",
    }).bindTooltip(`<strong>${esc(CHAIN_BY_ID[fl.chain].long)}</strong><br>${esc(fl.label)}`, { sticky: true });
    webLayer.addLayer(line);
    webLayer.addLayer(
      L.marker(g.mid, { pane: "arrows", icon: arrowIcon(color, g.angle, 20), interactive: false, opacity: dim ? 0.25 : 1 })
    );
    [fl.from, fl.to].forEach((h) => {
      (usedHubs[h] = usedHubs[h] || new Set()).add(fl.chain);
    });
  });

  nodes.forEach((node) => {
    if (node.hub) (usedHubs[node.hub] = usedHubs[node.hub] || new Set()).add(nodeColor(node));
    if (!node.hub || node.context) return;
    const hub = HUBS[node.hub];
    const color = nodeColor(node);
    const nodeDim = focusNode && focusNode.id !== node.id;
    sideRows(node).forEach((r) => {
      const hit = searchHit(r);
      const strong = hit && !nodeDim;
      const prev = pinState[r.id];
      pinState[r.id] = { row: r, strong: (prev && prev.strong) || strong };
      bounds.push([r.lat, r.lon]);
      const key = r.id + ">" + node.hub;
      if (drawnStrands.has(key)) return;
      drawnStrands.add(key);
      const from = node.dir === "out" ? hub.latlng : [r.lat, r.lon];
      const to = node.dir === "out" ? [r.lat, r.lon] : hub.latlng;
      const g = arc(from, to, 0.18);
      if (g.length < 0.25) return;
      webLayer.addLayer(
        L.polyline(g.latlngs, {
          pane: "strands",
          color,
          weight: strong ? 1.3 : 1,
          opacity: strong ? 0.75 : 0.12,
          interactive: false,
        })
      );
      if (g.length > 1.2) {
        webLayer.addLayer(
          L.marker(g.mid, {
            pane: "arrows",
            icon: arrowIcon(color, g.angle, 10),
            interactive: false,
            opacity: strong ? 0.9 : 0.15,
          })
        );
      }
    });
  });

  Object.values(pinState).forEach(({ row, strong }) => {
    const picked = state.plot === row.id;
    const m = L.marker([row.lat, row.lon], {
      icon: pinIcon(row, picked),
      opacity: strong || picked ? 1 : 0.25,
      zIndexOffset: picked ? 1000 : strong ? 100 : 0,
    });
    m.bindTooltip(`<strong>${esc((row.asset || row.id).slice(0, 110))}</strong><br>${esc(plotMeta(row))}`, {
      direction: "top",
      offset: [0, -6],
    });
    m.on("click", () => setPlot(row.id, false));
    webLayer.addLayer(m);
    pinById[row.id] = m;
  });

  Object.entries(usedHubs).forEach(([id, set]) => {
    const hub = HUBS[id];
    const colors = [...set].map((c) => (CHAIN_BY_ID[c] ? CHAIN_BY_ID[c].color : c));
    const uniq = [...new Set(colors)];
    const marker = L.marker(hub.latlng, { pane: "hubs", icon: hubIcon(hub, uniq), keyboard: false });
    const hubNodes = nodes.filter((n) => n.hub === id);
    if (hubNodes.length) {
      marker.bindTooltip(
        `<strong>${esc(hub.label)}</strong><br>` +
          hubNodes.map((n) => `${esc(n.label)}${n.context ? " (off map)" : ` · ${sideRows(n).length}`}`).join("<br>"),
        { direction: "right", offset: [10, 0] }
      );
    }
    webLayer.addLayer(marker);
    bounds.push(hub.latlng);
  });

  if (fit) {
    let fitPts = bounds;
    if (focusNode && focusNode.hub) {
      fitPts = sideRows(focusNode).map((r) => [r.lat, r.lon]).concat([HUBS[focusNode.hub].latlng]);
    }
    if (fitPts.length) map.fitBounds(L.latLngBounds(fitPts), { padding: [40, 40], maxZoom: 7 });
  }
}

// ---------- Panel ----------

function renderChips() {
  const all = uniqueRows(NODES);
  const chips = [
    `<button type="button" class="chip${state.chain === "all" ? " on" : ""}" data-chain="all">All pathways <span class="chip-n">${all.length}</span></button>`,
  ];
  CHAINS.forEach((c) => {
    const n = uniqueRows(NODES.filter((nd) => nd.chains.includes(c.id))).length;
    chips.push(
      `<button type="button" class="chip${state.chain === c.id ? " on" : ""}" data-chain="${c.id}" style="--chip:${c.color}">` +
        `<span class="chip-dot"></span>${esc(c.title)} <span class="chip-n">${n}</span></button>`
    );
  });
  $("chainChips").innerHTML = chips.join("");
}

function countLine(rows) {
  const c = sideCounts(rows);
  const parts = [
    `<span class="side-prc">PRC ${c.prc}</span>`,
    `<span class="side-us">U.S. ${c.us}</span>`,
  ];
  // U.S. vs PRC view already drops allied plots — don't show Allied / other 0.
  if (state.side !== "us_prc") {
    parts.push(`<span class="side-allied">Allied / other ${c.allied}</span>`);
  }
  return parts.join(" · ");
}

function scopeNodes() {
  if (state.node) return [NODE_BY_ID[state.node]];
  return visibleNodes();
}

function renderSummary() {
  const box = $("chainSummary");
  if (state.node) {
    const node = NODE_BY_ID[state.node];
    const rows = sideRows(node);
    const chainNames = node.chains.map((id) => CHAIN_BY_ID[id].title).join(" and ");
    box.innerHTML =
      `<div class="summary-card" style="border-top-color:${nodeColor(node)}">` +
      `<p class="summary-kicker">${esc(chainNames)} chain · Stage ${node.stage}</p>` +
      `<h2>${esc(node.label)}</h2>` +
      `<p>${esc(node.desc)}</p>` +
      (node.context
        ? `<p class="summary-note">${esc(node.context)}</p>`
        : `<p class="layer-line">${rows.length} matching plot${rows.length === 1 ? "" : "s"}: ${countLine(rows)}</p>`) +
      `<button type="button" class="link-btn" data-clear-node>Back to ${
        state.chain === "all" ? "all pathways" : esc(CHAIN_BY_ID[state.chain].long)
      }</button>` +
      `</div>`;
    return;
  }
  if (state.chain === "all") {
    const rows = uniqueRows(NODES);
    box.innerHTML =
      `<div class="summary-card">` +
      `<p class="summary-kicker">Team 2 brief · Capture Pathways</p>` +
      `<h2>Capture Pathways</h2>` +
      `<p>Thick arrows trace each pathway from the brief: from the mine, through the port, out to the PRC across the Pacific, and back into Latin American power. Thin strands tie each step to the existing map plots that fit it, found by searching the codebook.</p>` +
      `<p class="layer-line">${rows.length} distinct plots: ${countLine(rows)}</p>` +
      `</div>`;
    return;
  }
  const c = CHAIN_BY_ID[state.chain];
  const nodes = NODES.filter((n) => n.chains.includes(c.id));
  const rows = uniqueRows(nodes);
  const steps = [1, 2, 3]
    .map((s) => {
      const names = nodes
        .filter((n) => n.stage === s)
        .map((n) => `<button type="button" class="link-btn" data-node="${n.id}">${esc(n.label)}</button>`)
        .join(", ");
      return `<li><strong>${s} · ${esc(c.stages[s - 1])}</strong>: ${names}</li>`;
    })
    .join("");
  box.innerHTML =
    `<div class="summary-card" style="border-top-color:${c.color}">` +
    `<p class="summary-kicker" style="color:${c.color}">Capture pathway</p>` +
    `<h2>${esc(c.long)}</h2>` +
    `<p>${esc(c.tagline)}</p>` +
    `<ol class="stage-list">${steps}</ol>` +
    `<p class="security-read"><strong>Security read:</strong> ${esc(c.read)}</p>` +
    `<p class="layer-line">${rows.length} distinct plots: ${countLine(rows)}</p>` +
    `</div>`;
}

function plotMeta(r) {
  return [r.country, SIDE_LABEL[sideBucket(r.side)], r.year, fmtMoney(r.value_usd), r.evidence]
    .filter(Boolean)
    .join(" · ");
}

function renderList() {
  const groups = scopeNodes()
    .map((node) => {
      const swatch = `<span class="group-swatch" style="background:${nodeColor(node)}"></span>`;
      if (node.context) {
        return (
          `<section class="plot-group context"><h3>${swatch}${esc(node.label)}</h3>` +
          `<p class="empty">${esc(node.context)}</p></section>`
        );
      }
      const rows = sideRows(node).filter(searchHit);
      const head =
        `<h3>${swatch}<button type="button" class="link-btn" data-node="${node.id}">${esc(node.label)}</button>` +
        ` <span class="group-n">${rows.length}</span></h3>`;
      if (!rows.length) {
        const why =
          state.q || state.side !== "all" ? "No plots match the current filters." : "No plots on the map yet.";
        return `<section class="plot-group">${head}<p class="empty">${why}</p></section>`;
      }
      const items = rows
        .map(
          (r) =>
            `<li><button type="button" class="plot-item${state.plot === r.id ? " on" : ""}" data-plot="${esc(r.id)}">` +
            `<span class="plot-swatch" style="background:${SIDE_COLORS[sideBucket(r.side)]}"></span>` +
            `<span class="plot-text"><span class="plot-asset">${esc((r.asset || r.id).slice(0, 110))}</span>` +
            `<span class="meta">${esc(plotMeta(r))}</span></span></button></li>`
        )
        .join("");
      return `<section class="plot-group">${head}<ul>${items}</ul></section>`;
    })
    .join("");
  $("plotList").innerHTML = groups;
}

function renderDetail() {
  const box = $("plotDetail");
  const r = state.plot ? ROW_BY_ID[state.plot] : null;
  if (!r) {
    box.hidden = true;
    box.innerHTML = "";
    return;
  }
  const inNodes = (MEMBERSHIP[r.id] || []).map((id) => NODE_BY_ID[id].label).join(", ");
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
    `<p class="summary-note">Fits: ${esc(inNodes)} · <code>${esc(r.id)}</code></p>`;
}

function renderPanel() {
  renderChips();
  renderSummary();
  renderDetail();
  renderList();
}

function render(fit) {
  renderMap(fit);
  renderPanel();
  writeHash();
}

// ---------- State and events ----------

function writeHash() {
  const p = new URLSearchParams();
  if (state.chain !== "all") p.set("chain", state.chain);
  if (state.node) p.set("node", state.node);
  const h = p.toString();
  history.replaceState(null, "", h ? "#" + h : location.pathname + location.search);
}

function readHash() {
  const p = new URLSearchParams(location.hash.slice(1));
  const chain = p.get("chain");
  if (chain && CHAIN_BY_ID[chain]) state.chain = chain;
  const node = p.get("node");
  if (node && NODE_BY_ID[node] && chainActive(NODE_BY_ID[node].chains)) state.node = node;
}

function setChain(id) {
  state.chain = id;
  state.node = null;
  render(true);
}

function setNode(id) {
  state.node = state.node === id ? null : id;
  if (state.node && !chainActive(NODE_BY_ID[id].chains)) state.chain = NODE_BY_ID[id].chains[0];
  render(true);
}

function setPlot(id, pan) {
  state.plot = id;
  render(false);
  const m = pinById[id];
  if (m && pan) map.setView(m.getLatLng(), Math.max(map.getZoom(), 6));
  $("chainPanel").scrollTop = 0;
}

function bindEvents() {
  $("chainChips").addEventListener("click", (e) => {
    const chip = e.target.closest("[data-chain]");
    if (chip) setChain(chip.getAttribute("data-chain"));
  });
  $("chainPanel").addEventListener("click", (e) => {
    if (e.target.closest("[data-clear-node]")) {
      state.node = null;
      render(true);
      return;
    }
    if (e.target.closest("[data-close-plot]")) {
      state.plot = null;
      render(false);
      return;
    }
    const plot = e.target.closest("[data-plot]");
    if (plot) {
      setPlot(plot.getAttribute("data-plot"), true);
      return;
    }
    const node = e.target.closest("[data-node]");
    if (node) setNode(node.getAttribute("data-node"));
  });
  $("sideFilter").addEventListener("change", (e) => {
    state.side = e.target.value;
    render(false);
  });
  let timer = null;
  $("plotSearch").addEventListener("input", (e) => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      state.q = e.target.value.trim();
      render(false);
    }, 200);
  });
}

function renderLegend() {
  const chains = CHAINS.map(
    (c) => `<span class="legend-item"><span class="legend-line" style="background:${c.color}"></span>${esc(c.title)}</span>`
  ).join("");
  const sides = ["prc", "us", "allied"]
    .map(
      (k) =>
        `<span class="legend-item"><span class="pin-ring legend-pin" style="--pin:${SIDE_COLORS[k]}"><span class="pin-dot"></span></span>${SIDE_LABEL[k]} plot</span>`
    )
    .join("");
  $("webLegend").innerHTML =
    chains +
    "<span>·</span>" +
    sides +
    "<span>·</span>" +
    `<span class="legend-item"><span class="hub-square legend-hub"></span>Chain hub</span>` +
    `<span class="legend-item">Thick arrow: chain flow · thin strand: plot that fits a step</span>`;
}

async function boot() {
  readHash();
  $("sideFilter").value = state.side;
  renderLegend();
  initMap();
  $("plotList").innerHTML = '<p class="empty">Searching the codebook for plots that fit each chain…</p>';
  const rows = await fetch("data/observations.json").then((r) => r.json());
  ROWS = rows;
  ROW_BY_ID = Object.fromEntries(rows.map((r) => [r.id, r]));
  MEMBERSHIP = indexRows(rows);
  bindEvents();
  render(true);
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = { CHAINS, NODES, HUBS, FLOWS, indexRows, isPlot };
} else {
  boot().catch((err) => {
    $("plotList").innerHTML =
      '<p class="empty">Could not load data/observations.json. Rebuild with process/build_site_data.py.</p>';
    console.error(err);
  });
}
