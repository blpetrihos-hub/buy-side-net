updated: 2026-10-01
cycle: 54
remote: present
active_layer: resources
active_subcategory: balsa
next_query: Cycle 55 shuffle_seed=20261055; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory spend ≥1/3 budget on U.S. investors/firms (EDGAR/DFC/EXIM/USTDA/company/embassy/Commerce + ES/PT coverage of U.S. firms); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); graphite = mining/processing/anode chains (Brazil, Mexico). Prefer thin: balsa (21), then niobium/building_materials/copper/nickel/graphite/fission_smr/wind (22). For balsa prefer plantations/processors/wind-blade/offtakes/named projects — no duplicate trade/financing rows.
next_row_id: (follow cycle-55 shuffled_order)
dry_streak: 0

# Per-cycle shuffle (BRIEF.md):
# (1) Seeded shuffle of all 18 subcategories; equal base budget per subcategory.
# (2) Side balance: within each subcategory time box, spend ≥1/3 of the budget on
#     U.S. investors/firms (SEC EDGAR, DFC, U.S. EXIM, USTDA, U.S. company releases
#     and investor decks, U.S. embassy/Commerce notices, plus Spanish/Portuguese
#     coverage of U.S. firms); log rows_by_side_this_cycle.
# (3) Thin-subcategory top-up: after the shuffled pass, the 3 subcategories with
#     the fewest active rows (recompute each cycle) each get one extra half-budget.

shuffle_seed: 20261054
budget_per_subcategory: 1_source_family_min
# Equal base time box: at least one opened public source family (or documented miss)
# per subcategory before moving on. Same base budget for every subcategory.
# Within each box, reserve ≥1/3 for U.S.-side search (see BRIEF.md Rotation).

shuffled_order:
- energy/wind
- resources/lithium
- resources/nickel
- resources/graphite
- resources/niobium
- resources/water
- infrastructure/rail
- energy/other_renewables
- energy/solar
- resources/copper
- energy/fission_smr
- infrastructure/port_cranes
- energy/power_plants_grid
- infrastructure/engineering_epc
- infrastructure/port_ownership
- infrastructure/bridges_roads
- infrastructure/building_materials
- resources/balsa

rows_found_this_cycle:
  energy/wind: 0
  resources/lithium: 0
  resources/nickel: 1
  resources/graphite: 1
  resources/niobium: 1
  resources/water: 1
  infrastructure/rail: 1
  energy/other_renewables: 1
  energy/solar: 1
  resources/copper: 0
  energy/fission_smr: 0
  infrastructure/port_cranes: 1
  energy/power_plants_grid: 0
  infrastructure/engineering_epc: 0
  infrastructure/port_ownership: 1
  infrastructure/bridges_roads: 0
  infrastructure/building_materials: 0
  resources/balsa: 0

coverage_cumulative:
  # Active+hunt (non-archived, non-exclude) observation counts after cycle 54
  # (+ equal-pass: Fluence Tubarão SWRO / CCECC–Aldesa Querétaro–Irapuato /
  #   ContourGlobal Quillagua inaug / POWERCHINA Palmira III /
  #   SSA MIT ASC ZPMC / SSA–Blackstone Panama interest;
  #   thin_topup: CBMM–Toshiba Nb-oxide plant planned / Millstreet SMP USD 70m /
  #   South Star Sprott Phase 2 CapEx stream)
  infrastructure/port_ownership: 28
  infrastructure/port_cranes: 27
  infrastructure/rail: 30
  infrastructure/bridges_roads: 23
  infrastructure/building_materials: 22
  infrastructure/engineering_epc: 24
  resources/niobium: 22
  resources/lithium: 28
  resources/copper: 22
  resources/nickel: 22
  resources/graphite: 22
  resources/balsa: 21
  resources/water: 23
  energy/fission_smr: 22
  energy/solar: 26
  energy/wind: 22
  energy/power_plants_grid: 27
  energy/other_renewables: 31

