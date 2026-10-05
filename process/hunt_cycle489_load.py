"""Cycle 489 hunt: shuffle_seed=20261489; Rumo CapEx planilha 2T21.

Shuffle: nickel, bridges_roads, lithium, copper, rail, balsa, water, solar, building_materials, fission_smr, graphite, power_plants_grid, other_renewables, niobium, engineering_epc, port_ownership, wind, port_cranes.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 2T21 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_2t21_capex_1041m_brl", "Investimento Total", 1041.2716760466194,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_2t21_854m_brl", "Operação Norte", 854.0605147600003,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_2t21_138m_brl", "Operação Norte Recorrente", 138.09971221999956,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_2t21_716m_brl", "Operação Norte Expansão", 715.9608025400008,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_2t21_190m_brl", "Material Rodante", 190.21979077000003,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_2t21_386m_brl", "Capacitação Malha Ferroviária", 385.94492549000074,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_2t21_97m_brl", "Capacitação Porto e Terminais", 96.87840843,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_2t21_43m_brl", "Ferrovia do Mato Grosso", 42.91767785,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_2t21_171m_brl", "Operação Sul", 170.98791001000026,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_2t21_132m_brl", "Operação Sul Recorrente", 131.7503627000003,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_2t21_39m_brl", "Operação Sul Expansão", 39.23754731,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_2t21_16m_brl", "Brado (Contêineres)", 16.223251276618775,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_2t21_2m_brl", "Brado Recorrente", 1.6875,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_2t21_15m_brl", "Brado Expansão", 14.535751276618775,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
