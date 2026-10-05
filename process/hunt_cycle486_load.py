"""Cycle 486 hunt: shuffle_seed=20261486; Rumo CapEx planilha 1T22.

Shuffle: balsa, bridges_roads, water, engineering_epc, wind, graphite, niobium, fission_smr, nickel, lithium, solar, rail, port_cranes, building_materials, power_plants_grid, copper, other_renewables, port_ownership.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 1T22 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_1t22_capex_692m_brl", "Investimento Total", 691.9887186039639,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_1t22_588m_brl", "Operação Norte", 587.6949568600008,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_1t22_149m_brl", "Operação Norte Recorrente", 149.3156620799994,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_1t22_438m_brl", "Operação Norte Expansão", 438.3792947800015,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_1t22_77m_brl", "Material Rodante", 77.4567312399999,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_1t22_318m_brl", "Capacitação Malha Ferroviária", 317.8227447300016,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_1t22_25m_brl", "Capacitação Porto e Terminais", 25.265093369999995,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_1t22_18m_brl", "Ferrovia do Mato Grosso", 17.83472544,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_1t22_99m_brl", "Operação Sul", 98.73413219000014,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_1t22_97m_brl", "Operação Sul Recorrente", 96.81225522000014,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_1t22_2m_brl", "Operação Sul Expansão", 1.92187697,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_1t22_6m_brl", "Brado (Contêineres)", 5.55962955396288,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_1t22_1m_brl", "Brado Recorrente", 1.2,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_1t22_4m_brl", "Brado Expansão", 4.35962955396288,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
