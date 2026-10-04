#!/usr/bin/env python3
"""Cycle 190 hunt: shuffle_seed=20261190; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md codebook order + Random(20261190)):
niobium, copper, water, wind, solar, port_ownership, power_plants_grid, balsa,
fission_smr, bridges_roads, rail, graphite, lithium, engineering_epc, port_cranes,
building_materials, nickel, other_renewables.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (catalog dense; holdovers unsigned).
≥1/3 U.S. hunt budget spent on EXIM/DFC/USTDA/NADBank/AES/Atlas/Fluor/Bechtel/
Wabtec/Progress/Freeport/MasTec — 0 net-new U.S. rows (AES JK1–JK2 49% already logged
as ecopetrol_jk1_jk2_49pct_25p5m_2026 / other in cycle 177; duplicate dropped).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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


# 1. water / allied — Aqualia PTAR Chincha ProInversión award USD 96.5m
row_doc(
    "aqualia_ptar_chincha_96p5m_2025",
    "resources",
    "water",
    "allied",
    "FCC Aqualia — PTAR Chincha APP concession (ProInversión)",
    "Peru",
    "7 Jan 2025 ProInversión: awards Spanish FCC Aqualia design/finance/build/O&M of PTAR Chincha wastewater treatment APP — 24-year concession; ~21 km collector networks + pumping + two plants totaling 0.6 m³/s + 7.7 km treated-water lines; benefits 345,000 people across seven Chincha districts (Ica). Adjudicated CapEx face = USD 96.5 million (ProInversión). Contract later signed Jul 2025 (MEF cites ~USD 250m design/construction/O&M package — not dual-entered). Distinct from mota_engil_ptar_puerto_maldonado_150m_2025.",
    "96500000",
    "2025-01-07",
    "2025",
    "-13.45",
    "-76.13",
    "Chincha Alta / Chincha province, Ica Region, Peru (ProInversión geography; approximate Chincha Alta pin).",
    "proinversion_ptar_chincha_20250107",
    "PROINVERSIÓN adjudicó a la empresa española FCC Aqualia el diseño, financiamiento, construcción, operación y mantenimiento del proyecto … PTAR Chincha … El adjudicatario invertirá US$ 96.5 millones",
    "https://www.gob.pe/institucion/proinversion/noticias/1087293-fcc-aqualia-de-espana-desarrollara-la-planta-de-tratamiento-de-aguas-residuales-de-chincha",
    "Actor: FCC Aqualia (Spain) — allied. Official ProInversión Spanish award. CapEx = USD 96.5m adjudicated investment. Shuffle water.",
    "hunt_cycle190",
    investment_type="ppp_concession",
    evidence="documented",
    currency="USD",
    value_usd="96500000",
    fx_usd="1",
    bib_type="government",
    chicago='Agencia de Promoción de la Inversión Privada (PROINVERSIÓN). “FCC Aqualia de España desarrollará la Planta de Tratamiento de Aguas Residuales de Chincha.” January 7, 2025. https://www.gob.pe/institucion/proinversion/noticias/1087293-fcc-aqualia-de-espana-desarrollara-la-planta-de-tratamiento-de-aguas-residuales-de-chincha.',
    annotation="ProInversión: Aqualia PTAR Chincha USD 96.5m. Supports aqualia_ptar_chincha_96p5m_2025.",
    evid_note="Opened ProInversión Spanish award release 2026-10-04; MEF Jul 2025 contract-signing cross-checked (~USD 250m package not entered).",
)

# 2. rail / allied — Sacyr Fortaleza Metro Linha Leste three stations R$1.230bn
row_doc(
    "sacyr_fortaleza_metro_leste_1230m_brl_2026",
    "infrastructure",
    "rail",
    "allied",
    "Sacyr Construcción — Fortaleza Metro Linha Leste stations Sé / Luíza Távora / Leonardo Mota",
    "Brazil",
    "18 Sep 2026 Atlas Público (DOU republication): Governo do Ceará / Seinfra declares Sacyr Construccion S/A do Brasil winner of Concorrência Nacional Eletrônica nº 20260001 for integrated contracting of three underground Linha Leste Metrofor stations (Sé, Luíza Távora, Leonardo Mota) — basic/executive design, civil works, equipment, special services. Winning proposal face = R$ 1,230,612,738.18 (BRL stored without FX). Award published DOU 18 Sep 2026 (act dated 15 Sep); contract signing still administrative. Distinct from prior FTS Linha Leste consortium works.",
    "1230612738",
    "2026-09-18",
    "2026",
    "-3.73",
    "-38.52",
    "Fortaleza Metro Linha Leste / Sé–Luíza Távora–Leonardo Mota corridor, Ceará, Brazil (award geography; approximate Sé pin).",
    "atlas_publico_sacyr_fortaleza_20260918",
    "A empresa Sacyr Construccion S/A do Brasil foi declarada vencedora da licitação para a contratação integrada da construção de três estações subterrâneas da Linha Leste do Metrô de Fortaleza: Sé, Luíza Távora e Leonardo Mota. … O valor global informado para a contratação é de R$ 1.230.612.738,18.",
    "https://atlaspublico.com.br/noticias/governo-do-ceara-declara-sacyr-vencedora-de-licitacao-para-87968",
    "Actor: Sacyr Construcción (Spain) via Brazil subsidiary — allied. Atlas Público DOU-sourced award notice. CapEx = R$1,230,612,738.18 face. Shuffle rail.",
    "hunt_cycle190",
    investment_type="epc",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Atlas Público (Diário Oficial da União republication). “Governo do Ceará declara Sacyr vencedora de licitação para três estações do Metrô de Fortaleza.” September 18, 2026. https://atlaspublico.com.br/noticias/governo-do-ceara-declara-sacyr-vencedora-de-licitacao-para-87968.',
    annotation="DOU/Atlas Público: Sacyr Fortaleza Linha Leste R$1.230bn. Supports sacyr_fortaleza_metro_leste_1230m_brl_2026.",
    evid_note="Opened Atlas Público DOU-sourced award page 2026-10-04; Diário do Transporte corroborates figure.",
)

# 3. rail / allied — Mota-Engil CDMX Metro L3 coinversión offer MXN 25,180m
row_doc(
    "mota_engil_cdmx_metro_l3_25180m_mxn_2026",
    "infrastructure",
    "rail",
    "allied",
    "Mota-Engil México — CDMX Metro Línea 3 renovation coinversión (economic offer)",
    "Mexico",
    "23 Sep 2026 CDMX Jefatura de Gobierno: fallo names Mota Engil México winner of Línea 3 (Indios Verdes–Universidad) renovation coinversión — integral track/civil/rail systems, rolling stock provision, and long-term services; economic offer MXN 25,180 million excludes IVA, City contribution, and rolling-stock cost; SAF states overall investment >MXN 40bn; Congreso authorization via Paquete Económico 2027 still pending (fallo is not yet a financial commitment). CapEx face = MXN 25,180,000,000 offer (MXN stored without FX). Distinct from mota_engil_qi_tramo* and Santos–Guarujá rows.",
    "25180000000",
    "2026-09-23",
    "2026",
    "19.50",
    "-99.12",
    "STC Metro Línea 3 Indios Verdes–Universidad corridor, Mexico City (Jefatura geography; approximate Indios Verdes pin).",
    "cdmx_jefatura_metro_l3_20260923",
    "los 25 mil 180 millones de pesos que se mencionan en la propuesta de la empresa ganadora, Mota Engil Mexico, es la cantidad que corresponde al monto de oferta económica … monto que no incluye el IVA ni la aportación de la entidad, ni el costo del material rodante.",
    "https://jefaturadegobierno.cdmx.gob.mx/comunicacion/nota/gobierno-de-la-ciudad-de-mexico-informo-que-manana-se-publicara-en-la-gaceta-oficial-el-nombre-de-la-empresa-ganadora-del-concurso-de-licitacion-de-la-linea-3-del-metro",
    "Actor: Mota-Engil México (Portugal group) — allied. Official CDMX Jefatura Spanish press. CapEx = MXN 25,180m economic offer; Congress authorization pending. Shuffle rail.",
    "hunt_cycle190",
    investment_type="ppp_concession",
    evidence="documented",
    currency="MXN",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Jefatura de Gobierno de la Ciudad de México. “Gobierno de la Ciudad de México informó que mañana se publicará en la Gaceta Oficial el nombre de la Empresa Ganadora del Concurso de Licitación de la Línea 3 del Metro.” September 23, 2026. https://jefaturadegobierno.cdmx.gob.mx/comunicacion/nota/gobierno-de-la-ciudad-de-mexico-informo-que-manana-se-publicara-en-la-gaceta-oficial-el-nombre-de-la-empresa-ganadora-del-concurso-de-licitacion-de-la-linea-3-del-metro.',
    annotation="CDMX Jefatura: Mota-Engil Metro L3 MXN 25,180m offer. Supports mota_engil_cdmx_metro_l3_25180m_mxn_2026.",
    evid_note="Opened CDMX Jefatura Spanish press 2026-10-04; El Economista/El Universal corroborate Gaceta fallo and Congress caveat.",
)

# 4. solar / allied — Scatec Barzalosa Colombia FID USD 121m
row_doc(
    "scatec_barzalosa_121m_2026",
    "energy",
    "solar",
    "allied",
    "Scatec ASA / Norfund — Barzalosa 130 MW solar FID (Colombia)",
    "Colombia",
    "24 Feb 2026 Scatec: reaches financial close and starts construction of 130 MW Barzalosa solar plant in Colombia; 15-year PPA with BTG Pactual Comercializadora covering ~85% of production; Scatec 65% equity + Norfund 35%; CapEx estimated USD 121 million (~70% non-recourse debt; Bancolombia + FDN senior lenders); Scatec EPC ~70% of CapEx + O&M/AM; COD targeted 1H 2027. CapEx = USD 121m. Distinct from atlas_el_campano_fc_2026.",
    "121000000",
    "2026-02-24",
    "2026",
    "",
    "",
    "Barzalosa solar plant, Colombia (company release; municipality not named on primary — lat/lon blank).",
    "scatec_barzalosa_fc_20260224",
    "Scatec ASA … has reached financial close for the 130 MW “Barzalosa” solar plant in Colombia, and is starting construction. … The total capital expenditure (capex) for the project is estimated at USD 121 million",
    "https://www.scatec.com/en/scatec-reaches-financial-close-and-starts-construction-of-130-mw-solar-power-plant-in-colombia/",
    "Actor: Scatec ASA (Norway) with Norfund — allied. Company English regulatory release. CapEx = USD 121m. Shuffle solar.",
    "hunt_cycle190",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="121000000",
    fx_usd="1",
    bib_type="company",
    chicago='Scatec ASA. “Scatec reaches financial close and starts construction of 130 MW solar power plant in Colombia.” February 24, 2026. https://www.scatec.com/en/scatec-reaches-financial-close-and-starts-construction-of-130-mw-solar-power-plant-in-colombia/.',
    annotation="Scatec: Barzalosa Colombia USD 121m FID. Supports scatec_barzalosa_121m_2026.",
    evid_note="Opened Scatec English regulatory press 2026-10-04.",
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
    print(f"cycle190 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
