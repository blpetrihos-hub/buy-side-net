updated: 2026-10-04
cycle: 200
remote: present
active_layer: resources
active_subcategory: nickel
next_query: Cycle 201 shuffle_seed=20261201; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us393/prc367/allied353); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB corridors), Venezuela (beyond Tocoma/Macagua; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU. No U.S. territories.
next_row_id: (follow cycle-201 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 200) ===
# Filled this cycle: Brazil×bridges_roads (other Azevedo Rota Mogiana R$9.4bn),
#   Peru×bridges_roads (other COVIPERÚ Puente Asia USD 50.1m), Argentina×other_renewables
#   (other Copahue geothermal USD 46.1m proxy), Brazil×other_renewables (other WEG
#   Itajaí BESS R$280m), Chile×engineering_epc (us AWS Huechuraba USD 205m),
#   Brazil×power_plants_grid (allied EDP SA R$7bn 2025–26), Brazil×rail (other Metro SP
#   Linha 17 phase 1 R$5.9bn).
# Still thin/empty priority cells: Haiti (beyond RN2/WB), Venezuela (beyond hydro rehab),
#   Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (AWS Huechuraba, EXIM/DFC/AES/Freeport/Wabtec/Equinix
#   sweeps) — 1 new U.S. row (AWS). PRC equal-budget misses: GATE/SPIC/MMG/BYD BESS/
#   Goldwind CapEx already logged.

# === Cycle 200 (seed 20261200) ===
# Shuffled order (BRIEF.md numbered + Random(20261200).shuffle): bridges_roads,
#   other_renewables, nickel, copper, engineering_epc, balsa, graphite, solar, niobium,
#   wind, fission_smr, port_cranes, rail, power_plants_grid, building_materials,
#   port_ownership, water, lithium.
# Logged 7 new sourced rows (1 US / 0 PRC / 1 allied / 5 other; ≥1/3 US hunt budget spent):
#   other bridges_roads: azevedo_rota_mogiana_9p4bn_brl_2026 (R$9.4bn).
#   other bridges_roads: coviperu_puente_asia_50p1m_2026 (USD 50.1m).
#   other other_renewables: adi_nqn_copahue_geothermal_46p1m_2026 (USD 46.1m proxy).
#   other other_renewables: weg_itajai_bess_280m_brl_2026 (R$280m).
#   us engineering_epc: aws_huechuraba_205m_chile_2026 (USD 205m).
#   allied power_plants_grid: edp_south_america_7bn_brl_2025_2026 (R$7bn).
#   other rail: metro_sp_linha17_phase1_5p9bn_brl_2026 (R$5.9bn).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: nickel, copper, balsa, graphite, solar, niobium, wind,
#   fission_smr, port_cranes, building_materials, port_ownership, water, lithium
#   (catalog dense; PRC GATE/SPIC/MMG/BYD already logged; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 200: us393 / prc367 / allied353 / other78 (n=1191).
shuffle_seed: 20261200
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- energy/other_renewables
- resources/nickel
- resources/copper
- infrastructure/engineering_epc
- resources/balsa
- resources/graphite
- energy/solar
- resources/niobium
- energy/wind
- energy/fission_smr
- infrastructure/port_cranes
- infrastructure/rail
- energy/power_plants_grid
- infrastructure/building_materials
- infrastructure/port_ownership
- resources/water
- resources/lithium
rows_found_this_cycle:
  infrastructure/bridges_roads: 2
  energy/other_renewables: 2
  resources/nickel: 0
  resources/copper: 0
  infrastructure/engineering_epc: 1
  resources/balsa: 0
  resources/graphite: 0
  energy/solar: 0
  resources/niobium: 0
  energy/wind: 0
  energy/fission_smr: 0
  infrastructure/port_cranes: 0
  infrastructure/rail: 1
  energy/power_plants_grid: 1
  infrastructure/building_materials: 0
  infrastructure/port_ownership: 0
  resources/water: 0
  resources/lithium: 0
rows_by_side_this_cycle:
  us: 1
  prc: 0
  allied: 1
  other: 5
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
  rows_found: 0

# === Cycle 199 (seed 20261199) — prior ===
# Logged 5 new + 1 Graphcoa CapEx upgrade (1 US / 1 PRC / 0 new allied / 3 other).
# Active after: us392 / prc367 / allied352 / other73 (n=1184). Thin balsa/nickel/fission_smr dry.

# === Cycle 198 (seed 20261198) — prior ===
# Logged 6 new + 1 CBMM CapEx upgrade (1 US / 1 PRC / 2 allied / 2 other).
# Active after: us391 / prc366 / allied352 / other70 (n=1179). Thin balsa/nickel/fission_smr dry.

# === Cycle 197 (seed 20261197) — prior ===
# Logged 6 new + 1 PRC CapEx upgrade (2 US / 0 new PRC / 3 allied / 1 other).
# Active after: us390 / prc365 / allied350 / other68 (n=1173). Thin balsa/nickel/fission_smr dry.

# === Cycle 196 (seed 20261196) — prior ===
# Logged 5 sourced rows (2 US / 2 PRC / 1 allied / 0 other). Active after:
# us388 / prc365 / allied347 / other67 (n=1167). Thin balsa/nickel/fission_smr dry.

# === Cycle 195 (seed 20261195) — prior ===
# Logged 8 sourced rows (3 US / 1 PRC / 3 allied / 1 other). Active after:
# us386 / prc363 / allied346 / other67 (n=1162). Thin balsa/nickel/fission_smr dry.

# === Cycle 194 (seed 20261194) ===
# Shuffled order (BRIEF.md numbered + Random(20261194).shuffle): engineering_epc,
#   fission_smr, lithium, copper, graphite, wind, balsa, power_plants_grid, port_cranes,
#   other_renewables, nickel, rail, port_ownership, water, bridges_roads,
#   building_materials, niobium, solar.
# Logged 7 sourced rows (4 US / 1 PRC / 1 allied / 1 other; ≥1/3 US hunt budget spent):
#   us engineering_epc: equinix_sp6_114m_2026 (USD 114m).
#   us engineering_epc: equinix_st5_130m_chile_2025 (USD 130m).
#   us engineering_epc: ascenty_ai_1p2bn_brazil_2026 (USD 1.2bn).
#   us engineering_epc: scala_chile_pf_328m_2025 (USD 328m).
#   prc other_renewables: powerchina_ecuador_renewables_400m_2025 (USD 400m).
#   allied bridges_roads: bcie_nicaragua_xi_tramo_b_97m_2026 (USD 97m).
#   other building_materials: unacem_fy2025_capex_698p8m_pen (PEN 698.8m).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: fission_smr, lithium, copper, graphite, wind, balsa,
#   power_plants_grid, port_cranes, nickel, rail, port_ownership, water, niobium, solar
#   (catalog dense; AES Villagrán/CEEC Coremas/El Abra mill/Fénix RIGI already logged;
#   holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 194: us383 / prc362 / allied343 / other66 (n=1154).
shuffle_seed: 20261194
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- energy/fission_smr
- resources/lithium
- resources/copper
- resources/graphite
- energy/wind
- resources/balsa
- energy/power_plants_grid
- infrastructure/port_cranes
- energy/other_renewables
- resources/nickel
- infrastructure/rail
- infrastructure/port_ownership
- resources/water
- infrastructure/bridges_roads
- infrastructure/building_materials
- resources/niobium
- energy/solar
rows_found_this_cycle:
  infrastructure/engineering_epc: 4
  energy/fission_smr: 0
  resources/lithium: 0
  resources/copper: 0
  resources/graphite: 0
  energy/wind: 0
  resources/balsa: 0
  energy/power_plants_grid: 0
  infrastructure/port_cranes: 0
  energy/other_renewables: 1
  resources/nickel: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  resources/water: 0
  infrastructure/bridges_roads: 1
  infrastructure/building_materials: 1
  resources/niobium: 0
  energy/solar: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 1
  other: 1
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
  rows_found: 0

# === Cycle 193 (seed 20261193) ===
# Shuffled order (BRIEF.md numbered + Random(20261193).shuffle): bridges_roads, copper,
#   other_renewables, graphite, rail, port_cranes, lithium, nickel, solar, balsa,
#   niobium, fission_smr, wind, water, port_ownership, power_plants_grid,
#   building_materials, engineering_epc.
# Logged 6 sourced rows (4 US / 0 PRC / 1 allied / 1 other): Sacyr Ruta 68; Southern
#   Copper 2026 CapEx; Equinix MO2/RJ3/ST2/Bogotá DC2.
# Active after cycle 193: us379 / prc361 / allied342 / other65 (n=1147).

# === Cycle 192 (seed 20261192) ===
# Shuffled order (BRIEF.md numbered + Random(20261192).shuffle): building_materials,
#   fission_smr, lithium, engineering_epc, port_cranes, other_renewables, port_ownership,
#   copper, balsa, solar, graphite, power_plants_grid, nickel, water, wind, rail,
#   bridges_roads, niobium.
# Logged 6 sourced rows (2 US / 0 PRC / 2 allied / 2 other): Pacasmayo CapEx; Ascenty
#   SPO05/SPO06; Novopan biomass; Aggreko LatAm CapEx; COMSA QI Tramo III.
# Active after cycle 192: us375 / prc361 / allied341 / other64 (n=1141).

# === Cycle 191 (seed 20261191) ===
# Shuffled order (BRIEF.md codebook + Random(20261191)): copper, building_materials,
#   port_cranes, solar, power_plants_grid, port_ownership, bridges_roads, water,
#   fission_smr, lithium, nickel, wind, rail, other_renewables, niobium, balsa,
#   graphite, engineering_epc.
# Logged 8 sourced rows (1 US / 0 PRC / 6 allied / 1 other; ≥1/3 US hunt budget spent):
#   us copper: fcx_el_abra_sulfolix_741m_2025 (USD 741m).
#   allied building_materials: holcim_mexico_ecopact_silos_56mdp_2025 (MXN 56m).
#   allied port_cranes: timsa_ertg_manzanillo_70m_mxn_2026 (MXN 70m+).
#   allied power_plants_grid: engie_jaguara_expansion_1p2bn_brl_2026 (R$1.2bn).
#   allied power_plants_grid: engie_jaguara_modernization_500m_brl_2026 (R$500m).
#   other fission_smr: finep_diamante_mrn_50m_brl_2025 (R$50m).
#   allied wind: engie_pemuco_chequenes_228m_2025 (USD 228m).
#   allied wind: engie_pampa_fidelia_461m_2025 (USD 461m).
# Thin top-up (balsa/nickel/fission_smr): 1 fission_smr; balsa/nickel dry.
# Equal-budget misses: solar, port_ownership, bridges_roads, water, lithium, nickel,
#   rail, other_renewables, niobium, balsa, graphite, engineering_epc (catalog dense;
#   Campano/La Esperanza/NADBank Sonora/Bechtel-EIMISA already logged; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 191: us373 / prc361 / allied339 / other62 (n=1135).

# === Cycle 190 (seed 20261190) ===
# Shuffled order (BRIEF.md codebook + Random(20261190)): niobium, copper, water,
#   wind, solar, port_ownership, power_plants_grid, balsa, fission_smr, bridges_roads,
#   rail, graphite, lithium, engineering_epc, port_cranes, building_materials, nickel,
#   other_renewables.
# Logged 4 sourced rows (0 US / 0 PRC / 4 allied / 0 other; ≥1/3 US hunt budget spent):
#   allied water: aqualia_ptar_chincha_96p5m_2025 (USD 96.5m).
#   allied solar: scatec_barzalosa_121m_2026 (USD 121m).
#   allied rail: sacyr_fortaleza_metro_leste_1230m_brl_2026 (R$1,230,612,738.18).
#   allied rail: mota_engil_cdmx_metro_l3_25180m_mxn_2026 (MXN 25,180m offer).
# Dropped pre-commit: aes_ecopetrol_jk1_jk2_49pct_25p5m_2026 (duplicate of
#   ecopetrol_jk1_jk2_49pct_25p5m_2026 / other from cycle 177).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: niobium, copper, wind, port_ownership, power_plants_grid, balsa,
#   fission_smr, bridges_roads, graphite, lithium, engineering_epc, port_cranes,
#   building_materials, nickel, other_renewables (catalog dense; holdovers unsigned;
#   El Abra/EXIM Argentina framework/Graphcoa Jordânia already logged).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 190: us372 / prc361 / allied333 / other61 (n=1127).
shuffle_seed: 20261190
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- resources/copper
- resources/water
- energy/wind
- energy/solar
- infrastructure/port_ownership
- energy/power_plants_grid
- resources/balsa
- energy/fission_smr
- infrastructure/bridges_roads
- infrastructure/rail
- resources/graphite
- resources/lithium
- infrastructure/engineering_epc
- infrastructure/port_cranes
- infrastructure/building_materials
- resources/nickel
- energy/other_renewables
rows_found_this_cycle:
  resources/niobium: 0
  resources/copper: 0
  resources/water: 1
  energy/wind: 0
  energy/solar: 1
  infrastructure/port_ownership: 0
  energy/power_plants_grid: 0
  resources/balsa: 0
  energy/fission_smr: 0
  infrastructure/bridges_roads: 0
  infrastructure/rail: 2
  resources/graphite: 0
  resources/lithium: 0
  infrastructure/engineering_epc: 0
  infrastructure/port_cranes: 0
  infrastructure/building_materials: 0
  resources/nickel: 0
  energy/other_renewables: 0
rows_by_side_this_cycle:
  us: 0
  prc: 0
  allied: 4
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
  rows_found: 0

# === Cycle 189 (seed 20261189) ===
# Shuffled order (BRIEF.md codebook + Random(20261189)): power_plants_grid,
#   bridges_roads, water, building_materials, lithium, wind, balsa, rail, fission_smr,
#   port_ownership, engineering_epc, port_cranes, solar, copper, other_renewables,
#   niobium, graphite, nickel.
# Logged 7 sourced rows (2 US / 0 PRC / 2 allied / 3 other; ≥1/3 US hunt budget spent):
#   us power_plants_grid: black_veatch_andes_aet_ustda_2021 (FS; CapEx blank).
#   other bridges_roads: mopc_py04_acaray_lote1_242296m_pyg_2025 (G. 242.296m).
#   allied bridges_roads: mopc_py04_caminos_sur_lote2_204140m_pyg_2025 (G. 204.140m).
#   other building_materials: votorantim_brazil_plan_3p1bn_invested_2026 (R$3.1bn).
#   allied building_materials: holcim_pacasmayo_aspi_1850370k_pen_2026 (S/1,850.37m).
#   us engineering_epc: fluor_ica_mexico_divest_175m_2026 (USD 175m).
#   other wind: terralia_el_chorro_cfe_2026 (CFE mixto; CapEx blank).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Active after cycle 189: us372 / prc361 / allied329 / other61 (n=1123).

# === Cycle 188 (seed 20261188) ===
# Shuffled order (BRIEF.md numbered + Random(20261188)): building_materials,
#   engineering_epc, graphite, solar, nickel, other_renewables, fission_smr, copper,
#   water, bridges_roads, port_ownership, port_cranes, wind, niobium, lithium, rail,
#   power_plants_grid, balsa.
# Logged 5 sourced rows (1 US / 0 PRC / 2 allied / 2 other; ≥1/3 US hunt budget spent):
#   other building_materials: unacem_q2_2026_capex_3531m_pen (PEN 353.1m).
#   other building_materials: votorantim_brazil_plan_2p7bn_invested_2025 (R$2.7bn).
#   us power_plants_grid: impsa_tocoma_macagua_672mw_2026 (672 MW phase 1; CapEx blank).
#   allied rail: ani_bogota_belencito_284436m_cop_2026 (COP 284,436m).
#   allied rail: ani_pacifico_ferro_280522m_cop_2026 (COP 280,522m).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: engineering_epc, graphite, solar, nickel, other_renewables,
#   fission_smr, copper, water, bridges_roads, port_ownership, port_cranes, wind,
#   niobium, lithium, balsa (catalog dense; Bechtel-EIMISA / South Star / Atlas 3bn
#   refi / FCX / ENGIE / CCECC Aldesa QI already logged; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 188: us370 / prc361 / allied327 / other58 (n=1116).
shuffle_seed: 20261188
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- infrastructure/engineering_epc
- resources/graphite
- energy/solar
- resources/nickel
- energy/other_renewables
- energy/fission_smr
- resources/copper
- resources/water
- infrastructure/bridges_roads
- infrastructure/port_ownership
- infrastructure/port_cranes
- energy/wind
- resources/niobium
- resources/lithium
- infrastructure/rail
- energy/power_plants_grid
- resources/balsa
rows_found_this_cycle:
  infrastructure/building_materials: 2
  infrastructure/engineering_epc: 0
  resources/graphite: 0
  energy/solar: 0
  resources/nickel: 0
  energy/other_renewables: 0
  energy/fission_smr: 0
  resources/copper: 0
  resources/water: 0
  infrastructure/bridges_roads: 0
  infrastructure/port_ownership: 0
  infrastructure/port_cranes: 0
  energy/wind: 0
  resources/niobium: 0
  resources/lithium: 0
  infrastructure/rail: 2
  energy/power_plants_grid: 1
  resources/balsa: 0
rows_by_side_this_cycle:
  us: 1
  prc: 0
  allied: 2
  other: 2
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
  rows_found: 0

# === Cycle 187 (seed 20261187) ===
# Shuffled order (BRIEF.md numbered + Random(20261187)): bridges_roads, building_materials,
#   power_plants_grid, graphite, engineering_epc, fission_smr, nickel, other_renewables,
#   copper, lithium, balsa, water, port_cranes, port_ownership, wind, niobium, solar, rail.
# Logged 6 sourced rows (0 US / 0 PRC / 3 allied / 3 other; ≥1/3 US hunt budget spent):
#   allied bridges_roads: idb_haiti_les_cayes_rn2_69m_2026 (USD 69m).
#   other bridges_roads: dnit_porto_murtinho_access_472m_brl_2025 (R$472m).
#   allied bridges_roads: mopc_py15_fonplata_354m_2026 (USD 354.2m).
#   other bridges_roads: itaipu_ponte_bioceanica_103m_2026 (~USD 103m).
#   allied power_plants_grid: isa_energia_rm_370m_brl_1t26 (R$370m).
#   other power_plants_grid: copel_capex_2026_plan_3021m_brl (R$3.021bn).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: building_materials, graphite, engineering_epc, fission_smr, nickel,
#   other_renewables, copper, lithium, balsa, water, port_cranes, port_ownership, wind,
#   niobium, solar, rail (catalog dense; Votorantim / Graphcoa / Wabtec Contagem / Meitner /
#   Centaurus / ENGIE Libélula / FCX El Abra / AES / ZPMC Itapoá already logged;
#   holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 187: us369 / prc361 / allied325 / other56 (n=1111).
shuffle_seed: 20261187
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- infrastructure/building_materials
- energy/power_plants_grid
- resources/graphite
- infrastructure/engineering_epc
- energy/fission_smr
- resources/nickel
- energy/other_renewables
- resources/copper
- resources/lithium
- resources/balsa
- resources/water
- infrastructure/port_cranes
- infrastructure/port_ownership
- energy/wind
- resources/niobium
- energy/solar
- infrastructure/rail
rows_found_this_cycle:
  infrastructure/bridges_roads: 4
  infrastructure/building_materials: 0
  energy/power_plants_grid: 2
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  energy/fission_smr: 0
  resources/nickel: 0
  energy/other_renewables: 0
  resources/copper: 0
  resources/lithium: 0
  resources/balsa: 0
  resources/water: 0
  infrastructure/port_cranes: 0
  infrastructure/port_ownership: 0
  energy/wind: 0
  resources/niobium: 0
  energy/solar: 0
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 0
  prc: 0
  allied: 3
  other: 3
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
  rows_found: 0

# === Cycle 186 (seed 20261186) ===
# Shuffled order: other_renewables, power_plants_grid, graphite, water, solar, wind,
#   port_cranes, bridges_roads, building_materials, engineering_epc, lithium, copper,
#   niobium, fission_smr, rail, balsa, port_ownership, nickel.
# Logged 6 sourced rows (0 US / 1 PRC / 4 allied / 1 other; ≥1/3 US hunt budget spent):
#   prc other_renewables: edelmag_guerrico_8m_2026 (USD 8m; State Grid via CGE).
#   allied other_renewables: sonnedix_chile_refi_1p3bn_2026 (USD 1.3bn).
#   allied water: aguas_andinas_capex_189905m_clp_2025 (CLP 189,905m).
#   other bridges_roads: ecorodovias_rota_gerais_13bn_2026 (>R$13bn ANTT).
#   allied rail: efe_caf_ico_700m_2026 (USD 700m).
#   allied solar: wb_haiti_renewable_af_20m_2024 (USD 20m).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: power_plants_grid, graphite, wind, port_cranes, building_materials,
#   engineering_epc, lithium, copper, niobium, fission_smr, balsa, port_ownership, nickel
#   (catalog dense; AES Andes / ENGIE / PowerChina Coca Codo / Graphcoa / Fluence Azulão /
#   FQM Taca Taca / Progress Rail VLI / Wabtec MRS / CBMM / Meitner already logged;
#   holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 186: us369 / prc361 / allied322 / other53 (n=1105).
shuffle_seed: 20261186
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/other_renewables
- energy/power_plants_grid
- resources/graphite
- resources/water
- energy/solar
- energy/wind
- infrastructure/port_cranes
- infrastructure/bridges_roads
- infrastructure/building_materials
- infrastructure/engineering_epc
- resources/lithium
- resources/copper
- resources/niobium
- energy/fission_smr
- infrastructure/rail
- resources/balsa
- infrastructure/port_ownership
- resources/nickel
rows_found_this_cycle:
  energy/other_renewables: 2
  energy/power_plants_grid: 0
  resources/graphite: 0
  resources/water: 1
  energy/solar: 1
  energy/wind: 0
  infrastructure/port_cranes: 0
  infrastructure/bridges_roads: 1
  infrastructure/building_materials: 0
  infrastructure/engineering_epc: 0
  resources/lithium: 0
  resources/copper: 0
  resources/niobium: 0
  energy/fission_smr: 0
  infrastructure/rail: 1
  resources/balsa: 0
  infrastructure/port_ownership: 0
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 0
  prc: 1
  allied: 4
  other: 1
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
  rows_found: 0

# === Cycle 185 (seed 20261185) ===
# Shuffled order: water, lithium, fission_smr, copper, other_renewables, niobium,
#   graphite, bridges_roads, solar, wind, port_cranes, port_ownership, balsa, rail,
#   nickel, engineering_epc, building_materials, power_plants_grid.
# Logged 5 sourced rows (1 US / 2 PRC / 2 allied / 0 other; ≥1/3 US hunt budget):
#   allied copper: fqm_taca_taca_initial_capex_4232m_2026 (USD 4.232bn).
#   us solar: atlas_shangri_la_idb_113m_2024 (USD 113m).
#   allied power_plants_grid: engie_brasil_aneel_01_2026_15bn (~R$1.5bn).
#   prc power_plants_grid: cwe_cge_pitrufquen_14p2m_2026 (USD 14.23m).
#   prc copper: cr19g_mirador_south_pit_1537m_2026 (USD 1.537bn; proxy).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: water, lithium, fission_smr, other_renewables, niobium,
#   graphite, bridges_roads, wind, port_cranes, port_ownership, balsa, rail, nickel,
#   engineering_epc, building_materials (catalog dense; Sacyr Coquimbo / Vicuña RIGI
#   / AES Pacífico 1.745bn / ENGIE Peru Grupo1 award / Fluor ICA / Progress Rail
#   already logged; Halliburton O&G out of taxonomy; holdovers unsigned).
# Note: cycle-184 dfc_patria_pi_fund_v_75m_proposed (country=Regional) was
#   auto-archived by build_site_data as out-of-region; active tip after 184 was
#   us368/prc358/allied316/other52 (n=1094) before cycle-185 adds.
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 185: us369 / prc360 / allied318 / other52 (n=1099).
shuffle_seed: 20261185
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- resources/lithium
- energy/fission_smr
- resources/copper
- energy/other_renewables
- resources/niobium
- resources/graphite
- infrastructure/bridges_roads
- energy/solar
- energy/wind
- infrastructure/port_cranes
- infrastructure/port_ownership
- resources/balsa
- infrastructure/rail
- resources/nickel
- infrastructure/engineering_epc
- infrastructure/building_materials
- energy/power_plants_grid
rows_found_this_cycle:
  resources/water: 0
  resources/lithium: 0
  energy/fission_smr: 0
  resources/copper: 2
  energy/other_renewables: 0
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 0
  energy/solar: 1
  energy/wind: 0
  infrastructure/port_cranes: 0
  infrastructure/port_ownership: 0
  resources/balsa: 0
  infrastructure/rail: 0
  resources/nickel: 0
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  energy/power_plants_grid: 2
rows_by_side_this_cycle:
  us: 1
  prc: 2
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 184 (seed 20261184) ===
# Shuffled order: lithium, fission_smr, port_ownership, other_renewables, niobium,
#   bridges_roads, water, engineering_epc, building_materials, solar, wind, nickel,
#   power_plants_grid, balsa, port_cranes, rail, copper, graphite.
# Logged 6 sourced rows (1 US / 1 PRC / 4 allied / 0 other; ≥1/3 US hunt budget):
#   allied other_renewables: engie_bess_arica_cod_51m_2026 (USD 51m).
#   allied other_renewables: engie_bess_kallpa_69m_2026 (USD 69m).
#   allied other_renewables: engie_bess_lile_174m_2026 (USD 174m).
#   allied solar: grenergy_antofagasta1_seia_520m_2026 (USD 520m DIA; proxy).
#   prc power_plants_grid: nari_cge_parronal_casas_viejas_19p2m_2026 (USD 19.23m).
#   us engineering_epc: dfc_patria_pi_fund_v_75m_proposed (USD 75m proposed).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: lithium, fission_smr, port_ownership, niobium, bridges_roads,
#   water, building_materials, wind, nickel, balsa, port_cranes, rail, copper,
#   graphite (catalog dense; AES Andes hub / ARRAY Lupi / EXIM Argentina / Chilean
#   Cobalt LOI / Progress Rail VLI / Wabtec MRS / Albemarle TED / CWE Zapallar already
#   logged; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 184: us369 / prc358 / allied316 / other52 (n=1095).
shuffle_seed: 20261184
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/lithium
- energy/fission_smr
- infrastructure/port_ownership
- energy/other_renewables
- resources/niobium
- infrastructure/bridges_roads
- resources/water
- infrastructure/engineering_epc
- infrastructure/building_materials
- energy/solar
- energy/wind
- resources/nickel
- energy/power_plants_grid
- resources/balsa
- infrastructure/port_cranes
- infrastructure/rail
- resources/copper
- resources/graphite
rows_found_this_cycle:
  resources/lithium: 0
  energy/fission_smr: 0
  infrastructure/port_ownership: 0
  energy/other_renewables: 3
  resources/niobium: 0
  infrastructure/bridges_roads: 0
  resources/water: 0
  infrastructure/engineering_epc: 1
  infrastructure/building_materials: 0
  energy/solar: 1
  energy/wind: 0
  resources/nickel: 0
  energy/power_plants_grid: 1
  resources/balsa: 0
  infrastructure/port_cranes: 0
  infrastructure/rail: 0
  resources/copper: 0
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 4
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 183 (seed 20261183) ===
# Shuffled order: power_plants_grid, niobium, rail, nickel, balsa, port_ownership,
#   solar, fission_smr, copper, building_materials, port_cranes, water,
#   other_renewables, lithium, graphite, engineering_epc, wind, bridges_roads.
# Logged 4 sourced rows (0 US / 0 PRC / 4 allied / 0 other; ≥1/3 US hunt budget):
#   allied power_plants_grid: isa_energia_ie_madeira_49pct_1167m_2026 (R$1.167bn).
#   allied rail: caf_dorada_chiriguana_200m_2026 (USD 200m; BNamericas/CAF proxy).
#   allied bridges_roads: anillo_vial_periferico_190m_2026 (USD 190m).
#   allied bridges_roads: mota_engil_rota_dos_sertoes_43bn_2026 (R$4.3bn CapEx).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: niobium, nickel, balsa, port_ownership, solar, fission_smr,
#   copper, building_materials, port_cranes, water, other_renewables, lithium,
#   graphite, engineering_epc, wind (catalog dense; EXIM Guyana GTE / DFC Serra
#   Verde / Fluor ICA / AES Andes / Nextracker Casa dos Ventos / Freeport El Abra /
#   USTDA Ecuador CNEL-ARCONEL already logged; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 183: us368 / prc357 / allied312 / other52 (n=1089).
shuffle_seed: 20261183
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/power_plants_grid
- resources/niobium
- infrastructure/rail
- resources/nickel
- resources/balsa
- infrastructure/port_ownership
- energy/solar
- energy/fission_smr
- resources/copper
- infrastructure/building_materials
- infrastructure/port_cranes
- resources/water
- energy/other_renewables
- resources/lithium
- resources/graphite
- infrastructure/engineering_epc
- energy/wind
- infrastructure/bridges_roads
rows_found_this_cycle:
  energy/power_plants_grid: 1
  resources/niobium: 0
  infrastructure/rail: 1
  resources/nickel: 0
  resources/balsa: 0
  infrastructure/port_ownership: 0
  energy/solar: 0
  energy/fission_smr: 0
  resources/copper: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  resources/water: 0
  energy/other_renewables: 0
  resources/lithium: 0
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  energy/wind: 0
  infrastructure/bridges_roads: 2
rows_by_side_this_cycle:
  us: 0
  prc: 0
  allied: 4
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 182 (seed 20261182) ===
# Shuffled order: solar, other_renewables, fission_smr, niobium, nickel,
#   port_cranes, power_plants_grid, engineering_epc, rail, water, lithium,
#   port_ownership, balsa, wind, copper, graphite, bridges_roads,
#   building_materials.
# Logged 4 sourced rows (1 US / 0 PRC / 3 allied / 0 other; ≥1/3 US hunt budget):
#   allied other_renewables: grenergy_gabriela_cvc_dif_475m_2026 (USD 475m EV).
#   us engineering_epc: fluor_ica_fluor_daniel_divest_175m_2026 (USD 175m).
#   allied bridges_roads: sacyr_ruta_pie_de_monte_355m_2026 (USD 355m).
#   allied copper: sandvik_marmato_ug_sek250m_2026 (SEK 250m).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: solar, fission_smr, niobium, nickel, port_cranes,
#   power_plants_grid, rail, water, lithium, port_ownership, balsa, wind,
#   graphite, building_materials (catalog dense; Sungrow Observatorio / CATL
#   La Alegría / EXIM Guyana GTE / DFC Serra Verde / AES Pampas already logged;
#   holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 182: us368 / prc357 / allied308 / other52 (n=1085).
shuffle_seed: 20261182
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/solar
- energy/other_renewables
- energy/fission_smr
- resources/niobium
- resources/nickel
- infrastructure/port_cranes
- energy/power_plants_grid
- infrastructure/engineering_epc
- infrastructure/rail
- resources/water
- resources/lithium
- infrastructure/port_ownership
- resources/balsa
- energy/wind
- resources/copper
- resources/graphite
- infrastructure/bridges_roads
- infrastructure/building_materials
rows_found_this_cycle:
  energy/solar: 0
  energy/other_renewables: 1
  energy/fission_smr: 0
  resources/niobium: 0
  resources/nickel: 0
  infrastructure/port_cranes: 0
  energy/power_plants_grid: 0
  infrastructure/engineering_epc: 1
  infrastructure/rail: 0
  resources/water: 0
  resources/lithium: 0
  infrastructure/port_ownership: 0
  resources/balsa: 0
  energy/wind: 0
  resources/copper: 1
  resources/graphite: 0
  infrastructure/bridges_roads: 1
  infrastructure/building_materials: 0
rows_by_side_this_cycle:
  us: 1
  prc: 0
  allied: 3
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 181 (seed 20261181) ===
# Shuffled order: power_plants_grid, building_materials, bridges_roads, nickel,
#   other_renewables, port_ownership, rail, port_cranes, lithium, copper, balsa,
#   wind, fission_smr, water, niobium, graphite, engineering_epc, solar.
# Logged 8 sourced rows (1 US / 1 PRC / 5 allied / 1 other; ≥1/3 US hunt budget):
#   allied power_plants_grid: redeia_redinter_latam_150m_eur_2026 (~EUR 150m).
#   other power_plants_grid: weg_brazil_xfmr_543m_brl_2024 (R$543m).
#   allied power_plants_grid: bcie_siepac_segundo_circuito_37p2m_2025 (USD 37.2m).
#   prc rail: boc_icbc_bogota_metro_230m_2024 (USD 230m).
#   allied copper: sandvik_alumbrera_dr413i_3_2026 (CapEx blank).
#   allied copper: epiroc_peru_pit_viper_sek210m_2026 (SEK 210m).
#   allied copper: sandvik_cominvi_mexico_sek340m_2026 (SEK 340m).
#   us water: nadbank_nuevo_laredo_beif_8m_2025 (USD 8m).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: building_materials, bridges_roads, nickel, other_renewables,
#   port_ownership, port_cranes, lithium, balsa, wind, fission_smr, niobium,
#   graphite, engineering_epc, solar (catalog dense; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 181: us367 / prc357 / allied305 / other52 (n=1081).
shuffle_seed: 20261181
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/power_plants_grid
- infrastructure/building_materials
- infrastructure/bridges_roads
- resources/nickel
- energy/other_renewables
- infrastructure/port_ownership
- infrastructure/rail
- infrastructure/port_cranes
- resources/lithium
- resources/copper
- resources/balsa
- energy/wind
- energy/fission_smr
- resources/water
- resources/niobium
- resources/graphite
- infrastructure/engineering_epc
- energy/solar
rows_found_this_cycle:
  energy/power_plants_grid: 3
  infrastructure/building_materials: 0
  infrastructure/bridges_roads: 0
  resources/nickel: 0
  energy/other_renewables: 0
  infrastructure/port_ownership: 0
  infrastructure/rail: 1
  infrastructure/port_cranes: 0
  resources/lithium: 0
  resources/copper: 3
  resources/balsa: 0
  energy/wind: 0
  energy/fission_smr: 0
  resources/water: 1
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  energy/solar: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 5
  other: 1
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 180 (seed 20261180) ===
# Shuffled order: rail, other_renewables, water, nickel, lithium, copper,
#   bridges_roads, graphite, port_ownership, engineering_epc, niobium,
#   power_plants_grid, balsa, building_materials, fission_smr, solar, wind,
#   port_cranes.
# Logged 6 sourced rows (2 US / 0 PRC / 4 allied / 0 other; ≥1/3 US hunt budget):
#   us water: nadbank_cespt_tijuana_sewer_4p2m_2026 (USD 4.2m).
#   us copper: caterpillar_finning_alumbrera_250m_2026 (USD 250m UNVERIFIED).
#   allied bridges_roads: wb_guyana_itc_156m_2025 (USD 156m).
#   allied copper: sandvik_codelco_chuqui_lh515i_13_2026 (CapEx blank).
#   allied power_plants_grid: isa_nueva_lagunas_kimal_194p46m_2023 (USD 194.46m).
#   allied port_cranes: kalmar_ottawa_iti_iquique_600k_2026 (USD 600k floor).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: rail, other_renewables, nickel, lithium, graphite,
#   port_ownership, engineering_epc, niobium, balsa, building_materials,
#   fission_smr, solar, wind (catalog dense; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 180: us366 / prc356 / allied300 / other51 (n=1073).
shuffle_seed: 20261180
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/rail
- energy/other_renewables
- resources/water
- resources/nickel
- resources/lithium
- resources/copper
- infrastructure/bridges_roads
- resources/graphite
- infrastructure/port_ownership
- infrastructure/engineering_epc
- resources/niobium
- energy/power_plants_grid
- resources/balsa
- infrastructure/building_materials
- energy/fission_smr
- energy/solar
- energy/wind
- infrastructure/port_cranes
rows_found_this_cycle:
  infrastructure/rail: 0
  energy/other_renewables: 0
  resources/water: 1
  resources/nickel: 0
  resources/lithium: 0
  resources/copper: 2
  infrastructure/bridges_roads: 1
  resources/graphite: 0
  infrastructure/port_ownership: 0
  infrastructure/engineering_epc: 0
  resources/niobium: 0
  energy/power_plants_grid: 1
  resources/balsa: 0
  infrastructure/building_materials: 0
  energy/fission_smr: 0
  energy/solar: 0
  energy/wind: 0
  infrastructure/port_cranes: 1
rows_by_side_this_cycle:
  us: 2
  prc: 0
  allied: 4
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 179 (seed 20261179) ===
# Shuffled order: water, balsa, fission_smr, niobium, nickel, copper, other_renewables,
#   engineering_epc, building_materials, graphite, bridges_roads, power_plants_grid,
#   port_cranes, wind, solar, lithium, rail, port_ownership.
# Logged 7 sourced rows (2 US / 0 PRC / 5 allied / 0 other; ≥1/3 US hunt budget):
#   allied water: mota_engil_ptar_puerto_maldonado_150m_2025 (USD 150m floor).
#   us water: nadbank_jmas_juarez_ww_26p9m_2025 (USD 26.9m).
#   allied copper: bhp_spence_operational_adequacy_1p7bn_2024 (USD 1.7bn).
#   allied copper: bhp_spence_concentrator_chalcopyrite_2026 (CapEx blank).
#   us engineering_epc: exim_hokchi_mexico_69p8m_2021 (USD 69.8m).
#   allied power_plants_grid: omexom_energisa_lot12_epcm_2025 (CapEx blank).
#   allied solar: wb_haiti_jacmel_renewable_af_7p1m_2025 (USD 7.1m).
# Thin top-up (balsa/nickel/fission_smr): all dry.
# Equal-budget misses: balsa, fission_smr, niobium, nickel, other_renewables,
#   building_materials, graphite, bridges_roads, port_cranes, wind, lithium, rail,
#   port_ownership (catalog dense; holdovers unsigned).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 179: us364 / prc356 / allied296 / other51 (n=1067).
shuffle_seed: 20261179
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- resources/balsa
- energy/fission_smr
- resources/niobium
- resources/nickel
- resources/copper
- energy/other_renewables
- infrastructure/engineering_epc
- infrastructure/building_materials
- resources/graphite
- infrastructure/bridges_roads
- energy/power_plants_grid
- infrastructure/port_cranes
- energy/wind
- energy/solar
- resources/lithium
- infrastructure/rail
- infrastructure/port_ownership
rows_found_this_cycle:
  resources/water: 2
  resources/balsa: 0
  energy/fission_smr: 0
  resources/niobium: 0
  resources/nickel: 0
  resources/copper: 2
  energy/other_renewables: 0
  infrastructure/engineering_epc: 1
  infrastructure/building_materials: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 1
  infrastructure/port_cranes: 0
  energy/wind: 0
  energy/solar: 1
  resources/lithium: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
rows_by_side_this_cycle:
  us: 2
  prc: 0
  allied: 5
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 178 (seed 20261178) ===
# Shuffled order: power_plants_grid, lithium, balsa, port_cranes, solar, nickel,
#   bridges_roads, other_renewables, copper, rail, fission_smr, niobium, graphite,
#   water, engineering_epc, port_ownership, building_materials, wind.
# Logged 7 sourced rows + 1 value-fill (2 US / 1 PRC / 4 allied / 0 other; ≥1/3 US hunt):
#   allied solar: ifc_idb_solengy_haiti_13p5m_2025 (USD 13.5m).
#   allied bridges_roads: wb_haiti_resilient_corridors_80m_2025 (USD 80m).
#   prc bridges_roads: cpsi_itaparica_sondagem_200m_2025 (R$200m / USD 34.10m).
#   value-fill bridges_roads: ccecc_cccc_salvador_itaparica_2025 → R$10.42bn proxy.
#   us copper: caterpillar_codelco_det_rt_2025 (CapEx blank).
#   allied copper: komatsu_gaby_930e5_6_2025 (CapEx blank).
#   us port_ownership: ssa_cozumel_cruise_pier_882mdp_2025 (MXN 882.3m / USD 43.84m).
#   allied wind: equinor_esquina_do_vento_acq_2026 (CapEx blank).
# Thin top-up (balsa/nickel/fission_smr): all dry (Plantabal/AIMA/WITS Ecuador balsa;
#   Centaurus/BRN/Atlantic/Fenix nickel; Meitner/Colombia/Peru FIRST fission logged).
# Equal-budget misses: power_plants_grid, lithium, balsa, port_cranes, nickel,
#   other_renewables, rail, fission_smr, niobium, graphite, water, engineering_epc,
#   building_materials (catalog dense).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 178: us362 / prc356 / allied291 / other51 (n=1060).
shuffle_seed: 20261178
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/power_plants_grid
- resources/lithium
- resources/balsa
- infrastructure/port_cranes
- energy/solar
- resources/nickel
- infrastructure/bridges_roads
- energy/other_renewables
- resources/copper
- infrastructure/rail
- energy/fission_smr
- resources/niobium
- resources/graphite
- resources/water
- infrastructure/engineering_epc
- infrastructure/port_ownership
- infrastructure/building_materials
- energy/wind
rows_found_this_cycle:
  energy/power_plants_grid: 0
  resources/lithium: 0
  resources/balsa: 0
  infrastructure/port_cranes: 0
  energy/solar: 1
  resources/nickel: 0
  infrastructure/bridges_roads: 2
  energy/other_renewables: 0
  resources/copper: 2
  infrastructure/rail: 0
  energy/fission_smr: 0
  resources/niobium: 0
  resources/graphite: 0
  resources/water: 0
  infrastructure/engineering_epc: 0
  infrastructure/port_ownership: 1
  infrastructure/building_materials: 0
  energy/wind: 1
rows_by_side_this_cycle:
  us: 2
  prc: 1
  allied: 4
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 177 (seed 20261177) ===
# Shuffled order: building_materials, niobium, rail, port_ownership, lithium,
#   port_cranes, solar, graphite, power_plants_grid, copper, bridges_roads,
#   balsa, nickel, water, engineering_epc, other_renewables, wind, fission_smr.
# Logged 8 sourced rows (2 US / 1 PRC / 3 allied / 2 other; ≥1/3 US hunt budget):
#   other building_materials: cementos_argos_colombia_50m_2026 (USD 50m floor).
#   allied building_materials: holcim_comosa_mexico_2025 (CapEx blank).
#   allied port_ownership: dpworld_callao_adenda4_1470m_2026 (USD 1,470m proposal).
#   prc solar: sungrow_tonachihua_tlaxcala_2164mdp_2026 (MXN 2,164m / USD 126.13m).
#   us copper: fcx_cerro_verde_rcf_350m_2026 (USD 350m RCF).
#   allied copper: antamina_meia_2bn_2024 (USD 2bn envelope).
#   us copper: caterpillar_andina_798ac_18_2026 (CapEx blank).
#   other wind: ecopetrol_jk1_jk2_49pct_25p5m_2026 (USD 25.5m).
# Skipped already-active: fcx_cerro_verde_stake_107m_2026; byd_brazil_bess_factory_500m_2026.
# Thin top-up (balsa/nickel/fission_smr): all dry (AIMA/WITS Ecuador balsa,
#   Centaurus/BRN/MMG nickel, Meitner/Colombia/Peru FIRST fission already logged).
# Equal-budget misses: niobium, rail, lithium, port_cranes, graphite,
#   power_plants_grid, bridges_roads, balsa, nickel, water, engineering_epc,
#   other_renewables, fission_smr (catalog dense).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 177: us360 / prc355 / allied287 / other51 (n=1053).
shuffle_seed: 20261177
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- resources/niobium
- infrastructure/rail
- infrastructure/port_ownership
- resources/lithium
- infrastructure/port_cranes
- energy/solar
- resources/graphite
- energy/power_plants_grid
- resources/copper
- infrastructure/bridges_roads
- resources/balsa
- resources/nickel
- resources/water
- infrastructure/engineering_epc
- energy/other_renewables
- energy/wind
- energy/fission_smr
rows_found_this_cycle:
  infrastructure/building_materials: 2
  resources/niobium: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 1
  resources/lithium: 0
  infrastructure/port_cranes: 0
  energy/solar: 1
  resources/graphite: 0
  energy/power_plants_grid: 0
  resources/copper: 3
  infrastructure/bridges_roads: 0
  resources/balsa: 0
  resources/nickel: 0
  resources/water: 0
  infrastructure/engineering_epc: 0
  energy/other_renewables: 0
  energy/wind: 1
  energy/fission_smr: 0
rows_by_side_this_cycle:
  us: 2
  prc: 1
  allied: 3
  other: 2
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Country×subcategory sweep cells touched (session continuing from 176) ===
# Filled this cycle: Colombia×wind (us AES Guajira 549 MW ~USD 1bn),
#   Colombia×solar (us AES additional solar ~USD 100m), Uruguay×water
#   (allied NGE/Saceem OSE Metropolitan USD 212m), Brazil×port_cranes
#   (prc ZPMC Tecon Santos STS+RTG USD 57m), Chile×wind (other Colbún
#   Cuatro Vientos RCA USD 540m).
# Still thin/empty priority cells: Haiti (many), Venezuela (beyond solar), Nicaragua
#   rail past MoU, Peru balsa, Colombia graphite mine CapEx.

# === Cycle 176 (seed 20261176) ===
# Shuffled order: balsa, wind, nickel, building_materials, power_plants_grid,
#   niobium, port_ownership, engineering_epc, copper, solar, water, rail,
#   port_cranes, lithium, fission_smr, other_renewables, graphite, bridges_roads.
# Logged 5 sourced rows (2 US / 1 PRC / 1 allied / 1 other; ≥1/3 US hunt budget):
#   us wind: aes_colombia_guajira_549mw_1bn_2026 (USD 1bn).
#   us solar: aes_colombia_solar_expand_100m_2026 (USD 100m).
#   allied water: saceem_ose_agua_metropolitana_212m_2026 (USD 212m).
#   prc port_cranes: zpmc_tecon_santos_sts_rtg_57m_2026 (USD 57m).
#   other wind: colbun_cuatro_vientos_540m_2026 (USD 540m).
# Thin top-up (balsa/nickel/fission_smr): all dry (AIMA/WITS Ecuador balsa,
#   Centaurus/BRN/MMG nickel, Meitner/Colombia/Peru FIRST fission already logged).
# Equal-budget misses: balsa, nickel, building_materials, power_plants_grid,
#   niobium, port_ownership, engineering_epc, copper, rail, lithium, fission_smr,
#   other_renewables, graphite, bridges_roads (catalog dense).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 176: us358 / prc354 / allied284 / other49 (n=1045).
shuffle_seed: 20261176
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/balsa
- energy/wind
- resources/nickel
- infrastructure/building_materials
- energy/power_plants_grid
- resources/niobium
- infrastructure/port_ownership
- infrastructure/engineering_epc
- resources/copper
- energy/solar
- resources/water
- infrastructure/rail
- infrastructure/port_cranes
- resources/lithium
- energy/fission_smr
- energy/other_renewables
- resources/graphite
- infrastructure/bridges_roads
rows_found_this_cycle:
  resources/balsa: 0
  energy/wind: 2
  resources/nickel: 0
  infrastructure/building_materials: 0
  energy/power_plants_grid: 0
  resources/niobium: 0
  infrastructure/port_ownership: 0
  infrastructure/engineering_epc: 0
  resources/copper: 0
  energy/solar: 1
  resources/water: 1
  infrastructure/rail: 0
  infrastructure/port_cranes: 1
  resources/lithium: 0
  energy/fission_smr: 0
  energy/other_renewables: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 2
  prc: 1
  allied: 1
  other: 1
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
coverage_notes: >
  Cycle 176 filled wind (AES Guajira CapEx + Colbún Cuatro Vientos), solar
  (AES Colombia additional), water (NGE/Saceem OSE), port_cranes (ZPMC Tecon
  Santos). Thin balsa/nickel/fission dry. Next: prefer balsa/nickel/fission/
  niobium; continue Haiti/Venezuela/Nicaragua/Peru balsa and Colombia graphite.

# === Cycle 175 (seed 20261175) ===
# Shuffled order: other_renewables, nickel, rail, copper, water, fission_smr,
#   building_materials, port_cranes, balsa, engineering_epc, port_ownership,
#   niobium, power_plants_grid, lithium, wind, solar, graphite, bridges_roads.
# Logged 7 sourced rows (3 US / 1 PRC / 1 allied / 2 other; ≥1/3 US hunt budget):
#   other other_renewables: verano_domeyko_capex_247m_2025 (USD 247m).
#   allied nickel: centaurus_jaguar_ons_grid_2026 (CapEx blank; ONS approval).
#   us rail: wabtec_arauco_sucuriu_26es44_2026 (CapEx blank; 26× ES44).
#   us copper: caterpillar_antamina_798_45_2026 (CapEx blank; 27 trucks → 45).
#   us engineering_epc: caterpillar_las_bambas_fleet_2026 (CapEx blank; to 45).
#   other wind: aluar_la_flecha_400m_2024 (USD 400m Stage V).
#   prc solar: cgn_lagoinha_165mw_cod_2026 (R$650m / USD 125.90m ECB).
# Thin top-up (nickel/balsa/fission_smr): nickel filled; balsa/fission dry
#   (AIMA/WITS Ecuador balsa and Meitner/Colombia fission already logged).
# Equal-budget misses: water, fission_smr, building_materials, port_cranes, balsa,
#   port_ownership, niobium, power_plants_grid, lithium, graphite, bridges_roads
#   (catalog dense; PowerChina Chancay/CRCC Batuco/Huawei Aggreko already logged).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 175: us356 / prc353 / allied283 / other48 (n=1040).
shuffle_seed: 20261175
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/other_renewables
- resources/nickel
- infrastructure/rail
- resources/copper
- resources/water
- energy/fission_smr
- infrastructure/building_materials
- infrastructure/port_cranes
- resources/balsa
- infrastructure/engineering_epc
- infrastructure/port_ownership
- resources/niobium
- energy/power_plants_grid
- resources/lithium
- energy/wind
- energy/solar
- resources/graphite
- infrastructure/bridges_roads
rows_found_this_cycle:
  energy/other_renewables: 1
  resources/nickel: 1
  infrastructure/rail: 1
  resources/copper: 1
  resources/water: 0
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  resources/balsa: 0
  infrastructure/engineering_epc: 1
  infrastructure/port_ownership: 0
  resources/niobium: 0
  energy/power_plants_grid: 0
  resources/lithium: 0
  energy/wind: 1
  energy/solar: 1
  resources/graphite: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 3
  prc: 1
  allied: 1
  other: 2
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/nickel
  - resources/balsa
  - energy/fission_smr
coverage_notes: >
  Cycle 175 filled other_renewables (Verano Domeyko CapEx), nickel (Centaurus
  Jaguar ONS grid), rail (Wabtec Arauco ES44), copper (Caterpillar Antamina),
  engineering_epc (Caterpillar Las Bambas), wind (Aluar La Flecha), solar
  (CGN Lagoinha COD). Thin nickel filled; balsa/fission dry. Next: prefer
  balsa/nickel/fission/niobium; continue Haiti/Venezuela/Nicaragua/Peru balsa
  and Colombia graphite CapEx.

# === Cycle 174 (seed 20261174) ===
# Shuffled order: niobium, wind, nickel, engineering_epc, solar, power_plants_grid,
#   rail, port_ownership, graphite, water, other_renewables, copper, bridges_roads,
#   port_cranes, balsa, fission_smr, lithium, building_materials.
# Logged 7 sourced rows (3 US / 1 PRC / 3 allied / 0 other; ≥1/3 US hunt budget):
#   allied niobium: st_george_nanum_araxa_mou_2026 (CapEx blank; MoU).
#   allied engineering_epc: jan_de_nul_martin_garcia_carp_66m_2026 (USD 65.994m).
#   allied solar: zelestra_babilonia_176m_2026 (USD 176m).
#   us fission_smr: us_colombia_civil_nuclear_mou_202609 (CapEx blank; MoU).
#   us graphite: us_colombia_critical_minerals_framework_202609 (CapEx blank).
#   us engineering_epc: caterpillar_vale_northern_autonomous_2025 (CapEx blank).
#   prc lithium: ganfeng_lar_convertible_180m_2026 (USD 180m).
# Thin top-up (nickel/balsa/fission_smr): fission filled; nickel/balsa dry
#   (catalog dense; AIMA/WITS Ecuador balsa and Brazilian nickel already logged).
# Equal-budget misses: wind, nickel, power_plants_grid, rail, port_ownership,
#   water, other_renewables, copper, bridges_roads, port_cranes, balsa,
#   building_materials (catalog dense; many already logged this session).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 174: us353 / prc352 / allied282 / other46 (n=1033).
shuffle_seed: 20261174
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- energy/wind
- resources/nickel
- infrastructure/engineering_epc
- energy/solar
- energy/power_plants_grid
- infrastructure/rail
- infrastructure/port_ownership
- resources/graphite
- resources/water
- energy/other_renewables
- resources/copper
- infrastructure/bridges_roads
- infrastructure/port_cranes
- resources/balsa
- energy/fission_smr
- resources/lithium
- infrastructure/building_materials
rows_found_this_cycle:
  resources/niobium: 1
  energy/wind: 0
  resources/nickel: 0
  infrastructure/engineering_epc: 2
  energy/solar: 1
  energy/power_plants_grid: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  resources/graphite: 1
  resources/water: 0
  energy/other_renewables: 0
  resources/copper: 0
  infrastructure/bridges_roads: 0
  infrastructure/port_cranes: 0
  resources/balsa: 0
  energy/fission_smr: 1
  resources/lithium: 1
  infrastructure/building_materials: 0
rows_by_side_this_cycle:
  us: 3
  prc: 1
  allied: 3
  other: 0
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/nickel
  - resources/balsa
  - energy/fission_smr
coverage_notes: >
  Cycle 174 filled niobium (St George–Nanum Araxá MoU), engineering_epc
  (Jan De Nul Martín García + Caterpillar Vale autonomous), solar (Zelestra
  Babilonia), fission (U.S.–Colombia nuclear MoU), graphite (U.S.–Colombia
  critical-minerals framework), lithium (Ganfeng LAR USD 180m convertible).
  Thin nickel/balsa remained dry. Next: prefer nickel/balsa/niobium; continue
  Haiti/Venezuela/Nicaragua/Peru nickel-balsa and Colombia graphite CapEx.

# === Cycle 173 (seed 20261173) ===
# Shuffled order: graphite, building_materials, wind, fission_smr, bridges_roads,
#   copper, nickel, port_ownership, other_renewables, port_cranes, water, niobium,
#   power_plants_grid, lithium, engineering_epc, rail, balsa, solar.
# Logged 7 sourced rows (2 US / 3 PRC / 0 allied / 2 other; ≥1/3 US hunt budget):
#   other graphite: ingemmet_alto_chicama_graphite_2026 (CapEx blank; 2.6 Mt).
#   other building_materials: votorantim_edealina_argamassa_2026 (CapEx blank; 300 ktpy).
#   prc wind: sinoma_blade_camacari_104m_2023 (USD 19.5m @ ECB).
#   us wind: ge_vernova_lm_suape_closure_2025 (CapEx blank; closure).
#   prc fission_smr: cnnc_ien_cnen_centena_visit_202603 (CapEx blank; visit).
#   prc other_renewables: cgn_goldwind_tanque_novo_bess_2025 (CapEx blank; pilot).
#   us rail: us_argentina_andes_atlantic_corridor_2026 (CapEx blank; corridor).
# Thin top-up (nickel/balsa/fission_smr): fission filled; nickel/balsa dry
#   (AIMA/WITS Ecuador balsa 2025 already logged; nickel catalog dense).
# Equal-budget misses: bridges_roads, copper, nickel, port_ownership, port_cranes,
#   water, niobium, power_plants_grid, lithium, engineering_epc, balsa, solar
#   (catalog dense; many already logged this session / prior cycles).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 173: us350 / prc351 / allied279 / other46 (n=1026).
shuffle_seed: 20261173
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/graphite
- infrastructure/building_materials
- energy/wind
- energy/fission_smr
- infrastructure/bridges_roads
- resources/copper
- resources/nickel
- infrastructure/port_ownership
- energy/other_renewables
- infrastructure/port_cranes
- resources/water
- resources/niobium
- energy/power_plants_grid
- resources/lithium
- infrastructure/engineering_epc
- infrastructure/rail
- resources/balsa
- energy/solar
rows_found_this_cycle:
  resources/graphite: 1
  infrastructure/building_materials: 1
  energy/wind: 2
  energy/fission_smr: 1
  infrastructure/bridges_roads: 0
  resources/copper: 0
  resources/nickel: 0
  infrastructure/port_ownership: 0
  energy/other_renewables: 1
  infrastructure/port_cranes: 0
  resources/water: 0
  resources/niobium: 0
  energy/power_plants_grid: 0
  resources/lithium: 0
  infrastructure/engineering_epc: 0
  infrastructure/rail: 1
  resources/balsa: 0
  energy/solar: 0
rows_by_side_this_cycle:
  us: 2
  prc: 3
  allied: 0
  other: 2
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/nickel
  - resources/balsa
  - energy/fission_smr
coverage_notes: >
  Cycle 173 filled graphite (Peru INGEMMET), building_materials (Votorantim
  Edealina mortar), wind (Sinoma Camaçari + GE Suape closure), fission (CNNC
  Centena visit), other_renewables (CGN–Goldwind Tanque Novo BESS), rail
  (Andes-Atlantic Corridor). Thin nickel/balsa remained dry. Next: prefer
  nickel/balsa/niobium; continue Haiti/Venezuela/Nicaragua/Colombia graphite
  /Peru nickel-niobium-balsa sweeps.

# === Cycle 172 (seed 20261172) ===
# Shuffled order: port_cranes, power_plants_grid, rail, engineering_epc, balsa,
#   other_renewables, wind, fission_smr, niobium, port_ownership, solar,
#   bridges_roads, copper, water, lithium, building_materials, nickel, graphite.
# Logged 8 sourced rows (2 US / 2 PRC / 3 allied / 1 other; thin nickel/balsa dry):
#   prc port_cranes: hhmc_puerto_antioquia_sts_2025 (CapEx blank; 3 STS).
#   us power_plants_grid: ge_vernova_neuquen_aero_repair_2025 (CapEx blank).
#   us rail: ustda_brazil_freight_rail_rtm_2024 (CapEx blank; RTM).
#   prc rail: guangzhou_metro_regiotram_om_rmb2060m_2026 (USD 302.5m @ PBOC).
#   allied engineering_epc: eiffage_jande_nul_callao_norte_2026 (USD 117.8m floor).
#   other fission_smr: diamante_jorge_lacerda_smr_loi_2026 (CapEx blank; LOI).
#   allied wind: edf_naupac_pescadores_348mw_2026 (USD 393.5m MINEM).
#   allied wind: ande_edf_chaco_wind_studies_2025 (CapEx blank; studies).
# Thin top-up (nickel/balsa/fission_smr): fission filled; nickel/balsa dry
#   (AIMA/WITS Ecuador balsa 2025 already logged; nickel catalog dense).
# Equal-budget misses: balsa, other_renewables, niobium, port_ownership, solar,
#   bridges_roads, copper, water, lithium, building_materials, nickel, graphite
#   (catalog dense; many already logged this session).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree;
#   CCECC Nicaragua rail still prefeasibility/feasibility.
# Active after cycle 172: us348 / prc348 / allied279 / other44 (n=1019).
shuffle_seed: 20261172
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_cranes
- energy/power_plants_grid
- infrastructure/rail
- infrastructure/engineering_epc
- resources/balsa
- energy/other_renewables
- energy/wind
- energy/fission_smr
- resources/niobium
- infrastructure/port_ownership
- energy/solar
- infrastructure/bridges_roads
- resources/copper
- resources/water
- resources/lithium
- infrastructure/building_materials
- resources/nickel
- resources/graphite
rows_found_this_cycle:
  infrastructure/port_cranes: 1
  energy/power_plants_grid: 1
  infrastructure/rail: 2
  infrastructure/engineering_epc: 1
  resources/balsa: 0
  energy/other_renewables: 0
  energy/wind: 2
  energy/fission_smr: 1
  resources/niobium: 0
  infrastructure/port_ownership: 0
  energy/solar: 0
  infrastructure/bridges_roads: 0
  resources/copper: 0
  resources/water: 0
  resources/lithium: 0
  infrastructure/building_materials: 0
  resources/nickel: 0
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 3
  other: 1

# === Cycle 171 (seed 20261171) ===
# Shuffled order: other_renewables, port_cranes, graphite, balsa, niobium,
#   power_plants_grid, copper, bridges_roads, lithium, solar, port_ownership, wind,
#   fission_smr, nickel, engineering_epc, building_materials, water, rail.
# Logged 9 sourced rows (3 US / 2 PRC / 1 allied / 3 other; thin nickel/fission dry):
#   prc graphite: data_mexico_graphite_china_imp_2024 (USD 437k trade).
#   us graphite: data_mexico_graphite_us_imp_2024 (USD 4.72m trade; paired).
#   other balsa: balsa_de_colombia_presence (CapEx blank; thin top-up).
#   prc power_plants_grid: powerchina_coca_codo_aom_46m_yr_2026 (USD 46m/yr fee).
#   us lithium: atlas_lithium_us_japan_neves_2026 (CapEx blank; support considered).
#   other solar: ande_loma_plata_solar_140mw_2026 (CapEx blank; tender).
#   other wind: ice_tejona_wind_77p5m_2024 (USD 77.5m).
#   us water: xylem_amazon_vue_mexico_2025 (CapEx blank).
#   allied water: holcim_mexico_water_356mdp_2026 (USD 20m).
# Thin top-up (balsa/nickel/fission_smr): balsa filled; nickel/fission dry.
# Equal-budget misses: other_renewables, port_cranes, niobium, copper, bridges_roads,
#   port_ownership, fission_smr, nickel, engineering_epc, building_materials, rail
#   (catalog dense; many already logged this session).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree; CCECC rail MoU.
# Active after cycle 171: us346 / prc346 / allied276 / other43 (n=1011).
shuffle_seed: 20261171
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/other_renewables
- infrastructure/port_cranes
- resources/graphite
- resources/balsa
- resources/niobium
- energy/power_plants_grid
- resources/copper
- infrastructure/bridges_roads
- resources/lithium
- energy/solar
- infrastructure/port_ownership
- energy/wind
- energy/fission_smr
- resources/nickel
- infrastructure/engineering_epc
- infrastructure/building_materials
- resources/water
- infrastructure/rail
rows_found_this_cycle:
  energy/other_renewables: 0
  infrastructure/port_cranes: 0
  resources/graphite: 2
  resources/balsa: 1
  resources/niobium: 0
  energy/power_plants_grid: 1
  resources/copper: 0
  infrastructure/bridges_roads: 0
  resources/lithium: 1
  energy/solar: 1
  infrastructure/port_ownership: 0
  energy/wind: 1
  energy/fission_smr: 0
  resources/nickel: 0
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  resources/water: 2
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 3
  prc: 2
  allied: 1
  other: 3
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 170 (seed 20261170) ===
# Shuffled order: water, power_plants_grid, niobium, balsa, nickel, rail, engineering_epc,
#   building_materials, graphite, port_cranes, copper, solar, lithium, port_ownership,
#   bridges_roads, fission_smr, wind, other_renewables.
# Logged 7 sourced rows (4 US / 3 PRC; thin nickel/fission dry; no padding):
#   prc water: china_midagri_poechos_alto_piura_g2g_2025 (CapEx blank; G2G TA award).
#   us water: dfc_ecuador_amazon_biocorridor_pri_1bn_2024 (USD 1bn PRI).
#   us power_plants_grid: ge_vernova_itaipu_cmi_modernization_2025 (CapEx blank).
#   prc solar: byd_raizen_gera_nine_plants_26p5mw (CapEx blank; 26.5 MW Full EPC).
#   prc balsa: sinobalsa_ecuador_presence (CapEx blank; thin top-up).
#   us lithium: argentina_us_critical_minerals_framework_2026 (CapEx blank).
#   us graphite: mexico_us_critical_minerals_action_plan_2026 (CapEx blank; thin).
# Thin top-up (balsa/nickel/fission_smr): balsa filled; nickel/fission dry —
#   graphite also filled via Mexico Action Plan (named graphite priority).
# Equal-budget misses: niobium, nickel, rail, engineering_epc, building_materials,
#   port_cranes, copper, port_ownership, bridges_roads, fission_smr, wind,
#   other_renewables (many already logged this session: CBMM/ENGIE/ZPMC/Wabtec/etc.).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree; CCECC rail MoU.
# Active after cycle 170: us343 / prc344 / allied275 / other40 (n=1002).
shuffle_seed: 20261170
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- energy/power_plants_grid
- resources/niobium
- resources/balsa
- resources/nickel
- infrastructure/rail
- infrastructure/engineering_epc
- infrastructure/building_materials
- resources/graphite
- infrastructure/port_cranes
- resources/copper
- energy/solar
- resources/lithium
- infrastructure/port_ownership
- infrastructure/bridges_roads
- energy/fission_smr
- energy/wind
- energy/other_renewables
rows_found_this_cycle:
  resources/water: 2
  energy/power_plants_grid: 1
  resources/niobium: 0
  resources/balsa: 1
  resources/nickel: 0
  infrastructure/rail: 0
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  resources/graphite: 1
  infrastructure/port_cranes: 0
  resources/copper: 0
  energy/solar: 1
  resources/lithium: 1
  infrastructure/port_ownership: 0
  infrastructure/bridges_roads: 0
  energy/fission_smr: 0
  energy/wind: 0
  energy/other_renewables: 0
rows_by_side_this_cycle:
  us: 4
  prc: 3
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 169 (seed 20261169) ===
# Shuffled order: lithium, solar, balsa, nickel, building_materials, power_plants_grid,
#   fission_smr, engineering_epc, rail, other_renewables, port_cranes, copper, wind,
#   port_ownership, graphite, niobium, water, bridges_roads.
# Logged 8 sourced rows (4 US / 1 PRC / 2 allied / 1 other; thin balsa/nickel/fission dry):
#   us lithium: colombia_us_critical_minerals_framework_2026 (CapEx blank).
#   us lithium: peru_us_critical_minerals_mou_2026 (CapEx blank).
#   us lithium: paraguay_us_critical_minerals_mou_2026 (CapEx blank).
#   us lithium: ecuador_us_critical_minerals_framework_2026 (CapEx blank).
#   allied engineering_epc: casale_atome_villeta_epc_465m_2025 (USD 465m).
#   allied building_materials: holcim_ambiensa_ecopact_mundo_guayaquil (CapEx blank).
#   prc wind: cccc_la_mesita_wind_57p4m_esteli_2025 (USD 57.4m).
#   other port_ownership: ptp_villeta_bond_usd2m_202504 (USD 2m).
# Thin top-up (balsa/nickel/fission_smr): all dry once — graphite/niobium denser misses.
# Equal-budget misses: solar, balsa, nickel, power_plants_grid, fission_smr, rail,
#   other_renewables, port_cranes, copper, graphite, niobium, water, bridges_roads
#   (many already logged this session: AES DR solar, Coca Codo, Quiulacocha, etc.).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree; CCECC rail MoU.
# Active after cycle 169: us339 / prc341 / allied275 / other40 (n=995).
shuffle_seed: 20261169
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/lithium
- energy/solar
- resources/balsa
- resources/nickel
- infrastructure/building_materials
- energy/power_plants_grid
- energy/fission_smr
- infrastructure/engineering_epc
- infrastructure/rail
- energy/other_renewables
- infrastructure/port_cranes
- resources/copper
- energy/wind
- infrastructure/port_ownership
- resources/graphite
- resources/niobium
- resources/water
- infrastructure/bridges_roads
rows_found_this_cycle:
  resources/lithium: 4
  energy/solar: 0
  resources/balsa: 0
  resources/nickel: 0
  infrastructure/building_materials: 1
  energy/power_plants_grid: 0
  energy/fission_smr: 0
  infrastructure/engineering_epc: 1
  infrastructure/rail: 0
  energy/other_renewables: 0
  infrastructure/port_cranes: 0
  resources/copper: 0
  energy/wind: 1
  infrastructure/port_ownership: 1
  resources/graphite: 0
  resources/niobium: 0
  resources/water: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 2
  other: 1
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr

# === Cycle 168 (seed 20261168) ===
# Shuffled order: copper, niobium, solar, balsa, graphite, rail, water, port_cranes,
#   other_renewables, nickel, power_plants_grid, bridges_roads, engineering_epc, fission_smr,
#   lithium, wind, building_materials, port_ownership.
# Logged 9 sourced rows (3 US / 4 PRC / 2 allied; thin balsa/niobium dry; no padding):
#   allied copper: hudbay_constancia_34mtpa_senace_2026 (CapEx blank; SENACE 34 Mtpa).
#   prc copper: chinalco_toromocho_equip_400m_2026 (USD 400m floor proxy).
#   prc solar: grain_full_el_vigia_solar_52p8mw_venezuela (CapEx blank).
#   allied solar: ssangyong_caracol_solar_13p4mw_haiti_57m (USD 57m IDB).
#   prc water: powerchina_nickerie_paradise_drainage_2025 (CapEx blank).
#   us power_plants_grid: ustda_ice_costa_rica_mdi_2022 (CapEx blank).
#   us bridges_roads: fcx_cerro_verde_oxi_uchumayo_2026 (CapEx blank; >USD 14m package).
#   us fission_smr: mexico_us_123_agreement_2022 (CapEx blank).
#   prc port_ownership: chinaitc_corinto_julia_herrera_126p6m_2025 (USD 126.6m).
# Thin top-up (balsa/fission_smr/niobium): fission filled; balsa/niobium dry —
#   graphite/nickel already dense misses this pass.
# Equal-budget misses: niobium, balsa, graphite, rail, port_cranes, other_renewables,
#   nickel, engineering_epc, lithium, wind, building_materials; US copper searched
#   (Cerro Verde/Tía María already logged) — no new distinct US copper CapEx.
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km package decree; CCECC rail MoU.
# Active after cycle 168: us335 / prc340 / allied273 / other39 (n=987).
shuffle_seed: 20261168
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/copper
- resources/niobium
- energy/solar
- resources/balsa
- resources/graphite
- infrastructure/rail
- resources/water
- infrastructure/port_cranes
- energy/other_renewables
- resources/nickel
- energy/power_plants_grid
- infrastructure/bridges_roads
- infrastructure/engineering_epc
- energy/fission_smr
- resources/lithium
- energy/wind
- infrastructure/building_materials
- infrastructure/port_ownership
rows_found_this_cycle:
  resources/copper: 2
  resources/niobium: 0
  energy/solar: 2
  resources/balsa: 0
  resources/graphite: 0
  infrastructure/rail: 0
  resources/water: 1
  infrastructure/port_cranes: 0
  energy/other_renewables: 0
  resources/nickel: 0
  energy/power_plants_grid: 1
  infrastructure/bridges_roads: 1
  infrastructure/engineering_epc: 0
  energy/fission_smr: 1
  resources/lithium: 0
  energy/wind: 0
  infrastructure/building_materials: 0
  infrastructure/port_ownership: 1
rows_by_side_this_cycle:
  us: 3
  prc: 4
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - energy/fission_smr
  - resources/niobium

# === Cycle 167 (seed 20261167) ===
# Shuffled order: rail, balsa, graphite, water, power_plants_grid, copper, fission_smr, wind,
#   bridges_roads, other_renewables, building_materials, port_cranes, nickel, niobium,
#   engineering_epc, port_ownership, solar, lithium.
# Logged 6 sourced rows (1 US / 3 PRC / 2 allied; thin dry; no padding):
#   allied rail: sacyr_via_central_ferrocarril_uruguay_2025 (CapEx blank; ops cert 2025).
#   prc water: ccecc_matagalpa_water_wwtp_nicaragua (CapEx blank; proxy interview).
#   us water: usaid_haiti_wash_41p8m_2017 (USD 41.8m).
#   prc building_materials: cscec_nuevas_victorias_fase1_920_nicaragua (CapEx blank).
#   prc port_cranes: zpmc_caucedo_3rtg_7p9m_dr_2025 (USD 7.9m proxy).
#   allied wind: acciona_chiripa_ev_80m_costa_rica_2025 (USD 80m EV).
# Thin top-up (balsa/fission_smr/niobium): all dry once this session — nickel/graphite already used.
# Equal-budget misses: balsa, graphite, power_plants_grid, copper, fission_smr, bridges_roads,
#   other_renewables, nickel, niobium, engineering_epc, port_ownership, solar, lithium.
# Active after cycle 167: us332 / prc336 / allied271 / other39 (n=978).
shuffle_seed: 20261167
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/rail
- resources/balsa
- resources/graphite
- resources/water
- energy/power_plants_grid
- resources/copper
- energy/fission_smr
- energy/wind
- infrastructure/bridges_roads
- energy/other_renewables
- infrastructure/building_materials
- infrastructure/port_cranes
- resources/nickel
- resources/niobium
- infrastructure/engineering_epc
- infrastructure/port_ownership
- energy/solar
- resources/lithium
rows_found_this_cycle:
  infrastructure/rail: 1
  resources/balsa: 0
  resources/graphite: 0
  resources/water: 2
  energy/power_plants_grid: 0
  resources/copper: 0
  energy/fission_smr: 0
  energy/wind: 1
  infrastructure/bridges_roads: 0
  energy/other_renewables: 0
  infrastructure/building_materials: 1
  infrastructure/port_cranes: 1
  resources/nickel: 0
  resources/niobium: 0
  infrastructure/engineering_epc: 0
  infrastructure/port_ownership: 0
  energy/solar: 0
  resources/lithium: 0
rows_by_side_this_cycle:
  us: 1
  prc: 3
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family
  subcategories:

# === Cycle 166 (seed 20261166) ===
# Shuffled order: power_plants_grid, other_renewables, graphite, lithium, port_cranes,
#   building_materials, engineering_epc, copper, rail, fission_smr, solar, niobium, water,
#   nickel, bridges_roads, wind, balsa, port_ownership.
# Logged 9 sourced rows (3 US / 1 PRC / 5 allied; thin dry; no padding):
#   allied power_plants_grid: abengoa_ande_chaco_lote2_29p7m_paraguay (USD 29.7m).
#   allied power_plants_grid: abengoa_ande_chaco_lote3_35p7m_paraguay (USD 35.7m).
#   prc port_cranes: jiangsu_rainbow_corinto_4rtg_nicaragua_2026 (CapEx blank).
#   us engineering_epc: trigon_cap_haitien_port_cm_43m (USD 43m).
#   us copper: fcx_max_sierra_azul_4p8m_colombia_2025 (USD 4.8m).
#   allied solar: jps_marubeni_300m_solar_bess_jamaica_2025 (USD 300m).
#   allied wind: vestas_costa_rica_22mw_order_2025 (CapEx blank).
#   allied port_ownership: kftl_cma_westlands_80m_jamaica_2025 (USD 80m proxy).
#   us wind: ustda_jamaica_offshore_wind_875k (USD 875k).
# Thin top-up (balsa/fission_smr/niobium): all dry once this session — nickel/graphite already used.
# Equal-budget misses: other_renewables, graphite, lithium, building_materials, rail, fission_smr,
#   niobium, water, nickel, bridges_roads, balsa; PRC denser misses (no pad).
# Active after cycle 166: us331 / prc333 / allied269 / other39 (n=972).
shuffle_seed: 20261166
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/power_plants_grid
- energy/other_renewables
- resources/graphite
- resources/lithium
- infrastructure/port_cranes
- infrastructure/building_materials
- infrastructure/engineering_epc
- resources/copper
- infrastructure/rail
- energy/fission_smr
- energy/solar
- resources/niobium
- resources/water
- resources/nickel
- infrastructure/bridges_roads
- energy/wind
- resources/balsa
- infrastructure/port_ownership
rows_found_this_cycle:
  energy/power_plants_grid: 2
  energy/other_renewables: 0
  resources/graphite: 0
  resources/lithium: 0
  infrastructure/port_cranes: 1
  infrastructure/building_materials: 0
  infrastructure/engineering_epc: 1
  resources/copper: 1
  infrastructure/rail: 0
  energy/fission_smr: 0
  energy/solar: 1
  resources/niobium: 0
  resources/water: 0
  resources/nickel: 0
  infrastructure/bridges_roads: 0
  energy/wind: 2
  resources/balsa: 0
  infrastructure/port_ownership: 1
rows_by_side_this_cycle:
  us: 3
  prc: 1
  allied: 5
  other: 0
thin_topup:
  budget: 0.5_source_family
  subcategories:

# === Cycle 165 (seed 20261165) ===
# Shuffled order: water, building_materials, port_cranes, power_plants_grid, niobium, lithium,
#   fission_smr, nickel, port_ownership, bridges_roads, graphite, rail, other_renewables, solar,
#   wind, copper, engineering_epc, balsa.
# Logged 6 sourced rows (0 US / 2 PRC / 3 allied / 1 other; thin dry; no padding):
#   prc water: powerchina_wiesner_bogota_water_2023 (14→21 m³/s; CapEx blank).
#   prc water: powerchina_tibitoc_bogota_water_upgrade (nano COD Mar 2026; CapEx blank).
#   allied building_materials: holcim_cemex_guatemala_ops_2024 (USD 212m Cemex 4Q24).
#   other building_materials: cemex_carib_rockfort_42m_jamaica (USD 42m).
#   allied port_cranes: konecranes_chiquita_puerto_barrios_3rs_2024 (CapEx blank; Guatemala empty).
#   allied lithium: american_lithium_falchani_pea_681m_peru (USD 681m PEA Phase 1; Peru empty).
# Thin top-up (balsa/fission_smr/niobium): all dry once this session — nickel/graphite already used.
# Equal-budget misses: power_plants_grid, niobium, fission_smr, nickel, port_ownership, bridges_roads,
#   graphite, rail, other_renewables, solar, wind, copper, engineering_epc, balsa; US denser misses (no pad).
# Active after cycle 165: us328 / prc332 / allied264 / other39 (n=963).
shuffle_seed: 20261165
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- infrastructure/building_materials
- infrastructure/port_cranes
- energy/power_plants_grid
- resources/niobium
- resources/lithium
- energy/fission_smr
- resources/nickel
- infrastructure/port_ownership
- infrastructure/bridges_roads
- resources/graphite
- infrastructure/rail
- energy/other_renewables
- energy/solar
- energy/wind
- resources/copper
- infrastructure/engineering_epc
- resources/balsa
rows_found_this_cycle:
  resources/water: 2
  infrastructure/building_materials: 2
  infrastructure/port_cranes: 1
  energy/power_plants_grid: 0
  resources/niobium: 0
  resources/lithium: 1
  energy/fission_smr: 0
  resources/nickel: 0
  infrastructure/port_ownership: 0
  infrastructure/bridges_roads: 0
  resources/graphite: 0
  infrastructure/rail: 0
  energy/other_renewables: 0
  energy/solar: 0
  energy/wind: 0
  resources/copper: 0
  infrastructure/engineering_epc: 0
  resources/balsa: 0
rows_by_side_this_cycle:
  us: 0
  prc: 2
  allied: 3
  other: 1
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/balsa
  - energy/fission_smr
  - resources/niobium

# === Cycle 164 (seed 20261164) ===
# Shuffled order: engineering_epc, water, power_plants_grid, graphite, building_materials, niobium,
#   nickel, other_renewables, lithium, bridges_roads, balsa, copper, fission_smr, port_ownership,
#   solar, rail, port_cranes, wind.
# Logged 6 sourced rows (2 US / 2 PRC / 2 allied; thin graphite hit; no padding):
#   us engineering_epc: fluor_quellaveco_epcm_peru (CapEx blank).
#   prc power_plants_grid: powerchina_mexico_i20_p2_lot1_154m (USD 154m UNVERIFIED proxy; Mexico empty).
#   allied wind: vestas_guatemala_63mw_2024 (63 MW; CapEx blank; Guatemala empty).
#   allied power_plants_grid: geb_transnova_ifc_65m_guatemala (up to USD 65m IFC; Guatemala empty).
#   us+prc graphite: wits_mexico_graphite_us_imp_2023 / wits_mexico_graphite_china_imp_2023 (paired WITS).
# Thin top-up: graphite scored (WITS Mexico); balsa/fission_smr dry once — nickel already used; niobium dry.
# Equal-budget misses: water, building_materials, niobium, nickel, other_renewables, lithium,
#   bridges_roads, balsa, copper, fission_smr, port_ownership, solar, rail, port_cranes (no pad).
# Active after cycle 164: us328 / prc330 / allied261 / other38 (n=957).
shuffle_seed: 20261164
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- resources/water
- energy/power_plants_grid
- resources/graphite
- infrastructure/building_materials
- resources/niobium
- resources/nickel
- energy/other_renewables
- resources/lithium
- infrastructure/bridges_roads
- resources/balsa
- resources/copper
- energy/fission_smr
- infrastructure/port_ownership
- energy/solar
- infrastructure/rail
- infrastructure/port_cranes
- energy/wind
rows_found_this_cycle:
  infrastructure/engineering_epc: 1
  resources/water: 0
  energy/power_plants_grid: 2
  resources/graphite: 2
  infrastructure/building_materials: 0
  resources/niobium: 0
  resources/nickel: 0
  energy/other_renewables: 0
  resources/lithium: 0
  infrastructure/bridges_roads: 0
  resources/balsa: 0
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/port_ownership: 0
  energy/solar: 0
  infrastructure/rail: 0
  infrastructure/port_cranes: 0
  energy/wind: 1
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/balsa
  - energy/fission_smr
  - resources/niobium

# === Cycle 163 (seed 20261163) ===
# Shuffled order: niobium, lithium, fission_smr, copper, port_cranes, nickel, building_materials,
#   port_ownership, other_renewables, engineering_epc, rail, wind, solar, water, graphite, balsa,
#   bridges_roads, power_plants_grid.
# Logged 6 sourced rows (1 US / 3 PRC / 2 allied; thin dry; no padding):
#   prc copper: jchx_alacran_50pct_100m_earn_in_2025 (USD 100m; Colombia empty filled).
#   prc copper: jchx_veritas_alacran_128m_closing_2026 (USD 128m remaining 50% + 100% ownership).
#   prc rail: crrc_cdmx_linea1_full_open_2025 (CapEx blank; CDMX Line 1 full opening).
#   allied port_cranes: konecranes_puerto_antioquia_8rtg_2023 (8 electric RTGs; CapEx blank).
#   allied port_ownership: cma_puerto_antioquia_colombia (CMA Terminals shareholder; CapEx blank).
#   us solar: aes_adre_idb_368m_dr_2023 (~USD 368m IDB Invest package).
# Thin top-up (balsa/graphite/fission_smr): all dry once this session — nickel already used; niobium dry.
# Equal-budget misses: niobium, lithium, fission_smr, nickel, building_materials, other_renewables,
#   engineering_epc, wind, water, graphite, balsa, bridges_roads, power_plants_grid; US denser misses (no pad).
# Active after cycle 163: us326 / prc328 / allied259 / other38 (n=951).
shuffle_seed: 20261163
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- resources/lithium
- energy/fission_smr
- resources/copper
- infrastructure/port_cranes
- resources/nickel
- infrastructure/building_materials
- infrastructure/port_ownership
- energy/other_renewables
- infrastructure/engineering_epc
- infrastructure/rail
- energy/wind
- energy/solar
- resources/water
- resources/graphite
- resources/balsa
- infrastructure/bridges_roads
- energy/power_plants_grid
rows_found_this_cycle:
  resources/niobium: 0
  resources/lithium: 0
  energy/fission_smr: 0
  resources/copper: 2
  infrastructure/port_cranes: 1
  resources/nickel: 0
  infrastructure/building_materials: 0
  infrastructure/port_ownership: 1
  energy/other_renewables: 0
  infrastructure/engineering_epc: 0
  infrastructure/rail: 1
  energy/wind: 0
  energy/solar: 1
  resources/water: 0
  resources/graphite: 0
  resources/balsa: 0
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 0
rows_by_side_this_cycle:
  us: 1
  prc: 3
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 162 (seed 20261162) ===
# Shuffled order: niobium, nickel, graphite, lithium, rail, engineering_epc, solar, other_renewables,
#   port_cranes, power_plants_grid, bridges_roads, balsa, port_ownership, fission_smr, building_materials,
#   wind, copper, water.
# Logged 8 sourced rows (4 US / 1 PRC / 3 allied; thin nickel hit; no padding):
#   us nickel: dfc_techmet_brazil_nickel_30m_equity (USD 30m DFC equity).
#   prc bridges_roads: cscec_litoral_pacifico_fase2_nicaragua_2024 (RMB 1.805bn credit).
#   allied port_ownership: apm_tcbuen_buenaventura_colombia (CapEx blank; Colombia empty filled).
#   allied bridges_roads: sacyr_rutas_2_7_paraguay_530m (USD 530m PPP).
#   allied solar: butler_ciudadluz_puerto_esperanza_solar_py (USD 2.07m; Paraguay solar).
#   us solar: pattern_helios_zacatecas_150mw_2022 (150 MW; CapEx blank).
#   us wind: aes_mesa_la_paz_mexico_306mw (306 MW COD 2020; CapEx blank).
#   us wind: pattern_tuli_zacatecas_150mw_2019 (150 MW; CapEx blank).
# Thin top-up: nickel scored (DFC TechMet equity); balsa/graphite/fission_smr dry once — niobium dry shift.
# Equal-budget misses: niobium, graphite, lithium, rail, engineering_epc, other_renewables, port_cranes,
#   power_plants_grid, balsa, fission_smr, building_materials, copper, water; PRC denser misses (no pad).
# Active after cycle 162: us325 / prc325 / allied257 / other38 (n=945).
shuffle_seed: 20261162
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- resources/nickel
- resources/graphite
- resources/lithium
- infrastructure/rail
- infrastructure/engineering_epc
- energy/solar
- energy/other_renewables
- infrastructure/port_cranes
- energy/power_plants_grid
- infrastructure/bridges_roads
- resources/balsa
- infrastructure/port_ownership
- energy/fission_smr
- infrastructure/building_materials
- energy/wind
- resources/copper
- resources/water
rows_found_this_cycle:
  resources/niobium: 0
  resources/nickel: 1
  resources/graphite: 0
  resources/lithium: 0
  infrastructure/rail: 0
  infrastructure/engineering_epc: 0
  energy/solar: 2
  energy/other_renewables: 0
  infrastructure/port_cranes: 0
  energy/power_plants_grid: 0
  infrastructure/bridges_roads: 2
  resources/balsa: 0
  infrastructure/port_ownership: 1
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  energy/wind: 2
  resources/copper: 0
  resources/water: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 3
  other: 0
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 161 (seed 20261161) ===
# Shuffled order: fission_smr, port_ownership, power_plants_grid, lithium, other_renewables,
#   port_cranes, building_materials, graphite, balsa, wind, niobium, copper, nickel, water,
#   rail, bridges_roads, engineering_epc, solar.
# Logged 8 sourced rows (7 US / 1 PRC / 0 allied; thin dry; no padding):
#   prc power_plants_grid: cmec_uruguay_anillo_norte_500kv_191m_2021 (USD 191m; ~350 km 500 kV).
#   us power_plants_grid: invenergy_tealov_cardal_tx_uruguay_2024 (55 km 500 kV COD; CapEx blank).
#   us solar: invenergy_la_jacinta_solar_uruguay_64mw (64–65 MW ownership; CapEx blank).
#   us wind: invenergy_campo_palomas_wind_uruguay_70mw (70 MW; CapEx blank).
#   us solar: aes_panama_cedro_10mw_2021 (10 MW COD 2021; CapEx blank).
#   us solar: aes_panama_caoba_10mw_2021 (10 MW COD 2021; CapEx blank).
#   us solar: ustda_new_sun_road_guatemala_dcc_2023 (10-site solar DCC pilot; CapEx blank).
#   us power_plants_grid: aes_enadom_lng_tank2_253m_dr_2023 (120,000 m³; USD 253m).
# Thin top-up (balsa/graphite/fission_smr): all dry once this session — nickel/niobium also dry.
# Equal-budget misses: fission_smr, port_ownership, lithium, other_renewables, port_cranes,
#   building_materials, graphite, balsa, niobium, copper, nickel, water, rail, bridges_roads,
#   engineering_epc; PRC denser misses (no pad).
# Active after cycle 161: us321 / prc324 / allied254 / other38 (n=937).
shuffle_seed: 20261161
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/fission_smr
- infrastructure/port_ownership
- energy/power_plants_grid
- resources/lithium
- energy/other_renewables
- infrastructure/port_cranes
- infrastructure/building_materials
- resources/graphite
- resources/balsa
- energy/wind
- resources/niobium
- resources/copper
- resources/nickel
- resources/water
- infrastructure/rail
- infrastructure/bridges_roads
- infrastructure/engineering_epc
- energy/solar
rows_found_this_cycle:
  energy/fission_smr: 0
  infrastructure/port_ownership: 0
  energy/power_plants_grid: 3
  resources/lithium: 0
  energy/other_renewables: 0
  infrastructure/port_cranes: 0
  infrastructure/building_materials: 0
  resources/graphite: 0
  resources/balsa: 0
  energy/wind: 1
  resources/niobium: 0
  resources/copper: 0
  resources/nickel: 0
  resources/water: 0
  infrastructure/rail: 0
  infrastructure/bridges_roads: 0
  infrastructure/engineering_epc: 0
  energy/solar: 4
rows_by_side_this_cycle:
  us: 7
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 160 (seed 20261160) ===
# Shuffled order: solar, fission_smr, building_materials, balsa, water, niobium, rail, wind,
#   power_plants_grid, lithium, other_renewables, port_ownership, graphite, engineering_epc,
#   bridges_roads, port_cranes, copper, nickel.
# Logged 8 sourced rows (4 US / 3 PRC / 1 allied; thin dry; no padding):
#   us solar: dfc_gosolar_costa_rica_15m_2021 (USD 15m DFC debt/equity + 5 MW ICE).
#   us solar: aes_panama_pese_10mw_2021 (10 MW COD 2021; CapEx blank).
#   us solar: aes_panama_mayorca_10mw_2021 (10 MW COD 2021; CapEx blank).
#   prc solar: powerchina_goejaba_pikinslee_suriname_2020 (673.2 kW + 2.6 MWh; CapEx blank).
#   prc water: crec_canas_bebedero_water_costa_rica_2022 (CTCE; ₡9.815bn PRC grant; CapEx USD blank).
#   prc bridges_roads: crec_oruro_challapata_tramo1_bolivia_2024 (19.79 km; CapEx blank; proxy press).
#   us power_plants_grid: invenergy_edp_acajutla_380mw_1bn_2022 (380 MW; >USD 1bn).
#   allied port_ownership: apm_moin_costa_rica_modernization_2025 (TCM modernization; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry once this session — shift to nickel/niobium also dry.
# Equal-budget misses: fission_smr, building_materials, balsa, niobium, rail, wind, lithium,
#   other_renewables, graphite, engineering_epc, port_cranes, copper, nickel;
#   water US (Point Fortin COD 2013 out of preferred window; Emerald Bay renewal undated).
# Holdover note: POWERCHINA Baku Suriname Chinese URL 404 this cycle; English not found.
# Active after cycle 160: us314 / prc323 / allied254 / other38 (n=929).
shuffle_seed: 20261160
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/solar
- energy/fission_smr
- infrastructure/building_materials
- resources/balsa
- resources/water
- resources/niobium
- infrastructure/rail
- energy/wind
- energy/power_plants_grid
- resources/lithium
- energy/other_renewables
- infrastructure/port_ownership
- resources/graphite
- infrastructure/engineering_epc
- infrastructure/bridges_roads
- infrastructure/port_cranes
- resources/copper
- resources/nickel
rows_found_this_cycle:
  energy/solar: 4
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  resources/balsa: 0
  resources/water: 1
  resources/niobium: 0
  infrastructure/rail: 0
  energy/wind: 0
  energy/power_plants_grid: 1
  resources/lithium: 0
  energy/other_renewables: 0
  infrastructure/port_ownership: 1
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  infrastructure/bridges_roads: 1
  infrastructure/port_cranes: 0
  resources/copper: 0
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 4
  prc: 3
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 159 (seed 20261159) ===
# Shuffled order: fission_smr, niobium, rail, port_ownership, graphite,
#   bridges_roads, wind, other_renewables, power_plants_grid, water,
#   port_cranes, lithium, copper, building_materials, solar,
#   engineering_epc, balsa, nickel.
# Logged 5 sourced rows (2 US / 3 PRC; thin dry; no padding):
#   prc other_renewables: powerchina_patuca_iii_honduras_104mw (104 MW; CapEx blank).
#   prc other_renewables: powerchina_el_arenal_honduras_60mw (60 MW; CapEx blank).
#   us solar: aes_opico_power_5p2mwp_elsalvador (5.2 MWp; CapEx blank).
#   us solar: aes_cuscatlan_solar_10mw_elsalvador (10 MW; CapEx blank).
#   prc solar: powerchina_guayasamin_solar_ecuador_2026 (museum demo; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: fission_smr, niobium, rail, port_ownership, graphite,
#   bridges_roads, wind, power_plants_grid, water, port_cranes, lithium,
#   copper, building_materials, engineering_epc, balsa, nickel.
# Dense already-logged: ENEE 230 kV; Cartagena 23 MW; El Salvador nuclear MOUs;
#   Sajalices; Kingston ZPMC.
# Active after cycle 159: us310 / prc320 / allied253 / other38 (n=921).
shuffle_seed: 20261159
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/fission_smr
- resources/niobium
- infrastructure/rail
- infrastructure/port_ownership
- resources/graphite
- infrastructure/bridges_roads
- energy/wind
- energy/other_renewables
- energy/power_plants_grid
- resources/water
- infrastructure/port_cranes
- resources/lithium
- resources/copper
- infrastructure/building_materials
- energy/solar
- infrastructure/engineering_epc
- resources/balsa
- resources/nickel
rows_found_this_cycle:
  energy/fission_smr: 0
  resources/niobium: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 0
  energy/wind: 0
  energy/other_renewables: 2
  energy/power_plants_grid: 0
  resources/water: 0
  infrastructure/port_cranes: 0
  resources/lithium: 0
  resources/copper: 0
  infrastructure/building_materials: 0
  energy/solar: 3
  infrastructure/engineering_epc: 0
  resources/balsa: 0
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 2
  prc: 3
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 158 (seed 20261158) ===
# Shuffled order: rail, niobium, water, wind, bridges_roads, balsa,
#   other_renewables, building_materials, solar, lithium, nickel,
#   engineering_epc, port_ownership, power_plants_grid, graphite, copper,
#   fission_smr, port_cranes.
# Logged 5 sourced rows (3 US / 2 PRC; thin dry; no padding):
#   prc water: powerchina_panama_city_water_148p9m (~USD 148.9m contract).
#   us wind: aes_panama_penonome_i_55mw_2020 (55 MW acquisition; CapEx blank).
#   prc bridges_roads: powerchina_el_sillar_bolivia_2023 (30.3 km; CapEx blank).
#   us other_renewables: ormat_platanares_honduras_35mw (35 MW; CapEx blank).
#   us solar: aes_holcim_el_ronco_21p4mw_2023 (USD 14.8m Banco Cuscatlán financing).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: rail, niobium, balsa, building_materials, lithium, nickel,
#   engineering_epc, port_ownership, power_plants_grid, graphite, copper,
#   fission_smr, port_cranes.
# Dense already-logged: CRRC Melipilla/Batuco; AES San Fernando/Brisas; Sajalices;
#   CHEC Kingston yard; Corentyne Lot 2 paving (not bridge contract).
# Active after cycle 158: us308 / prc317 / allied253 / other38 (n=916).
shuffle_seed: 20261158
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/rail
- resources/niobium
- resources/water
- energy/wind
- infrastructure/bridges_roads
- resources/balsa
- energy/other_renewables
- infrastructure/building_materials
- energy/solar
- resources/lithium
- resources/nickel
- infrastructure/engineering_epc
- infrastructure/port_ownership
- energy/power_plants_grid
- resources/graphite
- resources/copper
- energy/fission_smr
- infrastructure/port_cranes
rows_found_this_cycle:
  infrastructure/rail: 0
  resources/niobium: 0
  resources/water: 1
  energy/wind: 1
  infrastructure/bridges_roads: 1
  resources/balsa: 0
  energy/other_renewables: 1
  infrastructure/building_materials: 0
  energy/solar: 1
  resources/lithium: 0
  resources/nickel: 0
  infrastructure/engineering_epc: 0
  infrastructure/port_ownership: 0
  energy/power_plants_grid: 0
  resources/graphite: 0
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/port_cranes: 0
rows_by_side_this_cycle:
  us: 3
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 157 (seed 20261157) ===
# Shuffled order: other_renewables, port_cranes, rail, balsa, water,
#   fission_smr, niobium, bridges_roads, power_plants_grid, wind, graphite,
#   nickel, copper, port_ownership, engineering_epc, solar, lithium,
#   building_materials.
# Logged 6 sourced rows (3 US / 3 PRC; thin dry; no padding):
#   us other_renewables: aes_nejapa_biogas_6mw_elsalvador (6 MW landfill gas; CapEx blank).
#   us water: seven_seas_barnacle_point_antigua_2migd_2026 (2 IMGD; CapEx blank).
#   us solar: aes_metapan_apopa_1p5mwp_2022 (1.5 MWp Solutions EPC; CapEx blank).
#   prc bridges_roads: crcc_diego_martin_westmoorings_tt_2023 (CRCC interchange; CapEx blank).
#   prc water: china_antigua_water_repiping_60m_2025 (USD 60m UNVERIFIED proxy).
#   prc solar: powerchina_botopasi_suriname_2025 (1,020 kW Phase II site; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: port_cranes, rail, balsa, fission_smr, niobium,
#   power_plants_grid, wind, graphite, nickel, copper, port_ownership,
#   engineering_epc, lithium, building_materials.
# Dense already-logged: Ormat Dominica; AES Santa Ana IV / Meanguera / Peravia;
#   EXIM Guyana GTE; POWERCHINA Kajana/Djoemoe; El Sillar company primary opened
#   but deferred to C158 load.
# Active after cycle 157: us305 / prc315 / allied253 / other38 (n=911).
shuffle_seed: 20261157
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/other_renewables
- infrastructure/port_cranes
- infrastructure/rail
- resources/balsa
- resources/water
- energy/fission_smr
- resources/niobium
- infrastructure/bridges_roads
- energy/power_plants_grid
- energy/wind
- resources/graphite
- resources/nickel
- resources/copper
- infrastructure/port_ownership
- infrastructure/engineering_epc
- energy/solar
- resources/lithium
- infrastructure/building_materials
rows_found_this_cycle:
  energy/other_renewables: 1
  infrastructure/port_cranes: 0
  infrastructure/rail: 0
  resources/balsa: 0
  resources/water: 2
  energy/fission_smr: 0
  resources/niobium: 0
  infrastructure/bridges_roads: 1
  energy/power_plants_grid: 0
  energy/wind: 0
  resources/graphite: 0
  resources/nickel: 0
  resources/copper: 0
  infrastructure/port_ownership: 0
  infrastructure/engineering_epc: 0
  energy/solar: 2
  resources/lithium: 0
  infrastructure/building_materials: 0
rows_by_side_this_cycle:
  us: 3
  prc: 3
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 156 (seed 20261156) ===
# Shuffled order: port_cranes, power_plants_grid, copper, rail, niobium,
#   bridges_roads, wind, port_ownership, engineering_epc, building_materials,
#   other_renewables, fission_smr, lithium, balsa, water, graphite, nickel, solar.
# Logged 6 sourced rows (3 US / 2 PRC / 1 allied; thin dry; no padding):
#   allied port_cranes: konecranes_kingstown_esp7_svg_2024 (ESP.7 MHC; CapEx blank).
#   us port_ownership: exim_liwathon_bos_bahamas_71p3m_2023 (EXIM >USD 71.3m).
#   us water: exim_trinidad_mou_500m_2024 (MOU ceiling USD 500m).
#   us solar: aes_panama_los_santos_8mw_2025 (8 MW COD year 2025; CapEx blank).
#   prc solar: china_cuba_martires_barbados_ii_5mw_2025 (PRC donation phase 1 close).
#   prc solar: powerchina_kajana_guyaba_suriname_2026 (Sites 3+9 COD; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: power_plants_grid, copper, rail, niobium, bridges_roads,
#   wind, engineering_epc, building_materials, other_renewables, fission_smr,
#   lithium, balsa, graphite, nickel.
# Dense already-logged: CRCC Demerara; POWERCHINA Djoemoe; ZPMC Kingston;
#   AES Corotú C155; MMG Anglo nickel; CBMM/CMOC.
# Active after cycle 156: us302 / prc312 / allied253 / other38 (n=905).
shuffle_seed: 20261156
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_cranes
- energy/power_plants_grid
- resources/copper
- infrastructure/rail
- resources/niobium
- infrastructure/bridges_roads
- energy/wind
- infrastructure/port_ownership
- infrastructure/engineering_epc
- infrastructure/building_materials
- energy/other_renewables
- energy/fission_smr
- resources/lithium
- resources/balsa
- resources/water
- resources/graphite
- resources/nickel
- energy/solar
rows_found_this_cycle:
  infrastructure/port_cranes: 1
  energy/power_plants_grid: 0
  resources/copper: 0
  infrastructure/rail: 0
  resources/niobium: 0
  infrastructure/bridges_roads: 0
  energy/wind: 0
  infrastructure/port_ownership: 1
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  energy/other_renewables: 0
  energy/fission_smr: 0
  resources/lithium: 0
  resources/balsa: 0
  resources/water: 1
  resources/graphite: 0
  resources/nickel: 0
  energy/solar: 3
rows_by_side_this_cycle:
  us: 3
  prc: 2
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 155 (seed 20261155) ===
# Shuffled order: building_materials, power_plants_grid, fission_smr, graphite,
#   other_renewables, port_ownership, nickel, engineering_epc, copper, lithium,
#   water, wind, solar, balsa, rail, port_cranes, bridges_roads, niobium.
# Logged 6 sourced rows (4 US / 2 PRC; thin dry; no padding):
#   us water: seven_seas_ffryes_antigua_1migd_2025 (1 IMGD BOOT Ffryes; CapEx blank).
#   us other_renewables: exim_saint_kitts_mou_300m_2024 (MOU ceiling USD 300m).
#   us water: exim_barbados_mou_500m_2024 (MOU ceiling USD 500m; water/sanitation).
#   us solar: aes_panama_corotu_10mw_2025 (10 MW COD year 2025; CapEx blank).
#   prc engineering_epc: crec5_dominica_intl_airport_wesley_2024 (CR5 Wesley; CapEx blank).
#   prc solar: shanghai_electric_castillo_agramonte_cuba_5mw_2026 (5 MW + 1 MW BESS).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: building_materials, power_plants_grid, fission_smr, graphite,
#   port_ownership, nickel, copper, lithium, wind, balsa, rail, port_cranes,
#   bridges_roads, niobium.
# Dense already-logged: Sinoma PANAM/Cibao; State Grid UHV; MMG Anglo nickel;
#   CBMM/CMOC; POWERCHINA Suriname microgrid P2; AES Andes Solar IIa/IIb.
# Active after cycle 155: us299 / prc310 / allied252 / other38 (n=899).
shuffle_seed: 20261155
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- energy/power_plants_grid
- energy/fission_smr
- resources/graphite
- energy/other_renewables
- infrastructure/port_ownership
- resources/nickel
- infrastructure/engineering_epc
- resources/copper
- resources/lithium
- resources/water
- energy/wind
- energy/solar
- resources/balsa
- infrastructure/rail
- infrastructure/port_cranes
- infrastructure/bridges_roads
- resources/niobium
rows_found_this_cycle:
  infrastructure/building_materials: 0
  energy/power_plants_grid: 0
  energy/fission_smr: 0
  resources/graphite: 0
  energy/other_renewables: 1
  infrastructure/port_ownership: 0
  resources/nickel: 0
  infrastructure/engineering_epc: 1
  resources/copper: 0
  resources/lithium: 0
  resources/water: 2
  energy/wind: 0
  energy/solar: 2
  resources/balsa: 0
  infrastructure/rail: 0
  infrastructure/port_cranes: 0
  infrastructure/bridges_roads: 0
  resources/niobium: 0
rows_by_side_this_cycle:
  us: 4
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 154 (seed 20261154) ===
# Shuffled order: building_materials, niobium, copper, wind, fission_smr, graphite,
#   power_plants_grid, engineering_epc, port_ownership, solar, lithium, nickel,
#   rail, water, other_renewables, port_cranes, balsa, bridges_roads.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us solar: aes_andes_solar_iia_81mw_cod_2021 (81 MW COD; CapEx blank).
#   us other_renewables: aes_andes_gecelca_438gwh_ppa_2021 (438 GWh/y; CapEx blank).
#   prc water: powerchina_malabar_wwtp_trinidad_2019 (40,000 m³/d; CapEx blank).
#   prc bridges_roads: crec_espino_highway_bolivia_2023 (Ruta 36 opening; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: building_materials, niobium, copper, wind, fission_smr,
#   graphite, power_plants_grid, engineering_epc, port_ownership, lithium, nickel,
#   rail, port_cranes, balsa.
# Dense already-logged: Mauriti COD; Chile G15/G04 substations; Conchagua;
#   MMG Anglo nickel; Goldwind Pemuco/Touros; CHEC Las Palmas.
# Active after cycle 154: us295 / prc308 / allied252 / other38 (n=893).
shuffle_seed: 20261154
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- resources/niobium
- resources/copper
- energy/wind
- energy/fission_smr
- resources/graphite
- energy/power_plants_grid
- infrastructure/engineering_epc
- infrastructure/port_ownership
- energy/solar
- resources/lithium
- resources/nickel
- infrastructure/rail
- resources/water
- energy/other_renewables
- infrastructure/port_cranes
- resources/balsa
- infrastructure/bridges_roads
rows_found_this_cycle:
  infrastructure/building_materials: 0
  resources/niobium: 0
  resources/copper: 0
  energy/wind: 0
  energy/fission_smr: 0
  resources/graphite: 0
  energy/power_plants_grid: 0
  infrastructure/engineering_epc: 0
  infrastructure/port_ownership: 0
  energy/solar: 1
  resources/lithium: 0
  resources/nickel: 0
  infrastructure/rail: 0
  resources/water: 1
  energy/other_renewables: 1
  infrastructure/port_cranes: 0
  resources/balsa: 0
  infrastructure/bridges_roads: 1
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 153 (seed 20261153) ===
# Shuffled order: graphite, building_materials, port_cranes, lithium, port_ownership,
#   rail, solar, power_plants_grid, balsa, other_renewables, engineering_epc, wind,
#   copper, water, niobium, nickel, fission_smr, bridges_roads.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us other_renewables: aes_andes_solar_iib_180mw_cod_2023 (180 MW + 112 MW/5h BESS).
#   us other_renewables: aes_andes_virtual_reservoir_ii_cod_2023 (up to 197 MWh).
#   prc solar: powerchina_tamberias_diaguitas_5m_2019 (~USD 5m UNVERIFIED proxy).
#   prc bridges_roads: crec_egd_highway_bid9_guyana_2023 (Bid 9 opening; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: graphite, building_materials, port_cranes, lithium,
#   port_ownership, rail, power_plants_grid, balsa, engineering_epc, wind, copper,
#   water, niobium, nickel, fission_smr.
# Dense already-logged: GUYSOL CREC/SUMEC Onderneeming; State Grid GATE/UHV;
#   MMG Anglo nickel Brazil; Goldwind Pemuco/SPIC Touros; CHEC Las Palmas.
# Active after cycle 153: us293 / prc306 / allied252 / other38 (n=889).
shuffle_seed: 20261153
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/graphite
- infrastructure/building_materials
- infrastructure/port_cranes
- resources/lithium
- infrastructure/port_ownership
- infrastructure/rail
- energy/solar
- energy/power_plants_grid
- resources/balsa
- energy/other_renewables
- infrastructure/engineering_epc
- energy/wind
- resources/copper
- resources/water
- resources/niobium
- resources/nickel
- energy/fission_smr
- infrastructure/bridges_roads
rows_found_this_cycle:
  resources/graphite: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  resources/lithium: 0
  infrastructure/port_ownership: 0
  infrastructure/rail: 0
  energy/solar: 1
  energy/power_plants_grid: 0
  resources/balsa: 0
  energy/other_renewables: 2
  infrastructure/engineering_epc: 0
  energy/wind: 0
  resources/copper: 0
  resources/water: 0
  resources/niobium: 0
  resources/nickel: 0
  energy/fission_smr: 0
  infrastructure/bridges_roads: 1
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 152 (seed 20261152) ===
# Shuffled order: balsa, power_plants_grid, other_renewables, rail, building_materials,
#   bridges_roads, nickel, solar, niobium, graphite, port_ownership, wind, port_cranes,
#   water, fission_smr, lithium, engineering_epc, copper.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us other_renewables: aes_andes_teck_cda_550gwh_2020 (550 GWh/y; CapEx blank).
#   us power_plants_grid: aes_andes_alto_maipo_531mw_cod_2022 (531 MW COD; CapEx blank).
#   prc solar: powerchina_cura_brochero_villa_maria_65mw_2020 (65 MW; CapEx blank).
#   prc solar: powerchina_andina_marianas_120mwp_2021 (120 MWp + 72 MW/288 MWh; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: balsa, rail, building_materials, bridges_roads, nickel,
#   niobium, graphite, port_ownership, wind, port_cranes, water, fission_smr,
#   lithium, engineering_epc, copper.
# Dense already-logged: Sajalices; Guyana DBIS Phase II; CHEC Kingston yard;
#   Helios/Loma Blanca; CTG Baranoa; Sungrow Aurora/Desierto.
# Active after cycle 152: us291 / prc304 / allied252 / other38 (n=885).
shuffle_seed: 20261152
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/balsa
- energy/power_plants_grid
- energy/other_renewables
- infrastructure/rail
- infrastructure/building_materials
- infrastructure/bridges_roads
- resources/nickel
- energy/solar
- resources/niobium
- resources/graphite
- infrastructure/port_ownership
- energy/wind
- infrastructure/port_cranes
- resources/water
- energy/fission_smr
- resources/lithium
- infrastructure/engineering_epc
- resources/copper
rows_found_this_cycle:
  resources/balsa: 0
  energy/power_plants_grid: 1
  energy/other_renewables: 1
  infrastructure/rail: 0
  infrastructure/building_materials: 0
  infrastructure/bridges_roads: 0
  resources/nickel: 0
  energy/solar: 2
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/port_ownership: 0
  energy/wind: 0
  infrastructure/port_cranes: 0
  resources/water: 0
  energy/fission_smr: 0
  resources/lithium: 0
  infrastructure/engineering_epc: 0
  resources/copper: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 151 (seed 20261151) ===
# Shuffled order: graphite, copper, other_renewables, engineering_epc, fission_smr,
#   water, building_materials, port_cranes, bridges_roads, rail, niobium, wind,
#   power_plants_grid, solar, balsa, nickel, lithium, port_ownership.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us other_renewables: aes_andes_google_440gwh_ppa_2019 (440 GWh/y 14y hybrid; CapEx blank).
#   us other_renewables: aes_andes_teck_qb2_1069gwh_2022 (1,069 GWh/y 17y; CapEx blank).
#   prc solar: powerchina_san_carlos_18p3mw_salta_2024 (18.3 MW EPC; CapEx blank).
#   prc other_renewables: powerchina_el_tambolar_520m_2019 (83.5 MW; USD 520m).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: graphite, copper, engineering_epc, fission_smr, water,
#   building_materials, port_cranes, bridges_roads, rail, niobium, wind,
#   power_plants_grid, balsa, nickel, lithium, port_ownership.
# Dense already-logged: Helios/Loma Blanca Miramar; CHEC Posorja; CRCC Batuco;
#   Sungrow BESS del Desierto / Aurora; CTG Baranoa; State Grid NE UHV.
# Active after cycle 151: us289 / prc302 / allied252 / other38 (n=881).
shuffle_seed: 20261151
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/graphite
- resources/copper
- energy/other_renewables
- infrastructure/engineering_epc
- energy/fission_smr
- resources/water
- infrastructure/building_materials
- infrastructure/port_cranes
- infrastructure/bridges_roads
- infrastructure/rail
- resources/niobium
- energy/wind
- energy/power_plants_grid
- energy/solar
- resources/balsa
- resources/nickel
- resources/lithium
- infrastructure/port_ownership
rows_found_this_cycle:
  resources/graphite: 0
  resources/copper: 0
  energy/other_renewables: 3
  infrastructure/engineering_epc: 0
  energy/fission_smr: 0
  resources/water: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  infrastructure/bridges_roads: 0
  infrastructure/rail: 0
  resources/niobium: 0
  energy/wind: 0
  energy/power_plants_grid: 0
  energy/solar: 1
  resources/balsa: 0
  resources/nickel: 0
  resources/lithium: 0
  infrastructure/port_ownership: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 150 (seed 20261150) ===
# Shuffled order: fission_smr, copper, engineering_epc, graphite, solar, water,
#   niobium, other_renewables, lithium, power_plants_grid, port_cranes, wind,
#   nickel, port_ownership, balsa, building_materials, rail, bridges_roads.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us other_renewables: aes_andes_codelco_ppa_1p6twh_2023 (1.6 TWh/y; CapEx blank).
#   us other_renewables: aes_andes_microsoft_chile_ppa_2022 (Microsoft DC PPA; CapEx blank).
#   prc solar: ctg_arinos_first_unit_78p4mw_2024 (78.4 MW first-unit COD; CapEx blank).
#   prc solar: sumec_guyana_trafalgar_8m_2025 (USD 8m UNVERIFIED proxy / 4 MWp).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: fission_smr, copper, engineering_epc, graphite, water,
#   niobium, lithium, power_plants_grid, port_cranes, wind, nickel,
#   port_ownership, balsa, building_materials, rail, bridges_roads.
# Dense already-logged: State Grid NE UHV; CTG Arinos full COD; Zijin Longking
#   Aurora/Rosebel; Sungrow San Martín; EXIM Guyana GTE.
# Active after cycle 150: us287 / prc300 / allied252 / other38 (n=877).
shuffle_seed: 20261150
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/fission_smr
- resources/copper
- infrastructure/engineering_epc
- resources/graphite
- energy/solar
- resources/water
- resources/niobium
- energy/other_renewables
- resources/lithium
- energy/power_plants_grid
- infrastructure/port_cranes
- energy/wind
- resources/nickel
- infrastructure/port_ownership
- resources/balsa
- infrastructure/building_materials
- infrastructure/rail
- infrastructure/bridges_roads
rows_found_this_cycle:
  energy/fission_smr: 0
  resources/copper: 0
  infrastructure/engineering_epc: 0
  resources/graphite: 0
  energy/solar: 2
  resources/water: 0
  resources/niobium: 0
  energy/other_renewables: 2
  resources/lithium: 0
  energy/power_plants_grid: 0
  infrastructure/port_cranes: 0
  energy/wind: 0
  resources/nickel: 0
  infrastructure/port_ownership: 0
  resources/balsa: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 149 (seed 20261149) ===
# Shuffled order: balsa, power_plants_grid, solar, fission_smr, engineering_epc,
#   port_ownership, niobium, building_materials, rail, graphite, port_cranes,
#   bridges_roads, other_renewables, copper, nickel, wind, water, lithium.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us solar: aes_bayasol_60m_dr_2021 (USD 60m / 58 MWp NTP).
#   us solar: aes_santanasol_45m_dr_2021 (USD 45m est. / 50 MW).
#   prc solar: crec_guyana_guysol_18mw_2025 (18 MW / 12 MWh portfolio COD; CapEx blank).
#   prc solar: sumec_guyana_charity_3mw_2025 (3 MWp COD; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: balsa, power_plants_grid, fission_smr, engineering_epc,
#   port_ownership, niobium, building_materials, rail, graphite, port_cranes,
#   bridges_roads, other_renewables, copper, nickel, wind, water, lithium.
# Dense already-logged: EXIM Guyana GTE; FOCOL Bahamas; SPIC São Simão UG7;
#   AES Mirasol/Peravia/Pampas; POWERCHINA Mauriti/Sajalices/Coca Codo.
# Active after cycle 149: us285 / prc298 / allied252 / other38 (n=873).
shuffle_seed: 20261149
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/balsa
- energy/power_plants_grid
- energy/solar
- energy/fission_smr
- infrastructure/engineering_epc
- infrastructure/port_ownership
- resources/niobium
- infrastructure/building_materials
- infrastructure/rail
- resources/graphite
- infrastructure/port_cranes
- infrastructure/bridges_roads
- energy/other_renewables
- resources/copper
- resources/nickel
- energy/wind
- resources/water
- resources/lithium
rows_found_this_cycle:
  resources/balsa: 0
  energy/power_plants_grid: 0
  energy/solar: 4
  energy/fission_smr: 0
  infrastructure/engineering_epc: 0
  infrastructure/port_ownership: 0
  resources/niobium: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  resources/graphite: 0
  infrastructure/port_cranes: 0
  infrastructure/bridges_roads: 0
  energy/other_renewables: 0
  resources/copper: 0
  resources/nickel: 0
  energy/wind: 0
  resources/water: 0
  resources/lithium: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === HQ retag (before cycle 148): ContourGlobal London HQ ===
# ContourGlobal is London-HQ (allied), not U.S.-HQ. Retagged 5 active rows
# previously tagged us → allied (post-audit residual missed in cycle-88+ sweep).
# side_retag_total: 5
# side_retag_by_from_to:
#   us->allied: 5
# side_retag_by_side_delta:
#   us: -5
#   allied: +5
# side_retag_by_subcategory:
#   energy/solar: 3 (victor_jara, los_maitenes, condor)
#   energy/other_renewables: 2 (oasis_atacama_ev, quillagua)
# side_retag_examples:
#   contourglobal_oasis_atacama_ev_2024; contourglobal_victor_jara_cod_2026;
#   contourglobal_los_maitenes_chile_2026; contourglobal_quillagua_inaug_2025;
#   contourglobal_condor_colombia_2025
# Active after Contour retag (before C148 load): us281 / prc294 / allied252 / other38 (n=865).

# === Cycle 148 (seed 20261148) ===
# Shuffled order: nickel, niobium, lithium, water, balsa, rail,
#   engineering_epc, building_materials, graphite, solar, fission_smr, wind,
#   power_plants_grid, port_ownership, copper, port_cranes, other_renewables,
#   bridges_roads.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us solar: aes_brisas_26mw_colombia_2023 (26 MWp COD Aipe; CapEx blank).
#   us wind: aes_agua_clara_acquisition_98m_dr_2022 (USD 98m SEC 10-Q).
#   prc solar: sumec_guyana_prospect_solar_5p5m_2025 (USD 5.5m / 3 MWp).
#   prc solar: sumec_guyana_hampshire_3mw_2025 (3 MWp COD; CapEx blank).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: nickel, niobium, lithium, water, balsa, rail,
#   engineering_epc, building_materials, graphite, fission_smr,
#   power_plants_grid, port_ownership, copper, port_cranes, other_renewables,
#   bridges_roads.
# Dense already-logged: POWERCHINA Mauriti/Tepuy/Sajalices/Ivirizu;
#   AES Pampas/Cristales/Mirasol/Peravia; Zijin 3Q RIGI; MMG Las Bambas CapEx.
# Active after cycle 148: us283 / prc296 / allied252 / other38 (n=869).
shuffle_seed: 20261148
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/nickel
- resources/niobium
- resources/lithium
- resources/water
- resources/balsa
- infrastructure/rail
- infrastructure/engineering_epc
- infrastructure/building_materials
- resources/graphite
- energy/solar
- energy/fission_smr
- energy/wind
- energy/power_plants_grid
- infrastructure/port_ownership
- resources/copper
- infrastructure/port_cranes
- energy/other_renewables
- infrastructure/bridges_roads
rows_found_this_cycle:
  resources/nickel: 0
  resources/niobium: 0
  resources/lithium: 0
  resources/water: 0
  resources/balsa: 0
  infrastructure/rail: 0
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  resources/graphite: 0
  energy/solar: 3
  energy/fission_smr: 0
  energy/wind: 1
  energy/power_plants_grid: 0
  infrastructure/port_ownership: 0
  resources/copper: 0
  infrastructure/port_cranes: 0
  energy/other_renewables: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 147 (seed 20261147) ===
# Shuffled order: power_plants_grid, solar, fission_smr, port_cranes, rail,
#   bridges_roads, engineering_epc, graphite, copper, building_materials, lithium,
#   port_ownership, niobium, other_renewables, wind, balsa, water, nickel.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us solar: aes_san_fernando_61mw_colombia_2021 (~USD 40m / 61 MWp).
#   us solar: aes_castilla_21mw_colombia_2019 (~USD 20m / 21 MWp).
#   prc copper: mmg_las_bambas_h1_2026_capex_272m (USD 272.4m H1 CapEx).
#   prc wind: powerchina_loma_blanca_miramar_355mw_epc (355 MW Goldwind EPC).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: power_plants_grid, fission_smr, port_cranes, rail,
#   bridges_roads, engineering_epc, graphite, building_materials, lithium,
#   port_ownership, niobium, other_renewables, balsa, water, nickel.
# Dense already-logged: ZPMC CMSA/Contecon Manzanillo; Sungrow Observatorio;
#   Aldesa Mexico hybrid (allied HQ); Ganfeng Lithea USD 962m.
# Active after cycle 147: us286 / prc294 / allied247 / other38 (n=865).
shuffle_seed: 20261147
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/power_plants_grid
- energy/solar
- energy/fission_smr
- infrastructure/port_cranes
- infrastructure/rail
- infrastructure/bridges_roads
- infrastructure/engineering_epc
- resources/graphite
- resources/copper
- infrastructure/building_materials
- resources/lithium
- infrastructure/port_ownership
- resources/niobium
- energy/other_renewables
- energy/wind
- resources/balsa
- resources/water
- resources/nickel
rows_found_this_cycle:
  energy/power_plants_grid: 0
  energy/solar: 2
  energy/fission_smr: 0
  infrastructure/port_cranes: 0
  infrastructure/rail: 0
  infrastructure/bridges_roads: 0
  infrastructure/engineering_epc: 0
  resources/graphite: 0
  resources/copper: 1
  infrastructure/building_materials: 0
  resources/lithium: 0
  infrastructure/port_ownership: 0
  resources/niobium: 0
  energy/other_renewables: 0
  energy/wind: 1
  resources/balsa: 0
  resources/water: 0
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 146 (seed 20261146) ===
# Shuffled order: water, wind, port_ownership, bridges_roads, other_renewables,
#   rail, fission_smr, niobium, copper, graphite, solar, building_materials,
#   port_cranes, engineering_epc, nickel, lithium, balsa, power_plants_grid.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us wind: aes_andes_mesamavida_68mw_cod_2022 (68 MW first-stage COD).
#   us rail: aecom_panama_david_master_plan_2p2m_2024 (B/.2.2m master plan).
#   prc wind: goldwind_lomas_taltal_342mw_install_2024 (57×6 MW / 342 MW).
#   prc solar: powerchina_cafayate_argentina_97p6mw_epc (97.6 MW Salta EPC).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: water, port_ownership, bridges_roads, other_renewables,
#   fission_smr, niobium, copper, graphite, building_materials, port_cranes,
#   engineering_epc, nickel, lithium, balsa, power_plants_grid.
# Dense already-logged: CHEC Las Palmas; CRCC Ruta 5; Sungrow Coya supply;
#   Palmira III / Francisco Juana; Goldwind Pemuco; State Grid NE UHV.
# Active after cycle 146: us284 / prc292 / allied247 / other38 (n=861).
shuffle_seed: 20261146
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- energy/wind
- infrastructure/port_ownership
- infrastructure/bridges_roads
- energy/other_renewables
- infrastructure/rail
- energy/fission_smr
- resources/niobium
- resources/copper
- resources/graphite
- energy/solar
- infrastructure/building_materials
- infrastructure/port_cranes
- infrastructure/engineering_epc
- resources/nickel
- resources/lithium
- resources/balsa
- energy/power_plants_grid
rows_found_this_cycle:
  resources/water: 0
  energy/wind: 2
  infrastructure/port_ownership: 0
  infrastructure/bridges_roads: 0
  energy/other_renewables: 0
  infrastructure/rail: 1
  energy/fission_smr: 0
  resources/niobium: 0
  resources/copper: 0
  resources/graphite: 0
  energy/solar: 1
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 0
  resources/nickel: 0
  resources/lithium: 0
  resources/balsa: 0
  energy/power_plants_grid: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 145 (seed 20261145) ===
# Shuffled order: solar, port_ownership, other_renewables, graphite, balsa, wind,
#   lithium, rail, water, engineering_epc, nickel, port_cranes, copper, niobium,
#   bridges_roads, fission_smr, building_materials, power_plants_grid.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us solar: dfc_ienova_mexico_4solar_241m_2020 (DFC up to USD 241m / 426 MW).
#   us wind: aes_andes_los_olmos_110mw_cod_2022 (110 MW Mulchén COD).
#   prc wind: powerchina_las_acacias_colombia_240mw_epc_2024 (240 MW Cundinamarca EPC).
#   prc rail: crec7_alameda_melipilla_depot_90m_2025 (USD 90m EFE depot).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: port_ownership, other_renewables, lithium, water,
#   engineering_epc, nickel, port_cranes, copper, niobium, bridges_roads,
#   fission_smr, building_materials, power_plants_grid, graphite, balsa.
# Dense already-logged: Mauriti COD; Sajalices; Serra da Palmeira; Touros/Goldwind;
#   El Barro; MMG Nickel Brazil SPA; State Grid NE UHV; ContourGlobal Quillagua
#   (London HQ → allied candidate, still tagged us pending batch retag).
# Holdovers opened next: AECOM Panama–David B/.2.2m (US rail); AES Mesamávida.
# Active after cycle 145: us282 / prc290 / allied247 / other38 (n=857).
shuffle_seed: 20261145
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/solar
- infrastructure/port_ownership
- energy/other_renewables
- resources/graphite
- resources/balsa
- energy/wind
- resources/lithium
- infrastructure/rail
- resources/water
- infrastructure/engineering_epc
- resources/nickel
- infrastructure/port_cranes
- resources/copper
- resources/niobium
- infrastructure/bridges_roads
- energy/fission_smr
- infrastructure/building_materials
- energy/power_plants_grid
rows_found_this_cycle:
  energy/solar: 1
  infrastructure/port_ownership: 0
  energy/other_renewables: 0
  resources/graphite: 0
  resources/balsa: 0
  energy/wind: 2
  resources/lithium: 0
  infrastructure/rail: 1
  resources/water: 0
  infrastructure/engineering_epc: 0
  resources/nickel: 0
  infrastructure/port_cranes: 0
  resources/copper: 0
  resources/niobium: 0
  infrastructure/bridges_roads: 0
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  energy/power_plants_grid: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 144 (seed 20261144) ===
# Shuffled order: copper, niobium, port_ownership, bridges_roads, solar, water,
#   other_renewables, power_plants_grid, port_cranes, lithium, wind, rail,
#   building_materials, balsa, graphite, engineering_epc, fission_smr, nickel.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   prc copper: mmg_las_bambas_2025_capex_494m (USD 494.2m 2025 CapEx).
#   prc solar: powerchina_colombia_3pv_260mw_cod_2025 (Guayepo III+Escobales+Paranova III).
#   us wind: aes_andes_campo_lindo_cod_2023 (66 MW Biobío COD).
#   us rail: progress_rail_vli_msa_norte_500m_brl_2025 (MSA até R$500m → USD 93.2m).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: niobium, port_ownership, bridges_roads, water, other_renewables,
#   power_plants_grid, port_cranes, lithium, building_materials, balsa, graphite,
#   engineering_epc, fission_smr, nickel.
# Dense already-logged: Toromocho ITS3; Chalcobamba Senace; MMG 2026 CapEx guidance;
#   Guayepo/Escobales/Paranova plant-level rows; Progress Rail SD70 delivery; Bolero BESS
#   under-construction row (COD company primary not opened this cycle).
# Active after cycle 144: us280 / prc288 / allied247 / other38 (n=853).
shuffle_seed: 20261144
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/copper
- resources/niobium
- infrastructure/port_ownership
- infrastructure/bridges_roads
- energy/solar
- resources/water
- energy/other_renewables
- energy/power_plants_grid
- infrastructure/port_cranes
- resources/lithium
- energy/wind
- infrastructure/rail
- infrastructure/building_materials
- resources/balsa
- resources/graphite
- infrastructure/engineering_epc
- energy/fission_smr
- resources/nickel
rows_found_this_cycle:
  resources/copper: 1
  resources/niobium: 0
  infrastructure/port_ownership: 0
  infrastructure/bridges_roads: 0
  energy/solar: 1
  resources/water: 0
  energy/other_renewables: 0
  energy/power_plants_grid: 0
  infrastructure/port_cranes: 0
  resources/lithium: 0
  energy/wind: 1
  infrastructure/rail: 1
  infrastructure/building_materials: 0
  resources/balsa: 0
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  energy/fission_smr: 0
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 143 (seed 20261143) ===
# Shuffled order: copper, fission_smr, rail, bridges_roads, engineering_epc,
#   building_materials, port_cranes, power_plants_grid, balsa, solar,
#   other_renewables, port_ownership, graphite, water, lithium, niobium, nickel, wind.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   us solar: aes_colombia_solar3_anla_100mw_2025 (100 MW ANLA license Tolima).
#   prc other_renewables: powerchina_barueri_wte_brazil_2025 (19.1 MW / 870 t/day WtE).
#   prc wind: ctg_lds_red_coral_marcona_256m_2025 (135.7 MW San Juan de Marcona USD 256m).
#   us wind: aes_andes_san_matias_cod_2024 (78 MW Biobío COD).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: copper, fission_smr, rail, bridges_roads, engineering_epc,
#   building_materials, port_cranes, power_plants_grid, balsa, port_ownership,
#   graphite, water, lithium, niobium, nickel.
# Dense already-logged: El Abra/Toromocho/Goldwind 470/FINAME; Progress Rail SD70+MSA
#   on same primary; State Grid NE UHV; Wabtec MRS 254m; SANY Suape/HGT Aracruz;
#   Francisco Juana; Baranoa II/III; Montego Bay perimeter contract.
# Active after cycle 143: us278 / prc286 / allied247 / other38 (n=849).
shuffle_seed: 20261143
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/copper
- energy/fission_smr
- infrastructure/rail
- infrastructure/bridges_roads
- infrastructure/engineering_epc
- infrastructure/building_materials
- infrastructure/port_cranes
- energy/power_plants_grid
- resources/balsa
- energy/solar
- energy/other_renewables
- infrastructure/port_ownership
- resources/graphite
- resources/water
- resources/lithium
- resources/niobium
- resources/nickel
- energy/wind
rows_found_this_cycle:
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/rail: 0
  infrastructure/bridges_roads: 0
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  energy/power_plants_grid: 0
  resources/balsa: 0
  energy/solar: 1
  energy/other_renewables: 1
  infrastructure/port_ownership: 0
  resources/graphite: 0
  resources/water: 0
  resources/lithium: 0
  resources/niobium: 0
  resources/nickel: 0
  energy/wind: 2
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 142 (seed 20261142) ===
# Shuffled order: water, bridges_roads, balsa, building_materials, engineering_epc,
#   nickel, niobium, solar, port_cranes, rail, copper, fission_smr, port_ownership,
#   wind, graphite, lithium, power_plants_grid, other_renewables.
# Logged 4 sourced rows (2 US / 2 PRC; thin dry; no padding):
#   prc bridges_roads: chec_ruta32_four_lane_open_2026 (104.24 km four-lane opening).
#   us solar: aes_dr_mirasol_100mw_2025 (100 MWn / 127 MWinst COD Feb 2025).
#   prc solar: trina_pampa_del_infierno_150mw_argentina (150.18 MW Vanguard-1P).
#   us other_renewables: aes_andes_solar_iv_cod_2024 (211 MW PV + 130 MW/5h BESS).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: water, balsa, building_materials, engineering_epc, nickel, niobium,
#   port_cranes, rail, copper, fission_smr, port_ownership, wind, graphite, lithium,
#   power_plants_grid.
# Dense already-logged: POWERCHINA Santo Domingo water/Conchagua/Guayepo; CHEC Kingston
#   yard/SCHIP/Ruta32 contract; Atlas Campano; CTG Arinos/Palmeira; Meitner ACR-300.
# Active after cycle 142: us276 / prc284 / allied247 / other38 (n=845).
shuffle_seed: 20261142
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- infrastructure/bridges_roads
- resources/balsa
- infrastructure/building_materials
- infrastructure/engineering_epc
- resources/nickel
- resources/niobium
- energy/solar
- infrastructure/port_cranes
- infrastructure/rail
- resources/copper
- energy/fission_smr
- infrastructure/port_ownership
- energy/wind
- resources/graphite
- resources/lithium
- energy/power_plants_grid
- energy/other_renewables
rows_found_this_cycle:
  resources/water: 0
  infrastructure/bridges_roads: 1
  resources/balsa: 0
  infrastructure/building_materials: 0
  infrastructure/engineering_epc: 0
  resources/nickel: 0
  resources/niobium: 0
  energy/solar: 2
  infrastructure/port_cranes: 0
  infrastructure/rail: 0
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/port_ownership: 0
  energy/wind: 0
  resources/graphite: 0
  resources/lithium: 0
  energy/power_plants_grid: 0
  energy/other_renewables: 1
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 141 (seed 20261141) ===
# Shuffled order: graphite, niobium, balsa, bridges_roads, other_renewables, water,
#   solar, port_ownership, port_cranes, wind, power_plants_grid, lithium,
#   building_materials, rail, nickel, fission_smr, engineering_epc, copper.
# Logged 4 sourced rows (1 US / 3 PRC; thin dry; no padding):
#   us other_renewables: invenergy_la_toba_70m_2022 (35 MW solar + 20 MW BESS; USD 70m).
#   prc other_renewables: sungrow_atlas_bess_del_desierto_2025 (PowerTitan 200 MW/800 MWh).
#   prc solar: ctg_baranoa_ii_iii_58p3mw_2025 (Phase II+III COD; three-phase 58.3 MW).
#   prc wind: spic_pedra_paraiso_touros_755m_brl_2025 (105.4 MW; BRL 755m → USD 137.4m).
# Thin top-up (balsa/graphite/fission_smr): all dry — shift to nickel/niobium also dry.
# Equal-budget misses: graphite, niobium, balsa, bridges_roads, water, port_ownership,
#   port_cranes, power_plants_grid, lithium, building_materials, rail, nickel,
#   fission_smr, engineering_epc, copper.
# Dense already-logged: POWERCHINA Catac/Ituango/Mauriti/Palmira/Francisco Juana/DBIS;
#   Goldwind Touros turbine supply; Array Lupi; GameChange Colombia; EXIM Guyana GTE.
# Active after cycle 141: us274 / prc282 / allied247 / other38 (n=841).
shuffle_seed: 20261141
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/graphite
- resources/niobium
- resources/balsa
- infrastructure/bridges_roads
- energy/other_renewables
- resources/water
- energy/solar
- infrastructure/port_ownership
- infrastructure/port_cranes
- energy/wind
- energy/power_plants_grid
- resources/lithium
- infrastructure/building_materials
- infrastructure/rail
- resources/nickel
- energy/fission_smr
- infrastructure/engineering_epc
- resources/copper
rows_found_this_cycle:
  resources/graphite: 0
  resources/niobium: 0
  resources/balsa: 0
  infrastructure/bridges_roads: 0
  energy/other_renewables: 2
  resources/water: 0
  energy/solar: 1
  infrastructure/port_ownership: 0
  infrastructure/port_cranes: 0
  energy/wind: 1
  energy/power_plants_grid: 0
  resources/lithium: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  resources/nickel: 0
  energy/fission_smr: 0
  infrastructure/engineering_epc: 0
  resources/copper: 0
rows_by_side_this_cycle:
  us: 1
  prc: 3
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - energy/fission_smr

# === Cycle 140 (seed 20261140) ===
# Shuffled order: port_cranes, lithium, nickel, solar, bridges_roads, wind,
#   fission_smr, graphite, power_plants_grid, balsa, water, engineering_epc,
#   building_materials, niobium, copper, rail, port_ownership, other_renewables.
# Logged 3 sourced rows (1 US / 1 PRC / 1 allied; thin dry; no padding):
#   us solar: gamechange_148mw_colombia_2024 (101 MW Genius + 47 MW MaxSpan; CapEx blank).
#   prc solar: powerchina_djoemoe_suriname_2026 (Djoemoe Station COD Jan 2026; CapEx blank).
#   allied solar: greenwood_terra_site1_52mwp_2026 (52 MWp El Copey FC; >USD 50m).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/niobium also dry.
# Equal-budget misses: port_cranes, lithium, nickel, bridges_roads, wind, fission_smr,
#   graphite, power_plants_grid, balsa, water, engineering_epc, building_materials,
#   niobium, copper, rail, port_ownership, other_renewables.
# Dense already-logged: ZPMC Tecon Santos/MultiRio; Sany Suape; Konecranes Arica/Yucatán;
#   Ganfeng Mariana/PPG; Zijin 3Q; Vestas Dom Inocêncio; EXIM Guyana GTE; San Gabán III.
# Active after cycle 140: us273 / prc279 / allied247 / other38 (n=837).
shuffle_seed: 20261140
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_cranes
- resources/lithium
- resources/nickel
- energy/solar
- infrastructure/bridges_roads
- energy/wind
- energy/fission_smr
- resources/graphite
- energy/power_plants_grid
- resources/balsa
- resources/water
- infrastructure/engineering_epc
- infrastructure/building_materials
- resources/niobium
- resources/copper
- infrastructure/rail
- infrastructure/port_ownership
- energy/other_renewables
rows_found_this_cycle:
  infrastructure/port_cranes: 0
  resources/lithium: 0
  resources/nickel: 0
  energy/solar: 3
  infrastructure/bridges_roads: 0
  energy/wind: 0
  energy/fission_smr: 0
  resources/graphite: 0
  energy/power_plants_grid: 0
  resources/balsa: 0
  resources/water: 0
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  resources/niobium: 0
  resources/copper: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  energy/other_renewables: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 139 (seed 20261139) ===
# Shuffled order: other_renewables, fission_smr, building_materials, port_cranes,
#   rail, engineering_epc, lithium, bridges_roads, wind, water, solar,
#   power_plants_grid, nickel, graphite, balsa, niobium, port_ownership, copper.
# Logged 4 sourced rows (1 US / 1 PRC / 2 allied; thin dry; no padding):
#   allied other_renewables: engie_bess_libelula_cod_219m_2026 (203 MW/1,034 MWh; USD 219m).
#   allied other_renewables: engie_bess_los_loros_cod_64m_2026 (48 MW/275.23 MWh; USD 64m).
#   us solar: gamechange_715mwp_latam_2025 (8 projects Chile/Colombia/El Salvador; CapEx blank).
#   prc solar: trina_colinas_vanguard_130mwp_2025 (Vanguard 1P Colinas PE; CapEx blank).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/niobium also dry.
# Equal-budget misses: fission_smr, building_materials, port_cranes, rail, engineering_epc,
#   lithium, bridges_roads, wind, water, power_plants_grid, nickel, graphite, balsa,
#   niobium, port_ownership, copper.
# Dense already-logged: POWERCHINA Santo Domingo water / Sajalices / Francisco Juana /
#   Palmira III / Chile G15-G04 / Suriname Phase II / Guyana DBIS; Goldwind Sento Sé;
#   USTDA Ecuador ARCONEL/CNEL; CCECC Quinto Puente; Nextracker Libélula/Casa dos Ventos.
# Active after cycle 139: us272 / prc278 / allied246 / other38 (n=834).
shuffle_seed: 20261139
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/other_renewables
- energy/fission_smr
- infrastructure/building_materials
- infrastructure/port_cranes
- infrastructure/rail
- infrastructure/engineering_epc
- resources/lithium
- infrastructure/bridges_roads
- energy/wind
- resources/water
- energy/solar
- energy/power_plants_grid
- resources/nickel
- resources/graphite
- resources/balsa
- resources/niobium
- infrastructure/port_ownership
- resources/copper
rows_found_this_cycle:
  energy/other_renewables: 2
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  infrastructure/rail: 0
  infrastructure/engineering_epc: 0
  resources/lithium: 0
  infrastructure/bridges_roads: 0
  energy/wind: 0
  resources/water: 0
  energy/solar: 2
  energy/power_plants_grid: 0
  resources/nickel: 0
  resources/graphite: 0
  resources/balsa: 0
  resources/niobium: 0
  infrastructure/port_ownership: 0
  resources/copper: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 138 (seed 20261138) ===
# Shuffled order: water, bridges_roads, power_plants_grid, port_cranes, copper,
#   wind, port_ownership, fission_smr, lithium, building_materials, rail, niobium,
#   nickel, graphite, solar, engineering_epc, balsa, other_renewables.
# Logged 3 sourced rows (1 US / 1 PRC / 1 allied; thin dry; no padding):
#   us wind: invenergy_patria_600mw_br_2024 (10% + O&M on ~600 MW Asa Branca/Chapada; CapEx blank).
#   prc solar: powerchina_piarco_trinidad_2024 (518.84 kW Piarco Airport COD Jul 2024; CapEx blank).
#   allied power_plants_grid: wartsila_origem_371mw_br_2026 (36×34SG / 371 MW LRCAP; CapEx blank).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: water, bridges_roads, port_cranes, copper, port_ownership,
#   fission_smr, lithium, building_materials, rail, niobium, nickel, graphite,
#   engineering_epc, balsa, other_renewables (power_plants_grid logged allied only).
# Dense already-logged: Salvador-Itaparica; Quinto Puente; State Grid UHV;
#   Sungrow Observatorio/Coya; Goldwind Pemuco; POWERCHINA Mauriti/Catac/Francisco Juana;
#   Nextracker Casa dos Ventos; Array Lupi; AES Andes III/Pampas; Zijin Longking Rosebel.
# Active after cycle 138: us271 / prc277 / allied244 / other38 (n=830).
shuffle_seed: 20261138
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- infrastructure/bridges_roads
- energy/power_plants_grid
- infrastructure/port_cranes
- resources/copper
- energy/wind
- infrastructure/port_ownership
- energy/fission_smr
- resources/lithium
- infrastructure/building_materials
- infrastructure/rail
- resources/niobium
- resources/nickel
- resources/graphite
- energy/solar
- infrastructure/engineering_epc
- resources/balsa
- energy/other_renewables
rows_found_this_cycle:
  resources/water: 0
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 1
  infrastructure/port_cranes: 0
  resources/copper: 0
  energy/wind: 1
  infrastructure/port_ownership: 0
  energy/fission_smr: 0
  resources/lithium: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  resources/niobium: 0
  resources/nickel: 0
  resources/graphite: 0
  energy/solar: 1
  infrastructure/engineering_epc: 0
  resources/balsa: 0
  energy/other_renewables: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 137 (seed 20261137) ===
# Shuffled order: solar, port_cranes, lithium, rail, wind, nickel, balsa,
#   power_plants_grid, graphite, building_materials, other_renewables, copper,
#   water, engineering_epc, niobium, fission_smr, port_ownership, bridges_roads.
# Logged 4 sourced rows (1 US / 3 PRC; thin dry; no padding):
#   prc solar: longi_sol_de_verano1_peru_53p2mw_2025 (Hi-MO 9 53.2 MW Majes; CapEx blank).
#   prc solar: longi_petalo_norte_colombia_19p9mw_2025 (Hi-MO 7 19.9 MW La Esperanza; CapEx blank).
#   us other_renewables: aes_dr_bess_138mw_94m_2025 (138.1 MW BESS NTP Dec 2025; USD 94m).
#   prc solar: ctg_arinos_solar_full_cod_2025 (Arinos MG full COD 2025; CapEx blank).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: port_cranes, lithium, rail, wind, nickel, balsa,
#   power_plants_grid, graphite, building_materials, copper, water,
#   engineering_epc, niobium, fission_smr, port_ownership, bridges_roads.
# Dense already-logged: ZPMC Santos/Itapoá/Aguadulce/ICAVE; PowerChina Conchagua;
#   Goldwind SPIC Touros; CHEC Kingston yard; BYD Grenergy; CRCC Batuco; Nextracker.
# Active after cycle 137: us270 / prc276 / allied243 / other38 (n=827).
shuffle_seed: 20261137
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/solar
- infrastructure/port_cranes
- resources/lithium
- infrastructure/rail
- energy/wind
- resources/nickel
- resources/balsa
- energy/power_plants_grid
- resources/graphite
- infrastructure/building_materials
- energy/other_renewables
- resources/copper
- resources/water
- infrastructure/engineering_epc
- resources/niobium
- energy/fission_smr
- infrastructure/port_ownership
- infrastructure/bridges_roads
rows_found_this_cycle:
  energy/solar: 3
  infrastructure/port_cranes: 0
  resources/lithium: 0
  infrastructure/rail: 0
  energy/wind: 0
  resources/nickel: 0
  resources/balsa: 0
  energy/power_plants_grid: 0
  resources/graphite: 0
  infrastructure/building_materials: 0
  energy/other_renewables: 1
  resources/copper: 0
  resources/water: 0
  infrastructure/engineering_epc: 0
  resources/niobium: 0
  energy/fission_smr: 0
  infrastructure/port_ownership: 0
  infrastructure/bridges_roads: 0
rows_by_side_this_cycle:
  us: 1
  prc: 3
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 136 (seed 20261136) ===
# Shuffled order: bridges_roads, other_renewables, engineering_epc, graphite,
#   copper, fission_smr, port_cranes, nickel, wind, water, building_materials,
#   port_ownership, solar, balsa, niobium, rail, lithium, power_plants_grid.
# Logged 5 sourced rows (2 US / 3 PRC; thin dry; no padding):
#   us port_ownership: nfe_tgs_lease_brazil_2026 (TGS lease Aug 2026; CapEx blank).
#   us power_plants_grid: nfe_ute_lins2_brazil_2031 (auction award; COD ~2031; CapEx blank).
#   prc solar: zijin_longking_rosebel_p2_suriname_150m_2026 (170 MWp+120 MW/120 MWh; USD 150m).
#   prc solar: zijin_longking_aurora_ug_guyana_55p24m_2026 (45 MWp+50 MW/100 MWh; USD 55.24m).
#   prc solar: zijin_longking_aurora_conc_p3_guyana_26p62m_2026 (15 MWp+20 MW/80 MWh; USD 26.62m).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: bridges_roads, other_renewables, engineering_epc, graphite,
#   copper, fission_smr, port_cranes, nickel, wind, water, building_materials,
#   balsa, niobium, rail, lithium.
# Active after cycle 136: us269 / prc273 / allied243 / other38 (n=823).
shuffle_seed: 20261136
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- energy/other_renewables
- infrastructure/engineering_epc
- resources/graphite
- resources/copper
- energy/fission_smr
- infrastructure/port_cranes
- resources/nickel
- energy/wind
- resources/water
- infrastructure/building_materials
- infrastructure/port_ownership
- energy/solar
- resources/balsa
- resources/niobium
- infrastructure/rail
- resources/lithium
- energy/power_plants_grid
rows_found_this_cycle:
  infrastructure/bridges_roads: 0
  energy/other_renewables: 0
  infrastructure/engineering_epc: 0
  resources/graphite: 0
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/port_cranes: 0
  resources/nickel: 0
  energy/wind: 0
  resources/water: 0
  infrastructure/building_materials: 0
  infrastructure/port_ownership: 1
  energy/solar: 3
  resources/balsa: 0
  resources/niobium: 0
  infrastructure/rail: 0
  resources/lithium: 0
  energy/power_plants_grid: 1
rows_by_side_this_cycle:
  us: 2
  prc: 3
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 135 (seed 20261135) ===
# Shuffled order: wind, copper, other_renewables, port_cranes, fission_smr,
#   engineering_epc, bridges_roads, lithium, port_ownership, nickel,
#   power_plants_grid, graphite, building_materials, rail, balsa, solar,
#   niobium, water.
# Logged 5 sourced rows (1 US / 2 PRC / 1 allied / 1 other; thin dry; no padding):
#   allied wind: solaer_calbuco_chile_65m_2026 (47 MW + 80 MWh; USD 65m financing).
#   us copper: fcx_cerro_verde_stake_107m_2026 (open-market buy to 55.66%; USD 107m).
#   prc other_renewables: jinko_ess_chile_340mw_1600mwh_2025 (METLEN 340 MW/1.6 GWh; CapEx blank).
#   prc other_renewables: xinyuan_spic_atacama_bess_chile_rmb381m_2024 (110 MW/220 MWh; RMB 381.8m).
#   other other_renewables: promigas_zelestra_latam_1p1bn_2026 (~3,500 MW; EV USD 1.1bn).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: port_cranes, fission_smr, engineering_epc, bridges_roads,
#   lithium, port_ownership, nickel, power_plants_grid, graphite,
#   building_materials, rail, balsa, solar, niobium, water.
# Skipped Exxon Hammerhead FID (oil-production CapEx outside 18 subcats).
# Active after cycle 135: us267 / prc270 / allied243 / other38 (n=818).
shuffle_seed: 20261135
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/wind
- resources/copper
- energy/other_renewables
- infrastructure/port_cranes
- energy/fission_smr
- infrastructure/engineering_epc
- infrastructure/bridges_roads
- resources/lithium
- infrastructure/port_ownership
- resources/nickel
- energy/power_plants_grid
- resources/graphite
- infrastructure/building_materials
- infrastructure/rail
- resources/balsa
- energy/solar
- resources/niobium
- resources/water
rows_found_this_cycle:
  energy/wind: 1
  resources/copper: 1
  energy/other_renewables: 3
  infrastructure/port_cranes: 0
  energy/fission_smr: 0
  infrastructure/engineering_epc: 0
  infrastructure/bridges_roads: 0
  resources/lithium: 0
  infrastructure/port_ownership: 0
  resources/nickel: 0
  energy/power_plants_grid: 0
  resources/graphite: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  resources/balsa: 0
  energy/solar: 0
  resources/niobium: 0
  resources/water: 0
rows_by_side_this_cycle:
  us: 1
  prc: 2
  allied: 1
  other: 1
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 134 (seed 20261134) ===
# Shuffled order: port_cranes, engineering_epc, wind, building_materials, nickel,
#   port_ownership, other_renewables, balsa, lithium, water, bridges_roads, rail,
#   fission_smr, solar, graphite, niobium, copper, power_plants_grid.
# Logged 8 sourced rows (1 US / 7 PRC; thin dry; no padding):
#   prc wind: goldwind_herradura1_cuba_51mw_2026 (34×1.5 MW design; CapEx blank).
#   prc port_ownership: cofco_sts11_santos_port_2023 (3→14 Mt; CapEx blank).
#   prc other_renewables: cwe_rucalhue_hydro_chile_90mw_2025 (90 MW; CapEx blank).
#   prc lithium: tsingshan_perico_jujuy_120m_2026 (USD 120m HCl/NaOH plant).
#   prc copper: zijin_rio_blanco_peru_2792m (MINEM CapEx USD 2.792bn).
#   prc copper: tongling_mirador_phase2_ecuador_2026 (built May 2025; COD delayed).
#   prc copper: minmetals_el_galeno_peru_3500m (MINEM CapEx USD 3.5bn).
#   us power_plants_grid: nfe_puerto_sandino_lng_power_2026 (H1 2027 COD; CapEx blank).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: port_cranes, engineering_epc, building_materials, nickel,
#   balsa, water, bridges_roads, rail, fission_smr, solar, graphite, niobium.
# Active after cycle 134: us266 / prc268 / allied242 / other37 (n=813).
# Holdover cleared: sandino (NFE Puerto Sandino 10-Q primary).
shuffle_seed: 20261134
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_cranes
- infrastructure/engineering_epc
- energy/wind
- infrastructure/building_materials
- resources/nickel
- infrastructure/port_ownership
- energy/other_renewables
- resources/balsa
- resources/lithium
- resources/water
- infrastructure/bridges_roads
- infrastructure/rail
- energy/fission_smr
- energy/solar
- resources/graphite
- resources/niobium
- resources/copper
- energy/power_plants_grid
rows_found_this_cycle:
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 0
  energy/wind: 1
  infrastructure/building_materials: 0
  resources/nickel: 0
  infrastructure/port_ownership: 1
  energy/other_renewables: 1
  resources/balsa: 0
  resources/lithium: 1
  resources/water: 0
  infrastructure/bridges_roads: 0
  infrastructure/rail: 0
  energy/fission_smr: 0
  energy/solar: 0
  resources/graphite: 0
  resources/niobium: 0
  resources/copper: 3
  energy/power_plants_grid: 1
rows_by_side_this_cycle:
  us: 1
  prc: 7
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 133 (seed 20261133) ===
# Shuffled order: copper, niobium, engineering_epc, port_cranes, wind,
#   bridges_roads, fission_smr, building_materials, other_renewables, water,
#   balsa, lithium, power_plants_grid, solar, port_ownership, graphite, rail,
#   nickel.
# Logged 6 sourced rows (1 US / 3 PRC / 2 allied; thin dry; no padding):
#   allied copper: metso_tia_maria_sxew_eur100m_2026 (EUR 100m / USD 114.84m ECB).
#   allied niobium: st_george_cit_senai_pilot_2026 (CIT-SENAI 9t pilot; CapEx blank).
#   prc bridges_roads: crec_saramiriza_road_peru_2025 (16.22 km; CapEx blank).
#   prc bridges_roads: ccecc_huancavelica_road_207km_2026 (207.8 km handover; CapEx blank).
#   us power_plants_grid: nfe_celba2_first_fire_624mw_2025 (624 MW first fire; CapEx blank).
#   prc rail: chec_bogota_metro_l1_5p016bn (USD 5.016bn franchise; first-train 2025).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: engineering_epc, port_cranes, wind, fission_smr,
#   building_materials, other_renewables, water, balsa, lithium, solar,
#   port_ownership, graphite, nickel.
# Active after cycle 133: us265 / prc261 / allied242 / other37 (n=805).
# Holdover cleared: nfe_celba2 first-fire primary opened this cycle.
shuffle_seed: 20261133
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/copper
- resources/niobium
- infrastructure/engineering_epc
- infrastructure/port_cranes
- energy/wind
- infrastructure/bridges_roads
- energy/fission_smr
- infrastructure/building_materials
- energy/other_renewables
- resources/water
- resources/balsa
- resources/lithium
- energy/power_plants_grid
- energy/solar
- infrastructure/port_ownership
- resources/graphite
- infrastructure/rail
- resources/nickel
rows_found_this_cycle:
  resources/copper: 1
  resources/niobium: 1
  infrastructure/engineering_epc: 0
  infrastructure/port_cranes: 0
  energy/wind: 0
  infrastructure/bridges_roads: 2
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  energy/other_renewables: 0
  resources/water: 0
  resources/balsa: 0
  resources/lithium: 0
  energy/power_plants_grid: 1
  energy/solar: 0
  infrastructure/port_ownership: 0
  resources/graphite: 0
  infrastructure/rail: 1
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 1
  prc: 3
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 132 (seed 20261132) ===
# Shuffled order: bridges_roads, wind, building_materials, fission_smr, nickel,
#   rail, other_renewables, copper, solar, water, port_ownership,
#   power_plants_grid, lithium, balsa, engineering_epc, niobium, port_cranes,
#   graphite.
# Logged 8 sourced rows (1 US / 7 PRC; thin dry; no padding):
#   prc bridges_roads: ccecc_cajamarca_highway_246km_2026 (CapEx blank).
#   prc bridges_roads: crcc_demerara_bridge_open_2025 (opening; CapEx blank).
#   prc wind: goldwind_rio_cullen_argentina_2026 (2×4.2 MW + BESS).
#   prc wind: goldwind_kallpa_chile_342mw_2026 (57×6.0 MW).
#   prc lithium: cbc_ylb_uyuni_dle_1p03bn_2024 (USD 1.03bn; Assembly pending proxy).
#   prc lithium: cmec_uyuni_lithium_plant_bolivia_2023 (15ktpa completion).
#   prc lithium: zijin_tres_quebradas_phase1_cod_2025 (20ktpa COD).
#   us water: fcx_el_abra_desal_aqueduct_2026 (desal component; CapEx blank).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, fission_smr, nickel, rail,
#   other_renewables, copper, solar, port_ownership, power_plants_grid, balsa,
#   engineering_epc, niobium, port_cranes, graphite.
# Active after cycle 132: us264 / prc258 / allied240 / other37 (n=799).
shuffle_seed: 20261132
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- energy/wind
- infrastructure/building_materials
- energy/fission_smr
- resources/nickel
- infrastructure/rail
- energy/other_renewables
- resources/copper
- energy/solar
- resources/water
- infrastructure/port_ownership
- energy/power_plants_grid
- resources/lithium
- resources/balsa
- infrastructure/engineering_epc
- resources/niobium
- infrastructure/port_cranes
- resources/graphite
rows_found_this_cycle:
  infrastructure/bridges_roads: 2
  energy/wind: 2
  infrastructure/building_materials: 0
  energy/fission_smr: 0
  resources/nickel: 0
  infrastructure/rail: 0
  energy/other_renewables: 0
  resources/copper: 0
  energy/solar: 0
  resources/water: 1
  infrastructure/port_ownership: 0
  energy/power_plants_grid: 0
  resources/lithium: 3
  resources/balsa: 0
  infrastructure/engineering_epc: 0
  resources/niobium: 0
  infrastructure/port_cranes: 0
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 1
  prc: 7
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 131 (seed 20261131) ===
# Shuffled order: engineering_epc, building_materials, port_cranes, balsa,
#   port_ownership, nickel, power_plants_grid, graphite, lithium, water, solar,
#   bridges_roads, rail, other_renewables, copper, niobium, wind, fission_smr.
# Logged 7 sourced rows (2 US / 4 PRC / 1 allied; thin dry; no padding):
#   prc port_ownership: cmport_vast_acu_70pct_spa_2025 (USD 448m SPA).
#   prc power_plants_grid: powerchina_chile_decree4_g15_g04_2025 (CapEx blank).
#   prc solar: powerchina_dune_plus_epc_chile_2025 (186 MWp + storage EPC).
#   prc lithium: ganfeng_lar_180m_convertible_ppg_2026 (USD 180m note).
#   us power_plants_grid: nfe_portocem_1p6gw_epc_2024 (1.6 GW Barcarena).
#   us power_plants_grid: seaboard_estrella_del_mar_iv_2025 (145 MW barge).
#   allied copper: fortescue_canariaco_alta_copper_2026 (CAD 139m equity).
# Also archived residual gold-primary cmoc_cangrejos_ecuador_1p7bn_2026
#   (out_of_scope — gold_silver).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: engineering_epc, building_materials, port_cranes, balsa,
#   nickel, graphite, water, bridges_roads, rail, other_renewables, niobium,
#   wind, fission_smr.
# Active after cycle 131: us263 / prc251 / allied240 / other37 (n=791).
shuffle_seed: 20261131
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- infrastructure/building_materials
- infrastructure/port_cranes
- resources/balsa
- infrastructure/port_ownership
- resources/nickel
- energy/power_plants_grid
- resources/graphite
- resources/lithium
- resources/water
- energy/solar
- infrastructure/bridges_roads
- infrastructure/rail
- energy/other_renewables
- resources/copper
- resources/niobium
- energy/wind
- energy/fission_smr
rows_found_this_cycle:
  infrastructure/engineering_epc: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  resources/balsa: 0
  infrastructure/port_ownership: 1
  resources/nickel: 0
  energy/power_plants_grid: 3
  resources/graphite: 0
  resources/lithium: 1
  resources/water: 0
  energy/solar: 1
  infrastructure/bridges_roads: 0
  infrastructure/rail: 0
  energy/other_renewables: 0
  resources/copper: 1
  resources/niobium: 0
  energy/wind: 0
  energy/fission_smr: 0
rows_by_side_this_cycle:
  us: 2
  prc: 4
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === PRE-STEP (before cycle 131): scope + side audit (2026-10-02) ===
# Trigger: U.S. active jumped 220→358 while PRC 226→248 in ~3h; many new rows
# were Puerto Rico / USVI domestic awards (not U.S.–PRC LatAm competition).
#
# 1) us_territory_out_of_scope — archived every active row sited in Puerto Rico
#    or USVI (plus CTDC Hostos DR–PR HVDC with Mayagüez landing / PR investor).
#    BRIEF.md + codebook.yml + build_site_data fallback: "Excludes U.S.
#    territories: Puerto Rico, USVI"; Puerto Rico removed from
#    latin_america_caribbean allow-list.
# scope_audit_archived_total: 105
# scope_audit_by_reason:
#   us_territory_out_of_scope: 105
# scope_audit_by_side:
#   us: 96
#   allied: 9
#   prc: 0
#   other: 0
# scope_audit_by_subcategory:
#   infrastructure/bridges_roads: 37
#   infrastructure/engineering_epc: 27
#   resources/water: 15
#   energy/power_plants_grid: 14
#   energy/other_renewables: 9
#   energy/solar: 2
#   infrastructure/building_materials: 1
# scope_audit_examples:
#   us: ge_vernova_prepa_lm2500xpress_pr_2025; tesla_genera_pr_bess_430mw_2025;
#       convergent_doe_lpo_584m_pr_2025; jose_carro_morovis_cemetery_2018;
#       aes_marahu_doe_lpo_861m_2024; quanta_luma_dist_525m_2025;
#       fhwa_* PR Bridge; USACE/USCG/FHWA PR residual; ctdc_hostos_hvdc_dr_pr_2026
#   allied: atkinsrealis_fhwa_pr_inspect_*; wsp_maria_*; wsp_aci_tep_pr_2022;
#       schneider_espc_pr_cool_roofs_2010; ferrovial_usace_drilled_shaft_6c_2024
#        (retagged us→allied then archived)
#
# 2) Side tags by HQ only — checked every us-tagged row from cycles 88–130.
#    Known non-U.S. examples (Alstom, Liebherr, Konecranes, Vergnet, Windey,
#    Siemens, ABB, Enel, Iberdrola, ENGIE, Shell, ACCIONA) already allied/prc.
# side_retag_total: 1
# side_retag_by_from_to:
#   us->allied: 1
# side_retag_by_subcategory:
#   resources/water: 1
# side_retag_examples:
#   ferrovial_usace_drilled_shaft_6c_2024 (Ferrovial Spain HQ)
#
# 3) Out of scope (outside 18 subcats: hospital/school/autos/digital/fertilizer/
#    gold-silver) — no new active residuals at pre-step; cycle 131 also archived
#    cmoc_cangrejos_ecuador_1p7bn_2026 (gold-primary).
# scope_oos_archived_total: 0 (pre-step) + 1 (cycle 131 cangrejos)
#
# Post-audit active sides before hunt: us261 / prc248 / allied239 / other37
#   (n=785). Thinnest: balsa/graphite (23), nickel/fission_smr (24), niobium (26).

# === Cycle 130 (seed 20261130) ===
# Shuffled order: copper, nickel, bridges_roads, niobium, lithium, balsa,
#   fission_smr, port_ownership, water, rail, wind, power_plants_grid,
#   other_renewables, engineering_epc, solar, graphite, port_cranes,
#   building_materials.
# Logged 6 sourced rows (3 US / 1 PRC / 2 allied; thin dry; no padding):
#   prc water: cmec_lima_three_districts_water_2025 (Sinomach handover).
#   allied rail: alstom_panama_metro_maint_90m_2026 (USD 90m).
#   us other_renewables: tesla_genera_pr_bess_430mw_2025 (USD 767m).
#   us solar: convergent_doe_lpo_584m_pr_2025 (USD 584.5m).
#   allied port_cranes: liebherr_antigua_lhm420_2025 (USD 6.2m proxy).
#   us engineering_epc: jose_carro_morovis_cemetery_2018 (USD 68.6m VA).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: copper, nickel, bridges_roads, niobium, lithium, balsa,
#   fission_smr, port_ownership, wind, power_plants_grid, graphite,
#   building_materials.
# Active after cycle 130: us358 / prc248 / allied247 / other37 (n=890).
# NOTE: post PRE-STEP audit above, PR/USVI rows archived → us261/prc248/allied239.
shuffle_seed: 20261130
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/copper
- resources/nickel
- infrastructure/bridges_roads
- resources/niobium
- resources/lithium
- resources/balsa
- energy/fission_smr
- infrastructure/port_ownership
- resources/water
- infrastructure/rail
- energy/wind
- energy/power_plants_grid
- energy/other_renewables
- infrastructure/engineering_epc
- energy/solar
- resources/graphite
- infrastructure/port_cranes
- infrastructure/building_materials

# === Cycle 129 (seed 20261129) ===
# Shuffled order: wind, graphite, engineering_epc, balsa, port_cranes, copper,
#   lithium, water, bridges_roads, solar, building_materials, niobium,
#   other_renewables, power_plants_grid, rail, nickel, fission_smr, port_ownership.
# Logged 6 sourced rows (2 US / 2 PRC / 2 allied; thin dry; no padding) from
#   Hunt C96/C97 verified unlogged leads:
#   prc wind: windey_warnes_ii_bolivia_45mw_2025 (ENDE WD156-4500).
#   allied wind: vergnet_claybury_barbados_2025 (EUR 1.6m).
#   allied port_cranes: konecranes_arawak_nassau_esp6_2024.
#   prc water: crseg_barbados_south_coast_water_2026 (BWA Component 1).
#   us other_renewables: pattern_amanecer_doe_edf_489m_pr_2026 (USD 489m).
#   us solar: aes_marahu_doe_lpo_861m_2024 (USD 861.3m).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: graphite, engineering_epc, balsa, copper, lithium,
#   bridges_roads, building_materials, niobium, power_plants_grid, rail, nickel,
#   fission_smr, port_ownership.
# Active after cycle 129: us355 / prc247 / allied245 / other37 (n=884).
shuffle_seed: 20261129
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/wind
- resources/graphite
- infrastructure/engineering_epc
- resources/balsa
- infrastructure/port_cranes
- resources/copper
- resources/lithium
- resources/water
- infrastructure/bridges_roads
- energy/solar
- infrastructure/building_materials
- resources/niobium
- energy/other_renewables
- energy/power_plants_grid
- infrastructure/rail
- resources/nickel
- energy/fission_smr
- infrastructure/port_ownership

# === Cycle 128 (seed 20261128) ===
# Shuffled order: balsa, port_cranes, building_materials, lithium, nickel, rail,
#   fission_smr, wind, other_renewables, copper, engineering_epc, water, niobium,
#   graphite, port_ownership, power_plants_grid, bridges_roads, solar.
# Logged 5 sourced rows (5 US; PRC OEM/regulator pass dry this cycle; thin dry;
#   no padding):
#   us engineering_epc: knik_gtmo_runway_2007 (USD 25.6m NAVFAC).
#   us engineering_epc: rb_degetau_hurricane_recovery_2019 (USD 25.1m GSA).
#   us engineering_epc: consigli_ceiba_afrc_2009 (USD 24.1m USACE).
#   us engineering_epc: cscg_mayaguez_cbp_2022 (USD 23.6m GSA/CBP).
#   us engineering_epc: fr_buchanan_astb_2025 (USD 22.3m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: balsa, port_cranes, building_materials, lithium, nickel,
#   rail, fission_smr, wind, other_renewables, copper, water, niobium, graphite,
#   port_ownership, power_plants_grid, bridges_roads, solar.
# Active after cycle 128: us353 / prc245 / allied243 / other37 (n=878).
shuffle_seed: 20261128
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/balsa
- infrastructure/port_cranes
- infrastructure/building_materials
- resources/lithium
- resources/nickel
- infrastructure/rail
- energy/fission_smr
- energy/wind
- energy/other_renewables
- resources/copper
- infrastructure/engineering_epc
- resources/water
- resources/niobium
- resources/graphite
- infrastructure/port_ownership
- energy/power_plants_grid
- infrastructure/bridges_roads
- energy/solar
rows_found_this_cycle:
  resources/balsa: 0
  infrastructure/port_cranes: 0
  infrastructure/building_materials: 0
  resources/lithium: 0
  resources/nickel: 0
  infrastructure/rail: 0
  energy/fission_smr: 0
  energy/wind: 0
  energy/other_renewables: 0
  resources/copper: 0
  infrastructure/engineering_epc: 5
  resources/water: 0
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/port_ownership: 0
  energy/power_plants_grid: 0
  infrastructure/bridges_roads: 0
  energy/solar: 0
rows_by_side_this_cycle:
  us: 5
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 127 (seed 20261127) ===
# Shuffled order: engineering_epc, balsa, lithium, wind, solar, other_renewables,
#   port_ownership, graphite, bridges_roads, niobium, building_materials, water,
#   rail, fission_smr, power_plants_grid, nickel, copper, port_cranes.
# Logged 5 sourced rows (4 US + 1 PRC; thin dry; no padding):
#   prc bridges_roads: crbc_saramacca_bridge_suriname_2025 (66 m CRBC; CapEx blank).
#   us power_plants_grid: nreca_caracol_power_2013 (USD 36.2m USAID).
#   us engineering_epc: conti_buchanan_range_ops_2024 (USD 32.5m USACE).
#   us engineering_epc: orion_autec_pier_2021 (USD 28.7m NAVFAC).
#   us engineering_epc: rq_gtmo_mass_migration_2018 (USD 24.6m NAVFAC).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: balsa, lithium, wind, solar, other_renewables,
#   port_ownership, graphite, niobium, building_materials, water, rail,
#   fission_smr, nickel, copper, port_cranes.
# Active after cycle 127: us348 / prc245 / allied243 / other37 (n=873).
shuffle_seed: 20261127
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- resources/balsa
- resources/lithium
- energy/wind
- energy/solar
- energy/other_renewables
- infrastructure/port_ownership
- resources/graphite
- infrastructure/bridges_roads
- resources/niobium
- infrastructure/building_materials
- resources/water
- infrastructure/rail
- energy/fission_smr
- energy/power_plants_grid
- resources/nickel
- resources/copper
- infrastructure/port_cranes
rows_found_this_cycle:
  infrastructure/engineering_epc: 3
  resources/balsa: 0
  resources/lithium: 0
  energy/wind: 0
  energy/solar: 0
  energy/other_renewables: 0
  infrastructure/port_ownership: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 1
  resources/niobium: 0
  infrastructure/building_materials: 0
  resources/water: 0
  infrastructure/rail: 0
  energy/fission_smr: 0
  energy/power_plants_grid: 1
  resources/nickel: 0
  resources/copper: 0
  infrastructure/port_cranes: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 126 (seed 20261126) ===
# Shuffled order: port_ownership, niobium, fission_smr, copper, lithium, rail,
#   power_plants_grid, water, balsa, bridges_roads, engineering_epc,
#   building_materials, other_renewables, graphite, nickel, port_cranes, solar, wind.
# Logged 5 sourced rows (3 US + 2 PRC; thin dry; no padding):
#   prc water: powerchina_barbados_water_infra_2025 (Haymans handover; CapEx blank).
#   prc solar: powerchina_tepuy_pv_108mw_2024 (108 MW EPM; CapEx blank).
#   us engineering_epc: aecom_gtmo_fuel_pier_2013 (USD 33.3m NAVFAC).
#   us water: v2x_gtmo_potable_water_2025 (USD 19.7m NAVFAC).
#   us engineering_epc: islands_mechanical_migrant_ops_2007 (USD 16.6m NAVFAC).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: port_ownership, niobium, fission_smr, copper, lithium,
#   rail, power_plants_grid, balsa, bridges_roads, building_materials,
#   other_renewables, graphite, nickel, port_cranes, wind.
# Active after cycle 126: us344 / prc244 / allied243 / other37 (n=868).
shuffle_seed: 20261126
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_ownership
- resources/niobium
- energy/fission_smr
- resources/copper
- resources/lithium
- infrastructure/rail
- energy/power_plants_grid
- resources/water
- resources/balsa
- infrastructure/bridges_roads
- infrastructure/engineering_epc
- infrastructure/building_materials
- energy/other_renewables
- resources/graphite
- resources/nickel
- infrastructure/port_cranes
- energy/solar
- energy/wind
rows_found_this_cycle:
  infrastructure/port_ownership: 0
  resources/niobium: 0
  energy/fission_smr: 0
  resources/copper: 0
  resources/lithium: 0
  infrastructure/rail: 0
  energy/power_plants_grid: 0
  resources/water: 2
  resources/balsa: 0
  infrastructure/bridges_roads: 0
  infrastructure/engineering_epc: 2
  infrastructure/building_materials: 0
  energy/other_renewables: 0
  resources/graphite: 0
  resources/nickel: 0
  infrastructure/port_cranes: 0
  energy/solar: 1
  energy/wind: 0
rows_by_side_this_cycle:
  us: 3
  prc: 2
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 125 (seed 20261125) ===
# Shuffled order: engineering_epc, balsa, power_plants_grid, water, fission_smr,
#   building_materials, nickel, port_cranes, lithium, rail, niobium, wind,
#   other_renewables, bridges_roads, copper, solar, graphite, port_ownership.
# Logged 5 sourced rows (4 US + 1 PRC; thin dry; no padding):
#   us engineering_epc: rq_gtmo_solid_waste_2019 (USD 60.0m NAVFAC).
#   us engineering_epc: rq_gtmo_wharf_bravo_2016 (USD 38.9m NAVFAC).
#   us engineering_epc: eterna_soto_cano_hangar_2021 (USD 39.2m USACE).
#   us engineering_epc: eterna_soto_cano_aviation_storage_2025 (USD 37.7m USACE).
#   prc solar: powerchina_ecopetrol_cartagena_23mw_2024 (23 MW; CapEx blank).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: balsa, power_plants_grid, water, fission_smr,
#   building_materials, nickel, port_cranes, lithium, rail, niobium, wind,
#   other_renewables, bridges_roads, copper, graphite, port_ownership.
# Active after cycle 125: us341 / prc242 / allied243 / other37 (n=863).
shuffle_seed: 20261125
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- resources/balsa
- energy/power_plants_grid
- resources/water
- energy/fission_smr
- infrastructure/building_materials
- resources/nickel
- infrastructure/port_cranes
- resources/lithium
- infrastructure/rail
- resources/niobium
- energy/wind
- energy/other_renewables
- infrastructure/bridges_roads
- resources/copper
- energy/solar
- resources/graphite
- infrastructure/port_ownership
rows_found_this_cycle:
  infrastructure/engineering_epc: 4
  resources/balsa: 0
  energy/power_plants_grid: 0
  resources/water: 0
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  resources/nickel: 0
  infrastructure/port_cranes: 0
  resources/lithium: 0
  infrastructure/rail: 0
  resources/niobium: 0
  energy/wind: 0
  energy/other_renewables: 0
  infrastructure/bridges_roads: 0
  resources/copper: 0
  energy/solar: 1
  resources/graphite: 0
  infrastructure/port_ownership: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 124 (seed 20261124) ===
# Shuffled order: building_materials, copper, power_plants_grid, wind,
#   other_renewables, bridges_roads, niobium, fission_smr, solar, lithium,
#   nickel, rail, balsa, water, graphite, port_cranes, port_ownership,
#   engineering_epc.
# Logged 5 sourced rows (4 US + 1 PRC; thin dry; no padding):
#   prc solar: powerchina_sajalices_panama_530mw_2024 (530 MW EPC; CapEx blank).
#   us engineering_epc: cmf_great_inagua_opbat_2011 (USD 17.2m USCG).
#   us engineering_epc: cce_soto_cano_barracks_2011 (USD 15.6m USACE).
#   us power_plants_grid: perini_haiti_substations_2011 (USD 14.9m USAID).
#   us engineering_epc: cavagnero_pos_nec_bridging_2020 (USD 14.5m State).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, copper, wind, other_renewables,
#   bridges_roads, niobium, fission_smr, lithium, nickel, rail, balsa, water,
#   graphite, port_cranes, port_ownership.
# Active after cycle 124: us337 / prc241 / allied243 / other37 (n=858).
shuffle_seed: 20261124
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- resources/copper
- energy/power_plants_grid
- energy/wind
- energy/other_renewables
- infrastructure/bridges_roads
- resources/niobium
- energy/fission_smr
- energy/solar
- resources/lithium
- resources/nickel
- infrastructure/rail
- resources/balsa
- resources/water
- resources/graphite
- infrastructure/port_cranes
- infrastructure/port_ownership
- infrastructure/engineering_epc
rows_found_this_cycle:
  infrastructure/building_materials: 0
  resources/copper: 0
  energy/power_plants_grid: 1
  energy/wind: 0
  energy/other_renewables: 0
  infrastructure/bridges_roads: 0
  resources/niobium: 0
  energy/fission_smr: 0
  energy/solar: 1
  resources/lithium: 0
  resources/nickel: 0
  infrastructure/rail: 0
  resources/balsa: 0
  resources/water: 0
  resources/graphite: 0
  infrastructure/port_cranes: 0
  infrastructure/port_ownership: 0
  infrastructure/engineering_epc: 3
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 123 (seed 20261123) ===
# Shuffled order: building_materials, water, balsa, bridges_roads, nickel,
#   lithium, other_renewables, port_ownership, rail, graphite, niobium, solar,
#   port_cranes, copper, fission_smr, power_plants_grid, engineering_epc, wind.
# Logged 5 sourced rows (4 US + 1 PRC; thin dry; no padding):
#   us engineering_epc: futron_san_salvador_csu_2022 (USD 28.9m State).
#   us engineering_epc: cce_bogota_annex_2005 (USD 23.1m State).
#   us engineering_epc: src_tegucigalpa_nec_pe_2019 (USD 16.9m State).
#   us engineering_epc: ics_borinquen_hangar_2019 (USD 3.2m USCG).
#   prc solar: powerchina_cauchari_solar_epc_2020 (315 MW CHEXIM/PowerChina; CapEx blank).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, water, balsa, bridges_roads, nickel,
#   lithium, other_renewables, port_ownership, rail, graphite, niobium,
#   port_cranes, copper, fission_smr, power_plants_grid, wind.
# Active after cycle 123: us333 / prc240 / allied243 / other37 (n=853).
shuffle_seed: 20261123
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- resources/water
- resources/balsa
- infrastructure/bridges_roads
- resources/nickel
- resources/lithium
- energy/other_renewables
- infrastructure/port_ownership
- infrastructure/rail
- resources/graphite
- resources/niobium
- energy/solar
- infrastructure/port_cranes
- resources/copper
- energy/fission_smr
- energy/power_plants_grid
- infrastructure/engineering_epc
- energy/wind
rows_found_this_cycle:
  infrastructure/building_materials: 0
  resources/water: 0
  resources/balsa: 0
  infrastructure/bridges_roads: 0
  resources/nickel: 0
  resources/lithium: 0
  energy/other_renewables: 0
  infrastructure/port_ownership: 0
  infrastructure/rail: 0
  resources/graphite: 0
  resources/niobium: 0
  energy/solar: 1
  infrastructure/port_cranes: 0
  resources/copper: 0
  energy/fission_smr: 0
  energy/power_plants_grid: 0
  infrastructure/engineering_epc: 4
  energy/wind: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 122 (seed 20261122) ===
# Shuffled order: copper, building_materials, other_renewables, port_cranes,
#   engineering_epc, fission_smr, bridges_roads, rail, balsa, niobium, solar,
#   wind, port_ownership, nickel, graphite, water, lithium, power_plants_grid.
# Logged 8 sourced rows (honest US residual; thin dry; PRC OEM pass
#   product/summit-only; no padding):
#   us water: dick_usace_dams_pr_2002 (USD 78.5m USACE dams PSC).
#   us engineering_epc: zachry_ecuador_construction_2005 (USD 73.5m State).
#   us engineering_epc: caddell_mexico_nec_2005 (USD 71.0m State).
#   us engineering_epc: fluor_jamaica_construction_2003 (USD 50.7m State).
#   us engineering_epc: vistas_porto_alegre_consulate_2015 (USD 44.8m State).
#   us engineering_epc: rb_buchanan_readiness_2012 (USD 38.4m USACE).
#   us engineering_epc: qb_munoz_ang_comms_2021 (USD 37.7m NAVFAC).
#   us engineering_epc: teksol_pier_echo_2025 (USD 3.7m USCG pier M&R).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: copper, building_materials, other_renewables, port_cranes,
#   fission_smr, bridges_roads, rail, balsa, niobium, solar, wind,
#   port_ownership, nickel, graphite, lithium, power_plants_grid.
# Active after cycle 122: us329 / prc239 / allied243 / other37 (n=848).
shuffle_seed: 20261122
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/copper
- infrastructure/building_materials
- energy/other_renewables
- infrastructure/port_cranes
- infrastructure/engineering_epc
- energy/fission_smr
- infrastructure/bridges_roads
- infrastructure/rail
- resources/balsa
- resources/niobium
- energy/solar
- energy/wind
- infrastructure/port_ownership
- resources/nickel
- resources/graphite
- resources/water
- resources/lithium
- energy/power_plants_grid
rows_found_this_cycle:
  resources/copper: 0
  infrastructure/building_materials: 0
  energy/other_renewables: 0
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 7
  energy/fission_smr: 0
  infrastructure/bridges_roads: 0
  infrastructure/rail: 0
  resources/balsa: 0
  resources/niobium: 0
  energy/solar: 0
  energy/wind: 0
  infrastructure/port_ownership: 0
  resources/nickel: 0
  resources/graphite: 0
  resources/water: 1
  resources/lithium: 0
  energy/power_plants_grid: 0
rows_by_side_this_cycle:
  us: 8
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 121 (seed 20261121) ===
# Shuffled order: building_materials, bridges_roads, wind, niobium, graphite,
#   lithium, fission_smr, rail, port_ownership, balsa, solar, port_cranes,
#   nickel, water, other_renewables, copper, engineering_epc, power_plants_grid.
# Logged 6 sourced rows (honest US residual; thin dry; PRC OEM pass
#   product/summit-only; no padding):
#   us bridges_roads: jose_carro_arecibo_branch2_2017 (USD 5.9m FHWA).
#   us bridges_roads: del_valle_mercedita_branch4_2017 (USD 5.1m FHWA).
#   us bridges_roads: desarrolladora_ja_ciales_branch4_2017 (USD 4.3m FHWA).
#   us engineering_epc: ch2m_uscg_frc_san_juan_2012 (USD 18.7m USCG).
#   us engineering_epc: tutor_perini_uscg_frc_p2_2013 (USD 7.5m USCG).
#   us engineering_epc: contractor_jv_prarng_jtc_2022 (USD 294.1m USACE MILCON).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, wind, niobium, graphite, lithium,
#   fission_smr, rail, port_ownership, balsa, solar, port_cranes, nickel, water,
#   other_renewables, copper, power_plants_grid.
# Active after cycle 121: us321 / prc239 / allied243 / other37 (n=840).
shuffle_seed: 20261121
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- infrastructure/bridges_roads
- energy/wind
- resources/niobium
- resources/graphite
- resources/lithium
- energy/fission_smr
- infrastructure/rail
- infrastructure/port_ownership
- resources/balsa
- energy/solar
- infrastructure/port_cranes
- resources/nickel
- resources/water
- energy/other_renewables
- resources/copper
- infrastructure/engineering_epc
- energy/power_plants_grid
rows_found_this_cycle:
  infrastructure/building_materials: 0
  infrastructure/bridges_roads: 3
  energy/wind: 0
  resources/niobium: 0
  resources/graphite: 0
  resources/lithium: 0
  energy/fission_smr: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  resources/balsa: 0
  energy/solar: 0
  infrastructure/port_cranes: 0
  resources/nickel: 0
  resources/water: 0
  energy/other_renewables: 0
  resources/copper: 0
  infrastructure/engineering_epc: 3
  energy/power_plants_grid: 0
rows_by_side_this_cycle:
  us: 6
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 120 (seed 20261120) ===
# Shuffled order: port_ownership, other_renewables, wind, engineering_epc,
#   graphite, lithium, copper, nickel, port_cranes, niobium, rail, fission_smr,
#   bridges_roads, balsa, building_materials, water, power_plants_grid, solar.
# Logged 5 sourced rows (honest US FHWA residual; thin dry; PRC OEM pass
#   product/summit-only; no padding):
#   us bridges_roads: design_build_ciales_branch2_2017 (USD 6.8m FHWA).
#   us bridges_roads: melendez_coamo_branch4_2017 (USD 4.5m FHWA).
#   us bridges_roads: lpcd_caguas_branch3_2017 (USD 4.3m FHWA).
#   us bridges_roads: santiago_utuado_branch2_2017 (USD 3.7m FHWA).
#   us bridges_roads: lagan_vieques_roads_2007 (USD 5.7m FHWA).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: port_ownership, other_renewables, wind, engineering_epc,
#   graphite, lithium, copper, nickel, port_cranes, niobium, rail, fission_smr,
#   balsa, building_materials, water, power_plants_grid, solar.
# Active after cycle 120: us315 / prc239 / allied243 / other37 (n=834).
shuffle_seed: 20261120
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_ownership
- energy/other_renewables
- energy/wind
- infrastructure/engineering_epc
- resources/graphite
- resources/lithium
- resources/copper
- resources/nickel
- infrastructure/port_cranes
- resources/niobium
- infrastructure/rail
- energy/fission_smr
- infrastructure/bridges_roads
- resources/balsa
- infrastructure/building_materials
- resources/water
- energy/power_plants_grid
- energy/solar
rows_found_this_cycle:
  infrastructure/port_ownership: 0
  energy/other_renewables: 0
  energy/wind: 0
  infrastructure/engineering_epc: 0
  resources/graphite: 0
  resources/lithium: 0
  resources/copper: 0
  resources/nickel: 0
  infrastructure/port_cranes: 0
  resources/niobium: 0
  infrastructure/rail: 0
  energy/fission_smr: 0
  infrastructure/bridges_roads: 5
  resources/balsa: 0
  infrastructure/building_materials: 0
  resources/water: 0
  energy/power_plants_grid: 0
  energy/solar: 0
rows_by_side_this_cycle:
  us: 5
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 119 (seed 20261119) ===
# Shuffled order: bridges_roads, other_renewables, balsa, rail, port_cranes,
#   copper, graphite, water, solar, engineering_epc, lithium, nickel,
#   building_materials, port_ownership, fission_smr, niobium,
#   power_plants_grid, wind.
# Logged 5 sourced rows (honest US FHWA residual; thin dry; ANEEL State Grid
#   lote already logged/excluded; no padding):
#   us bridges_roads: desarrolladora_culebrinas_bridge_2017 (USD 4.8m FHWA).
#   us bridges_roads: del_valle_manati_bridge_2017 (USD 4.5m FHWA).
#   us bridges_roads: lpcd_el_yunque_pr930_2018 (USD 4.7m FHWA).
#   us bridges_roads: aluma_vieques_camp_garcia_2008 (USD 6.8m FHWA).
#   us bridges_roads: lpcd_route9966_wall_2012 (USD 3.6m FHWA).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: other_renewables, balsa, rail, port_cranes, copper,
#   graphite, water, solar, engineering_epc, lithium, nickel,
#   building_materials, port_ownership, fission_smr, niobium,
#   power_plants_grid, wind.
# Active after cycle 119: us310 / prc239 / allied243 / other37 (n=829).
shuffle_seed: 20261119
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- energy/other_renewables
- resources/balsa
- infrastructure/rail
- infrastructure/port_cranes
- resources/copper
- resources/graphite
- resources/water
- energy/solar
- infrastructure/engineering_epc
- resources/lithium
- resources/nickel
- infrastructure/building_materials
- infrastructure/port_ownership
- energy/fission_smr
- resources/niobium
- energy/power_plants_grid
- energy/wind
rows_found_this_cycle:
  infrastructure/bridges_roads: 5
  energy/other_renewables: 0
  resources/balsa: 0
  infrastructure/rail: 0
  infrastructure/port_cranes: 0
  resources/copper: 0
  resources/graphite: 0
  resources/water: 0
  energy/solar: 0
  infrastructure/engineering_epc: 0
  resources/lithium: 0
  resources/nickel: 0
  infrastructure/building_materials: 0
  infrastructure/port_ownership: 0
  energy/fission_smr: 0
  resources/niobium: 0
  energy/power_plants_grid: 0
  energy/wind: 0
rows_by_side_this_cycle:
  us: 5
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 118 (seed 20261118) ===
# Shuffled order: building_materials, wind, balsa, fission_smr, copper,
#   port_cranes, nickel, power_plants_grid, lithium, engineering_epc,
#   other_renewables, bridges_roads, solar, water, port_ownership, rail,
#   graphite, niobium.
# Logged 2 sourced rows (honest US; thin dry; Jinko Chile ESS unnamed-site /
#   Bloomberg State Grid paywall; no padding):
#   us water: tec_lares_crib_dam_2008 (USD 16.4m USACE).
#   us water: carro_ponce_cofferdam_2020 (USD 15.6m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, wind, balsa, fission_smr, copper,
#   port_cranes, nickel, power_plants_grid, lithium, engineering_epc,
#   other_renewables, bridges_roads, solar, port_ownership, rail, graphite,
#   niobium.
# Active after cycle 118: us305 / prc239 / allied243 / other37 (n=824).
shuffle_seed: 20261118
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- energy/wind
- resources/balsa
- energy/fission_smr
- resources/copper
- infrastructure/port_cranes
- resources/nickel
- energy/power_plants_grid
- resources/lithium
- infrastructure/engineering_epc
- energy/other_renewables
- infrastructure/bridges_roads
- energy/solar
- resources/water
- infrastructure/port_ownership
- infrastructure/rail
- resources/graphite
- resources/niobium
rows_found_this_cycle:
  infrastructure/building_materials: 0
  energy/wind: 0
  resources/balsa: 0
  energy/fission_smr: 0
  resources/copper: 0
  infrastructure/port_cranes: 0
  resources/nickel: 0
  energy/power_plants_grid: 0
  resources/lithium: 0
  infrastructure/engineering_epc: 0
  energy/other_renewables: 0
  infrastructure/bridges_roads: 0
  energy/solar: 0
  resources/water: 2
  infrastructure/port_ownership: 0
  infrastructure/rail: 0
  resources/graphite: 0
  resources/niobium: 0
rows_by_side_this_cycle:
  us: 2
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 117 (seed 20261117) ===
# Shuffled order: niobium, graphite, port_cranes, balsa, rail, nickel, copper,
#   power_plants_grid, wind, water, fission_smr, other_renewables,
#   engineering_epc, solar, bridges_roads, lithium, port_ownership,
#   building_materials.
# Logged 5 sourced rows (honest US; thin dry; Graphcoa/CBMM/BRN/EXIM Guyana/
#   CHEC Las Palmas named-site pass dense; no padding):
#   us engineering_epc: bl_harbert_nuevo_laredo_ncc_2014 (USD 108.4m State).
#   us engineering_epc: jajones_belmopan_nec_2004 (USD 50.4m State).
#   us engineering_epc: caddell_tijuana_ncc_2007 (USD 76.2m State).
#   us engineering_epc: cce_guayaquil_nab_2008 (USD 50.3m State).
#   us engineering_epc: walsh_sj_federal_building_2016 (USD 81.7m GSA).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: niobium, graphite, port_cranes, balsa, rail, nickel,
#   copper, power_plants_grid, wind, water, fission_smr, other_renewables,
#   solar, bridges_roads, lithium, port_ownership, building_materials.
# Active after cycle 117: us303 / prc239 / allied243 / other37 (n=822).
shuffle_seed: 20261117
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- resources/graphite
- infrastructure/port_cranes
- resources/balsa
- infrastructure/rail
- resources/nickel
- resources/copper
- energy/power_plants_grid
- energy/wind
- resources/water
- energy/fission_smr
- energy/other_renewables
- infrastructure/engineering_epc
- energy/solar
- infrastructure/bridges_roads
- resources/lithium
- infrastructure/port_ownership
- infrastructure/building_materials
rows_found_this_cycle:
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/port_cranes: 0
  resources/balsa: 0
  infrastructure/rail: 0
  resources/nickel: 0
  resources/copper: 0
  energy/power_plants_grid: 0
  energy/wind: 0
  resources/water: 0
  energy/fission_smr: 0
  energy/other_renewables: 0
  infrastructure/engineering_epc: 5
  energy/solar: 0
  infrastructure/bridges_roads: 0
  resources/lithium: 0
  infrastructure/port_ownership: 0
  infrastructure/building_materials: 0
rows_by_side_this_cycle:
  us: 5
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 116 (seed 20261116) ===
# Shuffled order: port_cranes, power_plants_grid, lithium, rail,
#   building_materials, wind, balsa, bridges_roads, port_ownership, nickel,
#   solar, graphite, copper, engineering_epc, fission_smr, water,
#   other_renewables, niobium.
# Logged 6 sourced rows (honest US; thin dry; ZPMC/Trina/Goldwind named-site
#   pass dense; no padding):
#   us engineering_epc: caddell_panama_city_nec_2004 (USD 71.0m State).
#   us engineering_epc: zachry_managua_nec_2004 (USD 68.3m State).
#   us engineering_epc: bl_harbert_matamoros_nec_2015 (USD 124.6m State).
#   us engineering_epc: perini_montevideo_chancery_2017 (USD 125.9m State).
#   us engineering_epc: yates_desbuild_monterrey_nec_2009 (USD 124.8m State).
#   us engineering_epc: rq_gtmo_jtf_barracks_2019 (USD 82.8m NAVFAC).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: port_cranes, power_plants_grid, lithium, rail,
#   building_materials, wind, balsa, bridges_roads, port_ownership, nickel,
#   solar, graphite, copper, fission_smr, water, other_renewables, niobium.
# Active after cycle 116: us298 / prc239 / allied243 / other37 (n=817).
shuffle_seed: 20261116
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_cranes
- energy/power_plants_grid
- resources/lithium
- infrastructure/rail
- infrastructure/building_materials
- energy/wind
- resources/balsa
- infrastructure/bridges_roads
- infrastructure/port_ownership
- resources/nickel
- energy/solar
- resources/graphite
- resources/copper
- infrastructure/engineering_epc
- energy/fission_smr
- resources/water
- energy/other_renewables
- resources/niobium
rows_found_this_cycle:
  infrastructure/port_cranes: 0
  energy/power_plants_grid: 0
  resources/lithium: 0
  infrastructure/rail: 0
  infrastructure/building_materials: 0
  energy/wind: 0
  resources/balsa: 0
  infrastructure/bridges_roads: 0
  infrastructure/port_ownership: 0
  resources/nickel: 0
  energy/solar: 0
  resources/graphite: 0
  resources/copper: 0
  infrastructure/engineering_epc: 6
  energy/fission_smr: 0
  resources/water: 0
  energy/other_renewables: 0
  resources/niobium: 0
rows_by_side_this_cycle:
  us: 6
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 115 (seed 20261115) ===
# Shuffled order: building_materials, power_plants_grid, lithium, port_cranes,
#   bridges_roads, niobium, copper, fission_smr, engineering_epc, rail,
#   other_renewables, graphite, solar, water, balsa, wind, port_ownership,
#   nickel.
# Logged 6 sourced rows (honest US; thin dry; PRC Trina/Goldwind named-site
#   pass re-hit already-logged Luz del Norte/Alma Sur/SPIC Touros; no padding):
#   us engineering_epc: bl_harbert_hermosillo_ncc_2018 (USD 155.8m State).
#   us engineering_epc: bl_harbert_merida_ncc_2019 (USD 140.6m State).
#   us engineering_epc: bl_harbert_nogales_ncc_2018 (USD 135.2m State).
#   us engineering_epc: caddell_santo_domingo_nec_2010 (USD 150.9m State).
#   us engineering_epc: caddell_buenos_aires_sip_2025 (USD 170.9m State).
#   us engineering_epc: fluor_haiti_nec_2005 (USD 72.3m State).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, power_plants_grid, lithium,
#   port_cranes, bridges_roads, niobium, copper, fission_smr, rail,
#   other_renewables, graphite, solar, water, balsa, wind, port_ownership,
#   nickel (dense prior).
# Active after cycle 115: us292 / prc239 / allied243 / other37 (n=811).
shuffle_seed: 20261115
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- energy/power_plants_grid
- resources/lithium
- infrastructure/port_cranes
- infrastructure/bridges_roads
- resources/niobium
- resources/copper
- energy/fission_smr
- infrastructure/engineering_epc
- infrastructure/rail
- energy/other_renewables
- resources/graphite
- energy/solar
- resources/water
- resources/balsa
- energy/wind
- infrastructure/port_ownership
- resources/nickel
rows_found_this_cycle:
  infrastructure/building_materials: 0
  energy/power_plants_grid: 0
  resources/lithium: 0
  infrastructure/port_cranes: 0
  infrastructure/bridges_roads: 0
  resources/niobium: 0
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/engineering_epc: 6
  infrastructure/rail: 0
  energy/other_renewables: 0
  resources/graphite: 0
  energy/solar: 0
  resources/water: 0
  resources/balsa: 0
  energy/wind: 0
  infrastructure/port_ownership: 0
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 6
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 114 (seed 20261114) ===
# Shuffled order: building_materials, nickel, fission_smr, solar, graphite,
#   port_cranes, engineering_epc, niobium, bridges_roads, balsa,
#   port_ownership, power_plants_grid, other_renewables, water, copper, wind,
#   lithium, rail.
# Logged 6 sourced rows (honest US; thin dry; PRC OEM named-site pass dry;
#   no padding):
#   us engineering_epc: bl_harbert_tegucigalpa_nec_2018 (USD 268.2m State).
#   us engineering_epc: caddell_nassau_nec_2018 (USD 228.1m State).
#   us engineering_epc: caddell_asuncion_nec_2017 (USD 187.7m State).
#   us engineering_epc: caddell_rio_consulate_2022 (USD 322.4m State).
#   us engineering_epc: bl_harbert_guadalajara_ncc_2018 (USD 191.6m State).
#   us engineering_epc: tutor_perini_sj_customs_2021 (USD 63.6m CBP).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, nickel, fission_smr, solar, graphite,
#   port_cranes, niobium, bridges_roads, balsa, port_ownership,
#   power_plants_grid, other_renewables, water, copper, wind, lithium, rail
#   (dense prior; Goldwind SPIC/Pemuco already logged).
# Active after cycle 114: us286 / prc239 / allied243 / other37 (n=805).
shuffle_seed: 20261114
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- resources/nickel
- energy/fission_smr
- energy/solar
- resources/graphite
- infrastructure/port_cranes
- infrastructure/engineering_epc
- resources/niobium
- infrastructure/bridges_roads
- resources/balsa
- infrastructure/port_ownership
- energy/power_plants_grid
- energy/other_renewables
- resources/water
- resources/copper
- energy/wind
- resources/lithium
- infrastructure/rail
rows_found_this_cycle:
  infrastructure/building_materials: 0
  resources/nickel: 0
  energy/fission_smr: 0
  energy/solar: 0
  resources/graphite: 0
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 6
  resources/niobium: 0
  infrastructure/bridges_roads: 0
  resources/balsa: 0
  infrastructure/port_ownership: 0
  energy/power_plants_grid: 0
  energy/other_renewables: 0
  resources/water: 0
  resources/copper: 0
  energy/wind: 0
  resources/lithium: 0
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 6
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 113 (seed 20261113) ===
# Shuffled order: wind, bridges_roads, port_cranes, other_renewables, rail,
#   engineering_epc, balsa, fission_smr, port_ownership, water,
#   building_materials, solar, power_plants_grid, nickel, niobium, copper,
#   lithium, graphite.
# Logged 6 sourced rows (honest US/PRC/allied; thin dry; no padding):
#   us engineering_epc: caddell_mexico_city_nec_2017 (USD 584.2m State).
#   us engineering_epc: caddell_brasilia_nec_2022 (USD 415.3m State).
#   us engineering_epc: caddell_port_of_spain_nec_2024 (USD 353.6m State).
#   us engineering_epc: bl_harbert_guatemala_nec_2017 (USD 307.2m State).
#   prc solar: sungrow_vista_alegre_inverters_2024 (902 MWp 1+X; CapEx blank).
#   allied power_plants_grid: siemens_gtmo_lng_espc_2019 (USD 101.1m NAVFAC).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: wind, bridges_roads, port_cranes, other_renewables, rail,
#   balsa, fission_smr, port_ownership, water, building_materials, nickel,
#   niobium, copper, lithium, graphite (dense prior).
# Active after cycle 113: us280 / prc239 / allied243 / other37 (n=799).
shuffle_seed: 20261113
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/wind
- infrastructure/bridges_roads
- infrastructure/port_cranes
- energy/other_renewables
- infrastructure/rail
- infrastructure/engineering_epc
- resources/balsa
- energy/fission_smr
- infrastructure/port_ownership
- resources/water
- infrastructure/building_materials
- energy/solar
- energy/power_plants_grid
- resources/nickel
- resources/niobium
- resources/copper
- resources/lithium
- resources/graphite
rows_found_this_cycle:
  energy/wind: 0
  infrastructure/bridges_roads: 0
  infrastructure/port_cranes: 0
  energy/other_renewables: 0
  infrastructure/rail: 0
  infrastructure/engineering_epc: 4
  resources/balsa: 0
  energy/fission_smr: 0
  infrastructure/port_ownership: 0
  resources/water: 0
  infrastructure/building_materials: 0
  energy/solar: 1
  energy/power_plants_grid: 1
  resources/nickel: 0
  resources/niobium: 0
  resources/copper: 0
  resources/lithium: 0
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 112 (seed 20261112) ===
# Shuffled order: lithium, building_materials, port_ownership, engineering_epc,
#   copper, graphite, rail, solar, water, port_cranes, nickel, bridges_roads,
#   balsa, fission_smr, wind, other_renewables, power_plants_grid, niobium.
# Logged 2 sourced rows (honest US; thin dry; no padding):
#   us water: flatiron_portugues_dam_2008 (USD 217.7m USACE).
#   us bridges_roads: carro_de_diego_bridge_2007 (USD 35.0m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: lithium, building_materials, port_ownership,
#   engineering_epc, copper, graphite, rail, solar, port_cranes, nickel,
#   balsa, fission_smr, wind, other_renewables, power_plants_grid, niobium
#   (dense prior; Ferrovial RPN Contract 3 already logged).
# Active after cycle 112: us276 / prc238 / allied242 / other37 (n=793).
shuffle_seed: 20261112
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/lithium
- infrastructure/building_materials
- infrastructure/port_ownership
- infrastructure/engineering_epc
- resources/copper
- resources/graphite
- infrastructure/rail
- energy/solar
- resources/water
- infrastructure/port_cranes
- resources/nickel
- infrastructure/bridges_roads
- resources/balsa
- energy/fission_smr
- energy/wind
- energy/other_renewables
- energy/power_plants_grid
- resources/niobium
rows_found_this_cycle:
  resources/lithium: 0
  infrastructure/building_materials: 0
  infrastructure/port_ownership: 0
  infrastructure/engineering_epc: 0
  resources/copper: 0
  resources/graphite: 0
  infrastructure/rail: 0
  energy/solar: 0
  resources/water: 1
  infrastructure/port_cranes: 0
  resources/nickel: 0
  infrastructure/bridges_roads: 1
  resources/balsa: 0
  energy/fission_smr: 0
  energy/wind: 0
  energy/other_renewables: 0
  energy/power_plants_grid: 0
  resources/niobium: 0
rows_by_side_this_cycle:
  us: 2
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 111 (seed 20261111) ===
# Shuffled order: building_materials, fission_smr, niobium, power_plants_grid,
#   water, bridges_roads, port_ownership, wind, other_renewables, port_cranes,
#   nickel, graphite, engineering_epc, lithium, rail, balsa, copper, solar.
# Logged 3 sourced rows (honest US/allied; PRC OEM named-site pass dry;
#   no padding):
#   us power_plants_grid: weston_maria_temp_power_2017 (USD 218.4m USACE).
#   allied power_plants_grid: wsp_maria_power_install_2017 (USD 597.0m USACE PSC N030).
#   us water: foresight_guajataca_gates_2018 (USD 1.1m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: building_materials, fission_smr, niobium, bridges_roads,
#   port_ownership, wind, other_renewables, port_cranes, nickel, graphite,
#   engineering_epc, lithium, rail, balsa, copper, solar (dense prior).
# Active after cycle 111: us274 / prc238 / allied242 / other37 (n=791).
shuffle_seed: 20261111
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/building_materials
- energy/fission_smr
- resources/niobium
- energy/power_plants_grid
- resources/water
- infrastructure/bridges_roads
- infrastructure/port_ownership
- energy/wind
- energy/other_renewables
- infrastructure/port_cranes
- resources/nickel
- resources/graphite
- infrastructure/engineering_epc
- resources/lithium
- infrastructure/rail
- resources/balsa
- resources/copper
- energy/solar
rows_found_this_cycle:
  infrastructure/building_materials: 0
  energy/fission_smr: 0
  resources/niobium: 0
  energy/power_plants_grid: 2
  resources/water: 1
  infrastructure/bridges_roads: 0
  infrastructure/port_ownership: 0
  energy/wind: 0
  energy/other_renewables: 0
  infrastructure/port_cranes: 0
  resources/nickel: 0
  resources/graphite: 0
  infrastructure/engineering_epc: 0
  resources/lithium: 0
  infrastructure/rail: 0
  resources/balsa: 0
  resources/copper: 0
  energy/solar: 0
rows_by_side_this_cycle:
  us: 2
  prc: 0
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 110 (seed 20261110) ===
# Shuffled order: port_cranes, port_ownership, other_renewables, lithium,
#   building_materials, fission_smr, niobium, bridges_roads, solar, copper,
#   rail, water, power_plants_grid, graphite, balsa, wind, engineering_epc,
#   nickel.
# Logged 2 sourced rows (honest US/PRC; no padding):
#   prc solar: sungrow_hdec_atacama_480mw_2022 (480 MW Atacama / HDEC; CapEx blank).
#   us engineering_epc: rq_aecom_ponce_rio_2021 (USD 21.4m USCG).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: port_cranes, port_ownership, other_renewables, lithium,
#   building_materials, fission_smr, niobium, bridges_roads, copper, rail,
#   water, power_plants_grid, graphite, balsa, wind, nickel (dense prior;
#   Trina newsroom LatAm scan only re-hit Lagoa do Barro).
# Active after cycle 110: us272 / prc238 / allied241 / other37 (n=788).
shuffle_seed: 20261110
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/port_cranes
- infrastructure/port_ownership
- energy/other_renewables
- resources/lithium
- infrastructure/building_materials
- energy/fission_smr
- resources/niobium
- infrastructure/bridges_roads
- energy/solar
- resources/copper
- infrastructure/rail
- resources/water
- energy/power_plants_grid
- resources/graphite
- resources/balsa
- energy/wind
- infrastructure/engineering_epc
- resources/nickel
rows_found_this_cycle:
  infrastructure/port_cranes: 0
  infrastructure/port_ownership: 0
  energy/other_renewables: 0
  resources/lithium: 0
  infrastructure/building_materials: 0
  energy/fission_smr: 0
  resources/niobium: 0
  infrastructure/bridges_roads: 0
  energy/solar: 1
  resources/copper: 0
  infrastructure/rail: 0
  resources/water: 0
  energy/power_plants_grid: 0
  resources/graphite: 0
  resources/balsa: 0
  energy/wind: 0
  infrastructure/engineering_epc: 1
  resources/nickel: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 109 (seed 20261109) ===
# Shuffled order: fission_smr, balsa, solar, graphite, bridges_roads,
#   power_plants_grid, copper, lithium, port_ownership, water,
#   other_renewables, niobium, rail, nickel, building_materials, wind,
#   port_cranes, engineering_epc.
# Logged 4 sourced rows (honest US/PRC/allied; no padding):
#   prc solar: sungrow_focus_futura_juazeiro_2021 (852 MWp Futura I; CapEx blank).
#   prc other_renewables: sungrow_engie_bess_coya_638mwh_2022 (638 MWh; CapEx blank).
#   allied power_plants_grid: wsp_maria_nonfederal_generators_2017 (USD 22.6m).
#   us water: thompson_guajataca_pumping_2018 (USD 4.0m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: fission_smr, balsa, graphite, bridges_roads, copper,
#   lithium, port_ownership, niobium, rail, nickel, building_materials, wind,
#   port_cranes, engineering_epc (dense prior).
# Active after cycle 109: us271 / prc237 / allied241 / other37 (n=786).
shuffle_seed: 20261109
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/fission_smr
- resources/balsa
- energy/solar
- resources/graphite
- infrastructure/bridges_roads
- energy/power_plants_grid
- resources/copper
- resources/lithium
- infrastructure/port_ownership
- resources/water
- energy/other_renewables
- resources/niobium
- infrastructure/rail
- resources/nickel
- infrastructure/building_materials
- energy/wind
- infrastructure/port_cranes
- infrastructure/engineering_epc
rows_found_this_cycle:
  energy/fission_smr: 0
  resources/balsa: 0
  energy/solar: 1
  resources/graphite: 0
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 1
  resources/copper: 0
  resources/lithium: 0
  infrastructure/port_ownership: 0
  resources/water: 1
  energy/other_renewables: 1
  resources/niobium: 0
  infrastructure/rail: 0
  resources/nickel: 0
  infrastructure/building_materials: 0
  energy/wind: 0
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 0
rows_by_side_this_cycle:
  us: 1
  prc: 2
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 108 (seed 20261108) ===
# Shuffled order: engineering_epc, rail, wind, fission_smr, other_renewables,
#   bridges_roads, nickel, port_cranes, water, balsa, port_ownership, copper,
#   niobium, building_materials, power_plants_grid, lithium, solar, graphite.
# Logged 2 sourced rows (honest US/PRC; no padding):
#   prc solar: sungrow_mercury_helio_valgas_2022 (500 MWac / 650 MWp; CapEx blank).
#   us water: flatiron_margarita_channel_2010 (USD 57.7m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: engineering_epc, rail, wind, fission_smr,
#   other_renewables, bridges_roads, nickel, port_cranes, balsa,
#   port_ownership, copper, niobium, building_materials, power_plants_grid,
#   lithium, graphite (dense prior; Sungrow Chile 480 MW without named site
#   skipped).
# Active after cycle 108: us270 / prc235 / allied240 / other37 (n=782).
shuffle_seed: 20261108
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- infrastructure/rail
- energy/wind
- energy/fission_smr
- energy/other_renewables
- infrastructure/bridges_roads
- resources/nickel
- infrastructure/port_cranes
- resources/water
- resources/balsa
- infrastructure/port_ownership
- resources/copper
- resources/niobium
- infrastructure/building_materials
- energy/power_plants_grid
- resources/lithium
- energy/solar
- resources/graphite
rows_found_this_cycle:
  infrastructure/engineering_epc: 0
  infrastructure/rail: 0
  energy/wind: 0
  energy/fission_smr: 0
  energy/other_renewables: 0
  infrastructure/bridges_roads: 0
  resources/nickel: 0
  infrastructure/port_cranes: 0
  resources/water: 1
  resources/balsa: 0
  infrastructure/port_ownership: 0
  resources/copper: 0
  resources/niobium: 0
  infrastructure/building_materials: 0
  energy/power_plants_grid: 0
  resources/lithium: 0
  energy/solar: 1
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 107 (seed 20261107) ===
# Shuffled order: power_plants_grid, lithium, niobium, other_renewables,
#   engineering_epc, copper, port_ownership, fission_smr, wind, graphite,
#   bridges_roads, building_materials, nickel, balsa, rail, port_cranes,
#   solar, water.
# Logged 5 sourced rows (honest US; PRC named-site pass dry; no padding):
#   us power_plants_grid: fluor_pr_grid_restore_2017 (USD 276.3m USACE).
#   us engineering_epc: tutor_perini_uscg_sj_phase2_2022 (USD 117.0m USCG).
#   us engineering_epc: tutor_perini_uscg_sj_phase3_2022 (USD 17.9m USCG).
#   us engineering_epc: rq_aecom_borinquen_phase2_2022 (USD 126.6m USCG).
#   us engineering_epc: caddell_nova_borinquen_2022 (USD 84.0m USCG).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: lithium, niobium, other_renewables, copper,
#   port_ownership, fission_smr, wind, graphite, bridges_roads,
#   building_materials, nickel, balsa, rail, port_cranes, solar, water
#   (dense prior).
# Active after cycle 107: us269 / prc234 / allied240 / other37 (n=780).
shuffle_seed: 20261107
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/power_plants_grid
- resources/lithium
- resources/niobium
- energy/other_renewables
- infrastructure/engineering_epc
- resources/copper
- infrastructure/port_ownership
- energy/fission_smr
- energy/wind
- resources/graphite
- infrastructure/bridges_roads
- infrastructure/building_materials
- resources/nickel
- resources/balsa
- infrastructure/rail
- infrastructure/port_cranes
- energy/solar
- resources/water
rows_found_this_cycle:
  energy/power_plants_grid: 1
  resources/lithium: 0
  resources/niobium: 0
  energy/other_renewables: 0
  infrastructure/engineering_epc: 4
  resources/copper: 0
  infrastructure/port_ownership: 0
  energy/fission_smr: 0
  energy/wind: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 0
  infrastructure/building_materials: 0
  resources/nickel: 0
  resources/balsa: 0
  infrastructure/rail: 0
  infrastructure/port_cranes: 0
  energy/solar: 0
  resources/water: 0
rows_by_side_this_cycle:
  us: 5
  prc: 0
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 106 (seed 20261106) ===
# Shuffled order: water, solar, graphite, balsa, power_plants_grid,
#   other_renewables, lithium, copper, fission_smr, wind, niobium,
#   engineering_epc, nickel, port_ownership, bridges_roads, building_materials,
#   rail, port_cranes.
# Logged 6 sourced rows (honest US/allied; PRC named-site pass dry; no padding):
#   us power_plants_grid: fluor_pr_transmission_distribution_2017 (USD 505.7m).
#   us power_plants_grid: powersecure_pr_grid_survey_2017 (USD 505.5m).
#   us water: del_valle_guajataca_stage2_2018 (USD 17.8m USACE).
#   us water: del_valle_guajataca_risk_2018 (USD 5.8m USACE).
#   allied power_plants_grid: wsp_aci_tep_pr_2022 (USD 20.1m USACE).
#   us engineering_epc: tutor_perini_uscg_bayamon_2025 (USD 20.5m USCG).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: solar, graphite, balsa, other_renewables, lithium,
#   copper, fission_smr, wind, niobium, nickel, port_ownership, bridges_roads,
#   building_materials, rail, port_cranes (dense prior).
# Active after cycle 106: us264 / prc234 / allied240 / other37 (n=775).
shuffle_seed: 20261106
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/water
- energy/solar
- resources/graphite
- resources/balsa
- energy/power_plants_grid
- energy/other_renewables
- resources/lithium
- resources/copper
- energy/fission_smr
- energy/wind
- resources/niobium
- infrastructure/engineering_epc
- resources/nickel
- infrastructure/port_ownership
- infrastructure/bridges_roads
- infrastructure/building_materials
- infrastructure/rail
- infrastructure/port_cranes
rows_found_this_cycle:
  resources/water: 2
  energy/solar: 0
  resources/graphite: 0
  resources/balsa: 0
  energy/power_plants_grid: 3
  energy/other_renewables: 0
  resources/lithium: 0
  resources/copper: 0
  energy/fission_smr: 0
  energy/wind: 0
  resources/niobium: 0
  infrastructure/engineering_epc: 1
  resources/nickel: 0
  infrastructure/port_ownership: 0
  infrastructure/bridges_roads: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  infrastructure/port_cranes: 0
rows_by_side_this_cycle:
  us: 5
  prc: 0
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 105 (seed 20261105) ===
# Shuffled order: engineering_epc, wind, port_ownership, water, port_cranes,
#   copper, fission_smr, lithium, balsa, power_plants_grid, solar, rail,
#   graphite, nickel, niobium, bridges_roads, other_renewables, building_materials.
# Logged 7 sourced rows (honest US/allied split; PRC OEM named-site pass dry;
#   no padding):
#   us power_plants_grid: aptim_yabucoa_temp_power_2017 (USD 54.2m USACE).
#   us water: flatiron_bechara_puerto_nuevo_2011 (USD 43.1m USACE).
#   us water: del_valle_rpn_2d_walls_2017 (USD 24.0m USACE).
#   us water: lpcd_rpn_margarita_2014 (USD 21.2m USACE).
#   us other_renewables: johnson_controls_prng_espc_2014 (USD 29.3m USACE).
#   us building_materials: caribbean_lumber_valor_materials_2018 (USD 23.2m FEMA).
#   allied other_renewables: schneider_espc_pr_cool_roofs_2010 (USD 54.2m USCG).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr also dry.
# Equal-budget misses: engineering_epc, wind, port_ownership, port_cranes,
#   copper, fission_smr, lithium, balsa, solar, rail, graphite, nickel,
#   niobium, bridges_roads (dense prior; Sungrow 9 GW LatAm cumulative without
#   named site skipped).
# Active after cycle 105: us259 / prc234 / allied239 / other37 (n=769).
shuffle_seed: 20261105
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- energy/wind
- infrastructure/port_ownership
- resources/water
- infrastructure/port_cranes
- resources/copper
- energy/fission_smr
- resources/lithium
- resources/balsa
- energy/power_plants_grid
- energy/solar
- infrastructure/rail
- resources/graphite
- resources/nickel
- resources/niobium
- infrastructure/bridges_roads
- energy/other_renewables
- infrastructure/building_materials
rows_found_this_cycle:
  infrastructure/engineering_epc: 0
  energy/wind: 0
  infrastructure/port_ownership: 0
  resources/water: 3
  infrastructure/port_cranes: 0
  resources/copper: 0
  energy/fission_smr: 0
  resources/lithium: 0
  resources/balsa: 0
  energy/power_plants_grid: 1
  energy/solar: 0
  infrastructure/rail: 0
  resources/graphite: 0
  resources/nickel: 0
  resources/niobium: 0
  infrastructure/bridges_roads: 0
  energy/other_renewables: 2
  infrastructure/building_materials: 1
rows_by_side_this_cycle:
  us: 6
  prc: 0
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 104 (seed 20261104) ===
# Shuffled order: solar, building_materials, rail, engineering_epc, fission_smr,
#   power_plants_grid, wind, port_cranes, copper, water, other_renewables,
#   bridges_roads, port_ownership, nickel, lithium, balsa, graphite, niobium.
# Logged 5 sourced rows (honest US/PRC split; no padding):
#   prc solar: trinatracker_cgn_lagoa_barro_2025 (1,083 Vanguard 1P; 56.11 MWp; CapEx blank).
#   us other_renewables: rq_lord_ramey_arc_microgrid_2024 (USD 19.5m USACE ERCIP).
#   us other_renewables: parsons_pesquera_arc_microgrid_2024 (USD 17.2m USACE).
#   us other_renewables: johnson_controls_buchanan_res_0003_2011 (USD 54.4m USACE).
#   us other_renewables: johnson_controls_buchanan_res_0006_2012 (USD 34.7m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/
#   building_materials also dry.
# Equal-budget misses: building_materials, rail, engineering_epc, fission_smr,
#   power_plants_grid, wind, port_cranes, copper, water, bridges_roads,
#   port_ownership, nickel, lithium, balsa, graphite, niobium (dense prior;
#   USVI FHWA skipped — not in geography list).
# Active after cycle 104: us253 / prc234 / allied238 / other37 (n=762).
shuffle_seed: 20261104
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/solar
- infrastructure/building_materials
- infrastructure/rail
- infrastructure/engineering_epc
- energy/fission_smr
- energy/power_plants_grid
- energy/wind
- infrastructure/port_cranes
- resources/copper
- resources/water
- energy/other_renewables
- infrastructure/bridges_roads
- infrastructure/port_ownership
- resources/nickel
- resources/lithium
- resources/balsa
- resources/graphite
- resources/niobium
rows_found_this_cycle:
  energy/solar: 1
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  infrastructure/engineering_epc: 0
  energy/fission_smr: 0
  energy/power_plants_grid: 0
  energy/wind: 0
  infrastructure/port_cranes: 0
  resources/copper: 0
  resources/water: 0
  energy/other_renewables: 4
  infrastructure/bridges_roads: 0
  infrastructure/port_ownership: 0
  resources/nickel: 0
  resources/lithium: 0
  resources/balsa: 0
  resources/graphite: 0
  resources/niobium: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 103 (seed 20261103) ===
# Shuffled order: graphite, port_cranes, fission_smr, balsa, niobium, wind,
#   lithium, power_plants_grid, copper, port_ownership, solar, water, nickel,
#   bridges_roads, other_renewables, engineering_epc, building_materials, rail.
# Logged 6 sourced rows (honest US/PRC split; no padding):
#   us power_plants_grid: weston_palo_seco_temp_power_2023 (USD 816.2m USACE).
#   us power_plants_grid: weston_san_juan_temp_power_2023 (USD 668.9m USACE).
#   prc solar: sungrow_zelestra_aurora_bess_2025 (~1 GWh BESS + 220 MWdc; CapEx blank).
#   us water: ferrovial_usace_drilled_shaft_6c_2024 (USD 150.4m USACE).
#   us water: novel_cano_martin_pena_2025 (USD 57.4m USACE).
#   us engineering_epc: curtin_san_juan_harbor_dredge_2023 (USD 54.2m USACE).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/
#   building_materials also dry.
# Equal-budget misses: graphite, port_cranes, fission_smr, balsa, niobium, wind,
#   lithium, copper, port_ownership, nickel, bridges_roads, other_renewables,
#   building_materials, rail (dense prior; Jinko Casa dos Ventos / Bluefields /
#   ENEE 230 kV already logged).
# Active after cycle 103: us249 / prc233 / allied238 / other37 (n=757).
shuffle_seed: 20261103
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/graphite
- infrastructure/port_cranes
- energy/fission_smr
- resources/balsa
- resources/niobium
- energy/wind
- resources/lithium
- energy/power_plants_grid
- resources/copper
- infrastructure/port_ownership
- energy/solar
- resources/water
- resources/nickel
- infrastructure/bridges_roads
- energy/other_renewables
- infrastructure/engineering_epc
- infrastructure/building_materials
- infrastructure/rail
rows_found_this_cycle:
  resources/graphite: 0
  infrastructure/port_cranes: 0
  energy/fission_smr: 0
  resources/balsa: 0
  resources/niobium: 0
  energy/wind: 0
  resources/lithium: 0
  energy/power_plants_grid: 2
  resources/copper: 0
  infrastructure/port_ownership: 0
  energy/solar: 1
  resources/water: 2
  resources/nickel: 0
  infrastructure/bridges_roads: 0
  energy/other_renewables: 0
  infrastructure/engineering_epc: 1
  infrastructure/building_materials: 0
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 5
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 102 (seed 20261102) ===
# Shuffled order: power_plants_grid, wind, other_renewables, balsa, nickel,
#   building_materials, solar, lithium, copper, fission_smr, bridges_roads,
#   graphite, port_ownership, niobium, port_cranes, engineering_epc, water, rail.
# Logged 5 sourced rows (honest US/PRC/allied split; no padding):
#   us engineering_epc: jacobs_fhwa_pr25_inspect_2026 (USD 2.20m FHWA).
#   prc engineering_epc: cdb_bndes_rmb5bn_2024 (CNY 5bn CDB–BNDES facility).
#   allied engineering_epc: atkinsrealis_fhwa_yunque_inspect_2022 (USD 4.12m).
#   allied engineering_epc: atkinsrealis_fhwa_pr12_inspect_2024 (USD 2.78m).
#   allied engineering_epc: mj_cardno_fhwa_pr10_inspect_2023 (USD 3.32m).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/
#   building_materials also dry.
# Equal-budget misses: power_plants_grid, wind, other_renewables, balsa, nickel,
#   building_materials, solar, lithium, copper, fission_smr, bridges_roads,
#   graphite, port_ownership, niobium, port_cranes, water, rail (dense prior;
#   FHWA construction ≥USD 2.5m exhausted; Cangrejos/Ganfeng 180m/ZPMC Kingston
#   /SPIC UG7 already logged).
# Active after cycle 102: us244 / prc232 / allied238 / other37 (n=751).
shuffle_seed: 20261102
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/power_plants_grid
- energy/wind
- energy/other_renewables
- resources/balsa
- resources/nickel
- infrastructure/building_materials
- energy/solar
- resources/lithium
- resources/copper
- energy/fission_smr
- infrastructure/bridges_roads
- resources/graphite
- infrastructure/port_ownership
- resources/niobium
- infrastructure/port_cranes
- infrastructure/engineering_epc
- resources/water
- infrastructure/rail
rows_found_this_cycle:
  energy/power_plants_grid: 0
  energy/wind: 0
  energy/other_renewables: 0
  resources/balsa: 0
  resources/nickel: 0
  infrastructure/building_materials: 0
  energy/solar: 0
  resources/lithium: 0
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/bridges_roads: 0
  resources/graphite: 0
  infrastructure/port_ownership: 0
  resources/niobium: 0
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 5
  resources/water: 0
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 3
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 101 (seed 20261101) ===
# Shuffled order: lithium, other_renewables, fission_smr, copper, nickel, niobium,
#   port_cranes, engineering_epc, building_materials, power_plants_grid, graphite,
#   wind, solar, balsa, port_ownership, water, bridges_roads, rail.
# Logged 5 sourced rows (honest US/PRC/allied split; no padding):
#   prc lithium: ganfeng_pozuelos_dev_200m_2025 (USD 200m post-acquisition).
#   prc lithium: ganfeng_ppg_jv_framework_2025 (67% New JV framework; CapEx blank).
#   us bridges_roads: fhwa_jpi_anasco_2023 (USD 3.26m FHWA).
#   us bridges_roads: fhwa_jpi_naguabo_2021 (USD 2.89m FHWA).
#   allied engineering_epc: atkinsrealis_fhwa_pr_inspect_2023 (USD 8.52m).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/
#   building_materials also dry.
# Equal-budget misses: other_renewables, fission_smr, copper, nickel, niobium,
#   port_cranes, building_materials, power_plants_grid, graphite, wind, solar,
#   balsa, port_ownership, water, rail (dense prior + country×subcat; BYD Elena /
#   Zijin 3Q RIGI / Stage 1 PPG CAPEX already logged).
# Active after cycle 101: us243 / prc231 / allied235 / other37 (n=746).
shuffle_seed: 20261101
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/lithium
- energy/other_renewables
- energy/fission_smr
- resources/copper
- resources/nickel
- resources/niobium
- infrastructure/port_cranes
- infrastructure/engineering_epc
- infrastructure/building_materials
- energy/power_plants_grid
- resources/graphite
- energy/wind
- energy/solar
- resources/balsa
- infrastructure/port_ownership
- resources/water
- infrastructure/bridges_roads
- infrastructure/rail
rows_found_this_cycle:
  resources/lithium: 2
  energy/other_renewables: 0
  energy/fission_smr: 0
  resources/copper: 0
  resources/nickel: 0
  resources/niobium: 0
  infrastructure/port_cranes: 0
  infrastructure/engineering_epc: 1
  infrastructure/building_materials: 0
  energy/power_plants_grid: 0
  resources/graphite: 0
  energy/wind: 0
  energy/solar: 0
  resources/balsa: 0
  infrastructure/port_ownership: 0
  resources/water: 0
  infrastructure/bridges_roads: 2
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 100 (seed 20261100) ===
# Shuffled order: niobium, wind, solar, port_ownership, fission_smr,
#   other_renewables, engineering_epc, rail, port_cranes, power_plants_grid,
#   building_materials, bridges_roads, water, balsa, nickel, copper, lithium,
#   graphite.
# Logged 7 sourced rows (honest split; no padding; PRC dry this pass):
#   allied niobium: cbmm_araxa_capex_630m_2024 (R$630m CapEx documented).
#   us bridges_roads: fhwa_nieves_lares_2024 (USD 3.83m FHWA).
#   us bridges_roads: fhwa_caribbean_sign_pr123_2021 (USD 17.19m FHWA).
#   us bridges_roads: fhwa_jc_associates_east_2022 (USD 14.52m FHWA).
#   us bridges_roads: fhwa_master_pavement_pr52_2021 (USD 8.88m FHWA).
#   us bridges_roads: fhwa_jpi_maunabo_2023 (USD 6.15m FHWA).
#   us bridges_roads: fhwa_novel_yunque_fs27_2021 (USD 6.86m FHWA/FAA).
# Thin top-up: niobium hit (CBMM CapEx); balsa/graphite/nickel dry — shift
#   fission_smr/building_materials also dry. PRC Catalão CapEx not separately
#   disclosed on opened CMOC pages.
# Equal-budget misses: wind, solar, port_ownership, fission_smr,
#   other_renewables, engineering_epc, rail, port_cranes, power_plants_grid,
#   building_materials, water, balsa, nickel, copper, lithium, graphite.
# Active after cycle 100: us241 / prc229 / allied234 / other37 (n=741).
shuffle_seed: 20261100
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- energy/wind
- energy/solar
- infrastructure/port_ownership
- energy/fission_smr
- energy/other_renewables
- infrastructure/engineering_epc
- infrastructure/rail
- infrastructure/port_cranes
- energy/power_plants_grid
- infrastructure/building_materials
- infrastructure/bridges_roads
- resources/water
- resources/balsa
- resources/nickel
- resources/copper
- resources/lithium
- resources/graphite
rows_found_this_cycle:
  resources/niobium: 1
  energy/wind: 0
  energy/solar: 0
  infrastructure/port_ownership: 0
  energy/fission_smr: 0
  energy/other_renewables: 0
  infrastructure/engineering_epc: 0
  infrastructure/rail: 0
  infrastructure/port_cranes: 0
  energy/power_plants_grid: 0
  infrastructure/building_materials: 0
  infrastructure/bridges_roads: 6
  resources/water: 0
  resources/balsa: 0
  resources/nickel: 0
  resources/copper: 0
  resources/lithium: 0
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 6
  prc: 0
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 99 (seed 20261099) ===
# Shuffled order: bridges_roads, other_renewables, graphite, port_cranes, wind,
#   fission_smr, water, nickel, port_ownership, solar, lithium, copper, niobium,
#   balsa, power_plants_grid, building_materials, rail, engineering_epc.
# Logged 7 sourced rows (honest US/PRC split; no padding):
#   us bridges_roads: fhwa_lpc_pr10_utuado_2022 (USD 84.20m FHWA).
#   us bridges_roads: fhwa_jm_caribbean_signs_2022 (USD 22.61m FHWA).
#   us bridges_roads: fhwa_ddd_dvg_aibonito_2022 (USD 12.98m FHWA).
#   us bridges_roads: fhwa_nieves_angeles_utuado_2022 (USD 7.01m FHWA).
#   us bridges_roads: fhwa_caribe_tecno_yunque_2021 (USD 13.97m FHWA/USFS).
#   prc port_cranes: zpmc_chancay_sts_rmg_rtg_2024 (6 quay+15 RMG+6 RTG; no USD).
#   us solar: exim_atlantida_olanchito_solar_2022 (USD 52m EXIM First Solar).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/niobium/
#   building_materials also dry.
# Equal-budget misses: other_renewables, graphite, wind, fission_smr, water,
#   nickel, port_ownership, lithium, copper, niobium, balsa, power_plants_grid,
#   building_materials, rail, engineering_epc (dense prior + country×subcat;
#   Liwathon oil terminal out of scope; Corentyne Bridge unsigned).
# Active after cycle 99: us235 / prc229 / allied233 / other37 (n=734).
shuffle_seed: 20261099
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- energy/other_renewables
- resources/graphite
- infrastructure/port_cranes
- energy/wind
- energy/fission_smr
- resources/water
- resources/nickel
- infrastructure/port_ownership
- energy/solar
- resources/lithium
- resources/copper
- resources/niobium
- resources/balsa
- energy/power_plants_grid
- infrastructure/building_materials
- infrastructure/rail
- infrastructure/engineering_epc
rows_found_this_cycle:
  infrastructure/bridges_roads: 5
  energy/other_renewables: 0
  resources/graphite: 0
  infrastructure/port_cranes: 1
  energy/wind: 0
  energy/fission_smr: 0
  resources/water: 0
  resources/nickel: 0
  infrastructure/port_ownership: 0
  energy/solar: 1
  resources/lithium: 0
  resources/copper: 0
  resources/niobium: 0
  resources/balsa: 0
  energy/power_plants_grid: 0
  infrastructure/building_materials: 0
  infrastructure/rail: 0
  infrastructure/engineering_epc: 0
rows_by_side_this_cycle:
  us: 6
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 98 (seed 20261098) ===
# Shuffled order: lithium, nickel, power_plants_grid, rail, balsa, fission_smr,
#   graphite, bridges_roads, water, niobium, engineering_epc, other_renewables,
#   wind, port_cranes, solar, building_materials, port_ownership, copper.
# Logged 7 sourced rows (honest US/PRC split; no padding):
#   us bridges_roads: fhwa_lpc_pr144_ciales_2024 (USD 7.21m FHWA).
#   us bridges_roads: fhwa_obratec_barranquitas_2024 (USD 8.25m FHWA).
#   us bridges_roads: fhwa_lpc_utuado_46slides_2023 (USD 41.12m FHWA).
#   us bridges_roads: fhwa_novel_ciales_multi_2023 (USD 15.51m FHWA).
#   us bridges_roads: fhwa_professional_stx_bridges_2023 (USD 4.77m FHWA USVI).
#   prc bridges_roads: boc_demerara_bridge_loan_160p8m_eur_2022 (EUR 160.8m BOC).
#   us rail: ustda_honduras_interoceanic_rail_2026 (USTDA feasibility; no CapEx).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/niobium/
#   building_materials also dry.
# Equal-budget misses: lithium, nickel, power_plants_grid, balsa, fission_smr,
#   graphite, water, niobium, engineering_epc, other_renewables, wind,
#   port_cranes, solar, building_materials, port_ownership, copper (dense prior
#   + country×subcat; Corentyne Bridge unsigned financing; Coca Codo O&M
#   unsigned; El Sillar/Rurrenabaque AidData commitments pre-2021).
# Active after cycle 98: us229 / prc228 / allied233 / other37 (n=727).
shuffle_seed: 20261098
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/lithium
- resources/nickel
- energy/power_plants_grid
- infrastructure/rail
- resources/balsa
- energy/fission_smr
- resources/graphite
- infrastructure/bridges_roads
- resources/water
- resources/niobium
- infrastructure/engineering_epc
- energy/other_renewables
- energy/wind
- infrastructure/port_cranes
- energy/solar
- infrastructure/building_materials
- infrastructure/port_ownership
- resources/copper
rows_found_this_cycle:
  resources/lithium: 0
  resources/nickel: 0
  energy/power_plants_grid: 0
  infrastructure/rail: 1
  resources/balsa: 0
  energy/fission_smr: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 6
  resources/water: 0
  resources/niobium: 0
  infrastructure/engineering_epc: 0
  energy/other_renewables: 0
  energy/wind: 0
  infrastructure/port_cranes: 0
  energy/solar: 0
  infrastructure/building_materials: 0
  infrastructure/port_ownership: 0
  resources/copper: 0
rows_by_side_this_cycle:
  us: 6
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel

# === Cycle 97 (seed 20261097) ===
# Shuffled order: wind, lithium, solar, fission_smr, niobium, port_cranes,
#   copper, building_materials, graphite, rail, balsa, port_ownership,
#   nickel, water, other_renewables, bridges_roads, engineering_epc,
#   power_plants_grid.
# Logged 5 sourced rows (honest US/PRC split; no padding):
#   us bridges_roads: fhwa_maglez_pr108_2025 (USD 20.16m FHWA).
#   us bridges_roads: fhwa_lpc_pr1_pr10_adjuntas_2026 (USD 10.75m FHWA).
#   us bridges_roads: fhwa_caribbean_sign_pr_er27_2026 (USD 14.97m FHWA).
#   us bridges_roads: fhwa_jc_associates_pr_er16_2026 (USD 13.30m FHWA).
#   prc bridges_roads: chexim_guyana_east_coast_192m_2022 (USD 192m CHEXIM).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/niobium/
#   building_materials also dry.
# Equal-budget misses: wind, lithium, solar, fission_smr, niobium, port_cranes,
#   copper, building_materials, graphite, rail, balsa, port_ownership, nickel,
#   water, other_renewables, engineering_epc, power_plants_grid (dense prior +
#   country×subcat sweep; Vestas Esquina / Goldwind Sento Sé / CMOC Cangrejos /
#   Sinoma Cibao / Sungrow Observatorio already logged; Amaila unsigned;
#   fertilizer Pampa out of scope).
# Active after cycle 97: us224 / prc227 / allied233 / other37 (n=721).
shuffle_seed: 20261097
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/wind
- resources/lithium
- energy/solar
- energy/fission_smr
- resources/niobium
- infrastructure/port_cranes
- resources/copper
- infrastructure/building_materials
- resources/graphite
- infrastructure/rail
- resources/balsa
- infrastructure/port_ownership
- resources/nickel
- resources/water
- energy/other_renewables
- infrastructure/bridges_roads
- infrastructure/engineering_epc
- energy/power_plants_grid
rows_found_this_cycle:
  energy/wind: 0
  resources/lithium: 0
  energy/solar: 0
  energy/fission_smr: 0
  resources/niobium: 0
  infrastructure/port_cranes: 0
  resources/copper: 0
  infrastructure/building_materials: 0
  resources/graphite: 0
  infrastructure/rail: 0
  resources/balsa: 0
  infrastructure/port_ownership: 0
  resources/nickel: 0
  resources/water: 0
  energy/other_renewables: 0
  infrastructure/bridges_roads: 5
  infrastructure/engineering_epc: 0
  energy/power_plants_grid: 0
rows_by_side_this_cycle:
  us: 4
  prc: 1
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel
  # Misses: all three dry. Spare to fission_smr/niobium/building_materials also dry.
coverage_cumulative:

# === Cycle 96 (seed 20261096) ===
# Shuffled order: bridges_roads, copper, power_plants_grid, water, nickel,
#   building_materials, fission_smr, lithium, niobium, balsa, wind,
#   other_renewables, port_ownership, port_cranes, solar, rail, graphite,
#   engineering_epc.
# Logged 5 sourced rows (honest US/PRC/allied split; no padding):
#   prc bridges_roads: crbc_lima_canta_highway_2025 (S/86.45m PROVIAS).
#   us bridges_roads: fhwa_novel_pr155_morovis_2024 (USD 12.05m FHWA).
#   us bridges_roads: fhwa_ddd_dvg_canovanas_2026 (USD 35.84m FHWA).
#   allied water: acciona_cagepa_paraiba_498m_eur_2026 (EUR 498m PPP).
#   prc lithium: yahua_grandchen_bandeira_offtake_2026 (USD 20m prepay).
# Thin top-up (balsa/graphite/nickel): all dry — shift to fission_smr/niobium miss.
# Equal-budget misses: copper, power_plants_grid, nickel, building_materials,
#   fission_smr, niobium, balsa, wind, other_renewables, port_ownership,
#   port_cranes, solar, rail, graphite, engineering_epc (dense prior +
#   country×subcat sweep; Mirador/SolGold/Batuco already logged; Corentyne
#   bridge unsigned; Cameron County TX out of LAC scope).
# Active after cycle 96: us220 / prc226 / allied233 / other37 (n=716).
shuffle_seed: 20261096
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/bridges_roads
- resources/copper
- energy/power_plants_grid
- resources/water
- resources/nickel
- infrastructure/building_materials
- energy/fission_smr
- resources/lithium
- resources/niobium
- resources/balsa
- energy/wind
- energy/other_renewables
- infrastructure/port_ownership
- infrastructure/port_cranes
- energy/solar
- infrastructure/rail
- resources/graphite
- infrastructure/engineering_epc
rows_found_this_cycle:
  infrastructure/bridges_roads: 3
  resources/copper: 0
  energy/power_plants_grid: 0
  resources/water: 1
  resources/nickel: 0
  infrastructure/building_materials: 0
  energy/fission_smr: 0
  resources/lithium: 1
  resources/niobium: 0
  resources/balsa: 0
  energy/wind: 0
  energy/other_renewables: 0
  infrastructure/port_ownership: 0
  infrastructure/port_cranes: 0
  energy/solar: 0
  infrastructure/rail: 0
  resources/graphite: 0
  infrastructure/engineering_epc: 0
rows_by_side_this_cycle:
  us: 2
  prc: 2
  allied: 1
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel
  # Misses: all three dry. Spare to fission_smr/niobium also dry.
coverage_cumulative:
  energy/fission_smr: 24
  energy/other_renewables: 53
  energy/power_plants_grid: 63
  energy/solar: 70
  energy/wind: 36
  infrastructure/bridges_roads: 42
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 81
  infrastructure/port_cranes: 35
  infrastructure/port_ownership: 35
  infrastructure/rail: 40
  resources/balsa: 23
  resources/copper: 33
  resources/graphite: 23
  resources/lithium: 35
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 41

# === Cycle 95 (seed 20261095) ===
# Shuffled order: wind, solar, other_renewables, building_materials, nickel,
#   rail, balsa, port_ownership, engineering_epc, bridges_roads, water,
#   fission_smr, lithium, copper, port_cranes, power_plants_grid, niobium,
#   graphite.
# Logged 4 sourced rows (honest US/PRC/allied split; no padding):
#   allied wind: cox_santa_cruz_wind_panama_2026 (68.4 MW; CapEx blank PPA).
#   us solar: first_solar_zacapa_exim_guatemala_2021 (USD 8.7m EXIM).
#   allied other_renewables: maspv_estanzuela_guatemala_2026 (>USD 100m proxy).
#   prc port_cranes: zpmc_cct_hybrid_rtg_panama_2024 (USD 23m proxy).
# Thin top-up (balsa/graphite/nickel): all dry — fission_smr already filled C94.
# Equal-budget misses: building_materials, nickel, rail, balsa, port_ownership,
#   engineering_epc, bridges_roads, water, fission_smr, lithium, copper,
#   power_plants_grid, niobium, graphite (dense prior + country×subcat sweep;
#   Vestas Las Pavas / Sungrow IRESA lacked openable non-paywalled primaries).
# Active after cycle 95: us218 / prc224 / allied232 / other37 (n=711).
shuffle_seed: 20261095
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/wind
- energy/solar
- energy/other_renewables
- infrastructure/building_materials
- resources/nickel
- infrastructure/rail
- resources/balsa
- infrastructure/port_ownership
- infrastructure/engineering_epc
- infrastructure/bridges_roads
- resources/water
- energy/fission_smr
- resources/lithium
- resources/copper
- infrastructure/port_cranes
- energy/power_plants_grid
- resources/niobium
- resources/graphite
rows_found_this_cycle:
  energy/wind: 1
  energy/solar: 1
  energy/other_renewables: 1
  infrastructure/building_materials: 0
  resources/nickel: 0
  infrastructure/rail: 0
  resources/balsa: 0
  infrastructure/port_ownership: 0
  infrastructure/engineering_epc: 0
  infrastructure/bridges_roads: 0
  resources/water: 0
  energy/fission_smr: 0
  resources/lithium: 0
  resources/copper: 0
  infrastructure/port_cranes: 1
  energy/power_plants_grid: 0
  resources/niobium: 0
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 1
  prc: 1
  allied: 2
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel
  # Misses: all three dry. Spare to fission_smr already hit prior cycle.
coverage_cumulative:
  energy/fission_smr: 24
  energy/other_renewables: 53
  energy/power_plants_grid: 63
  energy/solar: 70
  energy/wind: 36
  infrastructure/bridges_roads: 39
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 81
  infrastructure/port_cranes: 35
  infrastructure/port_ownership: 35
  infrastructure/rail: 40
  resources/balsa: 23
  resources/copper: 33
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 40

# === Cycle 94 (seed 20261094) ===
# Shuffled order: niobium, fission_smr, nickel, wind, solar, other_renewables,
#   engineering_epc, bridges_roads, port_ownership, rail, graphite, balsa,
#   building_materials, lithium, copper, water, port_cranes, power_plants_grid.
# Logged 6 sourced rows (honest US/PRC/allied split; no padding):
#   prc bridges_roads: crcc_wismar_mackenzie_guyana_2024 (USD 35m DPI).
#   prc solar: danasun_choloma_solar_honduras_2024 (proxy; CapEx blank).
#   allied port_ownership: apmt_balboa_temp_panama_2026 (USD 26.1m).
#   allied port_ownership: til_cristobal_temp_panama_2026 (USD 15.8m).
#   allied fission_smr: terra_conuar_solo_argentina_2025 (thin top-up; CapEx blank).
#   us power_plants_grid: crowley_american_energy_lng_pr_2025 (CapEx blank).
# Thin top-up (balsa/graphite/nickel): dry — fission_smr hit (CONUAR×Terra).
# Equal-budget misses: niobium, nickel, wind, other_renewables, engineering_epc,
#   rail, graphite, balsa, building_materials, lithium, copper, water,
#   port_cranes (dense prior + country×subcat sweep).
# Active after cycle 94: us217 / prc223 / allied230 / other37 (n=707).
shuffle_seed: 20261094
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- energy/fission_smr
- resources/nickel
- energy/wind
- energy/solar
- energy/other_renewables
- infrastructure/engineering_epc
- infrastructure/bridges_roads
- infrastructure/port_ownership
- infrastructure/rail
- resources/graphite
- resources/balsa
- infrastructure/building_materials
- resources/lithium
- resources/copper
- resources/water
- infrastructure/port_cranes
- energy/power_plants_grid
rows_found_this_cycle:
  resources/niobium: 0
  energy/fission_smr: 1
  resources/nickel: 0
  energy/wind: 0
  energy/solar: 1
  energy/other_renewables: 0
  infrastructure/engineering_epc: 0
  infrastructure/bridges_roads: 1
  infrastructure/port_ownership: 2
  infrastructure/rail: 0
  resources/graphite: 0
  resources/balsa: 0
  infrastructure/building_materials: 0
  resources/lithium: 0
  resources/copper: 0
  resources/water: 0
  infrastructure/port_cranes: 0
  energy/power_plants_grid: 1
rows_by_side_this_cycle:
  us: 1
  prc: 2
  allied: 3
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/graphite
  - resources/nickel
  # Misses: balsa/graphite/nickel dry. Spare half-budget to fission_smr hit (CONUAR×Terra).
coverage_cumulative:
  energy/fission_smr: 24
  energy/other_renewables: 52
  energy/power_plants_grid: 63
  energy/solar: 69
  energy/wind: 35
  infrastructure/bridges_roads: 39
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 81
  infrastructure/port_cranes: 34
  infrastructure/port_ownership: 35
  infrastructure/rail: 40
  resources/balsa: 23
  resources/copper: 33
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 40

# === Cycle 93 (seed 20261093) ===
# Shuffled order: niobium, water, nickel, building_materials, graphite, solar,
#   rail, bridges_roads, port_ownership, balsa, engineering_epc, copper,
#   port_cranes, fission_smr, lithium, power_plants_grid, wind, other_renewables.
# Logged 4 sourced rows (honest US/PRC split; no padding):
#   us power_plants_grid: quanta_luma_dist_525m_2025 (USD 525m FOMB IDIQ).
#   prc port_cranes: zpmc_kingston_sts_2025 (two post-Panamax STS; CapEx blank).
#   prc bridges_roads: chec_sucre_yamparaez_bolivia_2025 (CHEC; CapEx blank).
#   prc other_renewables: huawei_aggreko_amazonas_bess_2026 (proxy ESS News; CapEx blank).
# Thin top-up (fission_smr/balsa/graphite): all dry — shift to nickel then miss.
#   Next-thinnest niobium dry.
# Equal-budget misses: niobium, water, nickel, building_materials, graphite,
#   solar, rail, port_ownership, balsa, engineering_epc, copper, fission_smr,
#   lithium, wind (dense prior + country×subcat sweep; Aguadulce/ICAVE/
#   Montego Bay already logged).
# Active after cycle 93: us216 / prc221 / allied227 / other37 (n=701).
shuffle_seed: 20261093
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/niobium
- resources/water
- resources/nickel
- infrastructure/building_materials
- resources/graphite
- energy/solar
- infrastructure/rail
- infrastructure/bridges_roads
- infrastructure/port_ownership
- resources/balsa
- infrastructure/engineering_epc
- resources/copper
- infrastructure/port_cranes
- energy/fission_smr
- resources/lithium
- energy/power_plants_grid
- energy/wind
- energy/other_renewables
rows_found_this_cycle:
  resources/niobium: 0
  resources/water: 0
  resources/nickel: 0
  infrastructure/building_materials: 0
  resources/graphite: 0
  energy/solar: 0
  infrastructure/rail: 0
  infrastructure/bridges_roads: 1
  infrastructure/port_ownership: 0
  resources/balsa: 0
  infrastructure/engineering_epc: 0
  resources/copper: 0
  infrastructure/port_cranes: 1
  energy/fission_smr: 0
  resources/lithium: 0
  energy/power_plants_grid: 1
  energy/wind: 0
  energy/other_renewables: 1
rows_by_side_this_cycle:
  us: 1
  prc: 3
  allied: 0
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - energy/fission_smr
  - resources/balsa
  - resources/graphite
  # Misses: all three dry (dense prior). Spare half-budgets to nickel then miss.
coverage_cumulative:
  energy/fission_smr: 23
  energy/other_renewables: 52
  energy/power_plants_grid: 62
  energy/solar: 68
  energy/wind: 35
  infrastructure/bridges_roads: 38
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 81
  infrastructure/port_cranes: 34
  infrastructure/port_ownership: 33
  infrastructure/rail: 40
  resources/balsa: 23
  resources/copper: 33
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 40

# === Cycle 92 (seed 20261092) ===
# Shuffled order: lithium, engineering_epc, copper, solar, niobium, port_cranes,
#   nickel, building_materials, fission_smr, other_renewables, bridges_roads,
#   power_plants_grid, balsa, wind, graphite, water, port_ownership, rail.
# Logged 6 sourced rows (honest US/PRC split; no padding):
#   us power_plants_grid: ctdc_hostos_hvdc_dr_pr_2026 (USD 2.5bn CTDC/Atabey).
#   prc engineering_epc: chexim_bndes_fund_600m_2025 (~USD 600m CEXIM; proxy).
#   prc wind: goldwind_jacobina_02_04_tsi_2025 (TSI; CapEx blank).
#   prc wind: goldwind_jacobina_05_tsi_2026 (TSI; CapEx blank).
#   us rail: wabtec_transap_c30aci_chile_2025 (four C30ACi).
#   prc solar: seraphim_spic_zuma_module_replace_2025 (12 MW replacement).
# Thin top-up (fission_smr/balsa/graphite): all dry — shift to nickel then miss.
#   Next-thinnest niobium dry.
# Equal-budget misses: lithium, copper, niobium, port_cranes, nickel,
#   building_materials, fission_smr, other_renewables, bridges_roads, balsa,
#   graphite, water, port_ownership (dense prior + country×subcat sweep).
# Active after cycle 92: us215 / prc218 / allied227 / other37 (n=697).
shuffle_seed: 20261092
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/lithium
- infrastructure/engineering_epc
- resources/copper
- energy/solar
- resources/niobium
- infrastructure/port_cranes
- resources/nickel
- infrastructure/building_materials
- energy/fission_smr
- energy/other_renewables
- infrastructure/bridges_roads
- energy/power_plants_grid
- resources/balsa
- energy/wind
- resources/graphite
- resources/water
- infrastructure/port_ownership
- infrastructure/rail
rows_found_this_cycle:
  resources/lithium: 0
  infrastructure/engineering_epc: 1
  resources/copper: 0
  energy/solar: 1
  resources/niobium: 0
  infrastructure/port_cranes: 0
  resources/nickel: 0
  infrastructure/building_materials: 0
  energy/fission_smr: 0
  energy/other_renewables: 0
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 1
  resources/balsa: 0
  energy/wind: 2
  resources/graphite: 0
  resources/water: 0
  infrastructure/port_ownership: 0
  infrastructure/rail: 1
rows_by_side_this_cycle:
  us: 2
  prc: 4
  allied: 0
  other: 0
coverage_cumulative:
  energy/fission_smr: 23
  energy/other_renewables: 51
  energy/power_plants_grid: 61
  energy/solar: 68
  energy/wind: 35
  infrastructure/bridges_roads: 37
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 81

# === Cycle 91 (seed 20261091) ===
# Shuffled order: fission_smr, solar, wind, building_materials, balsa, nickel,
#   lithium, copper, niobium, engineering_epc, other_renewables, bridges_roads,
#   port_ownership, rail, power_plants_grid, port_cranes, water, graphite.
# Logged 6 sourced rows (honest US/PRC split; no padding):
#   prc water: cwe_zapallar_embalse_chile_2026 (~USD 158m MOP).
#   us other_renewables: solarmax_pr_bess_epc_158m_2025 (USD 158.2m SEC 8-K).
#   us other_renewables: stem_granja_powertrack_ems_chile_2026 (EMS; USD blank).
#   us engineering_epc: cbi_vmos_punta_colorada_storage_2025 (significant band).
#   prc other_renewables: trina_luz_del_norte_bess_722mwh_2026 (141 MW/722 MWh).
#   prc other_renewables: trina_alma_sur_bess_481mwh_2026 (90 MW/481 MWh).
# Thin top-up (fission_smr/balsa/graphite): all dry — shift to nickel then miss
#   (DFC Piauí already). Next-thinnest niobium dry.
# Equal-budget misses: fission_smr, solar, wind, building_materials, balsa,
#   nickel, lithium, copper, niobium, bridges_roads, port_ownership, rail,
#   power_plants_grid, port_cranes, graphite (dense prior + country×subcat sweep).
# Active after cycle 91: us213 / prc214 / allied227 / other37 (n=691).
shuffle_seed: 20261091
budget_per_subcategory: 1_source_family_min
shuffled_order:
- energy/fission_smr
- energy/solar
- energy/wind
- infrastructure/building_materials
- resources/balsa
- resources/nickel
- resources/lithium
- resources/copper
- resources/niobium
- infrastructure/engineering_epc
- energy/other_renewables
- infrastructure/bridges_roads
- infrastructure/port_ownership
- infrastructure/rail
- energy/power_plants_grid
- infrastructure/port_cranes
- resources/water
- resources/graphite
rows_found_this_cycle:
  energy/fission_smr: 0
  energy/solar: 0
  energy/wind: 0
  infrastructure/building_materials: 0
  resources/balsa: 0
  resources/nickel: 0
  resources/lithium: 0
  resources/copper: 0
  resources/niobium: 0
  infrastructure/engineering_epc: 1
  energy/other_renewables: 4
  infrastructure/bridges_roads: 0
  infrastructure/port_ownership: 0
  infrastructure/rail: 0
  energy/power_plants_grid: 0
  infrastructure/port_cranes: 0
  resources/water: 1
  resources/graphite: 0
rows_by_side_this_cycle:
  us: 3
  prc: 3
  allied: 0
  other: 0
coverage_cumulative:
  energy/fission_smr: 23
  energy/other_renewables: 51
  energy/power_plants_grid: 60
  energy/solar: 67
  energy/wind: 33
  infrastructure/bridges_roads: 37
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 80
  infrastructure/port_cranes: 33
  infrastructure/port_ownership: 33
  infrastructure/rail: 39
  resources/balsa: 23
  resources/copper: 33
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 40
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - energy/fission_smr
  - resources/balsa
  - resources/graphite
  # Misses: all three dry (dense prior). Spare half-budgets to nickel then miss.

# === Cycle 90 (seed 20261090) ===
# Shuffled order: nickel, copper, building_materials, bridges_roads,
#   engineering_epc, fission_smr, lithium, other_renewables, niobium,
#   port_ownership, rail, solar, power_plants_grid, water, graphite, wind,
#   port_cranes, balsa.
# Logged 6 sourced rows (honest US/PRC split; no padding):
#   prc bridges_roads: crbc_ebd_good_success_timehri_2024 (USD 75.89m MoPW).
#   us engineering_epc: sheladia_ebd_supervision_2023 (USD 7.967m MoPW).
#   allied power_plants_grid: engie_peru_grupo1_transmision_230m_2026 (USD 230.8m).
#   us power_plants_grid: mcc_belize_energy_ambergris_41p7m_2024 (USD 41.7m).
#   prc solar: ja_solar_exel_400mw_mexico_2026 (400 MW Exel modules).
#   prc wind: mingyang_copel_brazil_wind_2024 (240 MW PSA + Copel MySE).
# Thin top-up (fission_smr/balsa/graphite): all dry — shift to nickel then miss
#   (DFC Piauí already). Next-thinnest niobium dry.
# Equal-budget misses: nickel, copper, building_materials, fission_smr, lithium,
#   other_renewables, niobium, port_ownership, rail, water, graphite,
#   port_cranes, balsa (dense prior + country×subcat sweep).
# Active after cycle 90: us210 / prc211 / allied227 / other37 (n=685).
shuffle_seed: 20261090
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/nickel
- resources/copper
- infrastructure/building_materials
- infrastructure/bridges_roads
- infrastructure/engineering_epc
- energy/fission_smr
- resources/lithium
- energy/other_renewables
- resources/niobium
- infrastructure/port_ownership
- infrastructure/rail
- energy/solar
- energy/power_plants_grid
- resources/water
- resources/graphite
- energy/wind
- infrastructure/port_cranes
- resources/balsa
rows_found_this_cycle:
  resources/nickel: 0
  resources/copper: 0
  infrastructure/building_materials: 0
  infrastructure/bridges_roads: 1
  infrastructure/engineering_epc: 1
  energy/fission_smr: 0
  resources/lithium: 0
  energy/other_renewables: 0
  resources/niobium: 0
  infrastructure/port_ownership: 0
  infrastructure/rail: 0
  energy/solar: 1
  energy/power_plants_grid: 2
  resources/water: 0
  resources/graphite: 0
  energy/wind: 1
  infrastructure/port_cranes: 0
  resources/balsa: 0
rows_by_side_this_cycle:
  us: 2
  prc: 3
  allied: 1
  other: 0
coverage_cumulative:
  energy/fission_smr: 23
  energy/other_renewables: 47
  energy/power_plants_grid: 60
  energy/solar: 67
  energy/wind: 33
  infrastructure/bridges_roads: 37
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 79
  infrastructure/port_cranes: 33
  infrastructure/port_ownership: 33
  infrastructure/rail: 39
  resources/balsa: 23
  resources/copper: 33
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 39
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - energy/fission_smr
  - resources/balsa
  - resources/graphite
  # Misses: all three dry (dense prior). Spare half-budgets to nickel then miss.

# === Cycle 89 (seed 20261089) ===
# Shuffled order: port_cranes, graphite, solar, niobium, lithium,
#   power_plants_grid, water, engineering_epc, building_materials, copper,
#   other_renewables, nickel, balsa, wind, rail, fission_smr, port_ownership,
#   bridges_roads.
# Logged 7 sourced rows (honest US/PRC split; no padding):
#   prc port_cranes: zpmc_contecon_manzanillo_sts_rtg_2026 (STS #13–14 + 5 RTG).
#   us solar: aes_dr_peravia_140mw_cod_2025 (140 MW Baní COD Sep 2025).
#   us water: nadbank_san_quintin_desal_665m_mxn_2026 (proposed MXN 665m).
#   allied water: gs_inima_espirito_santo_lot_a_2025 (>EUR 150m Lot A).
#   other copper: southern_copper_tia_maria_notes_1p25bn_2026 (USD 1.25bn notes).
#   us copper: dfc_cerro_pasco_quiulacocha_5m_2026 (USD 5m project-dev).
#   prc wind: sany_purranque_18mw_chile_2026 (first LatAm SANY wind).
# Thin top-up (fission_smr/balsa/graphite): all dry — shift to nickel then miss
#   (DFC Piauí already). Next-thinnest niobium dry.
# Equal-budget misses: graphite, niobium, lithium, power_plants_grid,
#   engineering_epc, building_materials, other_renewables, nickel, balsa, rail,
#   fission_smr, port_ownership, bridges_roads (dense prior coverage).
# Active after cycle 89: us208 / prc208 / allied226 / other37 (n=679).

# === Cycle 88 (seed 20261088) ===
# Shuffled order: port_cranes, solar, niobium, fission_smr, balsa, rail,
#   other_renewables, water, power_plants_grid, copper, port_ownership,
#   bridges_roads, wind, engineering_epc, nickel, lithium, graphite,
#   building_materials.
# Logged 6 sourced rows (honest US/PRC split; no padding):
#   us solar: atlas_latam_3bn_refi_2026 (USD 3bn GIP-backed Miami HQ refinancing);
#     dfc_solaramo_manta_200mw_ecuador (proposed USD 144m / 200 MW near Manta).
#   prc other_renewables: sungrow_sonnedix_librillo_bess_2026 (643.8 MWh Taltal);
#     sungrow_verano_observatorio_bess_2026 (152 MW/606 MWh Marchigüe).
#   prc wind: powerchina_jiangxi_ingenio_wind_epc_2025 (2×1.5 MW Oaxaca retrofit).
#   prc bridges_roads: crbc_corentyne_lot2_guyana_2026 (GYD >2.9bn Lot 2).
# Thin top-up (fission_smr/balsa/graphite): all dry — shift to nickel then miss
#   (DFC Piauí / Fenix / Corex / MMG already dense). Next-thinnest niobium dry.
# Equal-budget misses: port_cranes, niobium, fission_smr, balsa, rail, water,
#   power_plants_grid, copper, port_ownership, engineering_epc, nickel, lithium,
#   graphite, building_materials (dense prior coverage).
# Active after cycle 88: us205 / prc206 / allied225 / other36 (n=672).
rows_by_side_this_cycle:
  us: 2
  prc: 4
  allied: 0
  other: 0
coverage_cumulative:
  energy/fission_smr: 23
  energy/other_renewables: 47
  energy/power_plants_grid: 58
  energy/solar: 65
  energy/wind: 31
  infrastructure/bridges_roads: 36
  infrastructure/building_materials: 32
  infrastructure/engineering_epc: 78
  infrastructure/port_cranes: 32
  infrastructure/port_ownership: 33
  infrastructure/rail: 39
  resources/balsa: 23
  resources/copper: 31
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 37

# === Cycle 88 PRE-STEP: scope audit (2026-10-02) ===
# Archive hospital / school / fertilizer rows that are not in the BRIEF 18
# subcategories (building_materials = cement/aggregates; engineering_epc =
# non-grid EPC for listed layers — not social infrastructure or fertilizer).
# Gold/silver/auto/digital already archived in cycle 86 pre-step (23 rows).
#
# scope_audit_archived_total: 13
# scope_audit_by_side:
#   us: 1
#   prc: 12
#   allied: 0
#   other: 0
# scope_audit_by_subcategory:
#   infrastructure/building_materials: 10
#   infrastructure/engineering_epc: 3
# scope_audit_examples:
#   hospital: sinohydro_hospital_piura_3202m_pen_2025; sinohydro_hospital_la_caleta_chimbote_549m_pen_2025;
#     powerchina_montenegro_hospital_lima_2025; camce_sinopharm_west_dem_hospital_guyana_2025;
#     crcc_illapel/coquimbo/neurocirugia/ohiggins; crbc_red_maule_hospitals
#   school: chec_taltal_school_chile_2026
#   fertilizer: powerchina_ufn3 / ufn_iii_tres_lagoas; kbr_pampa_bahia_blanca_ammonia
# Post-audit active sides before hunt: us203 / prc202 / allied225 / other36 (n=666).
# Thinnest after archive: fission_smr/balsa/graphite (23) then nickel (24).

# Per-cycle shuffle (BRIEF.md):
# (1) Seeded shuffle of all 18 subcategories; equal base budget per subcategory.
# (2) Side balance (from cycle 64): within each subcategory time box, split budget
#     evenly between U.S. and PRC sources (U.S. push has worked). U.S.: EDGAR/DFC/
#     EXIM/USTDA/company/embassy/Commerce + ES/PT coverage. PRC: MOFCOM, SOE/company
#     releases, CDB/CHEXIM, BU Chinese Loans to LAC, AidData, Diálogo Chino,
#     Red ALC-China, ES/PT press. Log rows_by_side_this_cycle.
# (3) Thin-subcategory top-up: after the shuffled pass, the 3 subcategories with
#     the fewest active rows (recompute each cycle) each get one extra half-budget.

# === Cycle 86 PRE-STEP: scope audit (2026-10-02) ===
# Checked every active row against BRIEF.md 18-subcategory definitions.
# Archived status=archived with note marker "out_of_scope" when the asset was
# not actually a port/crane/rail/bridge-road/building-materials/infra-or-energy
# EPC / niobium/lithium/copper/nickel/graphite/balsa/water / fission-SMR/solar/
# wind/power-plants-grid/other-renewables. Generic manufacturing, autos,
# consumer goods, health devices, fintech/telecom, data centers, and non-list
# minerals (gold/silver/REE) archived even if they held US/PRC balance.
#
# scope_audit_archived_total: 23
# scope_audit_by_side:
#   us: 16
#   prc: 4
#   allied: 3
#   other: 0
# scope_audit_by_subcategory:
#   infrastructure/engineering_epc: 23
# scope_audit_examples:
#   us: gm_brazil_additional_3p5bn_brl_2026 (autos); abbott_queretaro_ep_plant_200m_2026
#       (medical devices); dfc_tembici_15m_equity_2023 (bike-share); cummins_monterrey_*
#       (auto parts); john_deere_canoas_* / agco_jundiai_reman (ag equipment);
#       cloudhq_queretaro / ustda_atlantico_datacenter / ustda_cocesna_cyber /
#       dfc_vtal_fiber (digital/telecom); dfc_serra_verde (REE); fluor_salares_norte /
#       m3_vizsla_panuco (gold/silver EPCM); flowserve_torreon (generic mfg)
#   prc: gwm_iracemapolis_4bn_brl_2025; geely_renault_brasil_3p8bn_brl_2025;
#        byd_camacari_ev_complex_5p5bn_2025 (auto/EV assembly);
#        cmoc_equinox_brazil_gold_1p015bn_2026 (gold)
#   allied: sedgman_colossus_epcm_2026 (REE); worley_diablillos_abrasilver_2026;
#           lycopodium_san_cristobal_epcm_2026 (silver)
# Kept: CSGI Enel Distribución Perú (power_plants_grid); cement/hospital/housing
# construction under building_materials; oil/gas/mining EPC tied to listed
# resources or energy; port/airport/rail EPC.
# Post-audit active sides before hunt: us199 / prc208 / allied222 / other36 (n=665).

# Side-tag audit — cycle 87:
# - Freeport renewable PPAs tagged us (Phoenix HQ). Sinohydro/CHEC tagged prc.
# - Zelestra San Martín tagged allied (Spanish/EQT). ENGIE Tocopilla COD tagged allied.
# - Thin top-up: fission_smr / balsa / graphite dry (existing dense coverage; no new
#   distinct US/PRC rows). Spare half-budgets moved to water (CHEC Las Palmas) and
#   building_materials (Sinohydro hospitals) rather than repeating dry thin searches.
# - Skipped Fluor Chile copper CM (mine unnamed). Skipped Falcondo (concession
#   termination, not investment). Skipped CNMC Taboca (tin primary — out_of_scope).

shuffle_seed: 20261087
budget_per_subcategory: 1_source_family_min

shuffled_order:
- resources/copper
- energy/wind
- infrastructure/bridges_roads
- resources/lithium
- infrastructure/engineering_epc
- energy/solar
- infrastructure/port_cranes
- resources/balsa
- resources/nickel
- energy/other_renewables
- infrastructure/building_materials
- energy/power_plants_grid
- energy/fission_smr
- resources/water
- infrastructure/rail
- infrastructure/port_ownership
- resources/niobium
- resources/graphite

rows_found_this_cycle:
  resources/copper: 1
  energy/wind: 0
  infrastructure/bridges_roads: 0
  resources/lithium: 0
  infrastructure/engineering_epc: 0
  energy/solar: 1
  infrastructure/port_cranes: 0
  resources/balsa: 0
  resources/nickel: 0
  energy/other_renewables: 1
  infrastructure/building_materials: 2
  energy/power_plants_grid: 0
  energy/fission_smr: 0
  resources/water: 1
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  resources/niobium: 0
  resources/graphite: 0

coverage_cumulative:
  # Active counts after cycle 87 (status=active)
  energy/fission_smr: 23
  energy/other_renewables: 45
  energy/power_plants_grid: 58
  energy/solar: 63
  energy/wind: 30
  infrastructure/bridges_roads: 35
  infrastructure/building_materials: 42
  infrastructure/engineering_epc: 81
  infrastructure/port_cranes: 32
  infrastructure/port_ownership: 33
  infrastructure/rail: 39
  resources/balsa: 23
  resources/copper: 31
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 37

rows_by_side_this_cycle:
  us: 1
  prc: 3
  allied: 2
  other: 0

thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - energy/fission_smr
  - resources/balsa
  - resources/graphite
  # Misses: fission_smr (Meitner/CAREM/Angra/Laguna Verde/FIRST already logged);
  #   balsa (Plantabal/Gurit/DIAB/CoreLite dense); graphite (Graphcoa/Atlas dense).
  # Reallocated half-budgets to next workable openings: water (CHEC Las Palmas) and
  #   building_materials second Sinohydro hospital (La Caleta), already counted above.

# Cycle 87 (seed 20261087): 6 sourced rows — Freeport Cerro Verde/El Abra renewable
#   PPAs (us copper); Sinohydro Piura hospital S/3.202bn + La Caleta Chimbote >S/549m
#   (prc building_materials); CHEC Embalse Las Palmas USD 158.8m (prc water);
#   Zelestra San Martín COD USD 179.7m (allied solar); ENGIE BESS Tocopilla COD
#   USD 170m (allied other_renewables). Honest US/PRC imbalance (1/3); no padding.
# Active after cycle 87: us204 / prc214 / allied225 / other36 (n=679).


# Side-tag audit — cycle 86:
# - Fenix Nickel tagged us (New York LLC HQ). Weatherford / EXIM / McDermott tagged us.
# - Sungrow / POWERCHINA tagged prc. CoreX Cerro Matoso tagged allied (Turkish HQ).
# - Pumpco Argentina LNG value fill >USD 1bn from State fact sheet (proxy).
# - Skipped CMOC Cangrejos (gold primary — out_of_scope). Skipped NADBank Texas WRF
#   (United States host). Thin balsa/fission_smr miss; nickel hit (Fenix + CoreX).

shuffle_seed: 20261086
budget_per_subcategory: 1_source_family_min

shuffled_order:
- energy/solar
- energy/other_renewables
- infrastructure/engineering_epc
- resources/balsa
- infrastructure/port_ownership
- energy/fission_smr
- infrastructure/building_materials
- infrastructure/port_cranes
- resources/copper
- infrastructure/bridges_roads
- energy/power_plants_grid
- energy/wind
- resources/water
- resources/nickel
- resources/niobium
- resources/lithium
- infrastructure/rail
- resources/graphite

rows_found_this_cycle:
  energy/solar: 2
  energy/other_renewables: 1
  infrastructure/engineering_epc: 3
  resources/balsa: 0
  infrastructure/port_ownership: 0
  energy/fission_smr: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  resources/copper: 0
  infrastructure/bridges_roads: 0
  energy/power_plants_grid: 0
  energy/wind: 0
  resources/water: 0
  resources/nickel: 2
  resources/niobium: 0
  resources/lithium: 0
  infrastructure/rail: 0
  resources/graphite: 0

coverage_cumulative:
  # Active counts after cycle 86 (status=active)
  energy/fission_smr: 23
  energy/other_renewables: 44
  energy/power_plants_grid: 58
  energy/solar: 62
  energy/wind: 30
  infrastructure/bridges_roads: 35
  infrastructure/building_materials: 40
  infrastructure/engineering_epc: 81
  infrastructure/port_cranes: 32
  infrastructure/port_ownership: 33
  infrastructure/rail: 39
  resources/balsa: 23
  resources/copper: 30
  resources/graphite: 23
  resources/lithium: 34
  resources/nickel: 24
  resources/niobium: 26
  resources/water: 36

rows_by_side_this_cycle:
  us: 4
  prc: 3
  allied: 1
  other: 0

thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/nickel
  - resources/balsa
  - energy/fission_smr
  # Hits: nickel (Fenix Guatemala us + CoreX Cerro Matoso allied).
  # Misses: balsa (Plantabal/Gurit/DIAB already dense; no new distinct US/PRC
  #   plantation/export row); fission_smr (CAREM/Meitner/Angra/Laguna Verde/
  #   CNNC/123 already logged; Angra 3 debt pause is Brazilian domestic).
  # Top-up reallocation: nickel yielded; did not burn dry repeats on balsa/
  #   fission — spare half-budget noted, not forced into next-thinnest graphite
  #   this cycle (nickel already filled both half-budgets effectively).

# Cycle 86 (seed 20261086): 8 sourced rows (6 shuffled + 2 thin_topup nickel);
#   shuffled: solar (Sungrow San Martín 273 MWac prc; POWERCHINA Mauriti 425 MW COD
#   prc); other_renewables (Sungrow SC2000UD @ ENGIE Tocopilla prc); engineering_epc
#   (Weatherford Ecopetrol 4×6y lift us; EXIM Argentina LNG USD 6bn term sheet proxy
#   us; McDermott Argentina LNG NGL EPCC us); + Pumpco pipeline >USD 1bn value fill.
#   Thin top-up nickel: Fenix El Estor USD 85m us; CoreX Cerro Matoso up-to USD 100m
#   allied. Balsa/fission miss.
#   rows_by_side: us 4 / prc 3 / allied 1 / other 0.
#   Merge --no-ff to main after build.

# Cycle 85 (seed 20261085): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (GM Brazil +R$3.5bn us; DFC Serra Verde USD 565m us;
#   Abbott Querétaro USD 200m proxy us; DFC Tembici USD 15m us; GWM Iracemápolis
#   R$4bn proxy prc; Geely Renault Brasil R$3.8bn/26.4% prc; CMOC Equinox Brazil
#   mines USD 1.015bn prc); power_plants_grid (CSGI Enel Distribución Perú
#   ~USD 3.1bn prc).
#   Thin top-up miss nickel/balsa/fission_smr. Merge --no-ff to main after build.

# Cycle 84 (seed 20261084): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (Cummins Monterrey Logistics USD 30m us; CAMCE
#   Punta Huete airport credit RMB 2.875bn AidData prc); water (NADBank Sonora
#   MXN 650m/~USD 36.2m us; NADBank SADM Monterrey USD 16.75m us; NADBank Tecate
#   Rancho La Puerta USD 5m us); bridges_roads (CAMCE Punta Huete road USD
#   71.9647m prc; CRTG Molinopampa S/273.2m proxy prc); building_materials
#   (CRBC Red Maule hospitals UF 6.634m/~USD 271.5m prc).
#   Thin top-up miss nickel/balsa/fission_smr. Merge --no-ff to main after build.

# Cycle 83 (seed 20261083): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (DFC V.tal USD 150m loan us; NADBank Engen MXN 400m/
#   ~USD 23.2m us; CloudHQ Querétaro USD 4.8bn proxy us; Cummins Monterrey ADB
#   USD 33m us; BYD Camaçari EV ~R$5.5bn proxy prc); wind (Goldwind Camaçari
#   turbine factory ~R$100m proxy prc); bridges_roads (CRCC Chillán–Collipulli
#   UF 14.215m/~USD 596m prc); solar (CEEC Coremas I–III ~R$520m EV prc).
#   Thin top-up miss nickel/balsa/fission_smr. Merge --no-ff to main after build.

# Cycle 82 (seed 20261082): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (John Deere Canoas pulverizer R$42m us; John Deere
#   Canoas electronics R$75m us; AGCO Jundiaí Reman USD 3.2m us; Flowserve Torreón
#   MXN 800m proxy us; CHEC Grenada MBIA airport prc); building_materials (CRCC
#   Coquimbo hospital UF 6.528m/~USD 274m prc; CRCC Red O’Higgins Rengo–Pichilemu
#   USD 177m prc; CRCC Instituto Nacional de Neurocirugía UF 3.509m/~USD 147m prc).
#   Thin top-up miss nickel/balsa/fission_smr. Merge --no-ff to main after build.

# Cycle 81 (seed 20261081): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: power_plants_grid (GE Vernova San Felipe DR H-Class us); building_materials
#   (CRCC Illapel hospital >CLP 132bn prc); copper (Jiangxi Copper SolGold Cascabel
#   ~GBP 867m prc); solar (POWERCHINA Suriname microgrid Phase II prc); engineering_epc
#   (NOV Hammerhead heated flex us; Oil States Petrobras subsea proxy us; Weatherford
#   Trion MPD Mexico us); wind (Goldwind Jacobina tower factory proxy prc). Thin
#   top-up miss nickel/balsa/fission_smr. Merge --no-ff to main after build.

# Cycle 80 (seed 20261080): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: bridges_roads (CRTG Abancay bypass S/93.0m prc); niobium (CNMC
#   Taboca acquisition USD 340m proxy prc); solar (CGN Piauí CSP MoU proxy prc);
#   engineering_epc (Oceaneering SSR USD 180m / umbilicals / Wayfarer ROV us;
#   SLB Búzios Wave II us; CHEC Chancay delivery prc). Thin top-up miss
#   nickel/balsa/fission_smr. Merge --no-ff to main after build.

# Cycle 79 (seed 20261079): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: bridges_roads (China Railway No.10 Chancay Tunnel prc; CRFG Guyana
#   East Coast Demerara US$184m proxy prc); building_materials (CAMCE/Sinopharm
#   West Demerara Hospital US$54.17m proxy prc; POWERCHINA Bogotá El Campín
#   stadium prc); engineering_epc (Baker Hughes Petrobras stim vessels us; 77 km
#   flex pipe us; workover/P&A us; ICM COAMO Campo Mourão biorefinery us).
#   Thin top-up miss nickel/balsa/fission_smr. Merge --no-ff to main after build.

# Cycle 78 (seed 20261078): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: bridges_roads (China Railway No.10 Piura Yapatera–Frías S/545.8m
#   prc); engineering_epc (NOV 96 km Brazil flexibles us; SLB–PETRONAS Suriname
#   SCA us; NOV Açu lease +30k m² to 2047 UNVERIFIED proxy us); power_plants_grid
#   (Excelerate Experience reliquefaction us; POWERCHINA Guyana DBIS Phase II
#   Lots I+III US$256.7m prc); building_materials (CHEC Boundbrook Urban Centre
#   J$2.8bn construction UNVERIFIED proxy prc; CHEC Northern Parcel Villa Phase I
#   CapEx blank prc).
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   thin_topup: nickel/graphite/balsa miss.

# Cycle 77 (seed 20261077): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (SLB Rio Decommissioning Center us; Baker Hughes–YPF
#   Lucida RSS/PermaFORCE 3-year us; CHEC Amador Cruise Terminal ~US$206.7m UNVERIFIED
#   prc; CHEC NMIA runway RESA US$72m UNVERIFIED prc), solar (Atlas Uruguay 76 MWp
#   sale us; SUMEC–XJ Onderneeming 5 MW / US$10.4m COD prc), other_renewables (AES
#   Andes Chile five-PF US$1.745bn us), building_materials (CHEC Lakes Pen Industrial
#   Park design-build US$20m prc).
#   Thin_topup: nickel/graphite/balsa miss.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.

# Cycle 76 (seed 20261076): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (USTDA Atlántico data-center TA us; USTDA COCESNA
#   cyber TA us; SLB–ExxonMobil Guyana Neuro/DrillOps us; CHEC Impro Mexico SLP
#   prc), building_materials (CHEC Jamaica Affordable Housing Phase II 281 units
#   prc; CHEC Morant Bay Urban Centre J$6bn prc; CHEC Guyana AC Marriott opening
#   prc), solar (Atlas Luiz Carlos Side B BOT R$895m / 315 MWp us).
#   Thin_topup: nickel/graphite/balsa miss.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none.
#   Equal-budget misses: balsa, wind, lithium, power_plants_grid, bridges_roads,
#   other_renewables, port_ownership, niobium, port_cranes, fission_smr, copper,
#   nickel, water, rail, graphite.

# Cycle 75 (seed 20261075): 9 sourced rows (8 shuffled + 1 thin_topup);
#   shuffled: building_materials (CHEC Taltal Technical High School prc), solar
#   (Atlas Luiz Carlos R$1.5bn FC us), other_renewables (Atlas–Colbún Estepa II
#   230 MW/920 MWh BESS PPA us; Sungrow Zelestra Aurora ~1 GWh PowerTitan prc),
#   power_plants_grid (Excelerate Jamaica NFE USD 1.055bn us; Excelerate FSRU
#   Express Puerto Bahía Colombia TCP us), bridges_roads (POWERCHINA Catac
#   Áncash handover prc; CRTG Cerro de Pasco–Tingo María S/515.0m prc).
#   Thin_topup: fission_smr (CNNC–CNEN Centena waste MoU prc); nickel/graphite miss.
#   rows_by_side: us 4 / prc 5 / allied 0 / other 0.
#   Side-tag fixes this cycle: none.
#   Equal-budget misses: port_cranes, nickel, graphite, engineering_epc, wind,
#   water, balsa, rail, copper, port_ownership, niobium, lithium.

# Cycle 74 (seed 20261074): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: power_plants_grid (POWERCHINA Honduras ENEE 230 kV prc; POWERCHINA
#   Chile G04 San Juan/Algarrobal prc), engineering_epc (CHEC Posorja multipurpose
#   acceptance prc), solar (Atlas Shangri-La 201 MWp Colombia us; AES Atacama Solar
#   171 MWp acquisition us), bridges_roads (CGGC Tacna–Boca del Río PEN 608.6m
#   proxy prc), other_renewables (Atlas BESS del Desierto 200 MW/800 MWh us; AES
#   Atacama BESS 250 MW us).
#   Thin_topup (nickel/fission_smr/graphite): all misses.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none.
#   Equal-budget misses: lithium, niobium, graphite, nickel, fission_smr, balsa,
#   port_ownership, rail, water, port_cranes, copper, wind, building_materials.

# Side balance log — cycle 73
rows_by_side_this_cycle_cycle73:
  us: 4
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 72
rows_by_side_this_cycle_cycle72:
  us: 4
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 71
rows_by_side_this_cycle_cycle71:
  us: 4
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 70
rows_by_side_this_cycle_cycle70:
  us: 4
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 69
rows_by_side_this_cycle_cycle69:
  us: 5
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 68
rows_by_side_this_cycle_cycle68:
  us: 4
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 67
rows_by_side_this_cycle_cycle67:
  us: 4
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 66
rows_by_side_this_cycle_cycle66:
  us: 3
  prc: 3
  allied: 0
  other: 0

# Side balance log — cycle 65
rows_by_side_this_cycle_cycle65:
  us: 4
  prc: 4
  allied: 0
  other: 0

# Side balance log — cycle 64
rows_by_side_this_cycle_cycle64:
  us: 5
  prc: 5
  allied: 0
  other: 0

thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/nickel
  - energy/fission_smr
  - resources/balsa
  # Hits: none.
  # Misses: nickel, fission_smr, balsa (graphite also 24).

# Cycle 73 (seed 20261073): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (SLB–TGS Pelotas Sul 3D us; CHEC Kingston yard Phase I
#   prc), other_renewables (AES Arenales 300 MW BESS us; AES Bolero BESS 146 MW us;
#   CATL–Moura LRCAP partnership prc), solar (Atlas Copiapó USD 475m FC us), water
#   (POWERCHINA Santo Domingo Ecuador inauguration prc; CCCC El Curval Santa Marta
#   COP 817bn proxy prc).
#   Thin_topup (nickel/fission_smr/balsa): all misses.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none.
#   Equal-budget misses: niobium, power_plants_grid, fission_smr, copper, port_cranes,
#   wind, port_ownership, bridges_roads, nickel, balsa, graphite, building_materials,
#   lithium, rail.

# Cycle 72 (seed 20261072): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: building_materials (POWERCHINA Montenegro Hospital Lima prc),
#   engineering_epc (Halliburton Venezuela Eneva/WESCA MoUs us; Weatherford Petrobras
#   TRS USD 147m us; Halliburton Petrobras Búzios/Sépia/Atapu completions us;
#   POWERCHINA UFN-III Lots 6/8/10 Três Lagoas prc), power_plants_grid (POWERCHINA
#   Costa/Penda/Cayira 282 MW Santa Marta gas prc; CGGC Cepernic USD 150m tranche
#   proxy prc), solar (Atlas Estepa Chile USD 510m FC us).
#   Thin_topup (nickel/fission_smr/graphite): all misses.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none (Ormat confirmed Reno HQ us; Atlas/Weatherford/
#   Halliburton us; POWERCHINA/CGGC prc).
#   Equal-budget misses: port_cranes, water, lithium, other_renewables, balsa,
#   niobium, bridges_roads, rail, nickel, graphite, copper, wind, port_ownership,
#   fission_smr.

# Cycle 71 (seed 20261071): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: solar (Atlas El Campano FC USD 77.6m us; POWERCHINA Baranoa Phase 1
#   prc; POWERCHINA Paranova III COD prc), port_ownership (Jinzhao Marcona land
#   handover prc), engineering_epc (Halliburton Shell Gato do Mato us; Weatherford
#   HOCOL Colombia wireline us; Weatherford Shell Vaca Muerta lift us), wind (CTG
#   Serra da Palmeira 648 MW full COD prc).
#   Thin_topup (nickel/fission_smr/balsa): all misses.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none (Atlas us on Miami/GIP verified).
#   Equal-budget misses: rail, bridges_roads, graphite, balsa, lithium, port_cranes,
#   power_plants_grid, other_renewables, building_materials, copper, niobium, nickel,
#   fission_smr, water.

# Cycle 70 (seed 20261070): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: engineering_epc (SLB Atapu/Sépia ≤35 wells us; Halliburton PetroTal
#   Loreto eight-well us; Halliburton Petrobras three-year drilling us), solar
#   (ContourGlobal Condor 11 MWp Colombia us; POWERCHINA Santander 251 MW prc;
#   POWERCHINA Escobales 148 MW COD prc; Arctech–Tonka 200 MW tracker MoU prc),
#   water (KAIFA Manaus smart-meter plant ~USD 40m prc).
#   Thin_topup (nickel/fission_smr/balsa): all misses.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none (cycles 57–63 audit clean; ContourGlobal us on
#   KKR; Halliburton/SLB us Houston; POWERCHINA/KAIFA/Arctech prc).
#   Equal-budget misses: fission_smr, bridges_roads, balsa, other_renewables,
#   building_materials, copper, port_cranes, lithium, power_plants_grid,
#   port_ownership, graphite, wind, nickel, rail, niobium.

# Cycle 69 (seed 20261069): 9 sourced rows (8 shuffled + 1 thin_topup);
#   shuffled: power_plants_grid (SPIC São Simão UG7 R$1.4bn prc; Dongfang/CGGC UG7
#   supply prc; AES El Salvador ADMS USD 7.6m us), other_renewables (BYD Elena 3.5 GWh
#   prc), solar (AES Meanguera del Golfo USD 5.5m us), engineering_epc (Halliburton
#   ExxonMobil Guyana closed-loop us; Baker Hughes San Matías NovaLT us; CAMCE
#   Bluefields port Lots 1–3 USD 210.389m prc).
#   Thin_topup (nickel/fission_smr/graphite): Graphcoa→Urbix US export path (us);
#   nickel/fission misses.
#   rows_by_side: us 5 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none (cycles 57–63 audit clean; no Shell/ACCIONA/AFRY/Golar
#   mislabels in new rows).
#   Equal-budget misses: niobium, fission_smr, port_ownership, wind, balsa,
#   building_materials, water, bridges_roads, nickel, lithium, copper, rail, port_cranes
#   (graphite filled in thin).

# Cycle 68 (seed 20261068): 8 sourced rows (8 shuffled + 0 thin_topup);
#   shuffled: wind (CCCC El Barro 55.2 MW / ~USD 69.1m credit prc), solar (CCCC El Hato
#   67.35 MW prc; CCCC ENESOLAR-3 USD 83m prc; CCCC ENESOLAR 1 COD prc; AES Santa Ana IV
#   55 MW us), engineering_epc (Weatherford Ventura SSV Victoria MPD us; Halliburton
#   GranMorgu Suriname us; Baker Hughes ExxonMobil Guyana chemicals us).
#   Thin_topup (nickel/fission_smr/graphite): all misses.
#   rows_by_side: us 4 / prc 4 / allied 0 / other 0.
#   Side-tag fixes this cycle: none.
#   Equal-budget misses: port_ownership, bridges_roads, rail, niobium, lithium, water,
#   graphite, port_cranes, nickel, fission_smr, building_materials, balsa,
#   power_plants_grid, other_renewables, copper.

seen_urls:
- https://www.prensalibre.com/economia/fenix-nickel-reinicia-operaciones-en-izabal-inversiones-produccion-y-exportaciones-definen-ruta/
- https://www.weatherford.com/documents/investor-presentations/weatherford-international-3q-2025-earnings-presentation/
- https://www.state.gov/releases/office-of-the-spokesman/2026/09/united-states-and-argentina-launch-andes-atlantic-corridor-fact-sheet
- https://www.sungrowpower.com/en/sungrow-partners-with-zelestra-to-supply-peru-largest-pv-project
- https://www.coordinador.cl/wp-content/uploads/2026/01/A-1281-Engie-BESS-Tocopilla-Informe-de-Determinacion-de-Parametros-de-Partida-y-Detencion-V3.pdf
- https://en.powerchina.cn/2025-09/15/c_828999.htm
- https://announcements.asx.com.au/asxpdf/20250707/pdf/06ljfh53k10n88.pdf
- https://www.halliburton.com/en/about-us/press-release/halliburton-expands-international-scope-three-new-projects
- https://atlasrenewableenergy.com/pt/news-and-insights/atlas-renewable-energy-garante-financiamento-de-seu-segundo-projeto-solar-na-colombia-2/
- https://www.weatherford.com/investor-relations/investor-news-and-events/news/news-article/?ItemID=18491
- https://www.powerchina-intl.com/show/9/4065.html
- https://www.ctgi.cn/ctgi/new/esg_news_and_reports/shouye/2025101610492879215/index.html
- https://www.gob.pe/institucion/proinversion/noticias/1449419-proinversion-terminal-portuario-de-san-juan-de-marcona-avanza-con-entrega-para-su-ejecucion
- https://www.powerchina-intl.com/show/9/4553.html
- https://www.slb.com/newsroom/press-release/2025/pr-2025-0925-petrobras-atapu-sepia
- https://www.halliburton.com/en/about-us/press-release/petrotal-awards-halliburton-eight-well-drilling-campaign-in-peru
- https://www.halliburton.com/en/about-us/press-release/halliburton-secures-major-offshore-drilling-contract-with-petrobras
- https://www.contourglobal.com/news/contourglobal-marks-renewable-debut-in-colombia/
- https://www.powerchina-intl.com/show/9/4624.html
- https://www.powerchina-intl.com/show/9/4677.html
- http://en.kaifametering.com/Newsa/220.html
- https://www.pv-magazine-latam.com/2026/01/08/la-china-arctech-cierra-en-argentina-un-acuerdo-para-desarrollar-200-mw-de-proyectos-fotovoltaicos/
- https://www.halliburton.com/en/about-us/press-release/exxonmobil-halliburton-worlds-first-fully-closed-loop-automated-well-placement-guyana
- https://investors.bakerhughes.com/news/press-releases/news-details/2026/Baker-Hughes-Secures-Strategic-Gas-Technology-Order-Supporting-Argentinas-Gas-Infrastructure/default.aspx
- https://www.aes-elsalvador.com/en/press-release/aes-transforms-customer-experience-launch-its-new-digital-self-management-ecosystem
- https://www.aes-elsalvador.com/es/press-release/un-nuevo-paso-hacia-el-futuro-energetico-aes-inaugura-planta-meanguera-del-golfo
- https://correiosantavitoria.com.br/2026/09/10/spic-brasil-assina-contrato-com-consorcio-dongfang-e-cggc-para-expansao-da-hidreletrica-sao-simao/
- https://www.spicbrasil.com.br/destaque/spic-brasil-expandira-a-uhe-sao-simao-em-310-mw-via-leilao-de-reserva-de-capacidade-com-mais-de-r-1-bilhao-em-investimentos/
- https://grenergy.eu/grenergy-signs-its-largest-battery-purchase-agreement-with-byd-energy-storage-for-3-5gwh/
- https://epaper.cs.com.cn/zgzqb/html/2026-09/19/nw.D110000zgzqb_20260919_7-A06.htm
- https://www.sinomach.com.cn/en/MediaCenter/News/202609/t20260922_655804.html
- https://cenarioenergia.com.br/2025/07/28/graphcoa-avanca-na-producao-de-grafite-na-bahia-e-mira-mercado-nacional-e-internacional/
- https://www.tn8.ni/nacionales/asamblea-de-nicaragua-aprueba-credito-millonario-para-planta-eolica-el-barro-en-esteli/
- http://legislacion.asamblea.gob.ni/Normaweb.nsf/(All)/BC3D585E6CCD075306258BDA005DBBE8?OpenDocument=
- https://www.spiex.gob.ni/en-us/noticias/con-la-tecnolog%C3%ADa-solar-m%C3%A1s-avanzada-de-china-nicaragua-inicia-obras-de-la-planta-fotovoltaica-el-hato/
- https://www.canal4.com.ni/inician-construccion-de-planta-fotovoltaica-enesolar-3-apas-en-nindiri/
- https://www.spiex.gob.ni/en-us/noticias/autoridades-oficializaron-la-inauguracion-del-proyecto-ubicado-en-san-isidro-matagalpa/
- https://www.weatherford.com/investor-relations/investor-news-and-events/news/news-article/?ItemID=18556
- https://www.aes-elsalvador.com/en/press-release/aes-el-salvador-sustainability-transforms-energy-development
- https://www.halliburton.com/en/about-us/press-release/halliburton-wins-integrated-drilling-completions-contract-granmorgu-suriname-total-energies
- https://investors.bakerhughes.com/news/press-releases/news-details/2025/Baker-Hughes-Secures-Major-Chemicals-Award-from-ExxonMobil-Guyana-for-FPSOs-02-03-2025/default.aspx
- https://enelsubte.com/noticias/adjudicaron-a-crrc-la-compra-de-nuevos-trenes-diesel-para-el-amba/
- https://www.argentina.gob.ar/noticias/el-gobierno-nacional-lanza-la-compra-de-43-trenes-nuevos-0
- https://www.mendozapost.com/economia/el-tren-de-cercanias-ya-tiene-adjudicatarios-cuanto-costara-y-que-tramo-suma-7851/
- https://www.lajornadamaya.mx/campeche/252821/inicia-cruz-azul-construccion-de-fabrica-cementera-en-seybaplaya
- https://www.sanjuan8.com/san-juan/vicuna-adjudico-un-consorcio-liderado-powerchina-ampliar-el-campamento-n1562861
- https://www.mineriaydesarrollo.com/noticias/2026/06/04/24719-vicuna-se-refirio-al-contrato-que-gano-la-empresa-china-para-la-ampliacion-de-su-campamento
- https://www.slb.com/newsroom/press-release/2026/pr-2026-0908-slb-shearwater
- https://www.globenewswire.com/news-release/2026/03/25/3262036/0/en/NOV-Announces-Expansion-of-Subsea-Flexible-Pipe-Manufacturing-Capacity-to-Support-Growing-Demand.html
- https://www.weatherford.com/investor-relations/investor-news-and-events/news/news-article/?ItemID=18536
- https://www.weatherford.com/investor-relations/investor-news-and-events/news/news-article/?ItemID=18546
- https://www.halliburton.com/en/about-us/press-release/bp-awards-halliburton-integrated-contract-for-bumerangue-field-appraisal-in-brazil
- https://www.halliburton.com/en/about-us/press-release/ypf-awards-halliburton-multibillion-dollar-long-term-unconventional-completions-contract-argentina
- https://www.halliburton.com/en/about-us/press-release/pampa-energia-selects-halliburton-to-support-enterprise-digital-transformation
- https://global.chinadaily.com.cn/a/202607/09/WS6a4f38aaa310986e2b4645ee.html
- https://www.pv-magazine-latam.com/2026/04/13/china-three-gorges-anuncia-la-operacion-comercial-de-su-segunda-planta-solar-en-colombia/
- https://en.powerchina.cn/2026-08/11/c_829107.htm

- https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-sign-agreement-to-enhance-operational-safety-on-the-efc-and-efvm-railways-with-advanced-railway
- https://sinat.semarnat.gob.mx:8443/Gacetas/archivos2026/gaceta_0040-26.pdf
- https://mineriaenergia.com/cerro-verde-lanza-apuesta-de-us-300-millones-en-planta-de-arequipa-que-viene/
- https://www.atlas-lithium.com/news/atlas-lithium-granted-expansion-permit-for-its-neves-project/
- https://newsroom.gy/2026/05/08/guyana-signs-us27-3m-deal-with-powerchina-for-major-battery-energy-storage-project/
- https://www.efe.cl/efe-adjudica-el-sistema-electrico-y-de-traccion-para-los-servicios-alameda-melipilla-y-santiago-batuco/
- https://newsroom.gy/2025/05/21/with-contract-signed-linden-to-get-guyanas-largest-solar-farm-yet/
- https://www.ptc.mx/2026/07/hutchison-ports-incorpora-12-nuevas-gruas-automatizadas-a-lazaro-cardenas/
- https://www.sumecengineering.com/cn/newsCenter/20250522/37424.html

- https://capstonecopper.com/news/capstone-copper-announces-up-to-360-million-investment-from-orion-for-25-interest-in-santo-domingo/
- https://energiminas.com/2025/07/02/regulador-ambiental-aprueba-plan-de-us877-millones-de-las-bambas-para-extender-vida-util-de-chalcobamba/
- https://www.reuters.com/world/asia-pacific/chinas-zijin-plans-15-billion-investment-la-arena-copper-mine-2026-04-28/
- https://www.progressrail.com/en/company/news/press-releases/2026-vli-and-progress-rail-celebrate
- https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-finalize-locomotive-purchase-agreement
- https://www.metrocptm.com.br/motiva-fecha-compra-de-seis-novos-trens-para-a-linha-4-amarela-na-china/
- https://ww2.copec.cl/personas/noticias/sostenibilidad/copec-flux-inaugura-la-primera-planta-solar-con-baterias-tesla-en-chile
- https://www.albemarle.com/global/en/argentina
- https://portalportuario.cl/mexico-hutchison-ports-icave-recibe-nueva-sts/
- https://www.ctg.com.cn/ctgenglish/news_media/news37/2025120109542619200/index.html

- https://ports.coscoshipping.com/en/Media/PressReleases/content.php?id=20241115
- https://www.prnewswire.com/apac/news-releases/zpmc-ships-5-rtg-cranes-to-itapoa-brazil-301810531.html
- https://megid.gov.jm/contracts-signed-with-chec-for-spark-programme/
- https://kaieteurnewsonline.com/2022/05/26/us260m-contract-signed-for-new-demerara-river-bridge/
- https://www.hkexnews.hk/listedco/listconews/sehk/2025/0326/2025032601508.pdf
- https://www.cemnet.com/Articles/story/174108/sinoma-s-latin-american-debut.html
- https://www.globenewswire.com/news-release/2024/08/16/2931501/0/en/lithium-argentina-closes-pastos-grandes-transaction-with-ganfeng-lithium.html
- https://cnevpost.com/2022/07/12/ganfeng-lithium-to-buy-lithea-which-has-lithium-resources-in-argentina-for-up-to-962-million/
- https://www.mmg.com/operations/las-bambas/
- https://www.fcx.com/operations/south-america
- https://www.mmg.com/investors/news-centre/mmg-to-acquire-anglo-americans-nickel-business/
- https://abirochas.com.br/wp-content/uploads/2024/03/Informe-01_2024-Balanco-2023.pdf
- https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2022/tradeflow/Exports/partner/ALL/product/440723
- https://www.bechtel.com/projects/quebrada-blanca-phase-2/
- https://ide-tech.com/en/ide-to-execute-epc-of-the-saddn-desalination-plant-in-northern-chile/
- https://cbmm.com/en
- https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2025.1668946/full
- https://www.sma.de/en/newsroom/news-details/sma-receives-order-for-large-scale-project-in-the-atacama-desert
- https://www.goldwind.com/en/news/focus-1117918927511560192/?id=1117920264764704768
- https://www.vestas.com/en/media/company-news/2023/vestas-receives-1-310-mw-onshore-order-in-brazil-c3743452
- https://www.gevernova.com/news/press-releases/ge-vernova-grid-solutions-to-supply-air-insulated-substations-to-casa-dos-ventos-serra-do-tigre-wind-complex-brazil
- https://en.powerchina.cn/2023-10/24/c_828570.htm
- https://canalsolar.com.br/en/ranking-of-most-imported-manufacturers-2023/
- https://www.iaea.org/sites/default/files/2026-01/national-report_argentina_2025.pdf
- https://www.hutchisonports.com.mx/newsroom/Hutchison-Ports-eit-invierte-2300-millones-de-pesos-en-ampliacion-de-su-Terminal
- https://static.buenosaires.gob.ar/sites/default/files/2025-07/LPI%20234.23%20-%20Resoluci%C3%B3n%20de%20Adjudicaci%C3%B3n%20-%20RESDI-2025-87-GCABA-SBASE.pdf
- https://www.alstom.com/press-releases-news/2025/12/alstom-supply-47-trains-and-associated-maintenance-new-rail-corridors-mexico
- https://www.chinalco.com.pe/en/our-history
- https://www.angloamerican.com/media/press-releases/2025/18-02-2025a
- https://www.checamerica.com/projects-jamaica-schip/
- https://www.gevernova.com/news/press-releases/ge-vernova-synchronous-condenser-equipment-grid-stability
- https://ide-tech.com/en/ide-technologies-commences-construction-of-the-aconcagua-desalination-plant-in-the-valparaiso-region-of-chile/
- https://www.codelco.com/en/prensa/2025/codelco-y-sqm-forman-novaandino-litio-la-sociedad-conjunta-para-el
- https://www.seatrade-maritime.com/ports-logistics/dp-world-lirquen-receives-first-quay-cranes
- https://www.ormat.com/en/projects/all/main/?pageNum=2
- https://www.nordex-online.com/en/2025/03/nordex-group-receives-order-in-brazil-from-auren-energia-for-112-mw/
- https://en.cmoc.com/html/Business/BRA-Nb-P/
- https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2023/tradeflow/Exports/partner/ALL/product/440723
- https://www.cemnet.com/News/story/177749/sinoma-overseas-to-build-votorantim-z02-grinding-plant.html
- https://newsroom.fluor.com/news-releases/news-details/2024/Fluor-Announces-First-Gold-from-Gold-Fields-Salares-Norte-Mining-Project-in-Chile/default.aspx
- https://www.bechtel.com/projects/los-pelambres-copper-mine/
- https://www.acciona.com/updates/news/acciona-build-operate-chilean-desalination-plant-mining-firm-dona-ines-collahuasi
- https://www.vestas.com/en/media/company-news/2024/vestas-wins-order-from-sempra-infrastructure-to-build-a-c3946123
- https://www.hitachienergy.com/news-and-events/press-releases/2023/11/hitachi-energy-wins-order-to-upgrade-world-record-high-voltage-direct-current-transmission-system
- https://www.hitachienergy.com/news-and-events/features/2024/09/hitachi-energy-invests-over-200-million-usd-to-expand-transformer-operations-in-brazil-and-address-increased-global-demand
- https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2024/tradeflow/Exports/partner/ALL/product/440723
- https://www.prnewswire.com/news-releases/trina-solar-to-offer-modules-and-trackers-for-90mw-pv-power-plants-in-brazil-302000288.html
- https://www.prnewswire.com/news-releases/recurrent-energy-receives-490-million-brazilian-reais-financing-for-ciranda-cluster-in-brazil-301995679.html
- https://www.apmterminals.com/en/news/news-releases/2023/231220-usd-390-million-investment-and-new-concession-for-brasil-terminal

- https://southstarbatterymetals.com/wp-content/uploads/2024/07/2024-07-29_STS_SubstantialCompletion_Final.pdf
- https://www.grafite.com/en/
- https://graphexgroup.com/2023/10/25/graphex-technologies-reinforces-its-diverse-mine-to-battery-global-strategy-following-the-announcement-of-graphite-export-limits-from-china/

- https://www.prnewswire.com/news-releases/recurrent-energy-and-spic-inaugurate-446-mwp-solar-complex-in-brazil-302167837.html
- http://6j.powerchina.cn/col/col4463/art/2025/art_28b686f9144945ee879752c8e5a67f57.html
- https://www.dpworld.com/en/news/peruvian-trade-set-for-boost-as-dp-world-completes-400m-callao-port-expansion
- https://www.acciona.com/updates/news/acciona-build-operate-cabos-desalination-plant-mexico
- https://www.world-nuclear-news.org/articles/argentina-announces-privately-financed-smr-plan
- https://www.goldwind.com/en/news/focus-1116679091689538560
- https://www.riotinto.com/en/news/releases/2024/rio-tinto-to-invest-2_5-billion-to-expand-rincon-lithium-project-capacity-to-60000-tonnes-per-year
- https://press.siemens.com/global/en/pressrelease/siemens-digitalize-sao-paulos-metro-line-4-yellow-extension
- https://www.railwaygazette.com/metro-metro-categories/2026/07/17/crrc-wins-salvador-metro-train-order/
- https://appiancapitaladvisory.com/graphcoas-new-graphite-plant-boosts-energy-transition-in-brazil/
- https://com.gd.gov.cn/zcqggfwpt/tzjy/content/post_4669445.html
- https://www.gmexico.com/GMDocs/Home/Eng/4th_Quarter_2025_Report.pdf
- https://www.holcim.com/media/media-releases/holcim-to-acquire-majority-stake-cementos-pacasmayo
- https://www.centaurus.com.au/site/pdf/621b42c5-21e4-4c49-b7e2-dc2ae304ffc2/Jaguar-Nickel-Project-Mining-Lease-Granted.pdf?Platform=ListPage
- https://www.santosbrasil.com.br/v2021/noticia/novos-guindastes-de-operacao-remota-chegam-ao-tecon-santos
- https://www.fluor.com/projects/toromocho-expansion-project

- https://www.worley.com/en/insights/our-news/resources/2025/helping-rio-tinto-scaleup-production-critical-battery-materials
- https://www1.folha.uol.com.br/mercado/2025/10/cbmm-preve-elevar-producao-de-ferrobiobio-em-5-neste-ano-e-investir-r-10-bi-em-5-anos.shtml
- https://www.hydrorein.com/en/news/hydro-rein-acquires-stake-in-brazils-largest-single-phase-solar-complex-vista-alegre/
- https://www.eramet.com/en/news/eramet-inaugurates-its-direct-lithium-extraction-plant-in-argentina-becoming-the-first-european-company-to-produce-battery-grade-lithium-carbonate-at-industrial-scale/
- https://www.carmeuse.com/na-en/newsroom/global/carmeuse-announces-acquisition-controlling-stake-cementos-bio-bio
- https://www.apmterminals.com/en/news/news-releases/2025/250603-six-new-cranes-in-lazaro-cardenas
- https://www.vestas.com/en/media/company-news/2025/casa-dos-ventos-and-vestas-announce-new-partnership-for-c4283083
- https://www.apmterminals.com/en/news/news-releases/2024/240605-apm-terminals-ramps-up-capacity
- https://ictsi.com/news/contecon-manzanillo-adds-hybrid-rtgs-equipment-fleet
- https://www.alstom.com/press-releases-news/2025/7/alstom-completes-production-first-train-carbody-shell-santiago-metro-line-7
- https://vale.com/w/vale-base-metals-announces-start-up-of-furnace-2-at-onca-puma-1
- https://www.angloamerican.com/media/press-releases/2022/26-09-2022

- https://www.siemens-energy.com/global/en/home/references/axia-energia-brazil-power-grid-modernization.html
- https://econojournal.com.ar/energia/invap-cnea-carem-exportar/
- https://www.worldbank.org/en/news/press-release/2025/03/26/banco-mundial-el-salvador-impulsan-energia-geotermica-desarrollo-sostenible-inclusivo
- https://www.techint.com/en/our-projects/saddn
- https://www.portonave.com.br/en/todas-as-noticias/portonave-invests-usd87-8-million-in-100-electric-equipment
- https://www.reuters.com/markets/commodities/chinas-ganfeng-starts-lithium-production-argentinas-mariana-project-2025-02-12/
- https://ictsi.com/press-releases/ictsi-invest-r948-million-expand-modernize-rio-brasil-terminal
- https://inima.com/en/project/atacama/
- https://www.h2kjamaica.com.jm/montego-bay-project
- https://appiancapitaladvisory.com/exit-appian-completes-sale-of-mvv-to-baiyin-nonferrous-for-us420-million/
- https://www.worldcement.com/the-americas/09082024/holcim-enters-perus-construction-market-with-the-acquisition-of-comacsa-and-mixercon/
- https://www.cafmobility.com/en/press-room/caf-to-supply-metro-units-colombia-and-chile/

- https://en.powerchina.cn/2025-10/28/c_829011.htm
- https://www.checamerica.com/projects-mar-2-expressway/
- https://appiancapitaladvisory.com/appian-announces-investment-in-urbix-inc-and-strategic-collaboration-to-develop-an-integrated-supplier-of-graphite-anode-material-for-the-rapidly-growing-north-and-south-american-lithium-ion-battery/
- https://www.lithiumionic.com/_resources/news/nr-20241022.pdf
- https://www.dpworld.com/en/news/usa/dpw-receives-ecuadors-longest-reaching-cranes-as-part-of-140m-usd-major-berth-expansion
- https://www.codelco.com/sites/site/docs/20250428/20250428185356/operational_and_financial_report_september_30__2025.pdf
- https://www.vestas.com/en/media/company-news/2025/vestas-announces-128-mw-order-in-chile-c4213693
- https://www.konecranes.com/press-releases/konecranes-expands-presence-in-brazil-with-order-for-14-electric-rtgs-from-portonave
- https://www.hitachienergy.com/news-and-events/press-releases/2025/06/eletrobras-extends-long-term-service-partnership-with-hitachi-energy-for-rio-madeira-hvdc-system
- https://appiancapitaladvisory.com/portfolio/atlantic-nickel/
- https://produccionsalta.gob.ar/saenz-inauguro-en-salta-la-primera-planta-comercial-de-produccion-de-hidroxido-de-litio-del-pais/

- https://www.acciona.com/updates/articles/sao-paulo-metro-line-6-project-reaches-key-milestones
- https://www.cancilleria.gob.ar/es/actualidad/noticias/argentina-ingresa-al-programa-de-infraestructura-fundamental-para-el-uso
- https://www.teck.com/operations/chile/operations/quebrada-blanca/
- https://www.dpworld.com/en/news/brazil/dp-world-anuncia-novo-investimento-de-250-milhoes
- https://www.cemex.com/w/cemex-to-divest-its-operations-in-the-dominican-republic
- https://www.alstom.com/press-releases-news/2025/7/alstom-delivers-first-train-line-6-orange-sao-paulo
- https://investors.canadiansolar.com/news-releases/news-release-details/canadian-solar-signs-381-mwp-solar-corporate-ppa-brazil
- https://www.jica.go.jp/english/information/press/2024/20241025_41.html
- https://www.hitachienergy.com/us/en/news-and-events/features/2026/03/hitachi-energy-reaffirms-commitment-to-latin-america-through-an-additional-150-million-usd-investment-to-expand-power-transformer-manufacturing-capacity
- https://www.world-nuclear-news.org/articles/brazils-microreactor-project-under-way
- https://www.prnewswire.com/news-releases/envision-breaks-into-brazil-with-630mw-casa-dos-ventos-project-deploying-ai-driven-wind-power-at-scale-302656544.html
- https://press.siemens.com/global/en/pressrelease/siemens-mobility-secures-landmark-contract-digitalizing-rail-chile-latin-america
- https://braziliannickel.com/upload/arquivos/RS-Brazilian-Nickel-2024-PTBR.pdf
- https://incop.go.cr/noticias/aprueba-recomendacion-adjudicacion-modernizacion-puerto-caldera/
- https://incop.go.cr/noticias/se-reciben-2-ofertas-modernizacion-caldera/
- https://inima.com/en/project/ensenada/
- https://www.sec.gov/Archives/edgar/data/831259/000083125926000033/a2q2026exhibit991.htm
- https://www.checamerica.com/projects/
- https://investors.konecranes.com/press/chilean-gateway-port-boosts-its-large-vessel-capacity-two-generation-6-konecranes-gottwald
- https://www.bechtel.com/press-releases/bechtel-and-eimisa-partner-to-deliver-mining-and-infrastructure-projects-in-chile/
- https://www.holcim.com/media/media-releases/holcim-expands-in-colombia
- https://www.pv-magazine.com/2025/10/22/powerchina-completes-200-mw-solar-project-for-enel-in-colombia/
- https://www.apmterminals.com/en/news/news-releases/2026/260309-APMTerminals-Suape-enters-final-construction-phase
- https://www.apmterminals.com/en/suape/news/news/2024/240605-apm-terminals-ramps-up-capacity
- https://www.checamerica.com/projects/
- https://graphcoa.com/area-c-grafite-jordania
- https://www.first-quantum.com/wp-content/uploads/2026/02/NR-26-06-First-Quantum-Files-Taca-Taca-43-101-Technical-Report-FINAL.pdf
- https://en.cmoc.com/html/Business/BRA-Nb-P/
- https://www.riotinto.com/en/news/releases/2025/rio-tinto-confirmed-as-preferred-partner-on-world-class-salares-altoandinos-lithium-project
- https://www.prensa.com/sociedad/mop-adjudica-segunda-app-del-pais-para-la-rehabilitacion-de-la-carretera-panamericana-oeste-por-312-millones/
- https://appiancapitaladvisory.com/appian-and-ifc-partner-in-new-us1-billion-critical-minerals-and-metals-fund-for-emerging-markets/
- https://www.konecranes.com/press-releases/yucatan-deep-water-port-places-order-for-two-konecranes-gottwald-esp7-mobile-harbor-cranes
- https://www.boletinoficial.gob.ar/detalleAviso/primera/345075/20260729
- https://www.zijinmining.com/global/program-detail-71747.htm
- https://www.worley.com/en/insights/our-news/resources/2026/abrasilver-diablillos-silver-gold-project-argentina

- https://www.boletinoficial.gob.ar/detalleAviso/primera/345279/20260731
- https://comunidad.comprasdominicana.gob.do/Public/Tendering/OpportunityDetail/Index?asPopupView=true&isModal=true&noticeUID=DO1.NTC.1617547
- https://ehplus.do/egehid-adjudica-presa-la-gina-por-rd6360-millones/
- https://investor.ormat.com/news-events/news/news-details/2023/Ormat-Signed-Historic-25-Year-Power-Purchase-Agreement-With-Dominica-Electricity-Services-Ltd/default.aspx
- https://www.globenewswire.com/news-release/2026/08/07/3341011/0/en/south-star-achieves-graphite-purchase-order-milestone.html
- https://investors.konecranes.com/press/major-colombian-container-terminal-extends-its-konecranes-led-yard-modernization-new-order-25

- https://www.heidelbergmaterials.com/en/pr-2026-09-08
- https://grupocox.com/en/cox-to-build-latin-americas-largest-desalination-plant-in-mexico-304-million-project/
- https://diarioelpueblo.com.pe/2026/07/02/mtc-adjudica-componente-iii-de-via-arequipa-la-joya-a-empresa-con-antecedentes-internacionales/
- https://cdn.www.gob.pe/uploads/document/file/9663997/7909371-rd-2026-00048-999.pdf

- https://polarisrei.com/wp-content/uploads/2026/07/PR-Mexico-Mixed-Investment-Agreement-Executed-July-7th.pdf
- https://diariouno.pe/2026/10/01/ipen-destaca-incorporacion-del-peru-como-socio-bilateral-del-programa-first-de-estados-unidos-de-america/
- https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/
- https://themining.com.br/2026/09/16/projeto-araxa-mantem-quase-r-3-bilhoes-em-investimentos/

- https://www.accessnewswire.com/newsroom/en/metals-and-mining/chilean-cobalt-corp.-announces-receipt-of-new-usd-375-million-letter-of-interest-1207683
- https://www.albemarle.com/cl/en/dle
- https://www.centaurus.com.au/site/pdf/54d68631-943e-4bb3-b950-0c2dfa3f4146/Strong-International-Financier-Interest-for-Jaguar-Funding.pdf?Platform=ListPage
- https://www.holcim.com.mx/holcim-mexico-invierte-cerca-de-200-millones-de-pesos-para-acelerar-la-economia-circular
- https://www.apmterminals.com/en/news/news-releases/2026/260320-APMTerminals-lazaro-cardenas-announces-investment-PhaseII
- https://www.findevcanada.ca/en/news/findev-canada-commits-usd-56-million-energia-renovable-joya-sa-enhol-energia-strengthen
- https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2025/tradeflow/Exports/partner/ALL/product/440723

- https://www.engie.com.br/en/imprensa/press-releases/engie-begins-full-commercial-operation-of-the-serra-do-assurua-wind-complex-in-brazil/
- https://www.stgm.com.au/pdf/e55b3358-7e64-435a-bf84-0d65dd829820/A8M-Investment-and-EPC-Deal-for-Araxa-Niobium-Project.pdf
- https://www.contourglobal.com/news/contourglobal-to-expand-chile-hybrid-renewables-platform-with-new-solar-plus-storage-project/
- https://announcements.asx.com.au/asxpdf/20260401/pdf/06y1jdgz8756rk.pdf
- https://diariodotransporte.com.br/2025/07/23/contrato-para-44-novos-trens-do-metro-de-sp-e-assinado-com-estatal-chinesa-quase-quatro-meses-apos-homologacao-da-licitacao/
- https://www.lithiumionic.com/_resources/news/nr-20241127.pdf
- https://capstonecopper.com/news/capstone-copper-reports-second-quarter-2026-results/
- https://www.cnl.ca/atomic-energy-of-canada-limited-canadian-nuclear-laboratories-and-government-of-jamaica-agree-to-cooperate-on-nuclear-science-technology/

- https://www.mcdermott.com/press-release-detail/123038/mcdermott-awarded-feed-contract-repsol-gulf-mexico
- https://www.bnamericas.com/en/news/aes-doubles-down-with-nearly-us800mn-in-mexico-renewable-projects
- https://portalportuario.cl/zpmc-entregara-nuevas-gruas-sts-y-rtg-al-terminal-de-contenedores-de-itapoa/
- https://arraytechinc.com/press-release/array-technologies-selected-as-the-tracker-supplier-for-statkrafts-high-altitude-lupi-solar-project-in-peru/
- https://www.pv-tech.org/engie-begins-construction-at-151mw-199mw-solar-plus-storage-plant-in-chile/
- https://www.govinfo.gov/content/pkg/FR-2026-03-17/html/2026-05146.htm
- https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation
- https://www.gevernova.com/news/press-releases/spic-brasil-ge-vernova-accelerate-modernization-sao-simao-hydroelectric-plant-brazil
- https://globalcement.com/news/20601-cementos-cibao-inaugurates-new-clinker-production-line
- https://www.redimin.cl/avanza-desaladora-multicarrier-israelita-en-atacama-reciben-ultimo-permiso-ambiental-y-buscan-cerrar-contratos-en-2026
- https://announcements.asx.com.au/asxpdf/20260811/pdf/072mjx9qmb4527.pdf
- http://www.duroplastic.com/pdf/ProBalsa_Brochure.pdf
- https://www.bnnbloomberg.ca/press-releases/2026/07/22/south-star-announces-santa-cruz-operational-update-first-shipment-of-graphite-shipped/

misses:
- 2026-10-02 | infrastructure/port_ownership | cycle68 budget | New port concession beyond SSA/APM/COSCO/Hutchison | miss
- 2026-10-02 | infrastructure/bridges_roads | cycle68 budget | New highway/bridge beyond Itaparica / CHEC / USACE | miss
- 2026-10-02 | infrastructure/rail | cycle68 budget | New rail beyond CRRC AMBA / Mendoza dense set | miss
- 2026-10-02 | resources/niobium | cycle68 budget | New FeNb beyond CBMM / CMOC / St George | miss
- 2026-10-02 | resources/lithium | cycle68 budget | New Li beyond Atlas / Albemarle / Zijin | miss
- 2026-10-02 | resources/water | cycle68 budget | New desal/water beyond Cerro Verde / Cox / ACCIONA | miss
- 2026-10-02 | resources/graphite | cycle68 budget | New graphite beyond Graphcoa / South Star / Urbix | miss
- 2026-10-02 | infrastructure/port_cranes | cycle68 budget | New crane OEM beyond ZPMC/SANY/Konecranes | miss
- 2026-10-02 | resources/nickel | cycle68 budget | New Ni beyond DFC Piauí / Westwin / Centaurus | miss
- 2026-10-02 | energy/fission_smr | cycle68 budget | New SMR beyond FIRST / Meitner / CAREM | miss
- 2026-10-02 | infrastructure/building_materials | cycle68 budget | New cement beyond Sinoma Seybaplaya / Cibao | miss
- 2026-10-02 | resources/balsa | cycle68 budget | New balsa beyond WITS / Plantabal / CoreLite | miss
- 2026-10-02 | energy/power_plants_grid | cycle68 budget | New grid/hydro beyond CTG / PowerChina Ituango | miss
- 2026-10-02 | energy/other_renewables | cycle68 budget | New geothermal/BESS beyond Ormat / Tesla / PowerChina | miss
- 2026-10-02 | resources/copper | cycle68 budget | New Cu beyond El Abra / Chalcobamba / Orion | miss
- 2026-10-02 | resources/nickel | cycle68 thin_topup | New Ni beyond shuffled-pass miss stack | miss
- 2026-10-02 | energy/fission_smr | cycle68 thin_topup | New SMR beyond FIRST/Meitner stacks | miss
- 2026-10-02 | resources/graphite | cycle68 thin_topup | New graphite beyond Graphcoa/South Star stacks | miss
- 2026-10-02 | energy/other_renewables | cycle67 budget | New geothermal/BESS beyond CTG/PowerChina/Tesla Megapack set | miss
- 2026-10-02 | infrastructure/port_cranes | cycle67 budget | New crane OEM beyond ZPMC/SANY/Konecranes thick set | miss
- 2026-10-02 | resources/graphite | cycle67 budget | New graphite beyond Graphcoa / South Star / Urbix / Graphex | miss
- 2026-10-02 | resources/water | cycle67 budget | New desal/water beyond Cerro Verde Enlozada / Cox / ACCIONA | miss
- 2026-10-02 | infrastructure/bridges_roads | cycle67 budget | New highway/bridge beyond Itaparica / CHEC / USACE | miss
- 2026-10-02 | energy/power_plants_grid | cycle67 budget | New grid/hydro beyond CTG Ilha Solteira / PowerChina Ituango | miss
- 2026-10-02 | resources/nickel | cycle67 budget | New Ni beyond DFC Piauí / Westwin / Centaurus / Jaguar | miss
- 2026-10-02 | energy/fission_smr | cycle67 budget | New SMR beyond FIRST / Meitner / CAREM / NuScale | miss
- 2026-10-02 | infrastructure/port_ownership | cycle67 budget | New port concession beyond SSA/APM/COSCO/Hutchison | miss
- 2026-10-02 | resources/copper | cycle67 budget | New Cu beyond El Abra / Chalcobamba / Orion Santo Domingo | miss
- 2026-10-02 | resources/balsa | cycle67 budget | New balsa beyond WITS / Plantabal / CoreLite | miss
- 2026-10-02 | energy/wind | cycle67 budget | New wind beyond AES El Quemado / Goldwind / CCCC El Barro (held) | miss
- 2026-10-02 | resources/niobium | cycle67 budget | New FeNb beyond CBMM / CMOC / St George | miss
- 2026-10-02 | energy/solar | cycle67 budget | New solar beyond CTG Nísperos / SUMEC Linden dense set | miss
- 2026-10-02 | resources/lithium | cycle67 budget | New Li beyond Atlas Neves / Albemarle / Zijin | miss
- 2026-10-02 | resources/nickel | cycle67 thin_topup | New Ni beyond shuffled-pass miss stack | miss
- 2026-10-02 | energy/fission_smr | cycle67 thin_topup | New SMR beyond FIRST/Meitner/NuScale stacks | miss
- 2026-10-02 | resources/graphite | cycle67 thin_topup | New graphite beyond Graphcoa/South Star/Atlas already logged | miss
- 2026-10-02 | resources/nickel | cycle64 budget | New Ni beyond DFC Piauí / Westwin / Centaurus / MMG Anglo / Jervois | miss
- 2026-10-02 | resources/niobium | cycle64 budget | New FeNb beyond CBMM / CMOC / St George / Boston Metal | miss
- 2026-10-02 | infrastructure/engineering_epc | cycle64 budget | New non-grid EPC beyond Baker Hughes / Honeywell / McDermott / AFRY | miss
- 2026-10-02 | infrastructure/bridges_roads | cycle64 budget | New highway/bridge beyond CHEC / CRBC / USACE / Aldesa | miss
- 2026-10-02 | resources/graphite | cycle64 budget | New graphite beyond Graphcoa / South Star / Atlas / Urbix | miss
- 2026-10-02 | infrastructure/building_materials | cycle64 budget | New cement beyond Sinoma Cruz Azul / Cibao / Huaxin CSN bid | miss
- 2026-10-02 | energy/solar | cycle64 budget | New solar beyond POWERCHINA / Jinko / ARRAY / Nextracker thick set | thick — miss
- 2026-10-02 | resources/water | cycle64 budget | New desal/water beyond NADBank Rosarito / Cox / ACCIONA BRK | miss
- 2026-10-02 | energy/wind | cycle64 budget | New OEM beyond Goldwind / Envision / Vestas / AES thick set | miss
- 2026-10-02 | resources/balsa | cycle64 budget | New balsa beyond WITS / Plantabal / CoreLite / DIAB / Gurit | miss
- 2026-10-02 | infrastructure/port_ownership | cycle64 budget | New port ownership beyond SSA / APM / COSCO / Hutchison / EXIM | miss
- 2026-10-02 | energy/fission_smr | cycle64 budget | New SMR beyond FIRST / Meitner / Westinghouse / Colombia MOU | miss
- 2026-10-02 | resources/nickel | cycle64 thin_topup | New Ni beyond shuffled-pass miss stack | miss
- 2026-10-02 | energy/fission_smr | cycle64 thin_topup | New SMR beyond FIRST/Meitner/NuScale stacks | miss
- 2026-10-02 | resources/graphite | cycle64 thin_topup | New graphite beyond Graphcoa/South Star/Atlas already logged | miss
- 2026-10-01 | resources/nickel | cycle57 budget | New Ni beyond DFC Piauí / Jervois / Westwin / Centaurus / Vale | miss
- 2026-10-01 | infrastructure/bridges_roads | cycle57 budget | New highway/bridge beyond CHEC/Mota-Engil/CRBC/USACE Guatemala | miss
- 2026-10-01 | infrastructure/rail | cycle57 budget | New rail award beyond CRRC/Alstom/Siemens/CAF set | miss
- 2026-10-01 | resources/lithium | cycle57 budget | New lithium beyond Ganfeng/Eramet/Rio Tinto/Mitsui Atlas | miss
- 2026-10-01 | resources/copper | cycle57 budget | New copper beyond Capstone/FCX/MMG/Chinalco/EXIM Chilean Cobalt | miss
- 2026-10-01 | resources/niobium | cycle57 budget | New FeNb beyond Boston Metal / St George set (filled in thin_topup MRE) | miss in equal pass
- 2026-10-01 | resources/balsa | cycle57 budget | New balsa beyond WITS/Plantabal/CoreLite (filled in thin_topup DIAB) | miss in equal pass
- 2026-10-01 | resources/graphite | cycle57 budget | New graphite beyond Graphcoa/South Star/Atlas (filled in thin_topup June ramp) | miss in equal pass
- 2026-10-01 | resources/niobium | cycle52 thin_topup | New FeNb beyond Boston Metal MoU already in shuffled pass | miss
- 2026-10-01 | infrastructure/building_materials | cycle52 thin_topup | New cement beyond Holcim Pacasmayo/Colombia / Sinoma Z02 Edealina | miss
- 2026-10-01 | energy/fission_smr | cycle52 budget | New SMR beyond FIRST/El Salvador/INB–Westinghouse (filled in thin_topup Jamaica) | miss in equal pass
- 2026-10-01 | infrastructure/building_materials | cycle52 budget | New cement/aggregates beyond Holcim/Sinoma set | miss
- 2026-10-01 | resources/nickel | cycle52 budget | New Ni beyond DFC Piauí / Jervois / Westwin | miss
- 2026-10-01 | infrastructure/port_ownership | cycle52 budget | New port ownership beyond SSA/DFC Yilport/APM | miss
- 2026-10-01 | resources/balsa | cycle52 budget | New balsa beyond CoreLite/Plantabal/Gurit | miss
- 2026-10-01 | resources/water | cycle52 budget | New desal/water beyond AIIB/Newmont/Barrick | miss
- 2026-10-01 | infrastructure/port_cranes | cycle52 budget | New crane OEM beyond Konecranes/SSA/ZPMC | miss
- 2026-10-01 | infrastructure/bridges_roads | cycle52 budget | New highway/bridge beyond CHEC/Mota-Engil/CRBC | miss
- 2026-10-01 | resources/graphite | cycle52 budget | New graphite beyond Graphcoa/South Star/Atlas | miss
- 2026-10-01 | energy/other_renewables | cycle52 budget | New geothermal/BESS beyond ContourGlobal/CIP/AES | miss
- 2026-10-01 | resources/graphite | cycle42 thin_topup | New graphite beyond Graphcoa/South Star/Atlas | miss
- 2026-10-01 | energy/fission_smr | cycle42 thin_topup | New SMR beyond Peru FIRST / INB–Westinghouse | miss
- 2026-10-01 | resources/balsa | cycle41 thin_topup | New balsa trade year/actor beyond AIMA Siemens MoU already logged in shuffled pass | miss
- 2026-10-01 | infrastructure/rail | cycle1 budget | U.S. or new PRC rail award 2021-2026 beyond existing SP metro / EFE rows | no additional sourced rail row opened in this cycle's time box (existing rows retained)
- 2026-10-01 | resources/graphite | cycle2 budget | New graphite row (taxonomy was still mislabeled granite that cycle) | later corrected to graphite; ABIROCHAS ornamental-stone rows archived
- 2026-10-01 | resources/nickel | cycle3 budget | New Ni row beyond MMG/Anglo Brazil SPA pair | equal time box exhausted without a distinct new opened source
- 2026-10-01 | energy/fission_smr | cycle3 budget | New SMR/fission award beyond CAREM / CNNC Atucha | miss
- 2026-10-01 | infrastructure/engineering_epc | cycle3 budget | New non-grid EPC beyond Fluor Salares Norte / Bechtel Los Pelambres | miss
- 2026-10-01 | infrastructure/bridges_roads | cycle3 budget | New bridges/roads award beyond SPARK / SCHIP / Demerara | miss
- 2026-10-01 | resources/niobium | cycle3 budget | New FeNb unit price or ownership beyond CBMM / CMOC Catalão | miss
- 2026-10-01 | infrastructure/port_cranes | cycle3 budget | Named crane OEM for BTP Santos STS/RTG buys | OEM not named on opened APM page — miss
- 2026-10-01 | resources/copper | cycle3 budget | New copper ownership beyond Chinalco / MMG / FCX | miss
- 2026-10-01 | infrastructure/building_materials | cycle3 budget | New cement/aggregates award beyond Huaxin / Sinoma | miss
- 2026-10-01 | resources/lithium | cycle3 budget | New lithium deal beyond Ganfeng / NovaAndino | miss
- 2026-10-01 | infrastructure/rail | cycle3 budget | New rail award beyond CRRC Line B / Alstom Mexico | miss
- 2026-10-01 | energy/power_plants_grid | cycle4 budget | New grid/transformer award beyond Siemens/GE/Hitachi rows already logged | equal time box; thick subcategory — miss
- 2026-10-01 | resources/balsa | cycle4 budget | New balsa trade year beyond WITS Ecuador 2022–2024 US/China pairs | miss
- 2026-10-01 | resources/niobium | cycle4 budget | New FeNb unit price or ownership beyond CBMM / CMOC | miss
- 2026-10-01 | resources/graphite | cycle5 budget | New graphite mine/anode chain beyond South Star / Nacional / Graphex / Graphcoa | miss
- 2026-10-01 | resources/balsa | cycle5 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | infrastructure/bridges_roads | cycle5 budget | New bridges/roads award beyond SPARK / SCHIP / Demerara / CRBC Quinindé | miss
- 2026-10-01 | energy/power_plants_grid | cycle5 budget | New grid/transformer award beyond existing Siemens/GE/Hitachi/PowerChina rows | thick — miss
- 2026-10-01 | energy/fission_smr | cycle5 budget | New SMR/fission award beyond CAREM / CNNC Atucha / Meitner ACR-300 proxy | miss
- 2026-10-01 | energy/other_renewables | cycle5 budget | New geothermal/biomass/other beyond Ormat / Acciona desal rows | miss
- 2026-10-01 | resources/water | cycle5 budget | New desal/water EPC beyond IDE / Acciona Los Cabos / Collahuasi | miss
- 2026-10-01 | resources/niobium | cycle6 budget | New FeNb ownership/price beyond CBMM / CMOC | miss
- 2026-10-01 | resources/graphite | cycle6 budget | New graphite mine/anode beyond South Star / Nacional / Graphex / Graphcoa | miss
- 2026-10-01 | resources/balsa | cycle6 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | energy/solar | cycle6 budget | New solar plant/module award beyond SPIC/Atlas/Trina/Recurrent/Jinko/SMA | thick — miss
- 2026-10-01 | resources/nickel | cycle6 budget | New Ni ownership beyond MMG / Anglo / Vale Onça Puma / Centaurus | miss
- 2026-10-01 | energy/wind | cycle6 budget | New named-project OEM award beyond Vestas / Goldwind SPIC / Nordex | miss
- 2026-10-01 | resources/niobium | cycle7 budget | New FeNb ownership/price beyond CBMM / CMOC | miss
- 2026-10-01 | energy/solar | cycle7 budget | New solar award beyond existing thick set | thick — miss
- 2026-10-01 | resources/water | cycle7 budget | New desal/water award beyond IDE/Acciona/GS Inima/Techint | miss
- 2026-10-01 | energy/fission_smr | cycle7 budget | New SMR award beyond CAREM/INVAP/Meitner/CNNC | miss
- 2026-10-01 | infrastructure/building_materials | cycle7 budget | New cement/aggregates beyond Huaxin/Sinoma/Holcim/Carmeuse | miss
- 2026-10-01 | infrastructure/rail | cycle7 budget | New rolling-stock beyond CAF/Alstom/CRRC/Siemens | miss
- 2026-10-01 | resources/balsa | cycle7 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | resources/balsa | cycle8 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | resources/lithium | cycle8 budget | New lithium deal beyond Ganfeng/Eramet/Rio Tinto/POSCO | miss
- 2026-10-01 | energy/other_renewables | cycle8 budget | New geothermal/hydro beyond Ivirizu/Chinameca/Ormat/San Gabán | miss
- 2026-10-01 | resources/niobium | cycle8 budget | New FeNb ownership/price beyond CBMM/CMOC | miss
- 2026-10-01 | resources/graphite | cycle8 budget | New graphite mine/anode beyond South Star/Graphcoa/Urbix/Nacional/Graphex | miss
- 2026-10-01 | resources/water | cycle8 budget | New desal beyond IDE/Acciona/GS Inima/Techint | miss
- 2026-10-01 | energy/wind | cycle8 budget | New OEM award beyond Vestas/Goldwind/Nordex | miss
- 2026-10-01 | energy/power_plants_grid | cycle8 budget | New grid award beyond Siemens/Hitachi/GE set | thick — miss
- 2026-10-01 | infrastructure/bridges_roads | cycle8 budget | New highway/bridge beyond CHEC Jamaica/Colombia/Ecuador | miss
- 2026-10-01 | infrastructure/port_cranes | cycle8 budget | Named OEM for DP World Santos quay cranes | OEM unnamed — miss
- 2026-10-01 | resources/nickel | cycle8 budget | New Ni ownership beyond MMG/Anglo/Vale/Centaurus/Atlantic Nickel | miss
- 2026-10-01 | resources/lithium | cycle9 budget | New lithium deal beyond NovaAndino/Ganfeng/Rio Tinto/POSCO/Eramet | miss
- 2026-10-01 | resources/balsa | cycle9 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | resources/graphite | cycle9 budget | New graphite mine/anode beyond South Star/Graphcoa/Urbix/Nacional/Graphex | miss
- 2026-10-01 | resources/niobium | cycle9 budget | New FeNb ownership/price beyond CBMM/CMOC | miss
- 2026-10-01 | infrastructure/rail | cycle10 budget | New rail award beyond Trenes del Norte / BA Line B / Siemens ETCS | miss
- 2026-10-01 | energy/power_plants_grid | cycle10 budget | New grid award beyond Hitachi/Siemens/GE thick set | thick — miss
- 2026-10-01 | energy/wind | cycle10 budget | New OEM award beyond Vestas/Goldwind/Nordex/Envision | miss
- 2026-10-01 | resources/water | cycle10 budget | New desal beyond IDE/Acciona/GS Inima | miss
- 2026-10-01 | resources/nickel | cycle10 budget | New Ni beyond MMG/Anglo/Vale/Centaurus/Atlantic/BRN DFC | miss
- 2026-10-01 | energy/solar | cycle10 budget | New solar beyond existing thick set | thick — miss
- 2026-10-01 | infrastructure/engineering_epc | cycle10 budget | New non-grid EPC beyond Acciona/Bechtel/Hatch/Techint/Worley | miss
- 2026-10-01 | infrastructure/building_materials | cycle10 budget | New cement/aggregates beyond Holcim/Huaxin/Cemex/Carmeuse | miss
- 2026-10-01 | energy/fission_smr | cycle10 budget | New SMR beyond CAREM/Meitner/FIRST/Brazil microreactor | miss
- 2026-10-01 | energy/other_renewables | cycle10 budget | New geothermal/hydro beyond JICA/PowerChina/LaGeo | miss
- 2026-10-01 | resources/balsa | cycle10 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | energy/fission_smr | cycle11 budget | New SMR beyond CAREM/Meitner/FIRST/Brazil microreactor (Finep/CNEN unreachable) | miss
- 2026-10-01 | infrastructure/rail | cycle11 budget | New rail award beyond Trenes del Norte / BA Line B / Siemens ETCS | miss
- 2026-10-01 | resources/niobium | cycle11 budget | New FeNb ownership/price beyond CBMM/CMOC Catalão | miss
- 2026-10-01 | resources/graphite | cycle11 budget | New graphite beyond Boa Sorte/Jordânia/Urbix/Nacional/South Star | miss
- 2026-10-01 | resources/copper | cycle11 budget | New copper ownership beyond FCX/FQM/Teck/Chinalco set | miss
- 2026-10-01 | energy/power_plants_grid | cycle11 budget | New grid award beyond Hitachi/Siemens/GE thick set | thick — miss
- 2026-10-01 | energy/solar | cycle11 budget | New solar beyond existing thick set | thick — miss
- 2026-10-01 | resources/water | cycle11 budget | New desal beyond IDE/Acciona/GS Inima | miss
- 2026-10-01 | infrastructure/port_ownership | cycle11 budget | New port ownership beyond APM Suape/Hutchison/DP World/ICTSI | miss
- 2026-10-01 | infrastructure/building_materials | cycle11 budget | New cement beyond Holcim/Huaxin/Cemex/Carmeuse (CSN bids open) | miss
- 2026-10-01 | energy/other_renewables | cycle11 budget | New geothermal/hydro beyond JICA/PowerChina/LaGeo | miss
- 2026-10-01 | resources/balsa | cycle11 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | energy/wind | cycle11 budget | New OEM award beyond Vestas/Goldwind/Nordex/Envision | miss

- 2026-10-01 | infrastructure/rail | cycle12 budget | New rail award beyond Alstom Mexico / Salvador CRRC | miss
- 2026-10-01 | resources/balsa | cycle12 budget | New balsa trade year beyond WITS Ecuador 2022–2024 | miss
- 2026-10-01 | infrastructure/building_materials | cycle12 budget | New cement beyond Holcim/Huaxin/Cemex (CSN bids open) | miss
- 2026-10-01 | infrastructure/engineering_epc | cycle12 budget | New non-grid EPC beyond Worley Diablillos C11 | miss
- 2026-10-01 | resources/nickel | cycle12 budget | New Ni beyond IFC/Appian Santa Rita fund | miss
- 2026-10-01 | resources/niobium | cycle12 budget | New FeNb beyond CBMM/CMOC (R$13bn press overlaps prior) | miss
- 2026-10-01 | infrastructure/bridges_roads | cycle12 budget | New bridges/roads beyond Panamericana Oeste C11 | miss
- 2026-10-01 | energy/wind | cycle12 budget | New OEM beyond Vestas/Goldwind/Nordex/Envision | miss
- 2026-10-01 | resources/water | cycle12 budget | New desal beyond IDE/Acciona/GS Inima | miss
- 2026-10-01 | resources/copper | cycle12 budget | New copper beyond FCX/FQM/Teck/Chinalco | miss
- 2026-10-01 | energy/solar | cycle12 budget | New solar beyond thick set | thick — miss
- 2026-10-01 | energy/power_plants_grid | cycle12 budget | New grid beyond Hitachi/Siemens/GE | thick — miss
- 2026-10-01 | infrastructure/port_ownership | cycle12 budget | New port ownership beyond APM/Hutchison/DP World/ICTSI | miss
- 2026-10-01 | energy/fission_smr | cycle12 budget | New SMR beyond CAREM/Meitner/FIRST/Brazil microreactor | miss

- 2026-10-01 | energy/fission_smr | cycle13 budget | New SMR beyond FIRST/CAREM/Brazil microreactor | miss
- 2026-10-01 | infrastructure/rail | cycle13 budget | PowerChina Chancay–Sierra Central (press-only / IRJ blocked) | miss
- 2026-10-01 | energy/other_renewables | cycle13 budget | New geothermal/hydro beyond La Gina/Ormat Dominica | miss
- 2026-10-01 | infrastructure/engineering_epc | cycle13 budget | New non-grid EPC beyond Worley Diablillos | miss
- 2026-10-01 | resources/copper | cycle13 budget | New copper beyond FCX/FQM/Teck/Chinalco | miss
- 2026-10-01 | infrastructure/port_ownership | cycle13 budget | New port ownership beyond APM/Hutchison/DP World/ICTSI | miss
- 2026-10-01 | energy/wind | cycle13 budget | New OEM beyond Vestas/Goldwind/Nordex/Envision | miss
- 2026-10-01 | resources/balsa | cycle13 budget | New balsa trade year beyond WITS 2022–2024 | miss
- 2026-10-01 | resources/nickel | cycle13 budget | New Ni beyond IFC/Appian Santa Rita | miss
- 2026-10-01 | energy/power_plants_grid | cycle13 budget | New grid beyond Hitachi/Siemens/GE | thick — miss
- 2026-10-01 | infrastructure/port_cranes | cycle13 budget | New crane OEM beyond Konecranes Cartagena C12 | miss
- 2026-10-01 | resources/lithium | cycle13 budget | New Li beyond POSCO II / Zijin RIGI | miss
- 2026-10-01 | resources/graphite | cycle13 budget | New graphite beyond South Star PO C12 | miss
- 2026-10-01 | resources/niobium | cycle13 budget | New FeNb beyond CBMM/CMOC | miss
- 2026-10-01 | energy/solar | cycle13 budget | New solar beyond thick set | thick — miss

# Redesign reset (2026-10-01). Geography: Latin America and the Caribbean only.
# Shuffle rule: equal per-subcategory budgets; logged seed each cycle.
# Cycle 2 (seed 20261002): 20 sourced rows; graphite miss.
# Cycle 3 (seed 20261003): 11 sourced rows; 10 equal-budget misses on already-covered subcats.
# Cycle 4 (seed 20261004): 16 sourced rows; thin hits on fission_smr, nickel, port_cranes, building_materials;
#   also filled cycle-3 miss targets (rail, bridges_roads, copper, lithium, engineering_epc, port_ownership).
#   Equal-budget misses: power_plants_grid, balsa, niobium.
# Cycle 5 (seed 20261005): 12 sourced rows; hits on engineering_epc, niobium, solar, lithium, building_materials,
#   port_ownership, wind, port_cranes (×2), rail, nickel, copper.
#   Equal-budget misses: graphite, balsa, bridges_roads, power_plants_grid, fission_smr, other_renewables, water.
# Cycle 6 (seed 20261006): 12 sourced rows; hits on power_plants_grid, fission_smr, other_renewables, engineering_epc,
#   port_cranes, lithium, port_ownership, water, bridges_roads, copper, building_materials, rail.
#   Equal-budget misses: niobium, graphite, balsa, solar, nickel, wind.
#   Thin/cycle-5 miss fills: fission_smr, other_renewables, bridges_roads, water.
# Cycle 7 (seed 20261007): 11 sourced rows; hits on other_renewables, bridges_roads, graphite (anode JDA),
#   engineering_epc, port_ownership, copper, wind, port_cranes, power_plants_grid, nickel, lithium.
#   Equal-budget misses: niobium, solar, water, fission_smr, building_materials, rail, balsa.
# Cycle 8 (seed 20261008): 8 sourced rows; hits on engineering_epc, fission_smr (FIRST), copper, port_ownership,
#   building_materials, rail, solar.
#   Equal-budget misses: balsa, lithium, other_renewables, niobium, graphite, water, wind, power_plants_grid,
#   bridges_roads, port_cranes, nickel.
# Cycle 9 (seed 20261009): 14 sourced rows; hits on other_renewables, power_plants_grid, fission_smr, wind, rail,
#   nickel, port_ownership, water, copper, bridges_roads, port_cranes, engineering_epc, building_materials, solar.
#   Thin fills: fission_smr, nickel, port_cranes, building_materials, bridges_roads, engineering_epc.
#   Equal-budget misses: lithium, balsa, graphite, niobium.
# Cycle 10 (seed 20261010): 7 sourced rows; hits on port_ownership (APM Suape), bridges_roads (CHEC Fourth Bridge),
#   graphite (Graphcoa Jordânia), copper (FQM Taca Taca), niobium (CMOC 2025 prod), port_cranes (Sany Suape),
#   lithium (Rio Altoandinos). Thin fills: graphite, niobium, port_cranes.
#   Equal-budget misses: rail, power_plants_grid, wind, water, nickel, solar, engineering_epc, building_materials,
#   fission_smr, other_renewables, balsa.
# Cycle 11 (seed 20261011): 5 sourced rows; hits on bridges_roads (Panamericana Oeste APP), nickel (IFC/Appian
#   Santa Rita fund), port_cranes (Konecranes Yucatán ESP.7), lithium (Zijin/Liex Tres Quebradas RIGI),
#   engineering_epc (Worley Diablillos LNTP). Thin fills: nickel, port_cranes, engineering_epc, bridges_roads.
#   Equal-budget misses: fission_smr, rail, niobium, graphite, copper, power_plants_grid, solar, water,
#   port_ownership, building_materials, other_renewables, balsa, wind.

# Cycle 12 (seed 20261012): 5 sourced rows; hits on lithium (POSCO Sal de Oro II RIGI), other_renewables
#   (Acciona La Gina DR + Ormat Dominica geothermal PPA), graphite (South Star 36t PO),
#   port_cranes (Konecranes Cartagena 25 RTGs). Thin fills: graphite, port_cranes, other_renewables.
#   Equal-budget misses: rail, balsa, building_materials, engineering_epc, nickel, niobium,
#   bridges_roads, wind, water, copper, solar, power_plants_grid, port_ownership, fission_smr.

# Cycle 13 (seed 20261013): 3 sourced rows; hits on building_materials (Heidelberg Cementos Inka),
#   water (Cox Rosarito desal USD 304m), bridges_roads (CRBC Arequipa–La Joya OxI — UNVERIFIED PEN).
#   Thin fills: building_materials, water, bridges_roads.
#   Equal-budget misses: fission_smr, rail, other_renewables, engineering_epc, copper, port_ownership,
#   wind, balsa, nickel, power_plants_grid, port_cranes, lithium, graphite, niobium, solar.

# Cycle 14 (seed 20261014): 6 sourced rows; hits on port_ownership (APM Callao Stage 3B USD 570m proxy),
#   wind (Vestas Esquina do Vento 230 MW + Goldwind Sento Sé 872 MW), lithium (Ganfeng USD 180m LAAC note),
#   engineering_epc (Lycopodium San Cristóbal A$37m + M3/Vizsla Panuco USD 170m).
#   Equal-budget misses: rail, fission_smr, bridges_roads, port_cranes, niobium, balsa, solar, graphite,
#   power_plants_grid, copper, nickel, water, building_materials, other_renewables.

# Cycle 15 (seed 20261015): 4 sourced rows; hits on engineering_epc (Sedgman Colossus REE),
#   port_cranes (ZPMC Tecon Rio Grande R$290m proxy), nickel (Centaurus BNDES LOI R$1bn + Glencore offtake).
#   Thin fills: nickel, port_cranes, engineering_epc.
#   Equal-budget misses: rail, balsa, wind, building_materials, graphite, power_plants_grid, copper,
#   bridges_roads, water, fission_smr, port_ownership, lithium, solar, other_renewables, niobium.

# Cycle 16 (seed 20261016): 3 sourced rows; hits on water (Sacyr Coquimbo desal USD 318m),
#   niobium (CBMM/Echion XNO anode plant Araxá), bridges_roads (CCECC Quinto Puente 1A USD 115.9m proxy).
#   Thin fills: niobium, water, bridges_roads.
#   Equal-budget misses: engineering_epc, graphite, port_ownership, balsa, wind, solar, nickel,
#   port_cranes, rail, lithium, other_renewables, copper, fission_smr, power_plants_grid, building_materials.

# Cycle 17 (seed 20261017): 2 sourced rows; hits on fission_smr (Nuclearis N1 FOAK proxy USD 600m),
#   rail (Hitachi Energy / Trívia Trens SP Lines 11–13 power supply).
#   Thin fills: fission_smr, rail.
#   Equal-budget misses: balsa, power_plants_grid, wind, niobium, bridges_roads, water, building_materials,
#   engineering_epc, nickel, other_renewables, lithium, port_cranes, graphite, solar, port_ownership, copper.

# Cycle 33 (seed 20261033): 4 new sourced rows (+2 value/evidence upgrades); hits on bridges_roads
#   (ERG El Estanquillo–Popayán COP 6.56tn ANI), solar (Aldesa/CRCC Mexico hybrid >EUR 160m proxy),
#   port_cranes (Portonave electric fleet BRL 61m), graphite (Atlas Malacacheta MRE USD 2.145m).
#   Upgrades: crbc_arequipa_la_joya_2026 → MTC documented; jervois_smp_restart_2025 CAPEX proxy USD 130m.
#   Thin fills: graphite, bridges_roads.
#   Equal-budget misses: balsa, water, port_ownership, rail, nickel (update only), engineering_epc,
#   fission_smr, power_plants_grid, niobium, wind, other_renewables, lithium, building_materials, copper.

# Cycle 34 (seed 20261034): 7 sourced rows; hits on building_materials (InterCement LATCEM inject USD 110m proxy),
#   lithium (Galan HMW RIGI USD 217.09m), other_renewables (Enal Celaya geothermal USD 80m proxy),
#   port_cranes (SSA Guaymas STS/eRTG), copper (MMG Las Bambas 2026 capex USD 800m floor),
#   bridges_roads (Sierra Tramo 4 USD 1.582bn), solar (Trina Sidón USD 100m proxy).
#   Thin fills: building_materials, bridges_roads.
#   Equal-budget misses: graphite, wind, niobium, port_ownership, power_plants_grid, engineering_epc,
#   water, fission_smr, balsa, nickel, rail.

# Cycle 35 (seed 20261035): 6 new sourced rows (+1 Graphcoa CAPEX refresh); hits on building_materials
#   (CBB Mejillones USD 42m; Cruz Azul Hidalgo USD 383m), power_plants_grid (Hitachi Brazil +USD 70m),
#   wind (Goldwind FINAME >470 MW), other_renewables (Jinko BESS Amanecer USD 500m),
#   niobium (CBMM 2026 spend R$2bn). Graphite: refreshed Jordânia to EIA-cited R$621.76m / USD 120m.
#   Thin fills: niobium, building_materials.
#   Equal-budget misses: port_cranes, copper, engineering_epc, bridges_roads, solar, rail, lithium,
#   fission_smr, nickel, water, port_ownership, balsa.

# Cycle 36 (seed 20261036): 7 sourced rows; hits on nickel (Brazilian Nickel Piauí CAPEX USD 1.4bn proxy),
#   building_materials (Holcim Macuspana grind USD 55m), solar (PowerChina Intrepid/Mauriti R$1.8bn),
#   niobium (St George Araxá A$60m Hancock placement), balsa (AIMA Spain 5.08% share ~USD 15.3m),
#   rail (PowerChina Chancay–Sierra Central USD 420m proxy), port_ownership (Hutchison ICAVE Fase II MXN 4.5bn).
#   Thin fills: nickel, niobium, balsa, rail.
#   Equal-budget misses: fission_smr, power_plants_grid, wind, lithium, copper, graphite,
#   bridges_roads, other_renewables, port_cranes, water, engineering_epc.

# Cycle 37 (seed 20261037): 9 sourced rows; hits on graphite (Graphcoa Jordânia USD 8m development),
#   nickel (Canada ECA up to USD 275m), building_materials (Holcim VES Villa 1 S/13.1m),
#   other_renewables (Jinko Aloe BESS USD 340m; AES Pampas PF USD 550m), port_cranes (ZPMC TCP Montevideo STS),
#   engineering_epc (GES Pampas EPC), port_ownership (Katoen Natie TCP USD 455m),
#   bridges_roads (Contreras Vicuña Corredor Norte USD 135m).
#   Thin fills: graphite, nickel, engineering_epc, bridges_roads.
#   Equal-budget misses: copper, niobium, water, solar, fission_smr, power_plants_grid, rail,
#   lithium, balsa, wind.

# Cycle 38 (seed 20261038): 5 sourced rows; hits on port_cranes (Kalmar TCP 20 hybrid straddles),
#   other_renewables (Acciona El Romero BESS 196MW/980MWh), water (Antofagasta Zaldívar USD 0.9bn),
#   fission_smr (Peru SMR promotion law; U.S.–Ecuador civil nuclear MoU).
#   Thin fills: water, fission_smr.
#   Equal-budget misses: rail, nickel, balsa, graphite, building_materials, lithium, solar,
#   port_ownership, wind, bridges_roads, niobium, power_plants_grid, engineering_epc, copper.

# Cycle 39 (seed 20261039): 5 sourced rows; hits on lithium (BID Invest Posco Sal de Oro up to USD 700m),
#   bridges_roads (Mota-Engil Santos–Guarujá tunnel R$6.8bn), rail (ACA Transnordestina R$312.8m;
#   Tren Macho Huancayo–Huancavelica USD 339m), copper (McEwen Los Azules USD 240m financing proxy).
#   Thin fills: rail, copper.
#   Equal-budget misses: wind, graphite, port_cranes, building_materials, other_renewables,
#   power_plants_grid, nickel, water, niobium, port_ownership, fission_smr, solar, balsa, engineering_epc.

# Cycle 40 (seed 20261040): 9 new sourced rows (+1 Chancay Phase I USD value fill; +9 lat/lon fills);
#   hits on bridges_roads (CAF Salvador–Itaparica up to USD 150m), solar (Ganfeng Mariana solar USD 190m),
#   other_renewables (BYD Brazil BESS factory up to R$500m), water (Sacyr Antofagasta reuse ~USD 292m),
#   fission_smr (INB–Westinghouse fuel-cycle coop), niobium (Codemig–CBMM renewal to 2070),
#   graphite (Graphcoa→Allied Graphite U.S. anode offtake path), wind (Nordex Ecuador 112 MW;
#   WEG/Statkraft Seabra 7 MW / Petrobras R$130m).
#   Thin fills: water, fission_smr, niobium, graphite, wind.
#   Equal-budget misses: nickel, lithium, balsa, port_cranes, building_materials, port_ownership
#   (value fill only), engineering_epc, copper, power_plants_grid, rail.

# Cycle 41 (seed 20261041): 8 sourced rows (5 shuffled + 3 thin_topup);
#   shuffled hits: solar (Polaris–CFE Mexico ~USD 217m), balsa (AIMA–Siemens Energy MoU),
#   engineering_epc (CHEC/CCCC Chancay port works USD 600m), wind (EDF Diana Jacobina 142.5 MW),
#   other_renewables (Cubico–CFE ~USD 1bn + BESS).
#   Thin_topup (balsa/graphite/fission_smr): Peru FIRST bilateral partner (us);
#   Graphcoa cumulative ~USD 75m invested; balsa thin miss (MoU already in pass).
#   Also logged St George Araxá ~R$3bn CAPEX plan (niobium) in thin window.
#   rows_by_side: us 1 / prc 1 / allied 6 / other 0.
#   Equal-budget misses: port_ownership, rail, power_plants_grid, port_cranes, bridges_roads,
#   nickel, copper, water, lithium, building_materials (+ balsa thin miss).

# Cycle 42 (seed 20261042): 8 new sourced rows (+1 Albemarle TED USD 3.1bn value fill);
#   shuffled: copper (Chilean Cobalt EXIM LOI USD 375m us), lithium (Albemarle La Negra pilot USD 30m us;
#   TED CAPEX fill), nickel (Centaurus Jaguar intl finance up to USD 320m), building_materials
#   (Holcim Geocycle Tecomán MXN 200m), port_ownership (APM Lazaro Phase III >USD 350m),
#   solar (FinDev Canada Illa USD 56m).
#   Thin_topup (balsa/graphite/fission_smr): WITS Ecuador HS 440723 2025 China USD 144.8m /
#   US USD 4.7m pair (China row evidence=paired — third paired LatAm row); graphite/fission miss.
#   rows_by_side: us 3 / prc 1 / allied 4 / other 0.
#   Equal-budget misses: other_renewables, wind, water, graphite, port_cranes, rail,
#   power_plants_grid, engineering_epc, niobium, balsa (shuffled; filled in thin), fission_smr, bridges_roads.

# Cycle 43 (seed 20261043): 12 sourced rows (10 shuffled + 2 thin_topup);
#   shuffled: other_renewables (AES Andes Solar III hub >USD 1.3bn us), lithium (EXIM Argentina
#   Build the Future up to USD 7bn us; Ganfeng LAR debt USD 130m prc), rail (Mota-Engil
#   Querétaro–Irapuato Tramo I ~EUR 290m + Tramo II ~EUR 820m), wind (Vestas Emma Peru 72 MW OEM),
#   fission_smr (Argentina FIRST LAC workshop us), niobium (St George–REAlloys U.S. offtake MoU),
#   graphite (South Star Santa Cruz restart), power_plants_grid (EXIM Guyana GtE ~USD 527m us).
#   Thin_topup (balsa/graphite/fission_smr): Plantabal 2025 planting 2,951 ha; Graphcoa Boa Sorte
#   →Urbix U.S. export path; fission thin miss.
#   rows_by_side: us 6 / prc 1 / allied 5 / other 0.
#   Equal-budget misses: nickel, port_ownership, water, building_materials, port_cranes,
#   bridges_roads, solar, balsa (shuffled; filled in thin), engineering_epc, copper.

# Cycle 57 (seed 20261057): 15 sourced rows (12 shuffled + 3 thin_topup);
#   shuffled: engineering_epc (McDermott Polok/Chinwol FEED us), wind (AES Villagrán USD 726m
#   proxy us), port_cranes (ZPMC Itapoá STS8 prc), graphite (South Star June ramp filled in
#   thin), solar (ARRAY Lupi OmniTrack us; Nextracker Libélula us), balsa (DIAB ProBalsa filled
#   in thin), port_ownership (FMS Peru Callao Naval USD 1.5bn us), other_renewables (AES San
#   Agustín USD 73m proxy us), fission_smr (Colombia–US civil nuclear MOU us), power_plants_grid
#   (GE Vernova São Simão UG3 us; PowerChina São Simão BOP prc), niobium (St George MRE filled
#   in thin), building_materials (Sinoma Cibao clinker prc), water (ENAPAC Solaer USD 1.5bn
#   proxy allied).
#   Thin_topup (niobium/balsa/graphite): St George Araxá MRE Nb (allied); DIAB Ecuador ProBalsa
#   (allied); South Star Santa Cruz June 2026 ROM ramp (allied).
#   rows_by_side: us 8 / prc 3 / allied 4 / other 0.
#   Equal-budget misses: nickel, bridges_roads, rail, lithium, copper,
#   niobium/balsa/graphite (filled in thin).

# Cycle 52 (seed 20261052): 9 sourced rows (8 shuffled + 1 thin_topup);
#   shuffled: wind (ENGIE Serra Assuruá 846 MW R$6bn/~USD 1.2bn), engineering_epc (Xinhai Araxá
#   EPC MoU A$8m prc), solar (ContourGlobal Los Maitenes 131 MWp + 90 MW BESS us),
#   niobium (Boston Metal MOE FeNb MoU us), rail (CRRC SP Metro Frota R R$3.104bn prc),
#   power_plants_grid (ENGIE Asa Branca TX BRL 2.7bn/~USD 540m), lithium (EXIM Lithium Ionic
#   Bandeira LOI USD 266m us), copper (Capstone Mantoverde Optimized USD 176m).
#   Thin_topup (niobium/fission_smr/building): Jamaica AECL/CNL SMR MoU (allied);
#   niobium/building thin misses.
#   rows_by_side: us 3 / prc 2 / allied 4 / other 0.
#   Equal-budget misses: fission_smr (filled in thin), building_materials, nickel, port_ownership,
#   balsa, water, port_cranes, bridges_roads, graphite, other_renewables.

# 2026-10-01 graphite taxonomy correction (Ben): former dimension_stone/granite
# renamed to graphite everywhere. ABIROCHAS ornamental-stone rows archived (exclude).
# Hunt retargeted to LatAm graphite mining/processing/anode chains; logged South Star,
# Nacional de Grafite, Graphex–Santa Cruz offtake; Cycle 4 added Graphcoa Boa Sorte.
