"""Cycle 472 hunt: shuffle_seed=20261472; Rumo CapEx planilha 3T25.

Shuffle: fission_smr, bridges_roads, copper, power_plants_grid, graphite, port_ownership, nickel, lithium, other_renewables, building_materials, balsa, wind, engineering_epc, water, solar, rail, port_cranes, niobium.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 3T25 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_3t25_capex_1474m_brl", "Investimento Total", 1474.3228862900005,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_3t25_1269m_brl", "Operação Norte", 1268.7105790499998,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_3t25_305m_brl", "Operação Norte Recorrente", 304.7611214899995,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_3t25_964m_brl", "Operação Norte Expansão", 963.9494575600002,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_3t25_0m_brl", "Material Rodante", 0.02685749,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_3t25_356m_brl", "Capacitação Malha Ferroviária", 356.3635917100001,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_3t25_32m_brl", "Capacitação Porto e Terminais", 32.316176639999995,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_3t25_575m_brl", "Ferrovia do Mato Grosso", 575.24283172,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_3t25_192m_brl", "Operação Sul", 191.66643550000046,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_3t25_192m_brl", "Operação Sul Recorrente", 191.66643550000046,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_conteiner_3t25_14m_brl", "Brado (Contêineres)", 13.945871740000001,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_3t25_6m_brl", "Brado Recorrente", 6.2645,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_3t25_8m_brl", "Brado Expansão", 7.6813717399999994,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
