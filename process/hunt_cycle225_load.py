#!/usr/bin/env python3
"""Cycle 225 hunt: shuffle_seed=20261225; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261225).shuffle):
balsa, niobium, nickel, lithium, bridges_roads, port_ownership, wind, solar,
engineering_epc, port_cranes, graphite, fission_smr, building_materials,
power_plants_grid, other_renewables, copper, rail, water.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    fission CapEx-fill (Brazil CNEN microreactor company dual US$9.1m);
    balsa/nickel dry.
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty sweeps (US blank-USD residual exhausted;
0 US CapEx-fills — honest residual).
PRC equal-budget: Goldwind Camaçari + PowerChina Intrepid Mauriti CapEx-fills;
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


# 1. fission_smr / other — CapEx-fill Brazil microreactor company dual US$9.1m (thin)
row_doc(
    "brazil_microreactor_cnen_2025",
    "energy", "fission_smr", "other",
    "CNEN / Brazil microreactor concept program (5 MWt)",
    "Brazil",
    "World Nuclear News: three-year BRL50 million (USD9.1 million) project brings together private and public sector bodies to develop a concept for a 5 MWt microreactor; CNEN project. CapEx-fill: enter company/press dual-quoted US$9.1 million as value_usd (retain R$50m face).",
    "50000000", "2025-11-13", "2025", "-15.78", "-47.93",
    "Brazil CNEN microreactor program (national concept; Brasília pin for agency HQ).",
    "wnn_brazil_microreactor_20251113",
    "A three-year BRL50 million (USD9.1 million) project brings together private and public sector bodies to develop a concept for a 5 MWt microreactor … The National Nuclear Energy Commission (CNEN) project.",
    "https://www.world-nuclear-news.org/articles/brazils-microreactor-project-under-way",
    "Actor: CNEN / Brazilian public–private microreactor consortium — other. CapEx-fill: company dual US$9.1m alongside R$50m. Thin fission_smr top-up.",
    "hunt_cycle225", investment_type="rd_program", evidence="documented", currency="BRL",
    value_usd="9100000", fx_usd=str(round(50000000 / 9100000, 4)), bib_type="press",
    chicago='World Nuclear News. “Brazil’s microreactor project under way.” November 13, 2025. https://www.world-nuclear-news.org/articles/brazils-microreactor-project-under-way.',
    annotation="Brazil microreactor CapEx-fill company dual US$9.1m. Supports brazil_microreactor_cnen_2025.",
    evid_note="Opened WNN English; BRL50m / USD9.1m dual / 5 MWt concept confirmed. CapEx-fill uses press USD.",
)

# 2. niobium / allied — CapEx-fill CBMM CapEx plan R$11bn to 2030
row_doc(
    "cbmm_capex_plan_11bn_2030",
    "resources", "niobium", "allied",
    "CBMM — CapEx and growth plan to 2030 (R$11bn)",
    "Brazil",
    "CBMM Sustainability Report: plans investment of R$ 11 billion in Capex and growth plan through 2030 (expansion of new lines and plants). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~2118.60m for stored R$11bn face. Distinct from annual spend CapEx-fills.",
    "11000000000", BRL_FX_DATE, "2025", "-19.59", "-46.94",
    "CBMM Araxá / growth plan footprint, Minas Gerais (company geography).",
    "cbmm_rs_2025",
    "Para os próximos anos, a empresa tem planos de investimento de R$ 11 bilhões em Capex e no plano de crescimento da CBMM até 2030. Serão direcionados investimentos na expansão de novas linhas e plantas.",
    "https://cbmm.com/relatorio-sustentabilidade/pdf/CBMM_RS25_D16_02.pdf",
    "Actor: CBMM (Brazilian Moreira Salles–controlled) — allied. CapEx-fill: retain R$11bn plan; add Fed H.10 Sep 25 2026 FX to USD ~2118.60m. Shuffle niobium.",
    "hunt_cycle225", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(11000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CBMM. Relatório de Sustentabilidade 2025. https://cbmm.com/relatorio-sustentabilidade/pdf/CBMM_RS25_D16_02.pdf.',
    annotation="CBMM to-2030 CapEx-fill ~USD 2118.60m via Fed H.10. Supports cbmm_capex_plan_11bn_2030.",
    evid_note="Opened CBMM RS2025 PDF; R$11bn Capex/growth to 2030 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. bridges_roads / allied — CapEx-fill Mota-Engil Santos–Guarujá R$6.8bn
row_doc(
    "mota_engil_santos_guaruja_6p8bn_2026",
    "infrastructure", "bridges_roads", "allied",
    "Mota-Engil / SP government — Santos–Guarujá immersed tunnel",
    "Brazil",
    "28 Jan 2026 G1: SP government signs contract for Santos–Guarujá tunnel; total estimated investment R$ 6.8 billion; 870 m immersed tunnel under port channel. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1309.68m for stored R$6.8bn face.",
    "6800000000", BRL_FX_DATE, "2026", "-23.98", "-46.3",
    "Santos–Guarujá channel, São Paulo (press geography).",
    "g1_santos_guaruja_20260128",
    "Com investimento total estimado em R$ 6,8 bilhões, o projeto prevê a construção de um túnel de 870 metros sob o canal portuário, com três faixas por sentido, passagem para pedestres e ciclistas.",
    "https://g1.globo.com/sp/sao-paulo/noticia/2026/01/28/governo-de-sp-assina-contrato-para-construir-o-tunel-santos-guaruja.ghtml",
    "Actor: Mota-Engil (Portugal) consortium / SP government — allied. CapEx-fill: retain R$6.8bn; add Fed H.10 Sep 25 2026 FX to USD ~1309.68m. Shuffle bridges_roads.",
    "hunt_cycle225", investment_type="epc", evidence="documented", currency="BRL",
    value_usd=str(round(6800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='G1. “Governo de SP assina contrato para construir o túnel Santos-Guarujá.” January 28, 2026. https://g1.globo.com/sp/sao-paulo/noticia/2026/01/28/governo-de-sp-assina-contrato-para-construir-o-tunel-santos-guaruja.ghtml.',
    annotation="Santos–Guarujá CapEx-fill ~USD 1309.68m via Fed H.10. Supports mota_engil_santos_guaruja_6p8bn_2026.",
    evid_note="Opened G1 Portuguese; R$6.8bn / 870 m tunnel confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. wind / prc — CapEx-fill Goldwind Camaçari ~R$100m
row_doc(
    "goldwind_camacari_turbine_factory_2024",
    "energy", "wind", "prc",
    "Goldwind — Camaçari wind-turbine manufacturing plant",
    "Brazil",
    "27–28 Aug 2024: Goldwind inaugurates first overseas wind-turbine factory at former GE complex in Camaçari (Bahia); planned CapEx ~R$ 100 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~19.26m for stored R$100m face.",
    "100000000", BRL_FX_DATE, "2024", "-12.70", "-38.32",
    "Camaçari, Bahia (press geography).",
    "movimento_goldwind_camacari_20240828",
    "A empresa chinesa Goldwind inaugurou uma fábrica de turbinas eólicas em Camaçari, na Região Metropolitana de Salvador, na Bahia. O grupo prevê um investimento de R$ 100 milhões no empreendimento que se instalou no antigo complexo da General Eletric (GE).",
    "https://movimentoeconomico.com.br/estados/bahia/2024/08/28/goldwind-inaugura-fabrica-de-turbinas-na-ba-com-investimento-de-r-100-mi/",
    "Actor: Goldwind (PRC) — prc. CapEx-fill: retain ~R$100m; add Fed H.10 Sep 25 2026 FX to USD ~19.26m. Shuffle wind / PRC equal-budget.",
    "hunt_cycle225", investment_type="greenfield_plant", evidence="documented", currency="BRL",
    value_usd=str(round(100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Movimento Econômico. “Goldwind inaugura fábrica de turbinas na BA com investimento de R$ 100 mi.” August 28, 2024. https://movimentoeconomico.com.br/estados/bahia/2024/08/28/goldwind-inaugura-fabrica-de-turbinas-na-ba-com-investimento-de-r-100-mi/.',
    annotation="Goldwind Camaçari CapEx-fill ~USD 19.26m via Fed H.10. Supports goldwind_camacari_turbine_factory_2024.",
    evid_note="Opened Movimento Econômico; ~R$100m / Camaçari factory confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. solar / prc — CapEx-fill PowerChina Intrepid Mauriti R$1.8bn
row_doc(
    "powerchina_intrepid_mauriti_1p8bn_2023",
    "energy", "solar", "prc",
    "PowerChina / Pontoon — Intrepid solar complex (Mauriti, Ceará)",
    "Brazil",
    "26 May 2023 Época Negócios: PowerChina–Pontoon partnership starts with Intrepid solar complex in Ceará — 425 MWp; investments of R$ 1.8 billion in engineering phase. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~346.68m for stored R$1.8bn face.",
    "1800000000", BRL_FX_DATE, "2023", "-7.39", "-38.77",
    "Mauriti / Intrepid solar, Ceará (press geography).",
    "epoca_powerchina_intrepid_20230526",
    "A parceria estratégia se inicia com o complexo solar Intrepid, localizado no Ceará, com capacidade instalada de 425 megawatts-pico (MWp) e investimentos de 1,8 bilhão de reais na fase de engenharia, aquisições e construção (EPC, na sigla em inglês).",
    "https://epocanegocios.globo.com/futuro-da-industria/noticia/2023/05/pontoon-e-powerchina-fecham-acordo-em-energia-solar-no-brasil.ghtml",
    "Actor: PowerChina (PRC) — prc. CapEx-fill: retain R$1.8bn; add Fed H.10 Sep 25 2026 FX to USD ~346.68m. Shuffle solar / PRC equal-budget.",
    "hunt_cycle225", investment_type="epc", evidence="documented", currency="BRL",
    value_usd=str(round(1800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Época Negócios. “Pontoon e PowerChina fecham acordo em energia solar no Brasil.” May 26, 2023. https://epocanegocios.globo.com/futuro-da-industria/noticia/2023/05/pontoon-e-powerchina-fecham-acordo-em-energia-solar-no-brasil.ghtml.',
    annotation="PowerChina Intrepid CapEx-fill ~USD 346.68m via Fed H.10. Supports powerchina_intrepid_mauriti_1p8bn_2023.",
    evid_note="Opened Época Negócios; R$1.8bn / 425 MWp Intrepid confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. port_cranes / allied — CapEx-fill Portonave electric fleet ~R$61m
row_doc(
    "portonave_electric_fleet_61m_2026",
    "infrastructure", "port_cranes", "allied",
    "Portonave (TIL) — electric terminal tractors + reach stackers fleet",
    "Brazil",
    "3 Aug 2026 Portonave: acquired 30 electric terminal tractors (Terberg) and five electric reach stackers (Kalmar); investment totals approximately R$ 61 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~11.75m for stored R$61m face. Distinct from portonave_ertg_210m_brl_2026.",
    "61000000", BRL_FX_DATE, "2026", "-26.9", "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina (company geography).",
    "portonave_electric_fleet_20260803",
    "Portonave … has acquired 30 electric terminal tractors (e-TTs) manufactured by Terberg in Malaysia and five electric reach stackers (e-RSs) manufactured by Kalmar in China. The investment totals approximately R$ 61 million.",
    "https://www.portonave.com.br/en/todas-as-noticias/portonave-invests-rusd61-million-in-new-electrical",
    "Actor: Portonave under TIL (MSC/Swiss) — allied. CapEx-fill: retain ~R$61m; add Fed H.10 Sep 25 2026 FX to USD ~11.75m. Shuffle port_cranes.",
    "hunt_cycle225", investment_type="equipment", evidence="documented", currency="BRL",
    value_usd=str(round(61000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Portonave. “Portonave invests R$61 million in new electrical equipment.” August 3, 2026. https://www.portonave.com.br/en/todas-as-noticias/portonave-invests-rusd61-million-in-new-electrical.',
    annotation="Portonave electric fleet CapEx-fill ~USD 11.75m via Fed H.10. Supports portonave_electric_fleet_61m_2026.",
    evid_note="Opened Portonave English; ~R$61m / 30 e-TT + 5 e-RS confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. building_materials / allied — CapEx-fill Holcim Zapopan electric ~MXN 51m
row_doc(
    "holcim_zapopan_electric_51m_mxn_2025",
    "infrastructure", "building_materials", "allied",
    "Holcim México — first 100% electric concrete plant (Zapopan, Jalisco)",
    "Mexico",
    "26 Nov 2025 Holcim México: inaugurates first 100% electric concrete plant in Mexico at Zapopan, Jalisco; investment of almost MXN 51 million. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~2.88m for stored MXN 51m face.",
    "51000000", MXN_FX_DATE, "2025", "20.72", "-103.39",
    "Zapopan, Jalisco (company geography).",
    "holcim_mx_zapopan_electric_20251126",
    "Con una inversión de casi 51 millones de pesos, esta planta ubicada en Jalisco representa el inicio de la electrificación de las operaciones de Holcim México. … inaugurar en Zapopan, Jalisco la primera planta de concreto 100% eléctrica en México.",
    "https://www.holcim.com.mx/holcim-inaugura-la-primera-planta-de-concreto-100-electrica-en-mexico",
    "Actor: Holcim México (Switzerland Holcim) — allied. CapEx-fill: retain ~MXN 51m; add Fed H.10 Sep 25 2026 FX to USD ~2.88m. Shuffle building_materials.",
    "hunt_cycle225", investment_type="plant_capex", evidence="documented", currency="MXN",
    value_usd=str(round(51000000 / float(MXN_USD), 2)), fx_usd=MXN_USD,
    chicago='Holcim México. “Holcim inaugura la primera planta de concreto 100% eléctrica en México.” November 26, 2025. https://www.holcim.com.mx/holcim-inaugura-la-primera-planta-de-concreto-100-electrica-en-mexico.',
    annotation="Holcim Zapopan CapEx-fill ~USD 2.88m via Fed H.10. Supports holcim_zapopan_electric_51m_mxn_2025.",
    evid_note="Opened Holcim México Spanish; ~MXN 51m / Zapopan electric plant confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
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
    print(f"cycle225 added {len(added)}: {added}")
    print(f"cycle225 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
