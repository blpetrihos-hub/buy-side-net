"""Cycle 483 hunt: shuffle_seed=20261483; Rumo CapEx planilha 4T22.

Shuffle: engineering_epc, wind, other_renewables, graphite, solar, rail, water, balsa, port_cranes, nickel, niobium, building_materials, fission_smr, port_ownership, bridges_roads, lithium, power_plants_grid, copper.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 4T22 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_4t22_capex_740m_brl", "Investimento Total", 740.4716733899995,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_4t22_615m_brl", "Operação Norte", 614.87531383,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_4t22_230m_brl", "Operação Norte Recorrente", 230.07043500999936,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_4t22_385m_brl", "Operação Norte Expansão", 384.8048788200007,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_4t22_68m_brl", "Material Rodante", 68.13683462,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_4t22_236m_brl", "Capacitação Malha Ferroviária", 236.07620029000074,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_4t22_43m_brl", "Capacitação Porto e Terminais", 43.098292830000005,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_4t22_37m_brl", "Ferrovia do Mato Grosso", 37.49355108,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_4t22_117m_brl", "Operação Sul", 116.98507550999952,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_4t22_105m_brl", "Operação Sul Recorrente", 105.2153136899995,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_4t22_12m_brl", "Operação Sul Expansão", 11.76976182,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_4t22_9m_brl", "Brado (Contêineres)", 8.611284049999998,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_4t22_1m_brl", "Brado Recorrente", 1.2,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_4t22_7m_brl", "Brado Expansão", 7.411284049999999,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
