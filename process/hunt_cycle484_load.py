"""Cycle 484 hunt: shuffle_seed=20261484; Rumo CapEx planilha 3T22.

Shuffle: wind, rail, graphite, power_plants_grid, port_ownership, niobium, nickel, other_renewables, building_materials, engineering_epc, copper, balsa, bridges_roads, fission_smr, solar, port_cranes, lithium, water.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 3T22 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_3t22_capex_607m_brl", "Investimento Total", 606.9308329799999,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_3t22_518m_brl", "Operação Norte", 518.2375363100002,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_3t22_220m_brl", "Operação Norte Recorrente", 220.42759015000024,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_3t22_298m_brl", "Operação Norte Expansão", 297.80994616000004,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_3t22_87m_brl", "Material Rodante", 86.79588811,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_3t22_185m_brl", "Capacitação Malha Ferroviária", 184.57282300000003,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_3t22_17m_brl", "Capacitação Porto e Terminais", 16.725186150000003,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_3t22_10m_brl", "Ferrovia do Mato Grosso", 9.716048899999999,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_3t22_76m_brl", "Operação Sul", 76.44921224999959,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_3t22_74m_brl", "Operação Sul Recorrente", 74.32761646999958,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_3t22_2m_brl", "Operação Sul Expansão", 2.12159578,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_3t22_12m_brl", "Brado (Contêineres)", 12.244084419999997,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_3t22_1m_brl", "Brado Recorrente", 1.2,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_3t22_11m_brl", "Brado Expansão", 11.044084419999997,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
