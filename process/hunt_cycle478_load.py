"""Cycle 478 hunt: shuffle_seed=20261478; Rumo CapEx planilha 1T24.

Shuffle: copper, balsa, other_renewables, graphite, rail, port_cranes, nickel, engineering_epc, niobium, power_plants_grid, building_materials, bridges_roads, port_ownership, lithium, wind, solar, water, fission_smr.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 1T24 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_1t24_capex_967m_brl", "Investimento Total", 967.1064865135721,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_1t24_778m_brl", "Operação Norte", 777.612477453572,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_1t24_256m_brl", "Operação Norte Recorrente", 255.66034343,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_1t24_522m_brl", "Operação Norte Expansão", 521.952134023572,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_1t24_96m_brl", "Material Rodante", 96.19796227999998,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_1t24_309m_brl", "Capacitação Malha Ferroviária", 309.138155823572,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_1t24_35m_brl", "Capacitação Porto e Terminais", 35.10376772,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_1t24_82m_brl", "Ferrovia do Mato Grosso", 81.5122482,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_1t24_186m_brl", "Operação Sul", 185.64239939000004,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_1t24_129m_brl", "Operação Sul Recorrente", 128.76365374000017,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_1t24_57m_brl", "Operação Sul Expansão", 56.87874564999984,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_1t24_4m_brl", "Brado (Contêineres)", 3.8516096699999993,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_1t24_6m_brl", "Brado Recorrente", 5.887499999999999,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente")
]
