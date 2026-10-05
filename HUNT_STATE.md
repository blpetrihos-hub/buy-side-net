updated: 2026-10-05
cycle: 261
remote: present
active_layer: infrastructure
active_subcategory: bridges_roads
next_query: Cycle 262 shuffle_seed=20261262; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us417/prc381/allied426); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco; Equatorial ADMS company primary if openable; Ascenty Vinhedo/Osasco USD breakouts if company primary opens; GATE R$20bn acceleration if State Grid company confirms vs R$18bn; Alupar TECP CapEx R$2.0518bn if company face distinct from Lot 7/TAP/TPC/TCN (Lot 7 + TAP/TPC/TCN logged C260–261); Ada Franco da Rocha R$2.7bn if company CapEx figure opens; Scala FY2025 CapEx if sustainability R$4.7bn reconciles to DFS; KIO QRO2/2026 nested breakouts; Grenergy €3.7bn Chile ~45% if separable primary; Copel 1S26 R$1.5388bn if full earnings-release PDF opens beyond 2T26 nested; ODATA SP04 >R$2.6bn if company CapEx primary distinct from DeltaFlow; Equinix São Paulo cabinets USD109m if company SEC/10-Q primary opens; BYD BESS up to R$500m if company CapEx primary opens; AXIA 2026–2027 plan R$12–14bn if distinct company primary beyond 2Q26 nested; WEG transformers Americas R$2.1bn if LatAm-only CapEx separable. No U.S. territories.
next_row_id: (follow cycle-262 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 261) ===
# Filled this cycle: Brazil×building_materials NEW×1 (other Gerdau 2Q26 Brazil CapEx R$800m);
#   Brazil×power_plants_grid NEW×3 (other Alupar TAP R$498.52m + TPC R$2,597.23m + TCN
#   R$1,390.64m CapEx previsto).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (residual — Equinix/Ascenty/Cirion/Scala/USTDA/EXIM dense).
# PRC equal-budget: honest residual (CPFL nested already logged).

# === Cycle 261 (seed 20261261) ===
# Shuffled order (BRIEF.md numbered + Random(20261261).shuffle): rail, nickel,
#   building_materials, graphite, lithium, engineering_epc, niobium, port_ownership,
#   other_renewables, power_plants_grid, water, balsa, port_cranes, wind, fission_smr,
#   copper, solar, bridges_roads.
# Logged 4 new (0 US / 0 PRC / 0 allied / 4 other; ≥1/3 US hunt budget spent / residual;
#   PRC residual):
#   other building_materials NEW: gerdau_2q26_brazil_capex_800m_brl (~USD 154.08m);
#   other power_plants_grid NEW: alupar_tap_capex_previsto_498p52m_brl (~USD 96.01m);
#     alupar_tpc_capex_previsto_2597p23m_brl (~USD 500.23m);
#     alupar_tcn_capex_previsto_1390p64m_brl (~USD 267.84m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: rail, nickel, graphite, lithium, engineering_epc, niobium,
#   port_ownership, other_renewables, water, balsa, port_cranes, wind, fission_smr,
#   copper, solar, bridges_roads (catalog dense; US/PRC CapEx dense; thin dry).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail;
#   CHEC San Carlos; Progress Rail VLI R$430m; Alupar TECP company face; Ada R$2.7bn;
#   Equinix SP USD109m SEC; BYD BESS R$500m company.
# Active after cycle 261: us417 / prc381 / allied426 / other128 (n=1352).

# === Cycle 260 (seed 20261260) summary ===
# Logged 8 new (0 US / 0 PRC / 4 allied / 4 other). Active after: us417/prc381/allied426/other124 (n=1348).

shuffle_seed: 20261261
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/rail
- resources/nickel
- infrastructure/building_materials
- resources/graphite
- resources/lithium
- infrastructure/engineering_epc
- resources/niobium
- infrastructure/port_ownership
- energy/other_renewables
- energy/power_plants_grid
- resources/water
- resources/balsa
- infrastructure/port_cranes
- energy/wind
- energy/fission_smr
- resources/copper
- energy/solar
- infrastructure/bridges_roads
rows_found_this_cycle:
  infrastructure/rail: 0
  resources/nickel: 0
  infrastructure/building_materials: 1
  resources/graphite: 0
  resources/lithium: 0
  infrastructure/engineering_epc: 0
  resources/niobium: 0
  infrastructure/port_ownership: 0
  energy/other_renewables: 0
  energy/power_plants_grid: 3
  resources/water: 0
  resources/balsa: 0
  infrastructure/port_cranes: 0
  energy/wind: 0
  energy/fission_smr: 0
  resources/copper: 0
  energy/solar: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 0
  prc: 0
  allied: 0
  other: 4
thin_topup_after_shuffle:
- resources/balsa
- resources/nickel
- energy/fission_smr
