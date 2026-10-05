updated: 2026-10-05
cycle: 305
remote: present
active_layer: energy
active_subcategory: power_plants_grid
next_query: Cycle 306 shuffle_seed=20261306; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us466/prc407/allied566); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco and R$600m 27-loco cumulative; Equatorial ADMS company primary if openable (MA/AP pages 403); Ascenty Vinhedo/Osasco/Sumaré USD breakouts if company primary opens (Valor press USD720/360/120 — company AI page 403); GATE R$20bn acceleration if State Grid company confirms vs R$18bn; Alupar TECP CapEx if distinct company face opens beyond RAP/debt; Ada Franco da Rocha R$2.7bn if company CapEx figure opens; KIO QRO2/2026 nested breakouts; Grenergy €3.7bn Chile ~45% if separable primary; Equinix São Paulo cabinets USD109m if company SEC/10-Q primary opens (SEC browse 403); AXIA 2026–2027 plan R$12–14bn if distinct company primary beyond 2Q26 nested; WEG transformers Americas R$2.1bn if LatAm-only CapEx separable; EPR Litoral Pioneiro 1S26 CapEx R$619.4m if company dual URL opens beyond financialfilings; Alupar 1S26 CapEx R$489.2m if company face opens beyond 2T26 Custo Infra nested; TCP green R$300m if company primary opens beyond trade press; ENGIE Colibri Aneel CapEx R$1.5747bn if company PDF host opens (1Q26 presentation / FRE 403); Cemig Gasmig / Energisa gás LoB / Cemig 2026 gás plan if taxonomy-fit (natural gas out of 18-subcat list); Wabtec Vale 50 loco CapEx if company/Vale dual discloses figure (press CapEx blank); CREC Cañas–Bebedero CRC→USD FX if Fed H.10 CRC retrieved; Motiva FY2025 aeroportos R$780m if taxonomy-fit (airports out of 18-subcat list); Antamina Segundo ITS if SENACE approval confirms beyond presented USD729m; AES Andes Arenales 300 MW BESS project CapEx if distinct from Pampas+Cristales USD1.1bn (AES Corp AR lists MW/COD only); SSA Guaymas STS/ERTG CapEx if dollar figure distinct from MXN424.8m TUM concession; Bechtel QB2 desal CapEx if company primary opens; ISA Energia older 2017–2020 greenfield CapEx ANEEL/ISA pairs (Paraguaçú/Aimorés/Itaúnas/Tibagi/Itaquerê/Aguapeí/Bauru/Lorena/Biguaçu/Três Lagoas/Triângulo Mineiro) if not yet logged. No U.S. territories.
next_row_id: (follow cycle-306 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 305) ===
# Filled this cycle: Brazil×power_plants_grid NEW×15 allied (ISA Energia CapEx ANEEL
#   + CapEx ISA até 30/06/2026 for Água Vermelha/Riacho Grande/Piraquê/Minuano/Ivaí
#   + CapEx ANEEL Serra Dourada/Itatiaia/Jacarandá + portfolio Totals).
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (AES AR CapEx-fill dry after Atacama; Arenales blank;
#   Fluor Quellaveco/Wabtec/Progress R$430m/Bechtel blanks).
# PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.

# === Cycle 305 (seed 20261305) ===
# Shuffled order (BRIEF.md numbered + Random(20261305).shuffle): engineering_epc,
#   copper, building_materials, bridges_roads, niobium, graphite, port_cranes, balsa,
#   nickel, lithium, water, fission_smr, other_renewables, rail, port_ownership, solar,
#   wind, power_plants_grid.
# Logged 15 NEW (0 US / 0 PRC / 15 allied / 0 other; ≥1/3 US hunt budget spent —
#   CapEx dry this pass; PRC CapEx-blank):
#   allied power_plants_grid NEW: isa_energia_agua_vermelha_capex_aneel_94p2m_brl;
#     isa_energia_agua_vermelha_capex_30jun26_87p1m_brl;
#     isa_energia_riacho_grande_capex_aneel_1140p6m_brl;
#     isa_energia_riacho_grande_capex_30jun26_922p1m_brl;
#     isa_energia_piraque_capex_aneel_3653p6m_brl;
#     isa_energia_piraque_capex_30jun26_3866p1m_brl;
#     isa_energia_minuano_capex_aneel_681p6m_brl;
#     isa_energia_minuano_capex_30jun26_737p6m_brl;
#     isa_energia_ivai_capex_aneel_968p2m_brl;
#     isa_energia_ivai_capex_30jun26_1064p4m_brl;
#     isa_energia_serra_dourada_capex_aneel_3156p8m_brl;
#     isa_energia_itatiaia_capex_aneel_2300p6m_brl;
#     isa_energia_jacaranda_capex_aneel_232p3m_brl;
#     isa_energia_greenfield_capex_aneel_total_15742p9m_brl;
#     isa_energia_greenfield_capex_30jun26_total_12083p7m_brl.
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: engineering_epc, copper, building_materials, bridges_roads,
#   niobium, graphite, port_cranes, balsa, nickel, lithium, water, fission_smr,
#   other_renewables, rail, port_ownership, solar, wind (catalog dense; thin dry;
#   US CapEx dry).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail;
#   CHEC San Carlos; Progress Rail VLI R$430m; Alupar TECP CapEx; Ada R$2.7bn;
#   Equinix SP USD109m SEC; EPR Litoral 1S26; Alupar 1S26; TCP R$300m; Ascenty;
#   ENGIE Colibri; Equatorial ADMS; Cemig Gasmig; Energisa gás; Wabtec Vale CapEx blank;
#   CREC Cañas CRC→USD FX; Motiva FY2025 airports taxonomy-out; Antamina Segundo ITS;
#   AES Arenales CapEx (AR MW/COD only); SSA Guaymas STS dollar; Bechtel QB2 desal;
#   ISA older 2017–2020 greenfield CapEx ANEEL/ISA pairs deferred.
# Active after cycle 305: us466 / prc407 / allied566 / other379 (n=1818).

# === Cycle 304 (seed 20261304) summary ===
# Logged 7 NEW Cemig TX. Active after: us466/prc407/allied551/other379 (n=1803).

# === Cycle 303 (seed 20261303) summary ===
# Logged 15 NEW. Active after: us466/prc407/allied551/other372 (n=1796).

shuffle_seed: 20261305
budget_per_subcategory: 1_source_family_min
shuffled_order:
- infrastructure/engineering_epc
- resources/copper
- infrastructure/building_materials
- infrastructure/bridges_roads
- resources/niobium
- resources/graphite
- infrastructure/port_cranes
- resources/balsa
- resources/nickel
- resources/lithium
- resources/water
- energy/fission_smr
- energy/other_renewables
- infrastructure/rail
- infrastructure/port_ownership
- energy/solar
- energy/wind
- energy/power_plants_grid
rows_found_this_cycle:
  infrastructure/engineering_epc: 0
  resources/copper: 0
  infrastructure/building_materials: 0
  infrastructure/bridges_roads: 0
  resources/niobium: 0
  resources/graphite: 0
  infrastructure/port_cranes: 0
  resources/balsa: 0
  resources/nickel: 0
  resources/lithium: 0
  resources/water: 0
  energy/fission_smr: 0
  energy/other_renewables: 0
  infrastructure/rail: 0
  infrastructure/port_ownership: 0
  energy/solar: 0
  energy/wind: 0
  energy/power_plants_grid: 15
rows_by_side_this_cycle:
  us: 0
  prc: 0
  allied: 15
  other: 0
thin_topup:
  budget: 0.5_source_family_min
  subcategories:
  - resources/balsa
  - resources/nickel
  - energy/fission_smr
  notes: dry after reshuffled pass; prefer thin balsa/nickel/fission_smr/niobium.
coverage_cumulative_active_rows:
  us: 466
  prc: 407
  allied: 566
  other: 379
  n: 1818
