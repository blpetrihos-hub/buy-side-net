updated: 2026-10-05
cycle: 235
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 236 shuffle_seed=20261236; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us397/prc369/allied387); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-236 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 235) ===
# Filled this cycle: Chile×rail NEW (allied OHLA Santiago L7 G5–6 stations ~USD 81.85m);
#   Brazil×other_renewables CapEx-fill (prc Huawei/Aggreko Amazonas USD 165m);
#   Chile×water CapEx-fill (us Freeport El Abra Continuidad USD 7.5bn);
#   Brazil×engineering_epc CapEx-fill (us Oceaneering Petrobras umbilicals USD 120m floor);
#   Argentina×engineering_epc CapEx-fill (us CB&I VMOS Punta Colorada USD 100m floor);
#   Chile×port_cranes CapEx-fill (prc ZPMC DP World Lirquén USD 45m);
#   Chile×lithium CapEx-fill (allied Rio Tinto Maricunga up-to USD 900m);
#   Colombia×copper CapEx-fill (allied Sandvik Marmato ~USD 25.24m);
#   Panama×solar CapEx-fill (us AES four-park >USD 50m floor).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget: Oceaneering / Freeport El Abra / CB&I / AES Panama CapEx-fills.
# PRC equal-budget: Huawei/Aggreko Amazonas; ZPMC Lirquén.

# === Cycle 235 (seed 20261235) ===
# Shuffled order (BRIEF.md numbered + Random(20261235).shuffle): other_renewables,
#   solar, bridges_roads, power_plants_grid, niobium, rail, nickel, water,
#   building_materials, engineering_epc, graphite, port_ownership, port_cranes, wind,
#   lithium, fission_smr, copper, balsa.
# Logged 1 new + 8 CapEx-fill upgrades (4 US / 2 PRC / 3 allied / 0 other):
#   allied rail NEW: ohla_santiago_l7_stations_g5g6_71p8m_eur_2026 (~USD 81.85m).
#   prc other_renewables CapEx-fill: huawei_aggreko_amazonas_bess_2026 (USD 165m).
#   us water CapEx-fill: fcx_el_abra_desal_aqueduct_2026 (USD 7500m).
#   us engineering_epc CapEx-fill: oceaneering_petrobras_umbilicals_2024 (USD 120m floor).
#   us engineering_epc CapEx-fill: cbi_vmos_punta_colorada_storage_2025 (USD 100m floor).
#   prc port_cranes CapEx-fill: zpmc_dpworld_lirquen_2022 (USD 45m).
#   allied lithium CapEx-fill: rio_tinto_codelco_maricunga_ceol_2026 (USD 900m).
#   allied copper CapEx-fill: sandvik_marmato_ug_sek250m_2026 (~USD 25.24m).
#   us solar CapEx-fill: aes_panama_pese_10mw_2021 (USD 50m floor).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: bridges_roads, power_plants_grid, niobium, nickel,
#   building_materials, graphite, port_ownership, wind, fission_smr, balsa
#   (catalog dense; holdovers unsigned; COP/CLP/PEN/RAP/Huaxin–CSN/Xinhai MoU skipped).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 235: us397 / prc369 / allied387 / other91 (n=1244).
shuffle_seed: 20261235
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/other_renewables
- energy/solar
- infrastructure/bridges_roads
- energy/power_plants_grid
- resources/niobium
- infrastructure/rail
- resources/nickel
- resources/water
- infrastructure/building_materials
- infrastructure/engineering_epc
- resources/graphite
- infrastructure/port_ownership
- infrastructure/port_cranes
- energy/wind
- resources/lithium
- energy/fission_smr
- resources/copper
- resources/balsa
rows_found_this_cycle:
  energy/other_renewables: 1
  energy/solar: 1
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 0
  resources/niobium: 0
  infrastructure/rail: 1
  resources/nickel: 0
  resources/water: 1
  infrastructure/building_materials: 0
  infrastructure/engineering_epc: 2
  resources/graphite: 0
  infrastructure/port_ownership: 0
  infrastructure/port_cranes: 1
  energy/wind: 0
  resources/lithium: 1
  energy/fission_smr: 0
  resources/copper: 1
  resources/balsa: 0
rows_by_side_this_cycle:
  us: 4
  prc: 2
  allied: 3
  other: 0
thin_topup_after_shuffle:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0

# === Cycle 234 (seed 20261234) — prior ===
# Logged 0 new + 9 CapEx-fill: ACA Transnordestina; CAMCE Punta Huete; Neoenergia Guará 2;
#   EPR Régis; CSCEC Litoral; Jiangxi Cascabel; Fortescue Cañariaco; Sandvik CoMinVi;
#   Epiroc Peru.
# Active after 234: us397/prc369/allied386/other91 (n=1243).

# === Cycle 233 (seed 20261233) — prior ===
# Logged 0 new + 9 CapEx-fill: CDB–BNDES; CAF Medellín/Trivia; Alstom Salvador;
#   Neoenergia Ilhabela; Statkraft Gran Sul; Mota-Engil Sertões; Cagece desal;
#   JICA Chachimbiro.
# Active after 233: us397/prc369/allied386/other91 (n=1243).
