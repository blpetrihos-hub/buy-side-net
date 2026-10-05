#!/usr/bin/env python3
"""Cycle 231 hunt: shuffle_seed=20261231; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261231).shuffle):
port_cranes, engineering_epc, power_plants_grid, graphite, solar, niobium, water, rail,
bridges_roads, fission_smr, nickel, wind, balsa, building_materials, lithium,
port_ownership, other_renewables, copper.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted; 0 new US CapEx — honest residual).
PRC equal-budget: CCECC/Aldesa Querétaro–Irapuato CapEx-fill; holdovers unsigned.
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
EUR_FX_DATE = "2026-09-25"


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


# 1. engineering_epc / allied — CapEx-fill ACCIONA SP Line 6 >BRL 19bn
row_doc(
    "acciona_sp_line6_epc_2025",
    "infrastructure", "engineering_epc", "allied",
    "ACCIONA — São Paulo Metro Line 6 Orange PPP construction",
    "Brazil",
    "12 Jan 2026 ACCIONA: São Paulo Metro Line 6 Orange PPP with Linha Uni; committed investment of more than BRL 19 billion; 15.3 km tunnel excavation completed; >77% completion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~3659.41m for stored R$19bn floor face.",
    "19000000000", BRL_FX_DATE, "2025", "-23.5", "-46.65",
    "São Paulo Metro Line 6 Orange (company geography).",
    "acciona_line6_milestones_20260112",
    "With a committed investment of more than BRL 19 billion, the Line 6 Orange project is a public private partnership (PPP) between the Government of the State of São Paulo and the Linha Universidade Concessionaire (Linha Uni).",
    "https://www.acciona.com/updates/articles/sao-paulo-metro-line-6-project-reaches-key-milestones",
    "Actor: ACCIONA (Spain) — allied. CapEx-fill: retain >BRL 19bn floor; add Fed H.10 Sep 25 2026 FX to USD ~3659.41m. Shuffle engineering_epc.",
    "hunt_cycle231", investment_type="epc_ppp", evidence="documented", currency="BRL",
    value_usd=str(round(19000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ACCIONA. “São Paulo Metro Line 6 project reaches key milestones.” January 12, 2026. https://www.acciona.com/updates/articles/sao-paulo-metro-line-6-project-reaches-key-milestones.',
    annotation="ACCIONA SP Line 6 CapEx-fill ~USD 3659.41m via Fed H.10. Supports acciona_sp_line6_epc_2025.",
    evid_note="Opened ACCIONA English; >BRL 19bn / Line 6 Orange PPP / >77% confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. power_plants_grid / other — CapEx-fill Copel 2026 CapEx ~R$3.021bn
row_doc(
    "copel_capex_2026_plan_3021m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — 2026 CapEx plan (~R$3.021bn)",
    "Brazil",
    "19 Nov 2025 Copel Material Fact / CapEx plan: Para 2026, o plano de investimento prevê um Capex de, aproximadamente, R$ 3,0 bilhões; Total Geral 3.021,3 (R$ million). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~581.90m for stored R$3,021.3m face.",
    "3021300000", BRL_FX_DATE, "2026", "-25.43", "-49.27",
    "Copel Paraná footprint (Curitiba HQ pin).",
    "copel_fr_15_25_capex_20251119",
    "Para 2026, o plano de investimento prevê um Capex de, aproximadamente, R$ 3,0 bilhões … Total Geral 3.021,3",
    "https://api.mziq.com/mzfilemanager/v2/d/16a31b1b-5ecd-4214-a2e0-308a2393e330/b4fe8c81-c5ea-c309-59d7-a14974bd3b3d",
    "Actor: Copel (Paraná utility) — other (host-country). CapEx-fill: retain R$3,021.3m 2026 plan; add Fed H.10 Sep 25 2026 FX to USD ~581.90m. Shuffle power_plants_grid.",
    "hunt_cycle231", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(3021300000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Copel. Material Fact / CapEx plan disclosure (FR 15/25). November 19, 2025. https://api.mziq.com/mzfilemanager/v2/d/16a31b1b-5ecd-4214-a2e0-308a2393e330/b4fe8c81-c5ea-c309-59d7-a14974bd3b3d.',
    annotation="Copel 2026 CapEx-fill ~USD 581.90m via Fed H.10. Supports copel_capex_2026_plan_3021m_brl.",
    evid_note="Opened Copel CapEx plan PDF excerpt; R$3,021.3m 2026 Total Geral confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. power_plants_grid / allied — CapEx-fill Neoenergia R$50bn 2026–2030 distribution
row_doc(
    "neoenergia_dist_50bn_brl_2026_2030",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — distribution CapEx cycle R$50bn (2026–2030)",
    "Brazil",
    "8 May 2026 Neoenergia: antecipação por mais 30 anos marks new investment cycle with aportes de R$ 50 bilhões entre 2026 e 2030 (+82% vs prior cycle). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~9629.92m. Distinct from neoenergia_fy2025_capex_10p1bn_brl and Coelba litoral package rows.",
    "50000000000", BRL_FX_DATE, "2026", "", "",
    "Neoenergia distribution concessions BA/PE/RN/SP-MS (national; no single-site pin).",
    "neoenergia_50bn_dist_20260508",
    "A antecipação por mais 30 anos marca o início de um novo ciclo de investimentos da companhia, com aportes de R$ 50 bilhões entre 2026 e 2030",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. CapEx-fill: retain R$50bn 2026–2030 distribution cycle; add Fed H.10 Sep 25 2026 FX to USD ~9629.92m. Shuffle power_plants_grid.",
    "hunt_cycle231", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(50000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia R$50bn CapEx-fill ~USD 9629.92m via Fed H.10. Supports neoenergia_dist_50bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Portuguese; R$50bn 2026–2030 distribution cycle confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. power_plants_grid / allied — CapEx-fill Redeia Redinter LatAm EUR 150m
row_doc(
    "redeia_redinter_latam_150m_eur_2026",
    "energy", "power_plants_grid", "allied",
    "Redeia / Redinter — LatAm transmission investment plan (~€150m to 2029)",
    "Brazil",
    "26 Feb 2026 Redeia: as part of Strategic Plan to 2029, group will roll out an investment plan worth around €150 million for electricity transmission in Latin America. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD ~171.00m. Pin Brazil as primary LatAm transmission footprint (no single-site).",
    "150000000", EUR_FX_DATE, "2026", "", "",
    "Redeia Redinter LatAm transmission plan (no single-site pin).",
    "redeia_strategic_plan_latam_20260226",
    "As part of its strategic path until 2029, the group will consolidate its activity in electricity transmission in Latin America and in the field of telecommunications. In the first case, it will roll out an investment plan worth around €150 million",
    "https://www.redeia.com/en/press-office/news/press-release/2026/02/redeia-increases-its-average-annual-investment-red-electrica-70-implement-next-plan",
    "Actor: Redeia (Spain) — allied. CapEx-fill: retain EUR 150m LatAm plan; add Fed H.10 Sep 25 2026 FX to USD ~171.00m. Shuffle power_plants_grid.",
    "hunt_cycle231", investment_type="greenfield", evidence="documented", currency="EUR",
    value_usd=str(round(150000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='Redeia. “Redeia increases its average annual investment in Red Eléctrica by 70% to implement the next plan.” February 26, 2026. https://www.redeia.com/en/press-office/news/press-release/2026/02/redeia-increases-its-average-annual-investment-red-electrica-70-implement-next-plan.',
    annotation="Redeia LatAm CapEx-fill ~USD 171.00m via Fed H.10. Supports redeia_redinter_latam_150m_eur_2026.",
    evid_note="Opened Redeia English; ~EUR 150m LatAm transmission plan confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 5. water / allied — CapEx-fill GS Inima Espírito Santo >EUR 150m
row_doc(
    "gs_inima_espirito_santo_lot_a_2025",
    "resources", "water", "allied",
    "GS Inima Brasil — Espírito Santo Sanitation Lot A concession",
    "Brazil",
    "9 Oct 2025 GS Inima: 24-year contract for wastewater collection/treatment in 35 municipalities (Lot A); investment exceeding EUR 150 million; 37 new WWTPs. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD ~171.00m for stored EUR 150m floor.",
    "150000000", EUR_FX_DATE, "2025", "-20.32", "-40.34",
    "Espírito Santo Lot A (Vitória pin).",
    "gs_inima_espirito_santo_20251009",
    "With an investment exceeding 150 million euros, the project includes the construction of 37 new Wastewater Treatment Plants (WWTPs)",
    "https://inima.com/en/gs-inima-signs-contract-the-integrated-sanitation-service-in-thestate-of-espirito-santo/",
    "Actor: GS Inima (Spain) — allied. CapEx-fill: retain >EUR 150m floor; add Fed H.10 Sep 25 2026 FX to USD ~171.00m. Shuffle water.",
    "hunt_cycle231", investment_type="concession", evidence="documented", currency="EUR",
    value_usd=str(round(150000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='GS Inima. “GS Inima has signed the contract for the Integrated Sanitation Service in the Brazilian State of Espírito Santo.” October 9, 2025. https://inima.com/en/gs-inima-signs-contract-the-integrated-sanitation-service-in-thestate-of-espirito-santo/.',
    annotation="GS Inima ES CapEx-fill ~USD 171.00m via Fed H.10. Supports gs_inima_espirito_santo_lot_a_2025.",
    evid_note="Opened GS Inima English; >EUR 150m / 24-year / 35 municipalities confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 6. rail / allied — CapEx-fill Siemens/Sonda ETCS (company dual ~US$192m)
row_doc(
    "siemens_sonda_mexico_etcs_2026",
    "infrastructure", "rail", "allied",
    "Siemens Mobility / Sonda — Mexico City–Querétaro–Irapuato ETCS Level 1",
    "Mexico",
    "26 Mar 2026 Sonda/Siemens: ATTPI award for ETCS Level 1 signaling/telecoms on México–Querétaro–Irapuato passenger corridor; contract valued at MXN 3,844 million (approximately US$192 million). CapEx-fill: enter company dual US$192 million as value_usd (retain MXN 3.844bn face).",
    "3844000000", "2026-03-26", "2026", "20.6", "-100.4",
    "México–Querétaro–Irapuato corridor (Querétaro pin).",
    "siemens_mexico_etcs_20260326",
    "El contrato, valorado en 3,844 millones de pesos (aproximadamente 192 millones de dólares) con un plazo de ejecución de casi cuatro años",
    "https://www.sonda.com/detalle-noticia/2026/03/26/sonda-impulsa-la-transformacion-ferroviaria-en-mexico-con-tecnologia-para-el-corredor-mexico-queretaro-irapuato",
    "Actor: Siemens Mobility (Germany) with Sonda — allied. CapEx-fill: company dual US$192m alongside MXN 3.844bn. Shuffle rail.",
    "hunt_cycle231", investment_type="equipment_supply", evidence="documented", currency="MXN",
    value_usd="192000000", fx_usd=str(round(3844000000 / 192000000, 4)),
    chicago='Sonda. “SONDA y Siemens Mobility ganan el proyecto de señalización ETCS en México.” March 26, 2026. https://www.sonda.com/detalle-noticia/2026/03/26/sonda-impulsa-la-transformacion-ferroviaria-en-mexico-con-tecnologia-para-el-corredor-mexico-queretaro-irapuato.',
    annotation="Siemens/Sonda ETCS CapEx-fill company dual US$192m. Supports siemens_sonda_mexico_etcs_2026.",
    evid_note="Opened Sonda Spanish; MXN 3,844m / ~US$192m dual / ETCS L1 confirmed. CapEx-fill uses company USD.",
)

# 7. rail / prc — CapEx-fill CCECC/Aldesa Querétaro–Irapuato MXN 3.279bn
row_doc(
    "ccecc_aldesa_queretaro_irapuato_2026",
    "infrastructure", "rail", "prc",
    "CCECC / Aldesa — Querétaro–Irapuato passenger rail auxiliary works",
    "Mexico",
    "5 Mar 2026 Aldesa: ATTRAPI awards international consortium including China Civil Engineering Construction Corporation (CCECC) and Aldesa MXN 3,279 million for key passenger-rail infrastructure on Querétaro–Irapuato. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~185.33m.",
    "3279000000", MXN_FX_DATE, "2026", "20.59", "-100.39",
    "Querétaro–Irapuato passenger rail corridor (company geography).",
    "aldesa_queretaro_irapuato_20260305",
    "El contrato ha sido adjudicado por la Agencia de Trenes y Transporte Público Integrado (ATTRAPI) … a un consorcio internacional en el que participa Aldesa",
    "https://aldesa.com/aldesa-participara-en-el-desarrollo-de-infraestructuras-clave-del-tren-de-pasajeros-queretaro-irapuato-en-mexico/",
    "Actor: CCECC (PRC) lead consortium with Aldesa — prc (CCECC SOE). CapEx-fill: retain MXN 3.279bn; add Fed H.10 Sep 25 2026 FX to USD ~185.33m. Shuffle rail.",
    "hunt_cycle231", investment_type="epc_contract", evidence="documented", currency="MXN",
    value_usd=str(round(3279000000 / float(MXN_USD), 2)), fx_usd=MXN_USD,
    chicago='Aldesa. “Aldesa Participará en el Desarrollo de Infraestructuras Clave del Tren de Pasajeros Querétaro–Irapuato en México.” March 5, 2026. https://aldesa.com/aldesa-participara-en-el-desarrollo-de-infraestructuras-clave-del-tren-de-pasajeros-queretaro-irapuato-en-mexico/.',
    annotation="CCECC/Aldesa Querétaro CapEx-fill ~USD 185.33m via Fed H.10. Supports ccecc_aldesa_queretaro_irapuato_2026.",
    evid_note="Opened Aldesa Spanish; MXN 3,279m ATTRAPI award / CCECC consortium confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 8. bridges_roads / other — CapEx-fill Azevedo Rota Mogiana R$9.4bn
row_doc(
    "azevedo_rota_mogiana_9p4bn_brl_2026",
    "infrastructure", "bridges_roads", "other",
    "Azevedo Travassos — Rota Mogiana state highway concession (~R$9.4bn)",
    "Brazil",
    "27 Feb 2026 Azevedo Travassos: wins auction for 520 km state highways concession 30 years; estimated investment R$ 9.4 billion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1810.44m.",
    "9400000000", BRL_FX_DATE, "2026", "-22.12", "-47.00",
    "Rota Mogiana state highway package, São Paulo (company geography).",
    "azevedo_rota_mogiana_20260227",
    "O projeto prevê que 520 quilômetros de rodovias estaduais passem à iniciativa privada por 30 anos. A estimativa é de R$ 9,4 bilhões",
    "https://azevedotravassos.com.br/noticias/2026/02/27/azevedo-travassos-investimentos-vence-leilao-da-concessao-rota-mogiana-com-520-km-de-rodovias/",
    "Actor: Azevedo Travassos (Brazilian) — other. CapEx-fill: retain R$9.4bn; add Fed H.10 Sep 25 2026 FX to USD ~1810.44m. Shuffle bridges_roads.",
    "hunt_cycle231", investment_type="concession_capex", evidence="documented", currency="BRL",
    value_usd=str(round(9400000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Azevedo Travassos. “Azevedo Travassos Investimentos vence leilão da Rota Mogiana.” February 27, 2026. https://azevedotravassos.com.br/noticias/2026/02/27/azevedo-travassos-investimentos-vence-leilao-da-concessao-rota-mogiana-com-520-km-de-rodovias/.',
    annotation="Azevedo Rota Mogiana CapEx-fill ~USD 1810.44m via Fed H.10. Supports azevedo_rota_mogiana_9p4bn_brl_2026.",
    evid_note="Opened Azevedo Travassos Portuguese; R$9.4bn / 520 km / 30-year confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 9. building_materials / other — CapEx-fill Votorantim plan invested R$2.7bn (FY2025)
row_doc(
    "votorantim_brazil_plan_2p7bn_invested_2025",
    "infrastructure", "building_materials", "other",
    "Votorantim Cimentos — Brazil 2024–2028 plan cumulative invested (R$2.7bn as of FY2025)",
    "Brazil",
    "18 Mar 2026 Votorantim FY2025: of the R$5 billion Brazil investment plan for 2024–2028, R$2.7 billion is already being invested. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~520.02m. Distinct from votorantim_brazil_plan_3p1bn_invested_2026 (2Q26 cumulative).",
    "2700000000", BRL_FX_DATE, "2025", "", "",
    "Votorantim Brazil investment plan (national footprint; no single-site pin).",
    "votorantim_fy2025_results_20260318",
    "Regarding the R$5 billion investment plan for the period 2024-2028 in Brazil, R$2.7 billion is already being invested in a comprehensive program for growth, decarbonization and structural competitiveness.",
    "https://www.votorantimcimentos.com/news/our-2025-financial-results/",
    "Actor: Votorantim Cimentos (Brazilian) — other. CapEx-fill: retain R$2.7bn cumulative; add Fed H.10 Sep 25 2026 FX to USD ~520.02m. Shuffle building_materials.",
    "hunt_cycle231", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(2700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Votorantim Cimentos. “Our 2025 financial results.” March 18, 2026. https://www.votorantimcimentos.com/news/our-2025-financial-results/.',
    annotation="Votorantim Brazil plan R$2.7bn CapEx-fill ~USD 520.02m via Fed H.10. Supports votorantim_brazil_plan_2p7bn_invested_2025.",
    evid_note="Opened Votorantim English FY2025; R$2.7bn cumulative of R$5bn Brazil plan confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle231 added {len(added)}: {added}")
    print(f"cycle231 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
