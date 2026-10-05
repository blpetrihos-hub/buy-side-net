"""Cycle 474 hunt: shuffle_seed=20261474; Rumo CapEx planilha 1T25.

Shuffle: power_plants_grid, building_materials, niobium, other_renewables, bridges_roads, water, port_ownership, lithium, balsa, solar, graphite, rail, engineering_epc, wind, copper, port_cranes, nickel, fission_smr.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 1T25 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_1t25_capex_1780m_brl", "Investimento Total", 1779.97667958,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_1t25_1596m_brl", "Operação Norte", 1595.7,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_1t25_286m_brl", "Operação Norte Recorrente", 286.4785429499996,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_1t25_1309m_brl", "Operação Norte Expansão", 1309.2664595499955,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_1t25_248m_brl", "Material Rodante", 248.03586058,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_1t25_637m_brl", "Capacitação Malha Ferroviária", 636.5657718299956,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_1t25_72m_brl", "Capacitação Porto e Terminais", 71.57621803,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_1t25_353m_brl", "Ferrovia do Mato Grosso", 353.0886091099999,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_1t25_179m_brl", "Operação Sul", 179.36590114000023,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_1t25_179m_brl", "Operação Sul Recorrente", 179.36590114000023,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_conteiner_1t25_5m_brl", "Brado (Contêineres)", 4.86577594,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_1t25_2m_brl", "Brado Recorrente", 2.1624548199999998,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_1t25_3m_brl", "Brado Expansão", 2.70332112,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
