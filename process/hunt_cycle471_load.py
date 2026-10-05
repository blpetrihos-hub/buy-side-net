"""Cycle 471 hunt: shuffle_seed=20261471; Rumo CapEx planilha 4T25.

Shuffle: solar, building_materials, niobium, water, fission_smr, port_ownership, rail, lithium, copper, wind, nickel, other_renewables, graphite, engineering_epc, port_cranes, power_plants_grid, balsa, bridges_roads.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 4T25 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_4t25_capex_1463m_brl", "Investimento Total", 1462.8206749199999,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_4t25_1240m_brl", "Operação Norte", 1239.6616761700006,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_4t25_306m_brl", "Operação Norte Recorrente", 305.6957795900006,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_4t25_934m_brl", "Operação Norte Expansão", 933.9658965800002,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_4t25_1m_brl", "Material Rodante", 0.821482,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_4t25_258m_brl", "Capacitação Malha Ferroviária", 257.77193907000014,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_4t25_49m_brl", "Capacitação Porto e Terminais", 48.539027759999996,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_4t25_627m_brl", "Ferrovia do Mato Grosso", 626.83344775,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_4t25_174m_brl", "Operação Sul", 174.04718477999927,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_4t25_174m_brl", "Operação Sul Recorrente", 174.04718477999927,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_conteiner_4t25_49m_brl", "Brado (Contêineres)", 49.11181397,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_4t25_10m_brl", "Brado Recorrente", 10.366545180000005,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_4t25_39m_brl", "Brado Expansão", 38.74526878999999,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
