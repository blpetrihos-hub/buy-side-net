"""Cycle 476 hunt: shuffle_seed=20261476; Rumo CapEx planilha 3T24.

Shuffle: power_plants_grid, balsa, wind, port_ownership, engineering_epc, solar, water, copper, rail, graphite, niobium, fission_smr, nickel, building_materials, lithium, other_renewables, port_cranes, bridges_roads.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 3T24 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_3t24_capex_1468m_brl", "Investimento Total", 1468.1940857899997,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_3t24_1281m_brl", "Operação Norte", 1281.3833694100003,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_3t24_286m_brl", "Operação Norte Recorrente", 285.96060936,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_3t24_995m_brl", "Operação Norte Expansão", 995.4227600500004,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_3t24_91m_brl", "Material Rodante", 91.45465625,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_3t24_341m_brl", "Capacitação Malha Ferroviária", 340.7104724000004,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_3t24_79m_brl", "Capacitação Porto e Terminais", 78.69978757,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_3t24_485m_brl", "Ferrovia do Mato Grosso", 484.55784383,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_3t24_175m_brl", "Operação Sul", 174.93889114999936,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_3t24_164m_brl", "Operação Sul Recorrente", 163.59301818000003,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_3t24_11m_brl", "Operação Sul Expansão", 11.345872969999363,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_3t24_12m_brl", "Brado (Contêineres)", 11.87182523,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_3t24_6m_brl", "Brado Recorrente", 5.887499999999999,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_3t24_6m_brl", "Brado Expansão", 5.98432523,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
