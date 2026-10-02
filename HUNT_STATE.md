updated: 2026-10-02
cycle: 91
remote: present
active_layer: energy
active_subcategory: other_renewables
next_query: Cycle 92 shuffle_seed=20261092; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us213/prc214/allied227); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: fission_smr/balsa/graphite then nickel. Keep US/PRC even split. If thin dry, move top-up to next-thinnest (niobium/building_materials). Country×subcategory sweep both sides + regulators.
next_row_id: (follow cycle-92 shuffled_order)
dry_streak: 0

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
