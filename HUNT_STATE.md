updated: 2026-10-05
cycle: 232
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 233 shuffle_seed=20261233; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us397/prc369/allied386); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-233 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 232) ===
# Filled this cycle (CapEx-fills): Brazil×rail CapEx-fill (other Metro SP Linha 17 Phase 1
#   ~USD 1136.34m), Mexico×rail CapEx-fill (allied FCC/CICSA Saltillo ~USD 1799.79m;
#   allied COMSA QI Tramo 3 ~USD 192.83m; prc CRRC México–Pachuca ~USD 330.43m),
#   Brazil×bridges_roads CapEx-fill (other Ecorodovias Rota das Gerais ~USD 2503.80m;
#   other DNIT Porto Murtinho ~USD 90.91m), Mexico×water CapEx-fill (allied ACCIONA
#   Los Cabos ~USD 153.33m), Brazil×power_plants_grid CapEx-fill (allied Neoenergia
#   Brasília ~USD 597.06m; allied Neoenergia Coelba litoral ~USD 1348.19m).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (honest US residual — blank-USD CapEx exhausted).
# PRC equal-budget: CRRC México–Pachuca CapEx-fill; holdovers unsigned.

# === Cycle 232 (seed 20261232) ===
# Shuffled order (BRIEF.md numbered + Random(20261232).shuffle): port_ownership,
#   building_materials, copper, rail, balsa, engineering_epc, bridges_roads,
#   port_cranes, fission_smr, lithium, niobium, graphite, other_renewables, nickel,
#   solar, water, wind, power_plants_grid.
# Logged 0 new + 9 CapEx-fill upgrades (0 US / 1 PRC / 5 allied / 3 other; ≥1/3 US hunt
#   budget via honest residual sweeps):
#   other rail CapEx-fill: metro_sp_linha17_phase1_5p9bn_brl_2026 (~USD 1136.34m).
#   allied rail CapEx-fill: fcc_cicsa_saltillo_santa_catarina_2025 (~USD 1799.79m).
#   allied rail CapEx-fill: comsa_qi_tramo3_3411p8m_mxn_2026 (~USD 192.83m).
#   prc rail CapEx-fill: crrc_mexico_pachuca_trains_2025 (~USD 330.43m).
#   other bridges_roads CapEx-fill: ecorodovias_rota_gerais_13bn_2026 (~USD 2503.80m).
#   other bridges_roads CapEx-fill: dnit_porto_murtinho_access_472m_brl_2025 (~USD 90.91m).
#   allied water CapEx-fill: acciona_los_cabos_desal_mexico (~USD 153.33m).
#   allied power_plants_grid CapEx-fill: neoenergia_brasilia_3p1bn_brl_2026_2030
#     (~USD 597.06m).
#   allied power_plants_grid CapEx-fill: neoenergia_coelba_litoral_7bn_brl_2026
#     (~USD 1348.19m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: port_ownership, building_materials, copper, balsa,
#   engineering_epc, port_cranes, fission_smr, lithium, niobium, graphite,
#   other_renewables, nickel, solar, wind
#   (catalog dense; Hutchison/ICTSI/Votorantim/Freeport/ACCIONA/Konecranes/ZPMC/
#   CBMM/Graphcoa/Ormat/Jervois/Nextracker/Vestas/holdovers already logged).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 232: us397 / prc369 / allied386 / other91 (n=1243).
shuffle_seed: 20261232
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_ownership
- infrastructure/building_materials
- resources/copper
- infrastructure/rail
- resources/balsa
- infrastructure/engineering_epc
- infrastructure/bridges_roads
- infrastructure/port_cranes
- energy/fission_smr
- resources/lithium
- resources/niobium
- resources/graphite
- energy/other_renewables
- resources/nickel
- energy/solar
- resources/water
- energy/wind
- energy/power_plants_grid
rows_found_this_cycle:
  infrastructure/port_ownership: 0
  infrastructure/building_materials: 0
  resources/copper: 0
  infrastructure/rail: 4
  resources/balsa: 0
  infrastructure/engineering_epc: 0
  infrastructure/bridges_roads: 2
  infrastructure/port_cranes: 0
  energy/fission_smr: 0
  resources/lithium: 0
  resources/niobium: 0
  resources/graphite: 0
  energy/other_renewables: 0
  resources/nickel: 0
  energy/solar: 0
  resources/water: 1
  energy/wind: 0
  energy/power_plants_grid: 2
rows_by_side_this_cycle:
  us: 0
  prc: 1
  allied: 5
  other: 3
thin_topup_after_shuffle:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0

# === Cycle 231 (seed 20261231) — prior ===
# Logged 0 new + 9 CapEx-fill: ACCIONA SP L6; Copel 2026; Neoenergia 50bn; Redeia LatAm;
#   GS Inima ES; Siemens/Sonda ETCS; CCECC/Aldesa QI; Azevedo Rota Mogiana; Votorantim 2.7bn.
# Active after 231: us397/prc369/allied386/other91 (n=1243).

# === Cycle 230 (seed 20261230) — prior ===
# Logged 0 new + 9 CapEx-fill: Vestas Aquiraz; Vergnet Claybury; Votorantim plan 3.1bn;
#   CRRC SP Metro; Mota-Engil CDMX L3; OHLA BR-040; SGBH GATE; Enel Brasil; ACCIONA Paraíba.
# Active after 230: us397/prc369/allied386/other91 (n=1243).

# === Cycle 229 (seed 20261229) — prior ===
# Logged 1 new + 8 CapEx-fill: CMPC Rio Grande TUP; St George A$60m; CTG Serra; Statkraft/
#   WEG Seabra; VLI FCA; Alstom Mexico DMU; Sacyr Fortaleza; ACCIONA BRK; WEG transformers.
# Active after 229: us397/prc369/allied386/other91 (n=1243).

# === Cycle 228 (seed 20261228) — prior ===
# Logged 0 new + 9 CapEx-fill: Votorantim Xambioá/FY2025; ISA FY2025; Neoenergia FY2025;
#   State Grid GATE; Hutchison EIT; ICTSI Rio; Portonave quay; CBMM R$13bn.
# Active after 228: us397/prc369/allied385/other91 (n=1242).
