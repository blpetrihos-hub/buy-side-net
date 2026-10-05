"""Cycle 543 hunt: shuffle_seed=20261543; Neoenergia CAPEX FY2022 (allied).
Shuffle: nickel, rail, building_materials, water, wind, engineering_epc, solar, copper, niobium, port_ownership, other_renewables, bridges_roads, balsa, port_cranes, graphite, fission_smr, lithium, power_plants_grid.
Thin/US CapEx dry. ALLIED: NEW Neoenergia CAPEX planilha FY2022 faces."""
ITEMS = [
    ("neoenergia_fy2022_capex_9892m_brl", "TOTAL", 9891.611792329999, "-23.55", "-46.63", "Neoenergia Brazil (São Paulo HQ pin).", True, "power_plants_grid", "total"),
    ("neoenergia_redes_fy2022_8091m_brl", "Redes", 8090.902356549999, "-23.55", "-46.63", "Neoenergia Redes (distribution+transmission; São Paulo HQ pin).", False, "power_plants_grid", "redes"),
    ("neoenergia_dist_fy2022_5458m_brl", "Distribuidoras", 5458.318221029999, "-23.55", "-46.63", "Neoenergia Distribuidoras aggregate (São Paulo HQ pin).", False, "power_plants_grid", "dist"),
    ("neoenergia_coelba_fy2022_2626m_brl", "Neoenergia Coelba", 2626.4925329199996, "-12.97", "-38.50", "Neoenergia Coelba (Salvador, Bahia pin).", False, "power_plants_grid", "coelba"),
    ("neoenergia_pernambuco_fy2022_898m_brl", "Neoenergia Pernambuco", 897.5427481000002, "-8.05", "-34.88", "Neoenergia Pernambuco (Recife pin).", False, "power_plants_grid", "pernambuco"),
    ("neoenergia_cosern_fy2022_500m_brl", "Neoenergia Cosern", 499.76551759000006, "-5.79", "-35.21", "Neoenergia Cosern (Natal, RN pin).", False, "power_plants_grid", "cosern"),
    ("neoenergia_elektro_fy2022_1093m_brl", "Neoenergia Elektro", 1093.30222114, "-22.91", "-47.06", "Neoenergia Elektro (Campinas, SP pin).", False, "power_plants_grid", "elektro"),
    ("neoenergia_brasilia_fy2022_341m_brl", "Neoenergia Brasília", 341.21520128, "-15.78", "-47.93", "Neoenergia Brasília (Brasília pin).", False, "power_plants_grid", "brasilia"),
    ("neoenergia_tx_fy2022_2633m_brl", "Transmissoras", 2632.5841355200005, "-15.78", "-47.93", "Neoenergia Transmissoras (Brasília pin).", False, "power_plants_grid", "tx"),
    ("neoenergia_geracao_fy2022_1798m_brl", "Geração e Clientes", 1797.8541726899998, "-23.55", "-46.63", "Neoenergia Geração e Clientes (São Paulo HQ pin).", False, "power_plants_grid", "geracao"),
    ("neoenergia_hidro_fy2022_59m_brl", "Hidrelétricas", 58.76694066, "-15.78", "-47.93", "Neoenergia hydropower portfolio (Brasília pin).", False, "power_plants_grid", "hidro"),
    ("neoenergia_eolicas_fy2022_1213m_brl", "Eólicas", 1213.21761964, "-7.12", "-34.88", "Neoenergia wind portfolio (Northeast Brazil pin).", False, "wind", "eolicas"),
    ("neoenergia_chafariz_fy2022_585m_brl", "Complexo Chafariz", 584.8979751499998, "-7.20", "-38.20", "Neoenergia Complexo Chafariz wind (Paraíba pin).", False, "wind", "chafariz"),
    ("neoenergia_oitis_fy2022_827m_brl", "Complexo Oitis", 827.0516307800001, "-9.40", "-41.90", "Neoenergia Complexo Oitis wind (Bahia/Piauí pin).", False, "wind", "oitis"),
    ("neoenergia_solar_fy2022_464m_brl", "Solar", 463.89107443, "-9.40", "-40.50", "Neoenergia solar portfolio (Northeast Brazil pin).", False, "solar", "solar"),
    ("neoenergia_termica_fy2022_54m_brl", "Térmica", 53.97837272000002, "-12.97", "-38.50", "Neoenergia thermal generation (Bahia pin).", False, "power_plants_grid", "termica")
]
