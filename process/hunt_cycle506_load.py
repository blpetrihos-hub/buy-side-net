"""Cycle 506 hunt: shuffle_seed=20261506; Equatorial Investimentos 2T22.
Shuffle: graphite, lithium, solar, rail, niobium, bridges_roads, nickel, port_cranes, building_materials, power_plants_grid, fission_smr, engineering_epc, balsa, other_renewables, water, port_ownership, wind, copper.
Thin/US CapEx dry. OTHER: NEW Equatorial Investimentos 2T22 faces."""
ITEMS = [
    ("equatorial_ma_2t22_243m_brl", "Maranhão Total", 242.76999939000115, "-2.53", "-44.30", "Equatorial Maranhão distribution (São Luís pin).", True, "power_plants_grid", "ma"),
    ("equatorial_ma_eletricos_2t22_206m_brl", "Maranhão Ativos elétricos", 206.06306611000107, "-2.53", "-44.30", "Equatorial Maranhão distribution (São Luís pin).", False, "power_plants_grid", "ma_eletricos"),
    ("equatorial_ma_oe_2t22_21m_brl", "Maranhão Obrigações especiais", 21.471118650000086, "-2.53", "-44.30", "Equatorial Maranhão distribution (São Luís pin).", False, "power_plants_grid", "ma_oe"),
    ("equatorial_ma_nonelectric_2t22_15m_brl", "Maranhão Ativos não elétricos", 15.235814629999997, "-2.53", "-44.30", "Equatorial Maranhão distribution (São Luís pin).", False, "power_plants_grid", "ma_nonelectric"),
    ("equatorial_ma_pe_2t22_1m_brl", "Maranhão Projetos Estratégicos", 0.899, "-2.53", "-44.30", "Equatorial Maranhão distribution (São Luís pin).", False, "power_plants_grid", "ma_pe"),
    ("equatorial_pa_2t22_438m_brl", "Pará Total", 438.0358254700046, "-1.46", "-48.50", "Equatorial Pará distribution (Belém pin).", True, "power_plants_grid", "pa"),
    ("equatorial_pa_eletricos_2t22_303m_brl", "Pará Ativos elétricos", 302.84574810000527, "-1.46", "-48.50", "Equatorial Pará distribution (Belém pin).", False, "power_plants_grid", "pa_eletricos"),
    ("equatorial_pa_oe_2t22_119m_brl", "Pará Obrigações especiais", 118.51523322999937, "-1.46", "-48.50", "Equatorial Pará distribution (Belém pin).", False, "power_plants_grid", "pa_oe"),
    ("equatorial_pa_nonelectric_2t22_17m_brl", "Pará Ativos não elétricos", 16.674844139999998, "-1.46", "-48.50", "Equatorial Pará distribution (Belém pin).", False, "power_plants_grid", "pa_nonelectric"),
    ("equatorial_pi_2t22_173m_brl", "Piauí Total", 172.59977101999968, "-5.09", "-42.80", "Equatorial Piauí distribution (Teresina pin).", True, "power_plants_grid", "pi"),
    ("equatorial_pi_eletricos_2t22_140m_brl", "Piauí Ativos elétricos", 140.15428201539802, "-5.09", "-42.80", "Equatorial Piauí distribution (Teresina pin).", False, "power_plants_grid", "pi_eletricos"),
    ("equatorial_pi_oe_2t22_20m_brl", "Piauí Obrigações especiais", 19.98686245460166, "-5.09", "-42.80", "Equatorial Piauí distribution (Teresina pin).", False, "power_plants_grid", "pi_oe"),
    ("equatorial_pi_nonelectric_2t22_12m_brl", "Piauí Ativos não elétricos", 12.45862655, "-5.09", "-42.80", "Equatorial Piauí distribution (Teresina pin).", False, "power_plants_grid", "pi_nonelectric"),
    ("equatorial_pi_pe_2t22_0m_brl", "Piauí Projetos Estratégicos", 0.0577935, "-5.09", "-42.80", "Equatorial Piauí distribution (Teresina pin).", False, "power_plants_grid", "pi_pe"),
    ("equatorial_al_2t22_104m_brl", "Alagoas Total", 104.48813831000018, "-9.67", "-35.74", "Equatorial Alagoas distribution (Maceió pin).", True, "power_plants_grid", "al"),
    ("equatorial_al_eletricos_2t22_94m_brl", "Alagoas Ativos elétricos", 94.06059588000018, "-9.67", "-35.74", "Equatorial Alagoas distribution (Maceió pin).", False, "power_plants_grid", "al_eletricos"),
    ("equatorial_al_nonelectric_2t22_10m_brl", "Alagoas Ativos não elétricos", 10.427542429999999, "-9.67", "-35.74", "Equatorial Alagoas distribution (Maceió pin).", False, "power_plants_grid", "al_nonelectric"),
    ("equatorial_al_pe_2t22_0m_brl", "Alagoas Projetos Estratégicos", 0.07172508, "-9.67", "-35.74", "Equatorial Alagoas distribution (Maceió pin).", False, "power_plants_grid", "al_pe"),
    ("equatorial_rs_2t22_83m_brl", "CEEE-D (RS) Total", 82.59207757999991, "-30.03", "-51.23", "Equatorial CEEE-D Rio Grande do Sul (Porto Alegre pin).", True, "power_plants_grid", "rs"),
    ("equatorial_rs_eletricos_2t22_60m_brl", "CEEE-D (RS) Ativos elétricos", 59.89863197999991, "-30.03", "-51.23", "Equatorial CEEE-D Rio Grande do Sul (Porto Alegre pin).", False, "power_plants_grid", "rs_eletricos"),
    ("equatorial_rs_oe_2t22_12m_brl", "CEEE-D (RS) Obrigações especiais", 11.938904229999999, "-30.03", "-51.23", "Equatorial CEEE-D Rio Grande do Sul (Porto Alegre pin).", False, "power_plants_grid", "rs_oe"),
    ("equatorial_rs_nonelectric_2t22_11m_brl", "CEEE-D (RS) Ativos não elétricos", 10.754541370000005, "-30.03", "-51.23", "Equatorial CEEE-D Rio Grande do Sul (Porto Alegre pin).", False, "power_plants_grid", "rs_nonelectric"),
    ("equatorial_ap_2t22_109m_brl", "CEA (AP) Total", 109.09771686999997, "0.03", "-51.07", "Equatorial CEA Amapá (Macapá pin).", True, "power_plants_grid", "ap"),
    ("equatorial_ap_eletricos_2t22_95m_brl", "CEA (AP) Ativos elétricos", 94.87967984999999, "0.03", "-51.07", "Equatorial CEA Amapá (Macapá pin).", False, "power_plants_grid", "ap_eletricos"),
    ("equatorial_ap_nonelectric_2t22_15m_brl", "CEA (AP) Ativos não elétricos", 14.588474479999984, "0.03", "-51.07", "Equatorial CEA Amapá (Macapá pin).", False, "power_plants_grid", "ap_nonelectric"),
    ("equatorial_tx_2t22_8m_brl", "Transmissão", 8.04071299, "-15.78", "-47.93", "Equatorial transmission SPEs (Brasília pin).", True, "power_plants_grid", "tx"),
    ("equatorial_echo_2t22_26m_brl", "Echoenergia", 26.129300500000017, "-8.05", "-34.88", "Equatorial Echoenergia renewables (Recife pin).", True, "other_renewables", "echo")
]
