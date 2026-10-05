"""Cycle 470 hunt: shuffle_seed=20261470; Rumo CapEx planilha 1T26.

Shuffle: balsa, graphite, wind, port_ownership, engineering_epc, bridges_roads, power_plants_grid, nickel, copper, niobium, fission_smr, lithium, rail, water, solar, port_cranes, building_materials, other_renewables.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 1T26 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_1t26_capex_1774m_brl", "Investimento Total", 1773.546408839999,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_1t26_1594m_brl", "Operação Norte", 1594.281858829999,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_1t26_365m_brl", "Operação Norte Recorrente", 365.29458757,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_1t26_1229m_brl", "Operação Norte Expansão", 1228.987271259999,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_1t26_432m_brl", "Material Rodante", 431.87298811,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_1t26_466m_brl", "Capacitação Malha Ferroviária", 466.21722033999896,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_1t26_2m_brl", "Capacitação Porto e Terminais", 1.622138899999994,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_1t26_329m_brl", "Ferrovia do Mato Grosso", 329.2749239100001,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_1t26_161m_brl", "Operação Sul", 160.56423532,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_1t26_161m_brl", "Operação Sul Recorrente", 160.56423532,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_conteiner_1t26_19m_brl", "Brado (Contêineres)", 18.70031469,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_1t26_7m_brl", "Brado Recorrente", 6.769792639999918,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_1t26_12m_brl", "Brado Expansão", 11.93052205000008,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
