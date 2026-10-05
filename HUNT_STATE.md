updated: 2026-10-05
cycle: 300
remote: present
active_layer: energy
active_subcategory: power_plants_grid
next_query: Cycle 301 shuffle_seed=20261301; reshuffle all 18; equal budget_per_subcategory=1_source_family_min; within each subcategory split budget evenly between U.S. and PRC sources (sides ~us466/prc407/allied500); log rows_by_side_this_cycle; after shuffled pass give 3 thinnest active-row subcats one half-budget top-up each (recompute); Prefer thin: balsa (25), nickel (26), fission_smr (29), niobium (30). Country×subcategory sweep both sides + regulators. Weight under-covered: Haiti (beyond RN2/WB/IDB/Solengy/Port Royal), Venezuela (beyond Tocoma/Macagua/GE Vernova grid/El Vigía solar; Chevron oil out of taxonomy), Nicaragua rail past MoU, Peru balsa, Colombia graphite mine CapEx (framework only). Holdovers: CRBC Corentyne if signed; CSCEC Nicaragua 290 km if decree; CCECC Nicaragua rail if feasibility past MoU; CHEC San Carlos central if contract signed (Contraloría aval only); Pacto Coronel Vivida Huawei BESS R$30m if PRC equipment CapEx separable; Progress Rail VLI R$430m if company dual confirms distinct from R$200m eight-loco and R$600m 27-loco cumulative; Equatorial ADMS company primary if openable (MA/AP pages 403); Ascenty Vinhedo/Osasco/Sumaré USD breakouts if company primary opens (Valor press USD720/360/120 — company AI page 403); GATE R$20bn acceleration if State Grid company confirms vs R$18bn; Alupar TECP CapEx if distinct company face opens beyond RAP/debt (TAP CapEx Previsto R$498.52m is TAP not TECP); Ada Franco da Rocha R$2.7bn if company CapEx figure opens; KIO QRO2/2026 nested breakouts; Grenergy €3.7bn Chile ~45% if separable primary; Equinix São Paulo cabinets USD109m if company SEC/10-Q primary opens (SEC browse 403); AXIA 2026–2027 plan R$12–14bn if distinct company primary beyond 2Q26 nested; WEG transformers Americas R$2.1bn if LatAm-only CapEx separable; EPR Litoral Pioneiro 1S26 CapEx R$619.4m if company dual URL opens beyond financialfilings; Alupar 1S26 CapEx R$489.2m if company face opens beyond 2T26 Custo Infra nested; TCP green R$300m if company primary opens beyond trade press; ENGIE Colibri Aneel CapEx R$1.5747bn if company PDF host opens (1Q26 presentation / FRE 403); Cemig Gasmig Centro-Oeste R$49.5m / Energisa gás 2T26 R$30m LoB / Cemig 2026 gás plan R$227m if taxonomy-fit (natural gas out of 18-subcat list); Wabtec Vale 50 loco CapEx if company/Vale dual discloses figure (press CapEx blank); CREC Cañas–Bebedero CRC→USD FX if Fed H.10 CRC retrieved; Motiva FY2025 aeroportos R$780m if taxonomy-fit (airports out of 18-subcat list); Antamina Segundo ITS if SENACE approval confirms beyond presented USD729m; AES Andes Arenales 300 MW BESS project CapEx if distinct from Pampas+Cristales USD1.1bn; SSA Guaymas STS/ERTG CapEx if dollar figure distinct from MXN424.8m TUM concession; Bechtel QB2 desal CapEx if company primary opens. No U.S. territories.
next_row_id: (follow cycle-301 shuffled_order)
dry_streak: 0

# === Country×subcategory sweep cells touched (session continuing from 300) ===
# Filled this cycle: Peru/Chile/Colombia×power_plants_grid NEW×7 allied CapEx Previsto
#   USD; Brazil×power_plants_grid NEW×6 allied TAP/TPC/TCN period cash + NEW×2 other
#   Energisa TX; Brazil×other_renewables NEW×2 other Energisa (re)energisa.
# Still thin/empty priority cells: Haiti, Venezuela, Nicaragua rail past MoU, Peru balsa,
#   Colombia graphite mine CapEx.
# ≥1/3 U.S. hunt budget spent (Arenales 404; SSA Guaymas 404; Wabtec Vale CapEx blank;
#   Progress Rail R$430m absent from VLI page; Fluor/FCX CapEx-fill blanks).
# PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.