# Side balance log (BRIEF Rotation §2). Required each cycle from cycle 41 on.
rows_by_side_this_cycle:
  us: 5
  prc: 2
  allied: 2
  other: 0

# Thin-subcategory top-up (BRIEF Rotation §3). After shuffled pass, 3 fewest active
# rows each get half of budget_per_subcategory. Recompute each cycle. From cycle 41 on.
# Post-pass thinnest: niobium/nickel/graphite/balsa (21).
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/niobium
  - resources/nickel
  - resources/graphite
  # Hits: CBMM–Toshiba planned 1,000 tpy oxide plant; Millstreet USD 70m SMP equity;
  #   South Star Sprott Phase 2 CapEx USD 27m / stream up to USD 18m.
  # Balsa remained miss (Plantabal/CoreLite/WITS already dense).

# Side balance log (BRIEF Rotation §2) — cycle 53
rows_by_side_this_cycle_cycle53:
  us: 3
  prc: 4
  allied: 2
  other: 0

# Side balance log (BRIEF Rotation §2) — cycle 52
rows_by_side_this_cycle_cycle52:
  us: 3
  prc: 2
  allied: 4
  other: 0

coverage_cumulative_cycle52:
  # Active+hunt after cycle 52
  infrastructure/port_ownership: 27
  infrastructure/port_cranes: 26
  infrastructure/rail: 28
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 21
  infrastructure/engineering_epc: 24
  resources/niobium: 19
  resources/lithium: 27
  resources/copper: 22
  resources/nickel: 21
  resources/graphite: 21
  resources/balsa: 21
  resources/water: 21
  energy/fission_smr: 21
  energy/solar: 24
  energy/wind: 22
  energy/power_plants_grid: 27
  energy/other_renewables: 29

# Side balance log (BRIEF Rotation §2) — cycle 51
rows_by_side_this_cycle_cycle51:
  us: 3
  prc: 0
  allied: 1
  other: 0

coverage_cumulative_cycle51:
  # Active+hunt after cycle 51
  infrastructure/port_ownership: 27
  infrastructure/port_cranes: 26
  infrastructure/rail: 27
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 21
  infrastructure/engineering_epc: 23
  resources/niobium: 19
  resources/lithium: 26
  resources/copper: 21
  resources/nickel: 21
  resources/graphite: 21
  resources/balsa: 21
  resources/water: 21
  energy/fission_smr: 20
  energy/solar: 23
  energy/wind: 21
  energy/power_plants_grid: 27
  energy/other_renewables: 29

# Side balance log (BRIEF Rotation §2) — cycle 50
rows_by_side_this_cycle_cycle50:
  us: 3
  prc: 0
  allied: 2
  other: 1

coverage_cumulative_cycle50:
  # Active+hunt after cycle 50
  infrastructure/port_ownership: 27
  infrastructure/port_cranes: 26
  infrastructure/rail: 26
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 21
  infrastructure/engineering_epc: 22
  resources/niobium: 19
  resources/lithium: 26
  resources/copper: 21
  resources/nickel: 21
  resources/graphite: 21
  resources/balsa: 20
  resources/water: 21
  energy/fission_smr: 20
  energy/solar: 23
  energy/wind: 20
  energy/power_plants_grid: 27
  energy/other_renewables: 29

# Side balance log (BRIEF Rotation §2) — cycle 49
rows_by_side_this_cycle_cycle49:
  us: 4
  prc: 0
  allied: 0
  other: 1

coverage_cumulative_cycle49:
  # Active+hunt after cycle 49
  infrastructure/port_ownership: 26
  infrastructure/port_cranes: 26
  infrastructure/rail: 26
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 20
  infrastructure/engineering_epc: 21
  resources/niobium: 19
  resources/lithium: 26
  resources/copper: 21
  resources/nickel: 20
  resources/graphite: 21
  resources/balsa: 19
  resources/water: 20
  energy/fission_smr: 20
  energy/solar: 23
  energy/wind: 20
  energy/power_plants_grid: 27
  energy/other_renewables: 29

