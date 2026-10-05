"""Cycle 475 hunt: shuffle_seed=20261475; Rumo CapEx planilha 4T24.

Shuffle: wind, solar, power_plants_grid, bridges_roads, other_renewables, rail, graphite, port_ownership, water, engineering_epc, niobium, fission_smr, building_materials, nickel, lithium, port_cranes, copper, balsa.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 4T24 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_4t24_capex_1912m_brl", "Investimento Total", 1911.6534154799988,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_4t24_1624m_brl", "Operação Norte", 1624.1845535599996,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_4t24_298m_brl", "Operação Norte Recorrente", 298.4267266799997,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_4t24_1326m_brl", "Operação Norte Expansão", 1325.75782688,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_4t24_184m_brl", "Material Rodante", 184.12162434,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_4t24_219m_brl", "Capacitação Malha Ferroviária", 218.72509688000005,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_4t24_75m_brl", "Capacitação Porto e Terminais", 74.8839794,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_4t24_848m_brl", "Ferrovia do Mato Grosso", 848.0271262599999,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_4t24_247m_brl", "Operação Sul", 246.7964852299993,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_4t24_208m_brl", "Operação Sul Recorrente", 208.2468137099996,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_4t24_39m_brl", "Operação Sul Expansão", 38.549671519999684,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_4t24_41m_brl", "Brado (Contêineres)", 40.67237668999999,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_4t24_6m_brl", "Brado Recorrente", 5.887499999999999,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_4t24_35m_brl", "Brado Expansão", 34.78487669,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
