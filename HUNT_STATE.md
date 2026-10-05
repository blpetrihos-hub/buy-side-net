updated: 2026-10-05
cycle: 234
remote: present
active_layer: energy
active_subcategory: fission_smr
next_query: Cycle 235 shuffle_seed=20261235; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us397/prc369/allied386); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only). No U.S. territories.
next_row_id: (follow cycle-235 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 234) ===
# Filled this cycle (CapEx-fills): Brazil×rail CapEx-fill (allied ACA Transnordestina
#   ~USD 60.25m), Nicaragua×engineering_epc CapEx-fill (prc CAMCE Punta Huete
#   ~USD 428.35m), Brazil×power_plants_grid CapEx-fill (allied Neoenergia Guará 2
#   ~USD 6.16m), Brazil×bridges_roads CapEx-fill (other EPR Régis Bittencourt
#   ~USD 1386.72m), Nicaragua×bridges_roads CapEx-fill (prc CSCEC Litoral Pacífico
#   Fase 2 ~USD 268.92m), Ecuador×copper CapEx-fill (prc Jiangxi Cascabel
#   ~USD 1148.78m), Peru×copper CapEx-fill (allied Fortescue Cañariaco ~USD 98.30m;
#   allied Epiroc Pit Viper ~USD 21.20m), Mexico×copper CapEx-fill (allied Sandvik
#   CoMinVi ~USD 34.33m).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (honest US residual — blank-USD CapEx exhausted).
# PRC equal-budget: CAMCE Punta Huete; CSCEC Litoral Pacífico Fase 2; Jiangxi Cascabel.

# === Cycle 234 (seed 20261234) ===
# Shuffled order (BRIEF.md numbered + Random(20261234).shuffle): balsa,
#   other_renewables, nickel, lithium, rail, building_materials, fission_smr,
#   engineering_epc, water, niobium, port_cranes, wind, power_plants_grid,
#   graphite, copper, bridges_roads, port_ownership, solar.
# Logged 0 new + 9 CapEx-fill upgrades (0 US / 3 PRC / 5 allied / 1 other; ≥1/3 US hunt
#   budget via honest residual sweeps):
#   allied rail CapEx-fill: aca_transnordestina_sps04_2026 (~USD 60.25m).
#   prc engineering_epc CapEx-fill: camce_punta_huete_airport_credit_2p875bn_rmb_2024
#     (~USD 428.35m).
#   allied power_plants_grid CapEx-fill: neoenergia_guara2_32m_brl_2026 (~USD 6.16m).
#   other bridges_roads CapEx-fill: epr_regis_bittencourt_7p2bn_2026 (~USD 1386.72m).
#   prc bridges_roads CapEx-fill: cscec_litoral_pacifico_fase2_nicaragua_2024
#     (~USD 268.92m).
#   prc copper CapEx-fill: jiangxi_copper_solgold_cascabel_2026 (~USD 1148.78m).
#   allied copper CapEx-fill: fortescue_canariaco_alta_copper_2026 (~USD 98.30m).
#   allied copper CapEx-fill: sandvik_cominvi_mexico_sek340m_2026 (~USD 34.33m).
#   allied copper CapEx-fill: epiroc_peru_pit_viper_sek210m_2026 (~USD 21.20m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: balsa, other_renewables, nickel, lithium, building_materials,
#   fission_smr, water, niobium, port_cranes, wind, graphite, port_ownership, solar
#   (catalog dense; Plantabal/JICA/Jervois/EnergyX/Holcim/CBMM/Konecranes/Vestas/
#   Graphcoa/Hutchison/Nextracker already logged; RAP/Huaxin–CSN/Xinhai MoU/Aldesa
#   EUR/ISA Madeira unwind skipped).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail
#   prefeasibility; CHEC San Carlos Contraloría aval only.
# Active after cycle 234: us397 / prc369 / allied386 / other91 (n=1243).
shuffle_seed: 20261234
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/balsa
- energy/other_renewables
- resources/nickel
- resources/lithium
- infrastructure/rail
- infrastructure/building_materials
- energy/fission_smr
- infrastructure/engineering_epc
- resources/water
- resources/niobium
- infrastructure/port_cranes
- energy/wind
- energy/power_plants_grid
- resources/graphite
- resources/copper
- infrastructure/bridges_roads
- infrastructure/port_ownership
- energy/solar
rows_found_this_cycle:
  resources/balsa: 0
  energy/other_renewables: 0
  resources/nickel: 0
  resources/lithium: 0
  infrastructure/rail: 1
  infrastructure/building_materials: 0
  energy/fission_smr: 0
  infrastructure/engineering_epc: 1
  resources/water: 0
  resources/niobium: 0
  infrastructure/port_cranes: 0
  energy/wind: 0
  energy/power_plants_grid: 1
  resources/graphite: 0
  resources/copper: 4
  infrastructure/bridges_roads: 2
  infrastructure/port_ownership: 0
  energy/solar: 0
rows_by_side_this_cycle:
  us: 0
  prc: 3
  allied: 5
  other: 1
thin_topup_after_shuffle:
- resources/balsa
- resources/nickel
- energy/fission_smr
thin_topup_rows: 0

# === Cycle 233 (seed 20261233) — prior ===
# Logged 0 new + 9 CapEx-fill: CDB–BNDES; CAF Medellín/Trivia; Alstom Salvador;
#   Neoenergia Ilhabela; Statkraft Gran Sul; Mota-Engil Sertões; Cagece desal;
#   JICA Chachimbiro.
# Active after 233: us397/prc369/allied386/other91 (n=1243).

# === Cycle 232 (seed 20261232) — prior ===
# Logged 0 new + 9 CapEx-fill: Metro SP L17; FCC/CICSA; COMSA QI T3; CRRC Pachuca;
#   Ecorodovias; DNIT Porto Murtinho; ACCIONA Los Cabos; Neoenergia Brasília/Coelba.
# Active after 232: us397/prc369/allied386/other91 (n=1243).