# Side balance log (BRIEF Rotation §2) — cycle 48
rows_by_side_this_cycle_cycle48:
  us: 3
  prc: 2
  allied: 4
  other: 1

coverage_cumulative_cycle48:
  # Active+hunt after cycle 48
  infrastructure/port_ownership: 26
  infrastructure/port_cranes: 26
  infrastructure/rail: 26
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 20
  infrastructure/engineering_epc: 21
  resources/niobium: 19
  resources/lithium: 26
  resources/copper: 21
  resources/nickel: 20
  resources/graphite: 20
  resources/balsa: 18
  resources/water: 20
  energy/fission_smr: 19
  energy/solar: 23
  energy/wind: 20
  energy/power_plants_grid: 25
  energy/other_renewables: 29

# Side balance log (BRIEF Rotation §2) — cycle 47
rows_by_side_this_cycle_cycle47:
  us: 4
  prc: 0
  allied: 1
  other: 0

coverage_cumulative_cycle47:
  # Active+hunt after cycle 47
  infrastructure/port_ownership: 24
  infrastructure/port_cranes: 26
  infrastructure/rail: 24
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 20
  infrastructure/engineering_epc: 21
  resources/niobium: 17
  resources/lithium: 26
  resources/copper: 20
  resources/nickel: 19
  resources/graphite: 20
  resources/balsa: 17
  resources/water: 19
  energy/fission_smr: 19
  energy/solar: 22
  energy/wind: 20
  energy/power_plants_grid: 24
  energy/other_renewables: 29

coverage_cumulative:
  # Active+hunt (non-archived, non-exclude) observation counts after cycle 44
  # (+ thin_topup: Aguas Pacífico desal CAPEX USD 1.2bn; paired Fangda↔REAlloys Araxá MoUs)
  infrastructure/port_ownership: 22
  infrastructure/port_cranes: 25
  infrastructure/rail: 23
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 20
  infrastructure/engineering_epc: 20
  resources/niobium: 18
  resources/lithium: 25
  resources/copper: 20
  resources/nickel: 17
  resources/graphite: 18
  resources/balsa: 15
  resources/water: 18
  energy/fission_smr: 17
  energy/solar: 21
  energy/wind: 19
  energy/power_plants_grid: 25
  energy/other_renewables: 27

# Side balance log (BRIEF Rotation §2) — cycle 44
rows_by_side_this_cycle_cycle44:
  us: 5
  prc: 1
  allied: 1
  other: 1

coverage_cumulative:
  # Active+hunt (non-archived, non-exclude) observation counts after cycle 43
  # (+ thin_topup: Plantabal 2025 planting; Graphcoa Boa Sorte→Urbix U.S. export)
  infrastructure/port_ownership: 21
  infrastructure/port_cranes: 25
  infrastructure/rail: 23
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 20
  infrastructure/engineering_epc: 20
  resources/niobium: 16
  resources/lithium: 24
  resources/copper: 20
  resources/nickel: 17
  resources/graphite: 17
  resources/balsa: 15
  resources/water: 17
  energy/fission_smr: 16
  energy/solar: 21
  energy/wind: 19
  energy/power_plants_grid: 24
  energy/other_renewables: 26

# Side balance log (BRIEF Rotation §2) — cycle 43
rows_by_side_this_cycle_cycle43:
  us: 6
  prc: 1
  allied: 5
  other: 0

coverage_cumulative:
  # Active+hunt (non-archived, non-exclude) observation counts after cycle 42
  # (+ Albemarle TED CAPEX fill USD 3.1bn; thin_topup WITS Ecuador balsa 2025 CN/US pair)
  infrastructure/port_ownership: 21
  infrastructure/port_cranes: 25
  infrastructure/rail: 21
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 20
  infrastructure/engineering_epc: 20
  resources/niobium: 15
  resources/lithium: 22
  resources/copper: 20
  resources/nickel: 17
  resources/graphite: 15
  resources/balsa: 14
  resources/water: 17
  energy/fission_smr: 15
  energy/solar: 21
  energy/wind: 18
  energy/power_plants_grid: 23
  energy/other_renewables: 25

