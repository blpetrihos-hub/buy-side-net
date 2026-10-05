"""Cycle 490 hunt: shuffle_seed=20261490; Rumo CapEx planilha 1T21.

Shuffle: engineering_epc, lithium, port_cranes, niobium, port_ownership, bridges_roads, solar, graphite, fission_smr, balsa, nickel, building_materials, water, rail, other_renewables, power_plants_grid, wind, copper.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 1T21 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_1t21_capex_937m_brl", "Investimento Total", 936.8146088100007,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_1t21_739m_brl", "Operação Norte", 738.7462846500003,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_1t21_157m_brl", "Operação Norte Recorrente", 156.84932798999915,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_1t21_582m_brl", "Operação Norte Expansão", 581.8969566600013,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_1t21_262m_brl", "Material Rodante", 262.36703909000005,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_1t21_202m_brl", "Capacitação Malha Ferroviária", 202.45407832000114,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_1t21_116m_brl", "Capacitação Porto e Terminais", 115.60297257999997,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_1t21_1m_brl", "Ferrovia do Mato Grosso", 1.47286667,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_1t21_187m_brl", "Operação Sul", 187.14063162000042,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_1t21_122m_brl", "Operação Sul Recorrente", 122.41606768000042,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_1t21_65m_brl", "Operação Sul Expansão", 64.72456394000001,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_1t21_11m_brl", "Brado (Contêineres)", 10.927692540000008,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_1t21_2m_brl", "Brado Recorrente", 1.6875,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_1t21_9m_brl", "Brado Expansão", 9.240192540000008,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
