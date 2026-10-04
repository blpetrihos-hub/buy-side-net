#!/usr/bin/env python3
"""Cycle 186 hunt: shuffle_seed=20261186; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261186)):
other_renewables, power_plants_grid, graphite, water, solar, wind, port_cranes,
bridges_roads, building_materials, engineering_epc, lithium, copper, niobium,
fission_smr, rail, balsa, port_ownership, nickel.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (Plantabal/AIMA dense; Centaurus/Atlantic Nickel dense;
Meitner Atucha / FIRST MoUs already logged).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
≥1/3 U.S. hunt budget spent on DFC/EXIM/USTDA/AES/Atlas/Fluor/Caterpillar/Progress
Rail/Wabtec — catalog dense; no net-new U.S. CapEx row this cycle.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. other_renewables / prc — Edelmag Guerrico minihydro (State Grid via CGE)
row_doc(
    "edelmag_guerrico_8m_2026",
    "energy",
    "other_renewables",
    "prc",
    "Edelmag (CGE / State Grid) — Minicentral Guerrico run-of-river (Puerto Williams)",
    "Chile",
    "16 Feb 2026 Edelmag: Magallanes COEVA grants RCA for Minicentral Hidroeléctrica de pasada río Guerrico — 1 MW run-of-river ~18 km west of Puerto Williams (Cabo de Hornos); 13.2 kV interconnection; investment ~USD 8 million with expected GORE Magallanes PEDZE co-financing; next step CNE approval before construction. CapEx = USD 8m company face. Edelmag controlled via CGE Magallanes / CGE; CGE ~97% owned by State Grid Chile Electricity SpA (PRC).",
    "8000000",
    "2026-02-16",
    "2026",
    "-54.93",
    "-67.61",
    "Río Guerrico / ~18 km west of Puerto Williams, Cabo de Hornos, Magallanes, Chile (company geography; approximate).",
    "edelmag_guerrico_rca_20260216",
    "La inversión de esta iniciativa bordea los ocho millones de dólares y se espera un financiamiento público privado de parte del Gobierno Regional de Magallanes mediante el Plan Especial de Zonas Extremas (PEDZE).",
    "https://www.edelmag.cl/puerto-williams-avanza-en-autonomia-energetica-tras-aprobacion-de-central-generadora-de-edelmag/",
    "Actor: Edelmag (Empresa Eléctrica de Magallanes) under CGE / State Grid Chile — prc. Company Spanish primary; ownership via FNE F255-2020 / CGE accionistas (State Grid Chile Electricity SpA 97.145%). Shuffle other_renewables.",
    "hunt_cycle186",
    investment_type="greenfield",
    evidence="documented",
    bib_type="company",
    chicago='Edelmag. “Puerto Williams avanza en autonomía energética tras aprobación de central generadora de EDELMAG.” February 16, 2026. https://www.edelmag.cl/puerto-williams-avanza-en-autonomia-energetica-tras-aprobacion-de-central-generadora-de-edelmag/.',
    annotation="Edelmag: Guerrico 1 MW CapEx ~USD 8m after RCA. Supports edelmag_guerrico_8m_2026.",
    evid_note="Opened Edelmag Spanish company page 2026-10-04; cross-checked State Grid/CGE control via CGE accionistas and FNE F255-2020.",
)

# 2. other_renewables / allied — Sonnedix Chile USD 1.3bn refinancing
row_doc(
    "sonnedix_chile_refi_1p3bn_2026",
    "energy",
    "other_renewables",
    "allied",
    "Sonnedix Chile — USD 1.3bn refinancing (1 GW operating + 117 MW BESS)",
    "Chile",
    "10 Sep 2026 Sonnedix: secures USD 1.3 billion landmark refinancing in Chile — refinances ~1 GW operational solar and wind capacity and finances 117 MW BESS under construction (Librillo standalone BESS in Taltal already tracked as Sungrow supply row). Seven commercial banks (BNP Paribas, BofA, CACIB, Santander JLAs; BBVA, Goldman Sachs, MUFG MLAs). CapEx/financing face = USD 1.3bn. Coded other_renewables for hybrid solar/wind/storage portfolio refinance.",
    "1300000000",
    "2026-09-10",
    "2026",
    "",
    "",
    "Chile multi-asset solar/wind + Librillo BESS portfolio — lat/lon blank (portfolio refinance).",
    "sonnedix_chile_refi_20260910",
    "Sonnedix, a global renewable energy company with 12GW of total capacity, has secured USD1.3 billion through a landmark refinancing transaction in Chile. The agreement refinances 1GW of operational solar and wind capacity across Chile, while also financing 117MW of battery energy storage systems (BESS) currently under construction",
    "https://www.sonnedix.com/news/sonnedix-secures-usd1-3-billion-landmark-refinancing-to-accelerate-chiles-renewable-energy-and-storage-pipeline",
    "Actor: Sonnedix (Spain/Europe renewables platform) — allied. Company English primary. Distinct from sungrow_sonnedix_librillo_bess_2026 OEM supply row. Shuffle other_renewables overflow.",
    "hunt_cycle186",
    investment_type="refinancing",
    evidence="documented",
    bib_type="company",
    chicago='Sonnedix. “Sonnedix secures USD1.3 billion landmark refinancing to accelerate Chile’s renewable energy and storage pipeline.” September 10, 2026. https://www.sonnedix.com/news/sonnedix-secures-usd1-3-billion-landmark-refinancing-to-accelerate-chiles-renewable-energy-and-storage-pipeline.',
    annotation="Sonnedix: Chile portfolio refinance USD 1.3bn. Supports sonnedix_chile_refi_1p3bn_2026.",
    evid_note="Opened Sonnedix English company press 2026-10-04.",
)

# 3. water / allied — Aguas Andinas 2025 CapEx (Veolia-controlled)
row_doc(
    "aguas_andinas_capex_189905m_clp_2025",
    "resources",
    "water",
    "allied",
    "Aguas Andinas (Veolia) — FY2025 Santiago sanitation CapEx executed",
    "Chile",
    "FY2025 Aguas Andinas earnings release: executed investments totaling CLP 189,905 million to strengthen Santiago sanitation infrastructure under Biociudad / tariff agreement — network renewal, treatment-plant upgrades, hydraulic efficiency, sondajes. Veolia Environnement is ultimate controller via IAM (50.1%). CapEx = CLP 189,905m executed face (CLP stored without FX). Distinct from Veolia Aguas Pacífico O&M / desal rows.",
    "189905000000",
    "2025-12-31",
    "2025",
    "-33.45",
    "-70.67",
    "Greater Santiago sanitation system, Región Metropolitana, Chile (company geography; approximate Santiago pin).",
    "aguas_andinas_earnings_4t25",
    "As of December 31, 2025, the Company executed investments totaling CLP 189,905 million, aimed at strengthening Santiago’s sanitation infrastructure.",
    "https://www.aguasandinasinversionistas.cl/documents/208629/456213/AA+and+Subsidiaries+Earnings+Release+4T25.pdf",
    "Actor: Aguas Andinas controlled by Veolia (France) via IAM — allied. Company English 4T25 earnings PDF. Shuffle water.",
    "hunt_cycle186",
    investment_type="capex",
    evidence="documented",
    currency="CLP",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Aguas Andinas S.A. “Aguas Andinas and Subsidiaries Earnings Release 4T25.” PDF. https://www.aguasandinasinversionistas.cl/documents/208629/456213/AA+and+Subsidiaries+Earnings+Release+4T25.pdf.',
    annotation="Aguas Andinas: FY2025 CapEx CLP 189,905m. Supports aguas_andinas_capex_189905m_clp_2025.",
    evid_note="Opened Aguas Andinas 4T25 earnings PDF 2026-10-04; controller path via company Grupo controlador / CMF.",
)

# 4. bridges_roads / other — Ecorodovias Rota das Gerais concession
row_doc(
    "ecorodovias_rota_gerais_13bn_2026",
    "infrastructure",
    "bridges_roads",
    "other",
    "Ecorodovias — Rota das Gerais BR-116/251/MG federal highway concession",
    "Brazil",
    "31 Mar 2026 ANTT: Ecorodovias wins first 2026 federal highway auction for Rota das Gerais (BR-116/251/MG) — ~735 km northern/northeastern Minas Gerais; 30-year concession; 19% toll discount; ANTT states more than R$13 billion in investments concentrated in early years; works include ~186.6 km duplications, ~160 km additional lanes, 16.9 km urban bypasses. CapEx/investment face = R$13bn ANTT package floor (company/press also cite R$7.3bn works + R$5.8bn opex — use ANTT >R$13bn). Brazilian operator — other.",
    "13000000000",
    "2026-03-31",
    "2026",
    "-16.72",
    "-43.86",
    "BR-116/251 Rota das Gerais corridor, northern Minas Gerais, Brazil (ANTT geography; approximate Montes Claros corridor pin).",
    "antt_rota_gerais_20260331",
    "Com prazo de 30 anos, o contrato prevê mais de R$ 13 bilhões em investimentos, concentrados nos primeiros anos, antecipando benefícios à população.",
    "https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/ecorodovias-vence-primeiro-leilao-rodoviario-federal-de-2026-com-19-de-desconto-e-assume-735-km-em-minas-gerais",
    "Actor: Ecorodovias Concessões e Serviços S.A. (Brazil) — other. Official ANTT Portuguese primary. Shuffle bridges_roads.",
    "hunt_cycle186",
    investment_type="concession",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Agência Nacional de Transportes Terrestres (ANTT). “Ecorodovias vence primeiro leilão rodoviário federal de 2026 com 19% de desconto e assume 735 km em Minas Gerais.” March 31, 2026. https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/ecorodovias-vence-primeiro-leilao-rodoviario-federal-de-2026-com-19-de-desconto-e-assume-735-km-em-minas-gerais.',
    annotation="ANTT: Rota das Gerais >R$13bn investments. Supports ecorodovias_rota_gerais_13bn_2026.",
    evid_note="Opened ANTT Portuguese auction result page 2026-10-04.",
)

# 5. rail / allied — EFE CAF+ICO USD 700m financing
row_doc(
    "efe_caf_ico_700m_2026",
    "infrastructure",
    "rail",
    "allied",
    "EFE Trenes de Chile — CAF + ICO Spain financing package (USD 700m)",
    "Chile",
    "23 Jan 2026 EFE: signs financing contract for USD 700 million with CAF (up to USD 500m) and Spain’s ICO (USD 200m cofinancing) — up to 20-year tenor, no state guarantee; complementary to prior CAF USD 500m (2025); part earmarked for Santiago–Melipilla Tramos 1–2 payments to international suppliers. CapEx/financing face = USD 700m. Distinct from CRCC Batuco civil / CRI electrification / CRRC EMU rows.",
    "700000000",
    "2026-01-23",
    "2026",
    "-33.45",
    "-70.75",
    "EFE network / Santiago–Melipilla corridor, Región Metropolitana, Chile (financing supports multi-project portfolio; approximate Santiago west pin).",
    "efe_caf_ico_20260123",
    "La Empresa de los Ferrocarriles del Estado y el Banco de Desarrollo de América Latina y el Caribe (CAF) firmaron un contrato de financiamiento por US$700 millones… El acuerdo considera un crédito de hasta US$500 millones comprometidos directamente por CAF, junto con un cofinanciamiento adicional de US$200 millones a través del Instituto de Crédito Oficial (ICO) de España",
    "https://www.efe.cl/efe-suscribe-financiamiento-por-us700-millones-con-caf-e-ico/",
    "Actor: CAF (LatAm development bank) + ICO Spain financing EFE — allied. Company Spanish primary. Shuffle rail.",
    "hunt_cycle186",
    investment_type="financing",
    evidence="documented",
    bib_type="company",
    chicago='EFE Trenes de Chile. “EFE suscribe financiamiento por US$700 millones con CAF e ICO.” January 23, 2026. https://www.efe.cl/efe-suscribe-financiamiento-por-us700-millones-con-caf-e-ico/.',
    annotation="EFE: CAF+ICO financing USD 700m. Supports efe_caf_ico_700m_2026.",
    evid_note="Opened EFE Spanish company press 2026-10-04.",
)

# 6. solar / allied — World Bank Haiti Renewable Energy for All AF USD 20m
row_doc(
    "wb_haiti_renewable_af_20m_2024",
    "energy",
    "solar",
    "allied",
    "World Bank IDA — Haiti Renewable Energy for All Additional Financing (USD 20m)",
    "Haiti",
    "18 Oct 2024 World Bank: Board approves USD 20 million IDA additional financing for Haiti Renewable Energy for All Project — scale-up solar PV mini-grids with storage, micro-grids, and stand-alone solar; hybridize ≥2 diesel isolated grids; PV+storage for priority hospitals; original project + AF support 5–12 MW renewable capacity. CapEx/financing face = USD 20m AF grant. Distinct from wb_haiti_jacmel_renewable_af_7p1m_2025 and ifc_idb_solengy_haiti_13p5m_2025.",
    "20000000",
    "2024-10-18",
    "2024",
    "",
    "",
    "Haiti national renewable mini-grid / hospital PV program — lat/lon blank (multi-site AF).",
    "wb_haiti_renewable_af_20241018",
    "The World Bank's Board of Executive Directors today approved US$20 million in International Development Association additional financing for the Haiti: Renewable Energy for All Project.",
    "https://www.worldbank.org/en/news/press-release/2024/10/18/world-bank-to-support-sustainable-energy-access-in-haiti",
    "Actor: World Bank IDA — allied multilateral. Official English press. Haiti under-covered weight. Shuffle solar.",
    "hunt_cycle186",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='World Bank. “World Bank to Support Sustainable Energy Access in Haiti.” October 18, 2024. https://www.worldbank.org/en/news/press-release/2024/10/18/world-bank-to-support-sustainable-energy-access-in-haiti.',
    annotation="World Bank: Haiti RE for All AF USD 20m. Supports wb_haiti_renewable_af_20m_2024.",
    evid_note="Opened World Bank English press release 2026-10-04.",
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
    added = []

    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle186 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