coverage_cumulative:
  # Active+hunt (non-archived, non-exclude) observation counts after cycle 41
  # (+ thin_topup: peru FIRST bilateral; Graphcoa USD 75m cumulative; St George Araxá R$3bn plan)
  infrastructure/port_ownership: 20
  infrastructure/port_cranes: 25
  infrastructure/rail: 21
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 19
  infrastructure/engineering_epc: 20
  resources/niobium: 15
  resources/lithium: 21
  resources/copper: 19
  resources/nickel: 16
  resources/graphite: 15
  resources/balsa: 12
  resources/water: 17
  energy/fission_smr: 15
  energy/solar: 20
  energy/wind: 18
  energy/power_plants_grid: 23
  energy/other_renewables: 25

coverage_cumulative:
  # Active+hunt (non-archived, non-exclude) observation counts after cycle 40
  # Also: cosco_chancay_port_2024 Phase I USD 1.3bn value fill; filled lat/lon for
  # Ciranda, XDCB NE UHV, WITS balsa trade flows, Jinko Brazil imports (cmoc_argus price series still blank).
  infrastructure/port_ownership: 20
  infrastructure/port_cranes: 25
  infrastructure/rail: 21
  infrastructure/bridges_roads: 22
  infrastructure/building_materials: 19
  infrastructure/engineering_epc: 19
  resources/niobium: 15
  resources/lithium: 21
  resources/copper: 19
  resources/nickel: 16
  resources/graphite: 14
  resources/balsa: 11
  resources/water: 17
  energy/fission_smr: 14
  energy/solar: 19
  energy/wind: 17
  energy/power_plants_grid: 23
  energy/other_renewables: 24

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 39
  infrastructure/port_ownership: 20
  infrastructure/port_cranes: 25
  infrastructure/rail: 21
  infrastructure/bridges_roads: 21
  infrastructure/building_materials: 19
  infrastructure/engineering_epc: 19
  resources/niobium: 13
  resources/lithium: 21
  resources/copper: 19
  resources/nickel: 16
  resources/graphite: 13
  resources/balsa: 11
  resources/water: 16
  energy/fission_smr: 13
  energy/solar: 18
  energy/wind: 15
  energy/power_plants_grid: 22
  energy/other_renewables: 23

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 38
  infrastructure/port_ownership: 20
  infrastructure/port_cranes: 25
  infrastructure/rail: 19
  infrastructure/bridges_roads: 20
  infrastructure/building_materials: 19
  infrastructure/engineering_epc: 19
  resources/niobium: 13
  resources/lithium: 20
  resources/copper: 18
  resources/nickel: 16
  resources/graphite: 13
  resources/balsa: 11
  resources/water: 16
  energy/fission_smr: 13
  energy/solar: 18
  energy/wind: 15
  energy/power_plants_grid: 22
  energy/other_renewables: 23

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 33
  # Also upgraded crbc_arequipa_la_joya_2026 to MTC documented; filled jervois_smp_restart_2025 CAPEX proxy (not new ids).
  infrastructure/port_ownership: 18
  infrastructure/port_cranes: 22
  infrastructure/rail: 18
  infrastructure/bridges_roads: 18
  infrastructure/building_materials: 14
  infrastructure/engineering_epc: 18
  resources/niobium: 11
  resources/lithium: 19
  resources/copper: 17
  resources/nickel: 14
  resources/graphite: 12
  resources/balsa: 10
  resources/water: 15
  energy/fission_smr: 11
  energy/solar: 16
  energy/wind: 14
  energy/power_plants_grid: 21
  energy/other_renewables: 18

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 32
  infrastructure/port_ownership: 18
  infrastructure/port_cranes: 21
  infrastructure/rail: 18
  infrastructure/bridges_roads: 17
  infrastructure/building_materials: 14
  infrastructure/engineering_epc: 18
  resources/niobium: 11
  resources/lithium: 19
  resources/copper: 17
  resources/nickel: 14
  resources/graphite: 11
  resources/balsa: 10
  resources/water: 15
  energy/fission_smr: 11
  energy/solar: 15
  energy/wind: 14
  energy/power_plants_grid: 21
  energy/other_renewables: 18

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 31
  # Also refreshed fcx_el_abra_mill_chile_2026 with USD 7.5bn company primary (value fill; not a new id).
  infrastructure/port_ownership: 18
  infrastructure/port_cranes: 20
  infrastructure/rail: 17
  infrastructure/bridges_roads: 17
  infrastructure/building_materials: 13
  infrastructure/engineering_epc: 18
  resources/niobium: 11
  resources/lithium: 19
  resources/copper: 16
  resources/nickel: 14
  resources/graphite: 11
  resources/balsa: 10
  resources/water: 14
  energy/fission_smr: 11
  energy/solar: 15
  energy/wind: 14
  energy/power_plants_grid: 21
  energy/other_renewables: 18

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 30
  infrastructure/port_ownership: 18
  infrastructure/port_cranes: 19
  infrastructure/rail: 17
  infrastructure/bridges_roads: 16
  infrastructure/building_materials: 13
  infrastructure/engineering_epc: 18
  resources/niobium: 11
  resources/lithium: 18
  resources/copper: 15
  resources/nickel: 13
  resources/graphite: 11
  resources/balsa: 10
  resources/water: 13
  energy/fission_smr: 11
  energy/solar: 14
  energy/wind: 13
  energy/power_plants_grid: 21
  energy/other_renewables: 17

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 29
  infrastructure/port_ownership: 18
  infrastructure/port_cranes: 19
  infrastructure/rail: 16
  infrastructure/bridges_roads: 15
  infrastructure/building_materials: 13
  infrastructure/engineering_epc: 18
  resources/niobium: 10
  resources/lithium: 17
  resources/copper: 15
  resources/nickel: 13
  resources/graphite: 11
  resources/balsa: 10
  resources/water: 13
  energy/fission_smr: 11
  energy/solar: 14
  energy/wind: 13
  energy/power_plants_grid: 21
  energy/other_renewables: 17

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 28
  infrastructure/port_ownership: 17
  infrastructure/port_cranes: 18
  infrastructure/rail: 15
  infrastructure/bridges_roads: 14
  infrastructure/building_materials: 12
  infrastructure/engineering_epc: 17
  resources/niobium: 10
  resources/lithium: 17
  resources/copper: 15
  resources/nickel: 13
  resources/graphite: 11
  resources/balsa: 10
  resources/water: 13
  energy/fission_smr: 11
  energy/solar: 13
  energy/wind: 13
  energy/power_plants_grid: 21
  energy/other_renewables: 16

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 27
  infrastructure/port_ownership: 17
  infrastructure/port_cranes: 17
  infrastructure/rail: 15
  infrastructure/bridges_roads: 14
  infrastructure/building_materials: 12
  infrastructure/engineering_epc: 17
  resources/niobium: 9
  resources/lithium: 16
  resources/copper: 15
  resources/nickel: 13
  resources/graphite: 11
  resources/balsa: 8
  resources/water: 13
  energy/fission_smr: 11
  energy/solar: 13
  energy/wind: 13
  energy/power_plants_grid: 21
  energy/other_renewables: 15

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 26
  infrastructure/port_ownership: 16
  infrastructure/port_cranes: 17
  infrastructure/rail: 14
  infrastructure/bridges_roads: 14
  infrastructure/building_materials: 11
  infrastructure/engineering_epc: 17
  resources/niobium: 9
  resources/lithium: 16
  resources/copper: 14
  resources/nickel: 13
  resources/graphite: 10
  resources/balsa: 7
  resources/water: 12
  energy/fission_smr: 10
  energy/solar: 13
  energy/wind: 13
  energy/power_plants_grid: 20
  energy/other_renewables: 15

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 25
  infrastructure/port_ownership: 16
  infrastructure/port_cranes: 16
  infrastructure/rail: 14
  infrastructure/bridges_roads: 14
  infrastructure/building_materials: 11
  infrastructure/engineering_epc: 17
  resources/niobium: 9
  resources/lithium: 16
  resources/copper: 13
  resources/nickel: 13
  resources/graphite: 9
  resources/balsa: 7
  resources/water: 12
  energy/fission_smr: 10
  energy/solar: 13
  energy/wind: 13
  energy/power_plants_grid: 20
  energy/other_renewables: 14

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 24
  infrastructure/port_ownership: 16
  infrastructure/port_cranes: 16
  infrastructure/rail: 13
  infrastructure/bridges_roads: 13
  infrastructure/building_materials: 10
  infrastructure/engineering_epc: 17
  resources/niobium: 8
  resources/lithium: 15
  resources/copper: 13
  resources/nickel: 13
  resources/graphite: 9
  resources/balsa: 7
  resources/water: 12
  energy/fission_smr: 10
  energy/solar: 12
  energy/wind: 13
  energy/power_plants_grid: 20
  energy/other_renewables: 13

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 23
  infrastructure/port_ownership: 16
  infrastructure/port_cranes: 15
  infrastructure/rail: 13
  infrastructure/bridges_roads: 13
  infrastructure/building_materials: 10
  infrastructure/engineering_epc: 17
  resources/niobium: 8
  resources/lithium: 14
  resources/copper: 13
  resources/nickel: 13
  resources/graphite: 9
  resources/balsa: 7
  resources/water: 11
  energy/fission_smr: 9
  energy/solar: 12
  energy/wind: 13
  energy/power_plants_grid: 20
  energy/other_renewables: 13

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 22
  infrastructure/port_ownership: 15
  infrastructure/port_cranes: 15
  infrastructure/rail: 13
  infrastructure/bridges_roads: 13
  infrastructure/building_materials: 10
  infrastructure/engineering_epc: 17
  resources/niobium: 8
  resources/lithium: 14
  resources/copper: 12
  resources/nickel: 13
  resources/graphite: 9
  resources/balsa: 7
  resources/water: 11
  energy/fission_smr: 8
  energy/solar: 11
  energy/wind: 13
  energy/power_plants_grid: 20
  energy/other_renewables: 12

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 21
  infrastructure/port_ownership: 15
  infrastructure/port_cranes: 15
  infrastructure/rail: 13
  infrastructure/bridges_roads: 13
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 17
  resources/niobium: 8
  resources/lithium: 13
  resources/copper: 12
  resources/nickel: 12
  resources/graphite: 9
  resources/balsa: 7
  resources/water: 11
  energy/fission_smr: 8
  energy/solar: 11
  energy/wind: 12
  energy/power_plants_grid: 19
  energy/other_renewables: 12

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 20
  infrastructure/port_ownership: 14
  infrastructure/port_cranes: 15
  infrastructure/rail: 13
  infrastructure/bridges_roads: 12
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 16
  resources/niobium: 8
  resources/lithium: 13
  resources/copper: 12
  resources/nickel: 12
  resources/graphite: 9
  resources/balsa: 7
  resources/water: 10
  energy/fission_smr: 8
  energy/solar: 11
  energy/wind: 12
  energy/power_plants_grid: 19
  energy/other_renewables: 11

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 19
  infrastructure/port_ownership: 13
  infrastructure/port_cranes: 14
  infrastructure/rail: 12
  infrastructure/bridges_roads: 12
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 16
  resources/niobium: 8
  resources/lithium: 13
  resources/copper: 11
  resources/nickel: 12
  resources/graphite: 9
  resources/balsa: 7
  resources/water: 10
  energy/fission_smr: 8
  energy/solar: 11
  energy/wind: 12
  energy/power_plants_grid: 19
  energy/other_renewables: 11

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 18
  infrastructure/port_ownership: 12
  infrastructure/port_cranes: 14
  infrastructure/rail: 12
  infrastructure/bridges_roads: 12
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 15
  resources/niobium: 8
  resources/lithium: 12
  resources/copper: 11
  resources/nickel: 11
  resources/graphite: 8
  resources/balsa: 7
  resources/water: 10
  energy/fission_smr: 8
  energy/solar: 11
  energy/wind: 12
  energy/power_plants_grid: 18
  energy/other_renewables: 11

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 17
  infrastructure/port_ownership: 12
  infrastructure/port_cranes: 13
  infrastructure/rail: 12
  infrastructure/bridges_roads: 12
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 14
  resources/niobium: 7
  resources/lithium: 12
  resources/copper: 11
  resources/nickel: 10
  resources/graphite: 8
  resources/balsa: 7
  resources/water: 10
  energy/fission_smr: 8
  energy/solar: 10
  energy/wind: 11
  energy/power_plants_grid: 18
  energy/other_renewables: 10

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 16
  infrastructure/port_ownership: 12
  infrastructure/port_cranes: 13
  infrastructure/rail: 11
  infrastructure/bridges_roads: 12
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 14
  resources/niobium: 7
  resources/lithium: 12
  resources/copper: 11
  resources/nickel: 10
  resources/graphite: 8
  resources/balsa: 7
  resources/water: 10
  energy/fission_smr: 7
  energy/solar: 10
  energy/wind: 11
  energy/power_plants_grid: 18
  energy/other_renewables: 10

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 15
  infrastructure/port_ownership: 12
  infrastructure/port_cranes: 13
  infrastructure/rail: 11
  infrastructure/bridges_roads: 11
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 14
  resources/niobium: 6
  resources/lithium: 12
  resources/copper: 11
  resources/nickel: 10
  resources/graphite: 8
  resources/balsa: 7
  resources/water: 9
  energy/fission_smr: 7
  energy/solar: 10
  energy/wind: 11
  energy/power_plants_grid: 18
  energy/other_renewables: 10

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 14
  infrastructure/port_ownership: 12
  infrastructure/port_cranes: 12
  infrastructure/rail: 11
  infrastructure/bridges_roads: 11
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 13
  resources/niobium: 6
  resources/lithium: 12
  resources/copper: 11
  resources/nickel: 8
  resources/graphite: 8
  resources/balsa: 7
  resources/water: 9
  energy/fission_smr: 7
  energy/solar: 10
  energy/wind: 11
  energy/power_plants_grid: 18
  energy/other_renewables: 10

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 13
  infrastructure/port_ownership: 11
  infrastructure/port_cranes: 12
  infrastructure/rail: 11
  infrastructure/bridges_roads: 11
  infrastructure/building_materials: 9
  infrastructure/engineering_epc: 11
  resources/niobium: 6
  resources/lithium: 11
  resources/copper: 11
  resources/nickel: 8
  resources/graphite: 8
  resources/balsa: 7
  resources/water: 9
  energy/fission_smr: 7
  energy/solar: 10
  energy/wind: 9
  energy/power_plants_grid: 18
  energy/other_renewables: 10

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 12
  infrastructure/port_ownership: 11
  infrastructure/port_cranes: 12
  infrastructure/rail: 11
  infrastructure/bridges_roads: 10
  infrastructure/building_materials: 8
  infrastructure/engineering_epc: 11
  resources/niobium: 6
  resources/lithium: 11
  resources/copper: 11
  resources/nickel: 8
  resources/graphite: 8
  resources/balsa: 7
  resources/water: 8
  energy/fission_smr: 7
  energy/solar: 10
  energy/wind: 9
  energy/power_plants_grid: 18
  energy/other_renewables: 10

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 11
  infrastructure/port_ownership: 11
  infrastructure/port_cranes: 11
  infrastructure/rail: 11
  infrastructure/bridges_roads: 10
  infrastructure/building_materials: 8
  infrastructure/engineering_epc: 11
  resources/niobium: 6
  resources/lithium: 10
  resources/copper: 11
  resources/nickel: 8
  resources/graphite: 7
  resources/balsa: 7
  resources/water: 8
  energy/fission_smr: 7
  energy/solar: 10
  energy/wind: 9
  energy/power_plants_grid: 18
  energy/other_renewables: 8

seen_urls:
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

misses:
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
