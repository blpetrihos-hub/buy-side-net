"""Cycle 542 hunt: shuffle_seed=20261542; Neoenergia CAPEX 1T23 (allied).
Shuffle: fission_smr, copper, lithium, wind, engineering_epc, port_cranes, nickel, graphite, rail, solar, bridges_roads, balsa, water, building_materials, power_plants_grid, port_ownership, other_renewables, niobium.
Thin/US CapEx dry. ALLIED: NEW Neoenergia CAPEX planilha 1T23 faces."""
ITEMS = [
    ("neoenergia_1t23_capex_2123m_brl", "TOTAL", 2123.1033464940015, "-23.55", "-46.63", "Neoenergia Brazil (São Paulo HQ pin).", True, "power_plants_grid", "total"),
    ("neoenergia_redes_1t23_1978m_brl", "Redes", 1978.231429830002, "-23.55", "-46.63", "Neoenergia Redes (distribution+transmission; São Paulo HQ pin).", False, "power_plants_grid", "redes"),
    ("neoenergia_dist_1t23_1241m_brl", "Distribuidoras", 1240.8239910700013, "-23.55", "-46.63", "Neoenergia Distribuidoras aggregate (São Paulo HQ pin).", False, "power_plants_grid", "dist"),
    ("neoenergia_coelba_1t23_578m_brl", "Neoenergia Coelba", 577.7580617200014, "-12.97", "-38.50", "Neoenergia Coelba (Salvador, Bahia pin).", False, "power_plants_grid", "coelba"),
    ("neoenergia_pernambuco_1t23_219m_brl", "Neoenergia Pernambuco", 218.98606278000003, "-8.05", "-34.88", "Neoenergia Pernambuco (Recife pin).", False, "power_plants_grid", "pernambuco"),
    ("neoenergia_cosern_1t23_121m_brl", "Neoenergia Cosern", 121.29891151999993, "-5.79", "-35.21", "Neoenergia Cosern (Natal, RN pin).", False, "power_plants_grid", "cosern"),
    ("neoenergia_elektro_1t23_248m_brl", "Neoenergia Elektro", 248.0862678, "-22.91", "-47.06", "Neoenergia Elektro (Campinas, SP pin).", False, "power_plants_grid", "elektro"),
    ("neoenergia_brasilia_1t23_75m_brl", "Neoenergia Brasília", 74.69468725, "-15.78", "-47.93", "Neoenergia Brasília (Brasília pin).", False, "power_plants_grid", "brasilia"),
    ("neoenergia_tx_1t23_737m_brl", "Transmissoras", 737.4074387600009, "-15.78", "-47.93", "Neoenergia Transmissoras (Brasília pin).", False, "power_plants_grid", "tx"),
    ("neoenergia_geracao_1t23_138m_brl", "Geração e Clientes", 138.05615918399985, "-23.55", "-46.63", "Neoenergia Geração e Clientes (São Paulo HQ pin).", False, "power_plants_grid", "geracao"),
    ("neoenergia_hidro_1t23_0m_brl", "Hidrelétricas", 0.06685399399999982, "-15.78", "-47.93", "Neoenergia hydropower portfolio (Brasília pin).", False, "power_plants_grid", "hidro"),
    ("neoenergia_eolicas_1t23_130m_brl", "Eólicas", 130.24572431999985, "-7.12", "-34.88", "Neoenergia wind portfolio (Northeast Brazil pin).", False, "wind", "eolicas"),
    ("neoenergia_chafariz_1t23_1m_brl", "Complexo Chafariz", 1.11054757999997, "-7.20", "-38.20", "Neoenergia Complexo Chafariz wind (Paraíba pin).", False, "wind", "chafariz"),
    ("neoenergia_oitis_1t23_121m_brl", "Complexo Oitis", 121.4817067, "-9.40", "-41.90", "Neoenergia Complexo Oitis wind (Bahia/Piauí pin).", False, "wind", "oitis"),
    ("neoenergia_solar_1t23_2m_brl", "Solar", 1.6397124600000001, "-9.40", "-40.50", "Neoenergia solar portfolio (Northeast Brazil pin).", False, "solar", "solar"),
    ("neoenergia_termica_1t23_5m_brl", "Térmica", 5.31688751, "-12.97", "-38.50", "Neoenergia thermal generation (Bahia pin).", False, "power_plants_grid", "termica")
]
