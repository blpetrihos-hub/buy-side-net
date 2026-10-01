updated: 2026-10-01
cycle: 8
remote: present
active_layer: infrastructure
active_subcategory: engineering_epc
next_query: Cycle 9 shuffle_seed=20261009; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; prefer empty/low-coverage subcats within each time box; graphite hunting = mining/processing/anode chains (Brazil, Mexico).
next_row_id: (follow cycle-9 shuffled_order)
dry_streak: 0

# Per-cycle shuffle (BRIEF.md): each cycle shuffles the 18-subcategory list with a
# logged seed, works through it with equal per-subcategory budgets, and records
# rows found per subcategory for coverage checks over time.

shuffle_seed: 20261008
budget_per_subcategory: 1_source_family_min
# Equal time box: at least one opened public source family (or documented miss)
# per subcategory before moving on. Same budget for every subcategory.

shuffled_order:
- infrastructure/engineering_epc
- energy/fission_smr
- resources/balsa
- resources/lithium
- resources/copper
- energy/other_renewables
- infrastructure/port_ownership
- resources/niobium
- resources/graphite
- resources/water
- energy/wind
- energy/power_plants_grid
- infrastructure/building_materials
- infrastructure/rail
- infrastructure/bridges_roads
- energy/solar
- infrastructure/port_cranes
- resources/nickel

rows_found_this_cycle:
  infrastructure/engineering_epc: 1
  energy/fission_smr: 1
  resources/balsa: 0
  resources/lithium: 0
  resources/copper: 1
  energy/other_renewables: 0
  infrastructure/port_ownership: 1
  resources/niobium: 0
  resources/graphite: 0
  resources/water: 0
  energy/wind: 0
  energy/power_plants_grid: 0
  infrastructure/building_materials: 1
  infrastructure/rail: 1
  infrastructure/bridges_roads: 0
  energy/solar: 1
  infrastructure/port_cranes: 0
  resources/nickel: 0

coverage_cumulative:
  # Active (non-archived, non-exclude) observation counts after cycle 8
  infrastructure/port_ownership: 9
  infrastructure/port_cranes: 8
  infrastructure/rail: 10
  infrastructure/bridges_roads: 7
  infrastructure/building_materials: 7
  infrastructure/engineering_epc: 9
  resources/niobium: 5
  resources/lithium: 8
  resources/copper: 9
  resources/nickel: 6
  resources/graphite: 6
  resources/balsa: 7
  resources/water: 7
  energy/fission_smr: 6
  energy/solar: 9
  energy/wind: 8
  energy/power_plants_grid: 17
  energy/other_renewables: 7

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

# 2026-10-01 graphite taxonomy correction (Ben): former dimension_stone/granite
# renamed to graphite everywhere. ABIROCHAS ornamental-stone rows archived (exclude).
# Hunt retargeted to LatAm graphite mining/processing/anode chains; logged South Star,
# Nacional de Grafite, Graphex–Santa Cruz offtake; Cycle 4 added Graphcoa Boa Sorte.
