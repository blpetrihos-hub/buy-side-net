"""Cycle 485 hunt: shuffle_seed=20261485; Rumo CapEx planilha 2T22.

Shuffle: solar, other_renewables, fission_smr, nickel, copper, lithium, building_materials, niobium, power_plants_grid, port_ownership, wind, graphite, balsa, water, engineering_epc, port_cranes, bridges_roads, rail.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 2T22 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_2t22_capex_678m_brl", "Investimento Total", 678.3534856700002,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_2t22_586m_brl", "Operação Norte", 586.2954522000009,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_2t22_200m_brl", "Operação Norte Recorrente", 199.5028658000001,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_2t22_387m_brl", "Operação Norte Expansão", 386.79258640000074,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_2t22_96m_brl", "Material Rodante", 96.06798767000006,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_2t22_278m_brl", "Capacitação Malha Ferroviária", 277.5167153100007,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_2t22_10m_brl", "Capacitação Porto e Terminais", 10.17582424,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_2t22_3m_brl", "Ferrovia do Mato Grosso", 3.0320591799999996,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_2t22_86m_brl", "Operação Sul", 85.8089931899992,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_2t22_84m_brl", "Operação Sul Recorrente", 84.47702016999921,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_2t22_1m_brl", "Operação Sul Expansão", 1.33197302,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_2t22_6m_brl", "Brado (Contêineres)", 6.2490402800000036,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_2t22_1m_brl", "Brado Recorrente", 1.2,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_2t22_5m_brl", "Brado Expansão", 5.049040280000003,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
