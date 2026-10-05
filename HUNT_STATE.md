updated: 2026-10-05
cycle: 233
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 234 shuffle_seed=20261234; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us397/prc369/allied386); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-234 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 233) ===
# Filled this cycle (CapEx-fills): Brazil×engineering_epc CapEx-fill (prc CDB–BNDES RMB 5bn
#   ~USD 745.05m), Colombia×rail CapEx-fill (allied CAF Medellín/Santiago ~USD 228.00m),
#   Brazil×rail CapEx-fill (allied CAF Trivia ~USD 570.00m; allied Alstom Salvador
#   ~USD 121.86m), Brazil×power_plants_grid CapEx-fill (allied Neoenergia Ilhabela
#   ~USD 38.52m), Brazil×wind CapEx-fill (allied Statkraft Gran Sul ~USD 288.90m),
#   Brazil×bridges_roads CapEx-fill (allied Mota-Engil Rota dos Sertões ~USD 828.18m),
#   Brazil×water CapEx-fill (other Cagece Fortaleza desal ~USD 597.06m), Ecuador×
#   other_renewables CapEx-fill (allied JICA Chachimbiro ~USD 41.88m).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (honest US residual — blank-USD CapEx exhausted).
# PRC equal-budget: CDB–BNDES RMB 5bn CapEx-fill; holdovers unsigned.

# === Cycle 233 (seed 20261233) ===
# Shuffled order (BRIEF.md numbered + Random(20261233).shuffle): engineering_epc,
#   niobium, lithium, rail, fission_smr, power_plants_grid, balsa, wind, nickel,
#   bridges_roads, graphite, water, building_materials, copper, other_renewables,
#   solar, port_ownership, port_cranes.
# Logged 0 new + 9 CapEx-fill upgrades (0 US / 1 PRC / 7 allied / 1 other; ≥1/3 US hunt
#   budget via honest residual sweeps):
#   prc engineering_epc CapEx-fill: cdb_bndes_rmb5bn_2024 (~USD 745.05m).
#   allied rail CapEx-fill: caf_medellin_santiago_metro_2024 (USD 228.00m).
#   allied rail CapEx-fill: caf_trivia_sp_maint_2025 (USD 570.00m).
#   allied rail CapEx-fill: alstom_salvador_metro_10trains_632p7m_2026 (~USD 121.86m).
#   allied power_plants_grid CapEx-fill: neoenergia_ilhabela_200m_brl_2026 (~USD 38.52m).
#   allied wind CapEx-fill: statkraft_gran_sul_280mw_2026 (~USD 288.90m).
#   allied bridges_roads CapEx-fill: mota_engil_rota_dos_sertoes_43bn_2026 (~USD 828.18m).
#   other water CapEx-fill: cagece_dessal_fortaleza_auth_2026 (~USD 597.06m).
#   allied other_renewables CapEx-fill: jica_chachimbiro_ecuador_2024 (~USD 41.88m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: niobium, lithium, fission_smr, balsa, nickel, graphite,
#   building_materials, copper, solar, port_ownership, port_cranes
#   (catalog dense; CBMM/EnergyX/SQM/Konecranes/ZPMC/Graphcoa/Holcim/Freeport/
#   Sandvik/Nextracker/Hutchison/ICTSI/holdovers already logged; COP/CLP/PEN/
#   RAP-as-CapEx/Huaxin–CSN skipped).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 233: us397 / prc369 / allied386 / other91 (n=1243).
shuffle_seed: 20261233
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- resources/niobium
- resources/lithium
- infrastructure/rail
- energy/fission_smr
- energy/power_plants_grid
- resources/balsa
- energy/wind
- resources/nickel
- infrastructure/bridges_roads
- resources/graphite
- resources/water
- infrastructure/building_materials
- resources/copper
- energy/other_renewables
- energy/solar
- infrastructure/port_ownership
- infrastructure/port_cranes
rows_found_this_cycle:
  infrastructure/engineering_epc: 1
  resources/niobium: 0
  resources/lithium: 0
  infrastructure/rail: 3
  energy/fission_smr: 0
  energy/power_plants_grid: 1
  resources/balsa: 0
  energy/wind: 1
  resources/nickel: 0
  infrastructure/bridges_roads: 1
  resources/graphite: 0
  resources/water: 1
  infrastructure/building_materials: 0
  resources/copper: 0
  energy/other_renewables: 1
  energy/solar: 0
  infrastructure/port_ownership: 0
  infrastructure/port_cranes: 0
rows_by_side_this_cycle:
  us: 0
  prc: 1
  allied: 7
  other: 1
thin_topup_after_shuffle:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0

# === Cycle 232 (seed 20261232) — prior ===
# Logged 0 new + 9 CapEx-fill: Metro SP L17; FCC/CICSA Saltillo; COMSA QI T3; CRRC Pachuca;
#   Ecorodovias Rota das Gerais; DNIT Porto Murtinho; ACCIONA Los Cabos; Neoenergia
#   Brasília; Neoenergia Coelba litoral.
# Active after 232: us397/prc369/allied386/other91 (n=1243).

# === Cycle 231 (seed 20261231) — prior ===
# Logged 0 new + 9 CapEx-fill: ACCIONA SP L6; Copel 2026; Neoenergia 50bn; Redeia LatAm;
#   GS Inima ES; Siemens/Sonda ETCS; CCECC/Aldesa QI; Azevedo Rota Mogiana; Votorantim 2.7bn.
# Active after 231: us397/prc369/allied386/other91 (n=1243).
