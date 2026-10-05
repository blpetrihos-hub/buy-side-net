"""Cycle 545 hunt: shuffle_seed=20261545; Neoenergia CAPEX 3T22 (allied).
Shuffle: graphite, water, fission_smr, building_materials, copper, balsa, bridges_roads, solar, other_renewables, port_ownership, lithium, port_cranes, niobium, power_plants_grid, rail, engineering_epc, wind, nickel.
Thin/US CapEx dry. ALLIED: NEW Neoenergia CAPEX planilha 3T22 faces."""
ITEMS = [
    ("neoenergia_3t22_capex_2550m_brl", "TOTAL", 2550.0, "-23.55", "-46.63", "Neoenergia Brazil (São Paulo HQ pin).", True, "power_plants_grid", "total"),
    ("neoenergia_redes_3t22_2188m_brl", "Redes", 2188.0, "-23.55", "-46.63", "Neoenergia Redes (distribution+transmission; São Paulo HQ pin).", False, "power_plants_grid", "redes"),
    ("neoenergia_dist_3t22_1569m_brl", "Distribuidoras", 1569.0, "-23.55", "-46.63", "Neoenergia Distribuidoras aggregate (São Paulo HQ pin).", False, "power_plants_grid", "dist"),
    ("neoenergia_coelba_3t22_771m_brl", "Neoenergia Coelba", 771.0, "-12.97", "-38.50", "Neoenergia Coelba (Salvador, Bahia pin).", False, "power_plants_grid", "coelba"),
    ("neoenergia_pernambuco_3t22_229m_brl", "Neoenergia Pernambuco", 229.0, "-8.05", "-34.88", "Neoenergia Pernambuco (Recife pin).", False, "power_plants_grid", "pernambuco"),
    ("neoenergia_cosern_3t22_164m_brl", "Neoenergia Cosern", 164.0, "-5.79", "-35.21", "Neoenergia Cosern (Natal, RN pin).", False, "power_plants_grid", "cosern"),
    ("neoenergia_elektro_3t22_299m_brl", "Neoenergia Elektro", 299.0, "-22.91", "-47.06", "Neoenergia Elektro (Campinas, SP pin).", False, "power_plants_grid", "elektro"),
    ("neoenergia_brasilia_3t22_106m_brl", "Neoenergia Brasília", 106.0, "-15.78", "-47.93", "Neoenergia Brasília (Brasília pin).", False, "power_plants_grid", "brasilia"),
    ("neoenergia_tx_3t22_618m_brl", "Transmissoras", 618.0, "-15.78", "-47.93", "Neoenergia Transmissoras (Brasília pin).", False, "power_plants_grid", "tx"),
    ("neoenergia_geracao_3t22_362m_brl", "Geração e Clientes", 361.82210345, "-23.55", "-46.63", "Neoenergia Geração e Clientes (São Paulo HQ pin).", False, "power_plants_grid", "geracao"),
    ("neoenergia_eolicas_3t22_338m_brl", "Eólicas", 338.0, "-7.12", "-34.88", "Neoenergia wind portfolio (Northeast Brazil pin).", False, "wind", "eolicas"),
    ("neoenergia_chafariz_3t22_126m_brl", "Complexo Chafariz", 125.64211007000006, "-7.20", "-38.20", "Neoenergia Complexo Chafariz wind (Paraíba pin).", False, "wind", "chafariz"),
    ("neoenergia_oitis_3t22_203m_brl", "Complexo Oitis", 202.98523543999997, "-9.40", "-41.90", "Neoenergia Complexo Oitis wind (Bahia/Piauí pin).", False, "wind", "oitis"),
    ("neoenergia_solar_3t22_18m_brl", "Solar", 18.0, "-9.40", "-40.50", "Neoenergia solar portfolio (Northeast Brazil pin).", False, "solar", "solar"),
    ("neoenergia_termica_3t22_7m_brl", "Térmica", 7.13752972, "-12.97", "-38.50", "Neoenergia thermal generation (Bahia pin).", False, "power_plants_grid", "termica")
]