# === Cycle 300 (seed 20261300) ===
# Shuffled order (BRIEF.md numbered + Random(20261300).shuffle): copper, wind, water,
#   port_ownership, balsa, engineering_epc, niobium, nickel, graphite, bridges_roads,
#   solar, building_materials, port_cranes, power_plants_grid, lithium, fission_smr,
#   other_renewables, rail.
# Logged 17 NEW (0 US / 0 PRC / 13 allied / 4 other; ≥1/3 US hunt budget spent —
#   CapEx dry this pass; PRC CapEx-blank):
#   allied power_plants_grid NEW: alupar_tes_capex_previsto_38p9m_usd (USD 38.9m);
#     alupar_tel_capex_previsto_40m_usd (USD 40.0m);
#     alupar_sed_capex_previsto_45p2m_usd (USD 45.2m);
#     alupar_tep_capex_previsto_145p9m_usd (USD 145.9m);
#     alupar_tsa_capex_previsto_19p6m_usd (USD 19.6m);
#     alupar_ter_capex_previsto_400p2m_usd (USD 400.2m);
#     alupar_geral_capex_previsto_42p8m_usd (USD 42.8m);
#     alupar_tap_capex_1t26_45p59m_brl (R$45.59m); alupar_tap_capex_2t26_41p55m_brl (R$41.55m);
#     alupar_tpc_capex_1t26_50p79m_brl (R$50.79m); alupar_tpc_capex_2t26_113p01m_brl (R$113.01m);
#     alupar_tcn_capex_1t26_9p17m_brl (R$9.17m); alupar_tcn_capex_2t26_9p61m_brl (R$9.61m).
#   other power_plants_grid NEW: energisa_tx_2t26_63m_brl (R$63m);
#     energisa_tx_6m26_100m_brl (R$100m).
#   other other_renewables NEW: energisa_reenergisa_2t26_36m_brl (R$36m);
#     energisa_reenergisa_6m26_72m_brl (R$72m).
# Thin top-up (balsa/nickel/fission_smr): dry.
# Equal-budget misses: copper, wind, water, port_ownership, balsa, engineering_epc,
#   niobium, nickel, graphite, bridges_roads, solar, building_materials, port_cranes,
#   lithium, fission_smr, rail (catalog dense; thin dry; US CapEx dry).
# Holdovers still unsigned: CRBC Corentyne; CSCEC 290 km; CCECC Nicaragua rail;
#   CHEC San Carlos; Progress Rail VLI R$430m; Alupar TECP CapEx (distinct from TAP);
#   Ada R$2.7bn; Equinix SP USD109m SEC; EPR Litoral 1S26; Alupar 1S26; TCP R$300m;
#   Ascenty Vinhedo/Osasco; ENGIE Colibri; Equatorial ADMS; Cemig Gasmig; Energisa gás;
#   Wabtec Vale 50 loco CapEx blank; CREC Cañas CRC→USD FX; Motiva FY2025 airports
#   R$780m taxonomy-out; Antamina Segundo ITS SENACE approval pending;
#   AES Andes Arenales project CapEx; SSA Guaymas STS/ERTG CapEx dollar figure;
#   Bechtel QB2 desal CapEx blank.
# Active after cycle 300: us466 / prc407 / allied500 / other372 (n=1745).

# === Cycle 299 (seed 20261299) summary ===
# Logged 7 NEW Alupar CapEx Realizado USD. Active after: us466/prc407/allied487/other368 (n=1728).

# === Cycle 298 (seed 20261298) summary ===
# Logged 4 NEW (incl. Progress Rail R$600m US). Active after: us466/prc407/allied480/other368 (n=1721).

shuffle_seed: 20261300
budget_per_subcategory: 1_source_family_min
shuffled_order:
- resources/copper
- energy/wind
- resources/water
- infrastructure/port_ownership
- resources/balsa
- infrastructure/engineering_epc
- resources/niobium
- resources/nickel
- resources/graphite
- infrastructure/bridges_roads
- energy/solar
- infrastructure/building_materials
- infrastructure/port_cranes
- energy/power_plants_grid
- resources/lithium
- energy/fission_smr
- energy/other_renewables
- infrastructure/rail
rows_found_this_cycle:
  resources/copper: 0
  energy/wind: 0
  resources/water: 0
  infrastructure/port_ownership: 0
  resources/balsa: 0
  infrastructure/engineering_epc: 0
  resources/niobium: 0
  resources/nickel: 0
  resources/graphite: 0
  infrastructure/bridges_roads: 0
  energy/solar: 0
  infrastructure/building_materials: 0
  infrastructure/port_cranes: 0
  energy/power_plants_grid: 15
  resources/lithium: 0
  energy/fission_smr: 0
  energy/other_renewables: 2
  infrastructure/rail: 0
rows_by_side_this_cycle:
  us: 0
  prc: 0
  allied: 13
  other: 4
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
  allied: 500
  other: 372
  n: 1745
