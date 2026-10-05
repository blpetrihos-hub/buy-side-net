#!/usr/bin/env python3
"""Cycle 223 hunt: shuffle_seed=20261223; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261223).shuffle):
bridges_roads, nickel, niobium, engineering_epc, solar, port_ownership, lithium,
building_materials, wind, graphite, fission_smr, port_cranes, water, balsa, copper,
rail, power_plants_grid, other_renewables.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry; next-thinnest niobium CapEx-fill (CBMM Araxá R$630m 2024 spend).
≥1/3 U.S. hunt budget spent on SSA Guaymas TUM CapEx-fill (MXN 424.8m ASIPONA via
Radar Sonora) + Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/Jervois/
Wabtec/Fluence sweeps (1 US CapEx-fill; US blank-USD residual otherwise exhausted).
PRC equal-budget: CPFL 2026–2030 plan + SPIC São Simão UG7 CapEx-fills; PowerChina
Vicuña / Sungrow Observatorio / Goldwind already logged; holdovers unsigned.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "codebook" / "observations.csv"
EVID = ROOT / "data" / "attribution" / "evidence"
BIB = ROOT / "sources" / "bibliography.yml"
FIELDS = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")).fieldnames)
ITEMS: list[tuple[dict, dict, dict]] = []

BRL_USD = "5.1921"
BRL_FX_DATE = "2026-09-25"
MXN_USD = "17.6932"
MXN_FX_DATE = "2026-09-25"
EUR_USD = "1.1400"  # Fed H.10 Sep 25 2026 USD per EUR (asterisk)


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid, "layer": layer, "subcategory": subcategory, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": currency,
            "value_usd": value_usd, "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "", "year": year, "status": "active",
            "lat": lat, "lon": lon, "geo_note": geo, "evidence": evidence,
            "source_id": source_id, "note": note, "pair_id": "", "counterpart_side": "",
            "counterpart_actor": "", "counterpart_value": "", "counterpart_currency": "",
            "counterpart_value_usd": "", "gap": "",
        },
        {
            "id": rid, "retrieved": "2026-10-04", "source_id": source_id, "url": url,
            "price_year": year, "evidence": evidence, "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id, "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url, "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. port_ownership / us — CapEx-fill SSA Guaymas TUM MXN 424.8m
row_doc(
    "ssa_guaymas_tum_concession_2025",
    "infrastructure", "port_ownership", "us",
    "SSA Marine México — Guaymas Multi-Use Terminal (TUM) concession / CapEx",
    "Mexico",
    "15 Oct 2025 SSA Marine México signs Guaymas TUM partial rights-transfer (106,439.689 m²; Dock T1 329 m / 16 m depth; 44,236 m² yard). CapEx-fill: Radar Sonora 19 Sep 2026 citing ASIPONA Guaymas — project investment MXN 424.8 million Mexican capital. Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~24.01m. Distinct from ssa_guaymas_sts_ertg_2026 crane-delivery presence (CapEx blank).",
    "424800000", MXN_FX_DATE, "2025", "27.92", "-110.89",
    "Puerto de Guaymas, Sonora (company / ASIPONA geography).",
    "radar_sonora_ssa_guaymas_20260919",
    "El proyecto de SSA Marine México contempla una inversión de 424.8 millones de pesos de capital mexicano y la generación de 50 empleos directos y 70 indirectos, de acuerdo con información presentada por la Administración del Sistema Portuario Nacional (ASIPONA) Guaymas.",
    "https://www.radarsonora.com/activaran-gruas-gigantes-antes-de-cerrar-el-ano/",
    "Actor: SSA Marine / Carrix (U.S.) via SSA Marine México — us. CapEx-fill: enter MXN 424.8m ASIPONA figure; Fed H.10 Sep 25 2026 FX to USD ~24.01m. ≥1/3 U.S. hunt / shuffle port_ownership.",
    "hunt_cycle223", investment_type="concession_capex", evidence="documented", currency="MXN",
    value_usd=str(round(424800000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='Radar Sonora. “Activarán grúas gigantes antes de cerrar el año.” September 19, 2026. https://www.radarsonora.com/activaran-gruas-gigantes-antes-de-cerrar-el-ano/.',
    annotation="SSA Guaymas TUM CapEx-fill ~USD 24.01m via Fed H.10 (ASIPONA MXN 424.8m). Supports ssa_guaymas_tum_concession_2025.",
    evid_note="Opened Radar Sonora Spanish citing ASIPONA Guaymas; MXN 424.8m investment confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 2. bridges_roads / allied — CapEx-fill ACCIONA Roberto Marinho R$2.099bn (company €334m dual)
row_doc(
    "acciona_roberto_marinho_sp_2p099bn_2026",
    "infrastructure", "bridges_roads", "allied",
    "ACCIONA — Avenida Roberto Marinho–Rodovia dos Imigrantes road link + linear park (São Paulo)",
    "Brazil",
    "15 Jan 2026 ACCIONA: City of São Paulo awards ACCIONA the contract to build the road section linking Avenida Jornalista Roberto Marinho with Rodovia dos Imigrantes; contract valued at R$2.099 billion (€334 million). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~404.27m for stored R$2.099bn face (company also duals €334m).",
    "2099000000", BRL_FX_DATE, "2026", "-23.65", "-46.65",
    "Avenida Roberto Marinho / Rodovia dos Imigrantes corridor, southern São Paulo (company geography).",
    "acciona_roberto_marinho_20260115",
    "The City Council of São Paulo (Brazil) has awarded ACCIONA the contract to build the road section linking Avenida Jornalista Roberto Marinho with Rodovia dos Imigrantes … The contract, valued at R$2.099 billion (€334 million), includes the construction of three new lanes in each carriageway along a 4.7 kilometer stretch, incorporating three viaducts and two tunnels, as well as a cycle lane.",
    "https://www.acciona.com/updates/news/acciona-awarded-road-link-southern-sao-paulo",
    "Actor: ACCIONA (Spain) — allied. CapEx-fill: retain R$2.099bn; add Fed H.10 Sep 25 2026 FX to USD ~404.27m. Shuffle bridges_roads.",
    "hunt_cycle223", investment_type="epc", evidence="documented", currency="BRL",
    value_usd=str(round(2099000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ACCIONA. “ACCIONA awarded road link project in southern São Paulo.” January 15, 2026. https://www.acciona.com/updates/news/acciona-awarded-road-link-southern-sao-paulo.',
    annotation="ACCIONA Roberto Marinho CapEx-fill ~USD 404.27m via Fed H.10. Supports acciona_roberto_marinho_sp_2p099bn_2026.",
    evid_note="Opened ACCIONA English; R$2.099bn / €334m dual / 4.7 km confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. bridges_roads / allied — CapEx-fill Aldesa Chiapas tunnels company EUR 33m dual
row_doc(
    "aldesa_chiapas_tunnels_659m_2026",
    "infrastructure", "bridges_roads", "allied",
    "Aldesa — two tunnels Palenque–Ocosingo (Chiapas / Palenque–San Cristóbal highway)",
    "Mexico",
    "27 Aug 2026 Aldesa: awarded two tunnels on Palenque–Ocosingo stretch (Palenque–San Cristóbal de las Casas highway, Chiapas) by SICT for more than MXN 659 million (about EUR 33 million); ~17-month execution. CapEx-fill: company dual-quotes ~EUR 33m — Fed H.10 Sep 25 2026 USD/EUR 1.1400 → USD ~37.62m (retain MXN 659m face).",
    "659000000", "2026-08-27", "2026", "17.15", "-92.25",
    "Palenque–Ocosingo highway stretch, Chiapas (company geography; approximate corridor pin).",
    "aldesa_chiapas_tuneles_20260827",
    "Las actuaciones para sendos proyectos, adjudicadas por la Secretaría de Infraestructura, Comunicaciones y Transporte por más de 659 millones de pesos mexicanos (unos 33 millones de euros), tienen un plazo previsto de ejecución de unos 17 meses.",
    "https://aldesa.com/aldesa-se-adjudica-la-construccion-de-dos-tuneles-en-mexico-por-33-millones-de-euros/",
    "Actor: Aldesa (Spain) — allied. CapEx-fill: company dual ~EUR 33m → USD ~37.62m via Fed H.10 EUR; retain MXN 659m face. Shuffle bridges_roads.",
    "hunt_cycle223", investment_type="epc", evidence="documented", currency="MXN",
    value_usd=str(round(33000000 * float(EUR_USD), 2)),
    fx_usd=str(round(659000000 / (33000000 * float(EUR_USD)), 4)),
    chicago='Aldesa. “Aldesa se adjudica la construcción de dos túneles en México por 33 millones de euros.” August 27, 2026. https://aldesa.com/aldesa-se-adjudica-la-construccion-de-dos-tuneles-en-mexico-por-33-millones-de-euros/.',
    annotation="Aldesa Chiapas CapEx-fill company EUR 33m dual → ~USD 37.62m via Fed H.10. Supports aldesa_chiapas_tunnels_659m_2026.",
    evid_note="Opened Aldesa Spanish; >MXN 659m / ~EUR 33m dual confirmed. CapEx-fill uses company EUR × Fed H.10 Sep 25 2026 1.1400 USD/EUR.",
)

# 4. building_materials / allied — CapEx-fill Holcim ECOPact silos MXN 56m
row_doc(
    "holcim_mexico_ecopact_silos_56mdp_2025",
    "infrastructure", "building_materials", "allied",
    "Holcim México — ECOPact production/distribution silo expansion",
    "Mexico",
    "Holcim México announces strategic investment of MXN 56 million to expand ECOPact production and distribution capacity (27 silos). CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~3.17m for stored MXN 56m face.",
    "56000000", MXN_FX_DATE, "2025", "", "",
    "Holcim México ECOPact silo network (company; multi-site — coordinates blank).",
    "holcim_mexico_ecopact_56mdp_20250625",
    "Holcim México … anunció una inversión estratégica de 56 millones de pesos para expandir significativamente su capacidad de producción y distribución de ECOPact … instalación de 27 silos.",
    "https://www.holcim.com.mx/holcim-mexico-impulsa-la-construccion-sostenible-con-inversion-de-56-millones-en-infraestructura",
    "Actor: Holcim México (Switzerland Holcim) — allied. CapEx-fill: retain MXN 56m; add Fed H.10 Sep 25 2026 FX to USD ~3.17m. Shuffle building_materials.",
    "hunt_cycle223", investment_type="plant_capex", evidence="documented", currency="MXN",
    value_usd=str(round(56000000 / float(MXN_USD), 2)), fx_usd=MXN_USD,
    chicago='Holcim México. “Holcim México impulsa la construcción sostenible con inversión de 56 millones en infraestructura.” June 25, 2025. https://www.holcim.com.mx/holcim-mexico-impulsa-la-construccion-sostenible-con-inversion-de-56-millones-en-infraestructura.',
    annotation="Holcim ECOPact CapEx-fill ~USD 3.17m via Fed H.10. Supports holcim_mexico_ecopact_silos_56mdp_2025.",
    evid_note="Opened Holcim México Spanish; MXN 56m / 27 ECOPact silos confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 5. power_plants_grid / prc — CapEx-fill CPFL 2026–2030 plan R$31.1bn
row_doc(
    "cpfl_capex_plan_31p1bn_2026_2030",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — 2026–2030 investment plan",
    "Brazil",
    "6 Mar 2026 CPFL Energia: Board approves new investment plan for 2026–2030 totaling R$ 31.1 billion (R$ 25.3 billion distribution). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~5990.28m for stored R$31.1bn face. Distinct from cpfl_fy2025_capex_6p1bn_brl executed CapEx.",
    "31100000000", BRL_FX_DATE, "2026", "", "",
    "CPFL Energia Brazil multi-concession footprint (national; no single-site pin).",
    "cpfl_fy2025_results_20260306",
    "O Conselho de Administração aprovou ainda o novo plano de investimentos para o período de 2026 a 2030, que totaliza R$ 31,1 bilhões, sendo R$ 25,3 bilhões para o segmento de Distribuição.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61",
    "Actor: CPFL Energia — State Grid–controlled — prc. CapEx-fill: retain R$31.1bn plan; add Fed H.10 Sep 25 2026 FX to USD ~5990.28m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle223", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(31100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CPFL Energia. “CPFL Energia registra EBITDA de R$ 13,5 bilhões em 2025 e investimento recorde de R$ 6,1 bilhões.” March 6, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61.',
    annotation="CPFL 2026–2030 CapEx-fill ~USD 5990.28m via Fed H.10. Supports cpfl_capex_plan_31p1bn_2026_2030.",
    evid_note="Opened CPFL Portuguese; R$31.1bn 2026–2030 plan confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. power_plants_grid / prc — CapEx-fill SPIC São Simão UG7 >R$1bn
row_doc(
    "spic_sao_simao_ug7_lrcap_2026",
    "energy", "power_plants_grid", "prc",
    "SPIC Brasil — UHE São Simão UG7 expansion via LRCAP (>R$1bn)",
    "Brazil",
    "19 Mar 2026 SPIC Brasil: will expand UHE São Simão by 310 MW via Capacity Reserve Auction with more than R$ 1 billion investment. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~192.60m for stored R$1bn floor face.",
    "1000000000", BRL_FX_DATE, "2026", "-18.99", "-50.51",
    "UHE São Simão, Minas Gerais / Goiás border (company geography).",
    "spic_brasil_sao_simao_ug7_20260319",
    "O projeto representa um investimento de mais de R$ 1 bilhão e reforça o papel estratégico da fonte hidrelétrica para a segurança elétrica, modicidade tarifária, sustentabilidade ambiental e desenvolvimento regional.",
    "https://www.spicbrasil.com.br/destaque/spic-brasil-expandira-a-uhe-sao-simao-em-310-mw-via-leilao-de-reserva-de-capacidade-com-mais-de-r-1-bilhao-em-investimentos/",
    "Actor: SPIC Brasil (State Power Investment Corp., PRC) — prc. CapEx-fill: retain >R$1bn floor; add Fed H.10 Sep 25 2026 FX to USD ~192.60m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle223", investment_type="expansion", evidence="documented", currency="BRL",
    value_usd=str(round(1000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='SPIC Brasil. “SPIC Brasil expandirá a UHE São Simão em 310 MW via Leilão de Reserva de Capacidade, com mais de R$ 1 bilhão em investimentos.” March 19, 2026. https://www.spicbrasil.com.br/destaque/spic-brasil-expandira-a-uhe-sao-simao-em-310-mw-via-leilao-de-reserva-de-capacidade-com-mais-de-r-1-bilhao-em-investimentos/.',
    annotation="SPIC São Simão UG7 CapEx-fill ~USD 192.60m via Fed H.10. Supports spic_sao_simao_ug7_lrcap_2026.",
    evid_note="Opened SPIC Brasil Portuguese; >R$1bn / 310 MW LRCAP confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. niobium / allied — CapEx-fill CBMM Araxá R$630m 2024 (thin next-thinnest)
row_doc(
    "cbmm_araxa_capex_630m_2024",
    "resources", "niobium", "allied",
    "CBMM — Araxá 2024 CapEx spend",
    "Brazil",
    "CBMM 2024 results release: continuous investments; CapEx of R$ 630 million in 2024 at Araxá operations (stored face). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~121.34m for stored R$630m face. Distinct from cbmm_araxa_2026_spend_2bn / 13bn plan rows.",
    "630000000", BRL_FX_DATE, "2024", "-19.59", "-46.94",
    "CBMM Araxá, Minas Gerais (company geography).",
    "cbmm_results_2024_release_20250424",
    "Os investimentos contínuos da companhia em pesquisa e desenvolvimento, além de sua sólida capacidade logística possibilitaram um resultado financeiro e operacional positivo com receita líquida de R$ 13 bilhões; lucro líquido de R$ 5 bilhões; e Capex de R$ 630 milhões.",
    "https://cbmm.com/-/media/CBMM/MEDIA-CENTER/Noticias-Internas/resultado-final-2024/CBMM_Release-de-Resultados-2025---Final---22042025.pdf",
    "Actor: CBMM (Brazilian Moreira Salles–controlled) — allied. CapEx-fill: retain R$630m 2024 CapEx; add Fed H.10 Sep 25 2026 FX to USD ~121.34m. Thin next-thinnest niobium (balsa/nickel/fission_smr dry).",
    "hunt_cycle223", investment_type="capex_spend", evidence="documented", currency="BRL",
    value_usd=str(round(630000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CBMM. “Release de Resultados 2024.” April 24, 2025. https://cbmm.com/-/media/CBMM/MEDIA-CENTER/Noticias-Internas/resultado-final-2024/CBMM_Release-de-Resultados-2025---Final---22042025.pdf.',
    annotation="CBMM Araxá 2024 CapEx-fill ~USD 121.34m via Fed H.10. Supports cbmm_araxa_capex_630m_2024.",
    evid_note="Opened CBMM Portuguese results PDF; R$630m 2024 CapEx confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added, updated = [], []
    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            existing = rows[by_id[rid]]
            for k, v in full.items():
                if k != "id" and v != "" and v is not None:
                    existing[k] = v
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        upsert_bib(bib, bib_by, bib_e)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle223 added {len(added)}: {added}")
    print(f"cycle223 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
