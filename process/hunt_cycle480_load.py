"""Cycle 480 hunt: shuffle_seed=20261480; Rumo CapEx planilha 3T23.

Shuffle: port_cranes, bridges_roads, building_materials, balsa, lithium, niobium, water, port_ownership, fission_smr, power_plants_grid, graphite, other_renewables, engineering_epc, wind, solar, copper, rail, nickel.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 3T23 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_3t23_capex_895m_brl", "Investimento Total", 895.2161477300002,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_3t23_765m_brl", "Operação Norte", 765.0714320425006,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_3t23_235m_brl", "Operação Norte Recorrente", 234.7139639174999,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_3t23_530m_brl", "Operação Norte Expansão", 530.3574681250008,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_3t23_42m_brl", "Material Rodante", 42.41900497999998,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_3t23_374m_brl", "Capacitação Malha Ferroviária", 374.4496877150008,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_3t23_46m_brl", "Capacitação Porto e Terminais", 45.817916860000004,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_3t23_68m_brl", "Ferrovia do Mato Grosso", 67.67085857000001,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_3t23_120m_brl", "Operação Sul", 119.62856138999965,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_3t23_104m_brl", "Operação Sul Recorrente", 103.70357296249945,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_3t23_16m_brl", "Operação Sul Expansão", 15.924988427500196,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_3t23_11m_brl", "Brado (Contêineres)", 10.5161543,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_3t23_7m_brl", "Brado Recorrente", 6.6625,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_3t23_4m_brl", "Brado Expansão", 3.8536543000000005,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
