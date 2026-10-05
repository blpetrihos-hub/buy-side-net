"""Cycle 487 hunt: shuffle_seed=20261487; Rumo CapEx planilha 4T21.

Shuffle: balsa, wind, fission_smr, bridges_roads, nickel, port_ownership, copper, lithium, niobium, building_materials, graphite, engineering_epc, solar, port_cranes, power_plants_grid, water, rail, other_renewables.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Rumo RI CAPEX planilha 4T21 rail + port_ownership nested faces.
"""
from __future__ import annotations

ITEMS = [
    ("rumo_4t21_capex_701m_brl", "Investimento Total", 700.8606962264585,
     "-23.55", "-46.63", "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).", True, "rail", "total"),
    ("rumo_norte_4t21_578m_brl", "Operação Norte", 578.3349712838567,
     "-23.55", "-46.63", "Rumo Operação Norte (São Paulo HQ pin; North corridor).", False, "rail", "norte"),
    ("rumo_norte_recorrente_4t21_235m_brl", "Operação Norte Recorrente", 234.69284628723992,
     "-23.55", "-46.63", "Rumo Operação Norte recurring CapEx (São Paulo HQ pin).", False, "rail", "norte_recorrente"),
    ("rumo_expansao_norte_4t21_344m_brl", "Operação Norte Expansão", 343.64212499661676,
     "-23.55", "-46.63", "Rumo Operação Norte expansion CapEx (São Paulo HQ pin).", False, "rail", "expansao_norte"),
    ("rumo_material_rodante_4t21_20m_brl", "Material Rodante", 20.06576926999999,
     "-23.55", "-46.63", "Rumo rolling-stock CapEx (São Paulo HQ pin).", False, "rail", "material_rodante"),
    ("rumo_capacitacao_4t21_255m_brl", "Capacitação Malha Ferroviária", 255.47811149661675,
     "-23.55", "-46.63", "Rumo rail-network capacity CapEx (São Paulo HQ pin).", False, "rail", "capacitacao"),
    ("rumo_porto_terminais_4t21_39m_brl", "Capacitação Porto e Terminais", 38.60749656,
     "-23.55", "-46.63", "Rumo port/terminal capacity CapEx (São Paulo HQ pin).", False, "port_ownership", "porto_terminais"),
    ("rumo_fmt_4t21_29m_brl", "Ferrovia do Mato Grosso", 29.490747669999998,
     "-15.60", "-56.10", "Ferrovia do Mato Grosso (Cuiabá corridor pin).", False, "rail", "fmt"),
    ("rumo_sul_4t21_119m_brl", "Operação Sul", 118.7553728651189,
     "-25.43", "-49.27", "Rumo Operação Sul (Curitiba corridor pin).", False, "rail", "sul"),
    ("rumo_sul_recorrente_4t21_68m_brl", "Operação Sul Recorrente", 67.79883375000048,
     "-25.43", "-49.27", "Rumo Operação Sul recurring CapEx (Curitiba corridor pin).", False, "rail", "sul_recorrente"),
    ("rumo_expansao_sul_4t21_51m_brl", "Operação Sul Expansão", 50.95653911511842,
     "-25.43", "-49.27", "Rumo Operação Sul expansion CapEx (Curitiba corridor pin).", False, "rail", "expansao_sul"),
    ("rumo_conteiner_4t21_4m_brl", "Brado (Contêineres)", 3.770352077482956,
     "-23.55", "-46.63", "Rumo Brado container rail CapEx (São Paulo HQ pin).", False, "rail", "conteiner"),
    ("rumo_conteiner_recorrente_4t21_2m_brl", "Brado Recorrente", 1.6875,
     "-23.55", "-46.63", "Rumo Brado recurring CapEx (São Paulo HQ pin).", False, "rail", "conteiner_recorrente"),
    ("rumo_conteiner_expansao_4t21_2m_brl", "Brado Expansão", 2.082852077482956,
     "-23.55", "-46.63", "Rumo Brado expansion CapEx (São Paulo HQ pin).", False, "rail", "conteiner_expansao")
]
