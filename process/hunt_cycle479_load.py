"""Cycle 479 hunt: shuffle_seed=20261479; Rumo CapEx planilha 4T23.

Shuffle: rail, wind, graphite, power_plants_grid, fission_smr, copper, engineering_epc, niobium, lithium, balsa, nickel, other_renewables, bridges_roads, port_ownership, water, port_cranes, building_materials, solar.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 4T23 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_4t23_capex_1221m_brl", "Investimento Total", 1221.267303180005,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_4t23_1046m_brl", "Operação Norte", 1046.2928593325048,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_4t23_279m_brl", "Operação Norte Recorrente", 279.11065121750084,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_4t23_767m_brl", "Operação Norte Expansão", 767.182208115004,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_4t23_160m_brl", "Material Rodante", 159.87148723,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_4t23_306m_brl", "Capacitação Malha Ferroviária", 305.87776050500395,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_4t23_44m_brl", "Capacitação Porto e Terminais", 44.26321534,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_4t23_257m_brl", "Ferrovia do Mato Grosso", 257.16974504,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_4t23_157m_brl", "Operação Sul", 156.53199462000052,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_4t23_138m_brl", "Operação Sul Recorrente", 138.2150495225003,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_4t23_18m_brl", "Operação Sul Expansão", 18.316945097500195,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_4t23_18m_brl", "Brado (Contêineres)", 18.44244923,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_4t23_7m_brl", "Brado Recorrente", 6.862499999999996,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_4t23_12m_brl", "Brado Expansão", 11.579949230000004,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
