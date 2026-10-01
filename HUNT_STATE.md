updated: 2026-10-01
cycle: 1
remote: present
active_layer: resources
active_subcategory: lithium
next_query: Cycle 2 shuffle_seed=20261002; start at energy/solar; equal budget_per_subcategory=1_source_family_min across all 18.
next_row_id: (follow cycle-2 shuffled_order)
dry_streak: 0

# Per-cycle shuffle (BRIEF.md): each cycle shuffles the 18-subcategory list with a
# logged seed, works through it with equal per-subcategory budgets, and records
# rows found per subcategory for coverage checks over time.

shuffle_seed: 20261001
budget_per_subcategory: 1_source_family_min
# Equal time box: at least one opened public source family (or documented miss)
# per subcategory before moving on. Same budget for every subcategory.

shuffled_order:
- infrastructure/bridges_roads
- energy/other_renewables
- infrastructure/building_materials
- resources/water
- infrastructure/port_ownership
- infrastructure/engineering_epc
- energy/solar
- infrastructure/rail
- infrastructure/port_cranes
- resources/niobium
- energy/power_plants_grid
- energy/wind
- resources/nickel
- resources/copper
- energy/fission_smr
- resources/balsa
- resources/dimension_stone
- resources/lithium

rows_found_this_cycle:
  infrastructure/bridges_roads: 2
  energy/other_renewables: 1
  infrastructure/building_materials: 1
  resources/water: 2
  infrastructure/port_ownership: 1
  infrastructure/engineering_epc: 1
  energy/solar: 1
  infrastructure/rail: 0
  infrastructure/port_cranes: 1
  resources/niobium: 1
  energy/power_plants_grid: 1
  energy/wind: 2
  resources/nickel: 1
  resources/copper: 2
  energy/fission_smr: 1
  resources/balsa: 2
  resources/dimension_stone: 1
  resources/lithium: 2

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 1
  infrastructure/bridges_roads: 2
  energy/other_renewables: 1
  infrastructure/building_materials: 1
  resources/water: 2
  infrastructure/port_ownership: 1
  infrastructure/engineering_epc: 1
  energy/solar: 2
  infrastructure/rail: 2
  infrastructure/port_cranes: 1
  resources/niobium: 2
  energy/power_plants_grid: 9
  energy/wind: 2
  resources/nickel: 1
  resources/copper: 2
  energy/fission_smr: 1
  resources/balsa: 2
  resources/dimension_stone: 1
  resources/lithium: 2

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

misses:
- 2026-10-01 | infrastructure/rail | cycle1 budget | U.S. or new PRC rail award 2021-2026 beyond existing SP metro / EFE rows | no additional sourced rail row opened in this cycle's time box (existing rows retained)

# Redesign reset (2026-10-01). Geography: Latin America and the Caribbean only.
# Shuffle rule: equal per-subcategory budgets; logged seed each cycle.
