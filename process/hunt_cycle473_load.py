"""Cycle 473 hunt: shuffle_seed=20261473; Rumo CapEx planilha 2T25.

Shuffle: bridges_roads, graphite, other_renewables, copper, lithium, building_materials, port_ownership, nickel, port_cranes, niobium, fission_smr, power_plants_grid, water, engineering_epc, wind, balsa, solar, rail.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 2T25 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_2t25_capex_1395m_brl", "Investimento Total", 1394.6288117200002,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_2t25_1186m_brl", "Operação Norte", 1185.8202574300003,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_2t25_305m_brl", "Operação Norte Recorrente", 305.07650474000025,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_2t25_881m_brl", "Operação Norte Expansão", 880.7437526900001,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_2t25_64m_brl", "Material Rodante", 63.84190796999998,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_2t25_321m_brl", "Capacitação Malha Ferroviária", 321.0490802500001,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_2t25_28m_brl", "Capacitação Porto e Terminais", 27.884535429999996,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_2t25_468m_brl", "Ferrovia do Mato Grosso", 467.96822904,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_2t25_192m_brl", "Operação Sul", 191.94188009999996,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_2t25_192m_brl", "Operação Sul Recorrente", 191.94188009999996,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_conteiner_2t25_17m_brl", "Brado (Contêineres)", 16.866674189999998,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_2t25_6m_brl", "Brado Recorrente", 6.2645,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_2t25_11m_brl", "Brado Expansão", 10.60217419,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
