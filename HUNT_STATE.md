updated: 2026-10-01
cycle: 3
remote: present
active_layer: infrastructure
active_subcategory: port_ownership
next_query: Cycle 4 shuffle_seed=20261004; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; prefer empty/low-coverage subcats within each time box; graphite hunting = mining/processing/anode chains (Brazil, Mexico).
next_row_id: (follow cycle-4 shuffled_order)
dry_streak: 0

# Per-cycle shuffle (BRIEF.md): each cycle shuffles the 18-subcategory list with a
# logged seed, works through it with equal per-subcategory budgets, and records
# rows found per subcategory for coverage checks over time.

shuffle_seed: 20261003
budget_per_subcategory: 1_source_family_min
# Equal time box: at least one opened public source family (or documented miss)
# per subcategory before moving on. Same budget for every subcategory.

shuffled_order:
- resources/nickel
- energy/fission_smr
- infrastructure/engineering_epc
- resources/water
- infrastructure/bridges_roads
- energy/wind
- energy/power_plants_grid
- resources/balsa
- resources/niobium
- infrastructure/port_cranes
- resources/copper
- infrastructure/building_materials
- resources/lithium
- infrastructure/rail
- energy/solar
- resources/graphite
- energy/other_renewables
- infrastructure/port_ownership

rows_found_this_cycle:
  resources/nickel: 0
  energy/fission_smr: 0
  infrastructure/engineering_epc: 0
  resources/water: 1
  infrastructure/bridges_roads: 0
  energy/wind: 1
  energy/power_plants_grid: 2
  resources/balsa: 2
  resources/niobium: 0
  infrastructure/port_cranes: 0
  resources/copper: 0
  infrastructure/building_materials: 0
  resources/lithium: 0
  infrastructure/rail: 0
  energy/solar: 2
  resources/graphite: 1
  energy/other_renewables: 1
  infrastructure/port_ownership: 1

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 3
  infrastructure/port_ownership: 3
  infrastructure/port_cranes: 2
  infrastructure/rail: 4
  infrastructure/bridges_roads: 3
  infrastructure/building_materials: 2
  infrastructure/engineering_epc: 3
  resources/niobium: 3
  resources/lithium: 3
  resources/copper: 3
  resources/nickel: 2
  resources/graphite: 3
  resources/balsa: 6
  resources/water: 4
  energy/fission_smr: 2
  energy/solar: 5
  energy/wind: 4
  energy/power_plants_grid: 12
  energy/other_renewables: 3

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

misses:
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

# Redesign reset (2026-10-01). Geography: Latin America and the Caribbean only.
# Shuffle rule: equal per-subcategory budgets; logged seed each cycle.
# Cycle 2 (seed 20261002): 20 sourced rows; graphite miss.
# Cycle 3 (seed 20261003): 11 sourced rows; 10 equal-budget misses on already-covered subcats.

# 2026-10-01 graphite taxonomy correction (Ben): former dimension_stone/granite
# renamed to graphite everywhere. ABIROCHAS ornamental-stone rows archived (exclude).
# Hunt retargeted to LatAm graphite mining/processing/anode chains; logged South Star,
# Nacional de Grafite, Graphex–Santa Cruz offtake.