"""Cycle 488 hunt: shuffle_seed=20261488; Rumo CapEx planilha 3T21.

Shuffle: power_plants_grid, balsa, copper, solar, lithium, wind, port_ownership, port_cranes, rail, nickel, other_renewables, fission_smr, water, niobium, bridges_roads, engineering_epc, graphite, building_materials.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 3T21 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_3t21_capex_774m_brl", "Investimento Total", 774.4591907700008,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_3t21_566m_brl", "Operação Norte", 566.0463796600002,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_3t21_157m_brl", "Operação Norte Recorrente", 157.3391768799998,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_3t21_409m_brl", "Operação Norte Expansão", 408.7072027800005,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_3t21_60m_brl", "Material Rodante", 60.43029034999993,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_3t21_286m_brl", "Capacitação Malha Ferroviária", 286.2367872400006,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_3t21_54m_brl", "Capacitação Porto e Terminais", 54.13185528999999,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_3t21_8m_brl", "Ferrovia do Mato Grosso", 7.9082699000000005,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_3t21_192m_brl", "Operação Sul", 191.56194211000056,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_3t21_106m_brl", "Operação Sul Recorrente", 105.8192495700001,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_3t21_86m_brl", "Operação Sul Expansão", 85.74269254000045,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_3t21_17m_brl", "Brado (Contêineres)", 16.850869000000007,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_3t21_2m_brl", "Brado Recorrente", 1.6875,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_3t21_15m_brl", "Brado Expansão", 15.163369000000007,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
