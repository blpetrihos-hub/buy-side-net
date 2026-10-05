"""Cycle 481 hunt: shuffle_seed=20261481; Rumo CapEx planilha 2T23.

Shuffle: engineering_epc, niobium, other_renewables, port_cranes, solar, wind, bridges_roads, lithium, building_materials, water, nickel, copper, rail, fission_smr, graphite, power_plants_grid, port_ownership, balsa.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 2T23 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_2t23_capex_693m_brl", "Investimento Total", 692.7741746299995,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_2t23_549m_brl", "Operação Norte", 549.3595538324993,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_2t23_213m_brl", "Operação Norte Recorrente", 213.31512760750013,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_2t23_336m_brl", "Operação Norte Expansão", 336.04442622499914,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_capacitacao_2t23_285m_brl", "Capacitação Malha Ferroviária", 285.3553516549992,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_2t23_10m_brl", "Capacitação Porto e Terminais", 9.563985469999995,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_2t23_44m_brl", "Ferrovia do Mato Grosso", 43.76258068,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_2t23_142m_brl", "Operação Sul", 141.78263353000037,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_2t23_126m_brl", "Operação Sul Recorrente", 125.54574492250002,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_2t23_16m_brl", "Operação Sul Expansão", 16.236888607500358,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_2t23_2m_brl", "Brado (Contêineres)", 1.6319872699999998,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_2t23_1m_brl", "Brado Recorrente", 0.7,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_2t23_1m_brl", "Brado Expansão", 0.93198727,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
