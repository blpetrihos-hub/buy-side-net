"""Cycle 477 hunt: shuffle_seed=20261477; Rumo CapEx planilha 2T24.

Shuffle: balsa, wind, building_materials, engineering_epc, port_cranes, fission_smr, solar, niobium, water, copper, lithium, port_ownership, nickel, other_renewables, bridges_roads, rail, graphite, power_plants_grid.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 2T24 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_2t24_capex_1176m_brl", "Investimento Total", 1175.7696843613276,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_2t24_984m_brl", "Operação Norte", 983.6169815953567,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_2t24_263m_brl", "Operação Norte Recorrente", 262.91739547999987,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_2t24_721m_brl", "Operação Norte Expansão", 720.699586115357,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_2t24_40m_brl", "Material Rodante", 39.56157964999999,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_2t24_326m_brl", "Capacitação Malha Ferroviária", 325.8817255703775,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_2t24_54m_brl", "Capacitação Porto e Terminais", 54.326372924979395,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_2t24_301m_brl", "Ferrovia do Mato Grosso", 300.92990797000004,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_2t24_186m_brl", "Operação Sul", 186.16787012597075,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_2t24_149m_brl", "Operação Sul Recorrente", 149.16611689,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_2t24_37m_brl", "Operação Sul Expansão", 37.00175323597072,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_2t24_6m_brl", "Brado (Contêineres)", 5.9848326400000005,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_2t24_6m_brl", "Brado Recorrente", 5.887499999999999,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_2t24_0m_brl", "Brado Expansão", 0.09733264000000014,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
