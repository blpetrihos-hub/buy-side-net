updated: 2026-10-05
cycle: 236
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 237 shuffle_seed=20261237; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us397/prc369/allied389); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-237 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 236) ===
# Filled this cycle: Chile×rail NEW (allied Colas Santiago L9 electrical/SCADA
#   ~USD 118.56m; allied Colas/VINCI Alameda–Melipilla S2 USD 114.00m);
#   Peru×building_materials CapEx-fill (allied Holcim Pacasmayo EV USD 1500m);
#   Honduras×solar CapEx-fill (prc Danasun Choloma USD 400m proxy);
#   Brazil×power_plants_grid CapEx-fill (allied ISA IE Madeira 49% ~USD 224.76m).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (honest US residual — blank-USD CapEx exhausted).
# PRC equal-budget: Danasun Choloma CapEx-fill.

# === Cycle 236 (seed 20261236) ===
# Shuffled order (BRIEF.md numbered + Random(20261236).shuffle): graphite, lithium,
#   nickel, bridges_roads, other_renewables, niobium, balsa, port_cranes,
#   port_ownership, building_materials, water, copper, wind, power_plants_grid,
#   fission_smr, solar, rail, engineering_epc.
# Logged 2 new + 3 CapEx-fill upgrades (0 US / 1 PRC / 4 allied / 0 other; ≥1/3 US hunt
#   budget via honest residual sweeps):
#   allied rail NEW: colas_santiago_l9_electrical_scada_104m_eur_2026 (~USD 118.56m).
#   allied rail NEW: colas_vinci_alameda_melipilla_s2_100m_eur_2025 (USD 114.00m).
#   allied building_materials CapEx-fill: holcim_pacasmayo_complete_2026 (USD 1500m).
#   prc solar CapEx-fill: danasun_choloma_solar_honduras_2024 (USD 400m proxy).
#   allied power_plants_grid CapEx-fill: isa_energia_ie_madeira_49pct_1167m_2026
#     (~USD 224.76m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: graphite, lithium, nickel, bridges_roads, other_renewables,
#   niobium, balsa, port_cranes, port_ownership, water, copper, wind, fission_smr,
#   engineering_epc
#   (catalog dense; Goldwind Sento Sé no contract USD; holdovers unsigned;
#   COP/CLP/PEN/RAP/Huaxin–CSN/Xinhai MoU/Aldesa EUR skipped).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 236: us397 / prc369 / allied389 / other91 (n=1246).
shuffle_seed: 20261236
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/graphite
- resources/lithium
- resources/nickel
- infrastructure/bridges_roads
- energy/other_renewables
- resources/niobium
- resources/balsa
- infrastructure/port_cranes
- infrastructure/port_ownership
- infrastructure/building_materials
- resources/water
- resources/copper
- energy/wind
- energy/power_plants_grid
- energy/fission_smr
- energy/solar
- infrastructure/rail
- infrastructure/engineering_epc
rows_found_this_cycle:
  resources/graphite: 0
  resources/lithium: 0
  resources/nickel: 0
  infrastructure/bridges_roads: 0
  energy/other_renewables: 0
  resources/niobium: 0
  resources/balsa: 0
  infrastructure/port_cranes: 0
  infrastructure/port_ownership: 0
  infrastructure/building_materials: 1
  resources/water: 0
  resources/copper: 0
  energy/wind: 0
  energy/power_plants_grid: 1
  energy/fission_smr: 0
  energy/solar: 1
  infrastructure/rail: 2
  infrastructure/engineering_epc: 0
rows_by_side_this_cycle:
  us: 0
  prc: 1
  allied: 4
  other: 0
thin_topup_after_shuffle:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0

# === Cycle 235 (seed 20261235) — prior ===
# Logged 1 new + 8 CapEx-fill: OHLA Santiago L7 stations; Huawei Amazonas; FCX El Abra;
#   Oceaneering; CB&I VMOS; ZPMC Lirquén; Rio Tinto Maricunga; Sandvik Marmato; AES Panama.
# Active after 235: us397/prc369/allied387/other91 (n=1244).

# === Cycle 234 (seed 20261234) — prior ===
# Logged 0 new + 9 CapEx-fill: ACA Transnordestina; CAMCE Punta Huete; Neoenergia Guará 2;
#   EPR Régis; CSCEC Litoral; Jiangxi Cascabel; Fortescue Cañariaco; Sandvik CoMinVi;
#   Epiroc Peru.
# Active after 234: us397/prc369/allied386/other91 (n=1243).
