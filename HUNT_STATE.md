updated: 2026-10-05
cycle: 238
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 239 shuffle_seed=20261239; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us399/prc370/allied394); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-239 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 238) ===
# Filled this cycle: LatAm×engineering_epc NEW (us Equinix USD 419m);
#   Brazil×engineering_epc CapEx-fill (us McDermott Brava USD 1m floor);
#   Brazil×rail CapEx-fill (prc CRRC Araraquara R$50m ~USD 9.63m);
#   Argentina×copper NEW (allied Vicuña Stage 1 USD 7.1bn);
#   Brazil×port_cranes CapEx-fill (allied Konecranes Manaus R$120m ~USD 23.11m).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Equinix NEW + McDermott CapEx-fill + honest residual).
# PRC equal-budget: CRRC Araraquara CapEx-fill.

# === Cycle 238 (seed 20261238) ===
# Shuffled order (BRIEF.md numbered + Random(20261238).shuffle): niobium, engineering_epc,
#   bridges_roads, nickel, lithium, copper, port_cranes, graphite, power_plants_grid, rail,
#   other_renewables, port_ownership, solar, fission_smr, building_materials, water, wind,
#   balsa.
# Logged 2 new + 3 CapEx-fill upgrades (2 US / 1 PRC / 2 allied / 0 other; ≥1/3 US hunt
#   budget via Equinix NEW + McDermott CapEx-fill + honest residual):
#   us engineering_epc NEW: equinix_latam_419m_2025_2026 (USD 419m).
#   us engineering_epc CapEx-fill: mcdermott_brava_papa_terra_atlanta_2025 (USD 1m floor).
#   prc rail CapEx-fill: crrc_araraquara_factory_2026 (~USD 9.63m).
#   allied copper NEW: vicuna_stage1_capex_7p1bn_2026 (USD 7.1bn).
#   allied port_cranes CapEx-fill: konecranes_super_terminais_manaus_2025 (~USD 23.11m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: niobium, bridges_roads, nickel, lithium, graphite,
#   power_plants_grid, other_renewables, port_ownership, solar, fission_smr,
#   building_materials, water, wind, balsa
#   (catalog dense; CBMM/CPFL/State Grid already loaded; Siemens/Hitachi Trivia CapEx
#   undisclosed; UFN fertilizer archived out-of-scope; holdovers unsigned;
#   COP/CLP/PEN/RAP/Huaxin–CSN/Xinhai MoU/Aldesa EUR skipped).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 238: us399 / prc370 / allied394 / other91 (n=1254).
shuffle_seed: 20261238
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- infrastructure/engineering_epc
- infrastructure/bridges_roads
- resources/nickel
- resources/lithium
- resources/copper
- infrastructure/port_cranes
- resources/graphite
- energy/power_plants_grid
- infrastructure/rail
- energy/other_renewables
- infrastructure/port_ownership
- energy/solar
- energy/fission_smr
- infrastructure/building_materials
- resources/water
- energy/wind
- resources/balsa
rows_found_this_cycle:
  resources/niobium: 0
  infrastructure/engineering_epc: 2
  infrastructure/bridges_roads: 0
  resources/nickel: 0
  resources/lithium: 0
  resources/copper: 1
  infrastructure/port_cranes: 1
  resources/graphite: 0
  energy/power_plants_grid: 0
  infrastructure/rail: 1
  energy/other_renewables: 0
  infrastructure/port_ownership: 0
  energy/solar: 0
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  resources/water: 0
  energy/wind: 0
  resources/balsa: 0
rows_by_side_this_cycle:
  us: 2
  prc: 1
  allied: 2
  other: 0
thin_topup_after_shuffle:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0

# === Cycle 237 (seed 20261237) — prior ===
# Logged 6 new: EDP Brazil tx R$3.7bn; EDP Goiás R$450m nested; EDP SP dist R$5bn;
#   ANDRITZ COPEL EUR 300m floor; PowerChina NENCOL USD 195.2m; AES Greentegra USD 4bn.
# Active after 237: us398/prc370/allied393/other91 (n=1252).

# === Cycle 236 (seed 20261236) — prior ===
# Logged 2 new + 3 CapEx-fill: Colas L9; Colas/VINCI Alameda–Melipilla; Holcim Pacasmayo;
#   Danasun Choloma; ISA IE Madeira.
# Active after 236: us397/prc369/allied389/other91 (n=1246).
