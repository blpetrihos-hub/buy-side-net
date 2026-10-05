"""Cycle 482 hunt: shuffle_seed=20261482; Rumo CapEx planilha 1T23.

Shuffle: port_cranes, wind, graphite, nickel, solar, engineering_epc, building_materials, power_plants_grid, fission_smr, niobium, rail, water, lithium, copper, balsa, other_renewables, port_ownership, bridges_roads.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 1T23 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_1t23_capex_928m_brl", "Investimento Total", 927.8331002899981,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_1t23_782m_brl", "Operação Norte", 782.4891023724981,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_1t23_194m_brl", "Operação Norte Recorrente", 194.36236039749917,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_1t23_588m_brl", "Operação Norte Expansão", 588.1267419749989,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_1t23_81m_brl", "Material Rodante", 81.11252457999998,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_1t23_481m_brl", "Capacitação Malha Ferroviária", 480.620141944999,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_1t23_2m_brl", "Capacitação Porto e Terminais", 1.96645012000001,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_1t23_24m_brl", "Ferrovia do Mato Grosso", 24.42762533,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_1t23_145m_brl", "Operação Sul", 145.48257650000008,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_1t23_129m_brl", "Operação Sul Recorrente", 129.01433486249988,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_1t23_16m_brl", "Operação Sul Expansão", 16.468241637500192,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_recorrente_1t23_0m_brl", "Brado Recorrente", 0.4,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente")
]
