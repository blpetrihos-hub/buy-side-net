#!/usr/bin/env python3
"""Cycle 227 hunt: shuffle_seed=20261227; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261227).shuffle):
port_ownership, nickel, graphite, copper, lithium, power_plants_grid, engineering_epc,
water, solar, wind, niobium, building_materials, other_renewables, fission_smr,
port_cranes, balsa, rail, bridges_roads.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry; next-thinnest niobium CapEx-fill (CBMM R$10bn 5-year plan).
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty sweeps (US blank-USD residual exhausted;
SSA Progreso already CapEx-filled; 0 new US CapEx this pass — honest residual).
PRC equal-budget: CTG Serra da Palmeira CapEx-fill; CRRC/State Grid already dense;
holdovers unsigned.
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
EUR_USD = "1.1400"


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
            "id": rid, "retrieved": "2026-10-05", "source_id": source_id, "url": url,
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


# 1. port_ownership / other — CapEx-fill Hutchison ICAVE Fase II >MXN 4.5bn
row_doc(
    "hutchison_icave_fase2_4500m_mxn_2026",
    "infrastructure", "port_ownership", "other",
    "Hutchison Ports ICAVE — Veracruz Phase II expansion",
    "Mexico",
    "26 Jan 2026 La Razón: Hutchison Ports ICAVE announces investment exceeding MXN 4,500 million for Phase II at Veracruz to increase operational efficiency and sustainability. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~254.34m for stored MXN 4.5bn floor face.",
    "4500000000", MXN_FX_DATE, "2026", "19.2", "-96.13",
    "Hutchison Ports ICAVE, Veracruz (press geography).",
    "razon_icave_fase2_20260126",
    "Como parte de este proyecto, Hutchison Ports ICAVE anunció una inversión superior a los 4,500 millones de pesos, destinada a incrementar la eficiencia operativa y la sostenibilidad de sus operaciones en el Golfo de México.",
    "https://www.razon.com.mx/negocios/2026/01/26/hutchison-ports-icave-arranca-fase-ii-en-veracruz-con-inversion-superior-a-4500-millones-de-pesos/",
    "Actor: Hutchison Ports (HK) — other. CapEx-fill: retain >MXN 4.5bn floor; add Fed H.10 Sep 25 2026 FX to USD ~254.34m. Shuffle port_ownership.",
    "hunt_cycle227", investment_type="terminal_expansion", evidence="documented", currency="MXN",
    value_usd=str(round(4500000000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='La Razón. “Hutchison Ports ICAVE arranca Fase II en Veracruz con inversión superior a 4,500 millones de pesos.” January 26, 2026. https://www.razon.com.mx/negocios/2026/01/26/hutchison-ports-icave-arranca-fase-ii-en-veracruz-con-inversion-superior-a-4500-millones-de-pesos/.',
    annotation="Hutchison ICAVE Fase II CapEx-fill ~USD 254.34m via Fed H.10. Supports hutchison_icave_fase2_4500m_mxn_2026.",
    evid_note="Opened La Razón Spanish; >MXN 4.5bn / ICAVE Fase II confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 2. port_ownership / other — CapEx-fill ICTSI Aratu HSIM R$1.8bn
row_doc(
    "ictsi_aratu_hsim_2026",
    "infrastructure", "port_ownership", "other",
    "ICTSI Americas — purchase of HSIM (ATU12/ATU18 Aratu terminals)",
    "Brazil",
    "23 Jul 2026 CVM IPE: SIMPAR/CS Brasil binding SPA with ICTSI AMERICAS B.V. for 100% of HSIM (wholly owns ATU12 and ATU18 Aratu terminals); stored deal face R$1.8 billion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~346.68m for stored R$1.8bn face.",
    "1800000000", BRL_FX_DATE, "2026", "-12.78", "-38.5",
    "Porto de Aratu / HSIM ATU12–ATU18, Bahia (company geography).",
    "simpar_fr_aratu_ictsi_20260723",
    "on July 23, 2026, the Company and CS Brasil Holding … entered into a binding purchase and sale agreement with ICTSI AMERICAS B.V. for the sale of 100% of the stake in HSIM … which wholly owns ATU12 … and ATU18",
    "https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1547175",
    "Actor: ICTSI (Philippines) — other. CapEx-fill: retain R$1.8bn deal face; add Fed H.10 Sep 25 2026 FX to USD ~346.68m. Shuffle port_ownership.",
    "hunt_cycle227", investment_type="mna_acquisition", evidence="documented", currency="BRL",
    value_usd=str(round(1800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='SIMPAR / CVM. Material Fact — ICTSI Americas acquisition of HSIM (Aratu). July 23, 2026. https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1547175.',
    annotation="ICTSI Aratu CapEx-fill ~USD 346.68m via Fed H.10. Supports ictsi_aratu_hsim_2026.",
    evid_note="Opened SIMPAR CVM IPE English; HSIM/ATU12–18 Aratu SPA confirmed; CapEx-fill uses stored R$1.8bn face via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. power_plants_grid / allied — CapEx-fill Hitachi Brazil service dual US$11m
row_doc(
    "hitachi_brazil_service_50m_brl_2026",
    "energy", "power_plants_grid", "allied",
    "Hitachi Energy — Brazil Service capabilities expansion",
    "Brazil",
    "20 May 2026 Hitachi Energy: new investment of around R$50 million ($11 million USD) to expand Service capabilities in Brazil for grid modernization. CapEx-fill: enter company dual-quoted US$11 million as value_usd (retain R$50m face).",
    "50000000", "2026-05-20", "2026", "-23.55", "-46.63",
    "Hitachi Energy Brazil Service expansion (national footprint; São Paulo metro pin).",
    "hitachi_brazil_service_20260520",
    "Hitachi Energy, a global leader in electrification, will make a new investment of around R$50 million ($11 million USD) to expand its Service capabilities in Brazil.",
    "https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/05/hitachi-energy-announces-new-r-50-million-11-million-usd-investment-to-accelerate-brazil-s-grid-modernization",
    "Actor: Hitachi Energy (Japan) — allied. CapEx-fill: company dual US$11m alongside R$50m. Shuffle power_plants_grid.",
    "hunt_cycle227", investment_type="service_capex", evidence="documented", currency="BRL",
    value_usd="11000000", fx_usd=str(round(50000000 / 11000000, 4)),
    chicago='Hitachi Energy. “Hitachi Energy announces new R$50 million ($11 million USD) investment to accelerate Brazil’s grid modernization.” May 20, 2026. https://www.hitachienergy.com/us/en/news-and-events/press-releases/2026/05/hitachi-energy-announces-new-r-50-million-11-million-usd-investment-to-accelerate-brazil-s-grid-modernization.',
    annotation="Hitachi Brazil CapEx-fill company dual US$11m. Supports hitachi_brazil_service_50m_brl_2026.",
    evid_note="Opened Hitachi Energy English; R$50m / US$11m dual confirmed. CapEx-fill uses company USD.",
)

# 4. power_plants_grid / allied — CapEx-fill ENGIE Jaguara expansion R$1.2bn
row_doc(
    "engie_jaguara_expansion_1p2bn_brl_2026",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil / WEG — UHE Jaguara expansion (two new units / +232 MW)",
    "Brazil",
    "27 Jul 2026 Valor: project total investment R$ 1.2 billion to expand Jaguara installed capacity by 232 MW via two new generating units; WEG signed contract with ENGIE Brasil. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~231.12m for stored R$1.2bn face. Distinct from engie_jaguara_modernization_500m_brl_2026.",
    "1200000000", BRL_FX_DATE, "2026", "-20.02", "-47.28",
    "UHE Jaguara, Minas Gerais / São Paulo border (press geography).",
    "valor_weg_jaguara_20260727",
    "O projeto prevê um investimento total de R$ 1,2 bilhão, que permitirá ampliar a capacidade instalada da usina em 232 megawatts (MW), por meio da instalação de duas novas unidades geradoras em poços já existentes.",
    "https://valor.globo.com/empresas/noticia/2026/07/27/weg-assina-contrato-de-r-12-bi-com-a-engie-brasil-para-expanso-na-usina-de-jaguara.ghtml",
    "Actor: ENGIE Brasil (France) owner / WEG supplier — allied CapEx on ENGIE expansion row. CapEx-fill: retain R$1.2bn; add Fed H.10 Sep 25 2026 FX to USD ~231.12m. Shuffle power_plants_grid.",
    "hunt_cycle227", investment_type="expansion", evidence="documented", currency="BRL",
    value_usd=str(round(1200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Valor Econômico. “WEG assina contrato de R$ 1,2 bi com a ENGIE Brasil para expansão na usina de Jaguara.” July 27, 2026. https://valor.globo.com/empresas/noticia/2026/07/27/weg-assina-contrato-de-r-12-bi-com-a-engie-brasil-para-expanso-na-usina-de-jaguara.ghtml.',
    annotation="ENGIE Jaguara expansion CapEx-fill ~USD 231.12m via Fed H.10. Supports engie_jaguara_expansion_1p2bn_brl_2026.",
    evid_note="Opened Valor Portuguese; R$1.2bn / +232 MW confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. power_plants_grid / allied — CapEx-fill ISA Energia R&M R$370m
row_doc(
    "isa_energia_rm_370m_brl_1t26",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Q1 2026 Reinforcements & Improvements CapEx",
    "Brazil",
    "23 Jun 2026 ISA Energia Brasil: invested R$ 370 million in Reinforcements & Improvements (R&M) projects in Q1 2026 (+20.9% YoY). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~71.26m for stored R$370m face.",
    "370000000", BRL_FX_DATE, "2026", "-23.55", "-46.63",
    "ISA Energia Brasil national transmission R&M (no single-site pin; São Paulo HQ pin).",
    "isa_energia_rm_370m_20260623",
    "A ISA ENERGIA BRASIL … investiu R$ 370 milhões em projetos de Reforços e Melhorias (R&M) no primeiro trimestre de 2026, valor 20,9% superior ao registrado no mesmo período do ano anterior.",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-370-milhoes-em-reforcos-e-melhorias-na-rede-de-transmissao-nacional/",
    "Actor: ISA Energia Brasil (Colombia ISA / allied) — allied. CapEx-fill: retain R$370m Q1 2026 R&M; add Fed H.10 Sep 25 2026 FX to USD ~71.26m. Shuffle power_plants_grid.",
    "hunt_cycle227", investment_type="capex_spend", evidence="documented", currency="BRL",
    value_usd=str(round(370000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ISA Energia Brasil. “ISA Energia Brasil investe R$ 370 milhões em reforços e melhorias na rede de transmissão nacional.” June 23, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-investe-r-370-milhoes-em-reforcos-e-melhorias-na-rede-de-transmissao-nacional/.',
    annotation="ISA Energia R&M CapEx-fill ~USD 71.26m via Fed H.10. Supports isa_energia_rm_370m_brl_1t26.",
    evid_note="Opened ISA Energia Portuguese; R$370m Q1 2026 R&M confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. niobium / allied — CapEx-fill CBMM R$10bn 5-year plan (thin next)
row_doc(
    "cbmm_araxa_capex_plan_2025",
    "resources", "niobium", "allied",
    "CBMM — five-year investment plan (~R$10bn)",
    "Brazil",
    "30 Oct 2025 Folha: CBMM forecasts investments of R$ 10 billion over the next five years, half related to industrial expansion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1926.00m for stored R$10bn face. Distinct from cbmm_capex_plan_11bn_2030 / annual spend rows.",
    "10000000000", BRL_FX_DATE, "2025", "-19.59", "-46.94",
    "CBMM Araxá, Minas Gerais (company geography).",
    "folha_cbmm_capex_20251030",
    "a empresa conta com uma previsão de investimentos de R$ 10 bilhões nos próximos cinco anos, sendo que metade desse valor está relacionada com a expansão das atividades industriais",
    "https://www1.folha.uol.com.br/mercado/2025/10/cbmm-preve-elevar-producao-de-ferrobiobio-em-5-neste-ano-e-investir-r-10-bi-em-5-anos.shtml",
    "Actor: CBMM (Brazilian Moreira Salles–controlled) — allied. CapEx-fill: retain R$10bn 5-year plan; add Fed H.10 Sep 25 2026 FX to USD ~1926.00m. Thin next-thinnest niobium (balsa/nickel/fission_smr dry).",
    "hunt_cycle227", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(10000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Folha de S.Paulo. “CBMM prevê elevar produção de ferro-nióbio em 5% neste ano e investir R$ 10 bi em 5 anos.” October 30, 2025. https://www1.folha.uol.com.br/mercado/2025/10/cbmm-preve-elevar-producao-de-ferrobiobio-em-5-neste-ano-e-investir-r-10-bi-em-5-anos.shtml.',
    annotation="CBMM 5-year CapEx-fill ~USD 1926.00m via Fed H.10. Supports cbmm_araxa_capex_plan_2025.",
    evid_note="Opened Folha Portuguese; R$10bn / 5-year plan confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. port_cranes / other — CapEx-fill TIMSA MHC ESP.10 >MXN 300m
row_doc(
    "timsa_mhc_esp10_manzanillo_300m_mxn_2026",
    "infrastructure", "port_cranes", "other",
    "Hutchison Ports TIMSA — two MHC ESP.10 electric mobile harbor cranes (Manzanillo)",
    "Mexico",
    "28 Apr 2026 Cluster Industrial: Hutchison Ports TIMSA incorporates two electric MHC ESP.10 cranes; investment exceeding MXN 300 million. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~16.96m for stored MXN 300m floor face. Distinct from timsa_ertg_manzanillo_70m_mxn_2026.",
    "300000000", MXN_FX_DATE, "2026", "19.06", "-104.32",
    "Hutchison Ports TIMSA, Manzanillo, Colima (press geography).",
    "cluster_timsa_mhc_esp10_20260428",
    "Hutchison Ports TIMSA fortaleció su infraestructura operativa con la incorporación de dos grúas eléctricas tipo MHC ESP.10 … La llegada de estas unidades representó una inversión superior a 300 millones de pesos",
    "https://clusterindustrial.com.mx/hutchison-ports-timsa-invierte-300-mdp-en-gruas-electricas-para-elevar-capacidad-en-manzanillo/",
    "Actor: Hutchison Ports TIMSA (HK) — other. CapEx-fill: retain >MXN 300m floor; add Fed H.10 Sep 25 2026 FX to USD ~16.96m. Shuffle port_cranes.",
    "hunt_cycle227", investment_type="equipment", evidence="documented", currency="MXN",
    value_usd=str(round(300000000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='Cluster Industrial. “Hutchison Ports TIMSA invierte 300 MDP en grúas eléctricas para elevar capacidad en Manzanillo.” April 28, 2026. https://clusterindustrial.com.mx/hutchison-ports-timsa-invierte-300-mdp-en-gruas-electricas-para-elevar-capacidad-en-manzanillo/.',
    annotation="TIMSA MHC CapEx-fill ~USD 16.96m via Fed H.10. Supports timsa_mhc_esp10_manzanillo_300m_mxn_2026.",
    evid_note="Opened Cluster Industrial Spanish; >MXN 300m / two MHC ESP.10 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
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
    print(f"cycle227 added {len(added)}: {added}")
    print(f"cycle227 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
