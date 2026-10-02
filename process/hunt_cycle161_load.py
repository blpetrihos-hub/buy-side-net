#!/usr/bin/env python3
"""Cycle 161 hunt: shuffle_seed=20261161; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: fission_smr, port_ownership, power_plants_grid, lithium,
other_renewables, port_cranes, building_materials, graphite, balsa, wind, niobium,
copper, nickel, water, rail, bridges_roads, engineering_epc, solar.

Weight under-covered: Uruguay, Guatemala, Panama, Dominican Republic.
PRC ahead by 9 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite/fission_smr once each (dry → nickel/niobium).
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
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
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


# 1. power_plants_grid / prc — CMEC Uruguay Anillo Norte 500 kV USD 191m
row_doc(
    "cmec_uruguay_anillo_norte_500kv_191m_2021",
    "energy",
    "power_plants_grid",
    "prc",
    "CMEC (China Machinery Engineering Corporation) — Anillo Norte 500 kV transmission closure (Chamberlain)",
    "Uruguay",
    "31 May 2021 UTE: leasing contract signed with CMEC / RAFISA for Norte transmission ring closure — ~350 km 500 kV (Tacuarembó–Chamberlain–Salto Grande), new Chamberlain 500 kV substation, two 150 kV ties; project cost USD 191m via UTE–RAFISA trust; largest Chinese-origin infrastructure locally per UTE. UTE 25 May 2026: first 500 kV segment Salto Grande–Tacuarembó energized. CapEx USD 191m documented. Distinct from Invenergy Cardal TX row.",
    "191000000",
    "2021-05-31",
    "2021",
    "-31.880",
    "-56.020",
    "Chamberlain, Tacuarembó department, Uruguay (new 500 kV substation node).",
    "ute_cmec_anillo_norte_20210531",
    "se suscribió el contrato de suministro y construcción … cierre del Anillo de Transmisión del Norte … unirá Tacuarembó con Salto. … será la más grande realizada localmente por una empresa de origen chino. … dos tramos: uno Tacuarembó – Chamberlain y otro Chamberlain – Salto Grande, cubriendo en total una distancia de aproximadamente 350 km. … El proyecto … tiene un costo de U$S 191 millones. … firmado … por las empresas China Machinery Engineering Coporation (CMEC) y República Administradora de Fondos de Inversión S.A. (RAFISA).",
    "https://ute.com.uy/noticias/ute-concreta-el-cierre-del-anillo-norte-de-trasmision",
    "Actor: CMEC (Beijing SOE) — prc. UTE Spanish primary (opened). USD 191m leasing contract. First Uruguay PRC power_plants_grid row; fills undersampled Uruguay×grid.",
    "hunt_energy_power_plants_grid",
    investment_type="epc",
    bib_type="government",
    chicago='Administración Nacional de Usinas y Trasmisiones Eléctricas (UTE). “UTE concreta el cierre del Anillo Norte de trasmisión.” May 31, 2021. https://ute.com.uy/noticias/ute-concreta-el-cierre-del-anillo-norte-de-trasmision.',
    annotation="UTE primary: CMEC Anillo Norte 500 kV / ~350 km / USD 191m leasing. Supports cmec_uruguay_anillo_norte_500kv_191m_2021.",
    evid_note="Opened UTE 31 May 2021 (CMEC Anillo Norte USD 191m contract).",
)

# 2. power_plants_grid / us — Invenergy Tealov Cardal 500 kV Uruguay COD 2024
row_doc(
    "invenergy_tealov_cardal_tx_uruguay_2024",
    "energy",
    "power_plants_grid",
    "us",
    "Invenergy — Tealov Cardal 500 kV transmission (Uruguay)",
    "Uruguay",
    "16 Feb 2024 Invenergy: commercial operations on Tealov Cardal HV transmission — new 55 km 500 kV line, 20 km 150 kV line, new 500 kV substation; connects Punta del Tigre substation and 150 kV in Salto; UTE operates under 30-year lease; financed with IDB Invest A/B bond private placement (Moody’s Baa2); EPC consortium Saceem/Ingener; 480 construction jobs. CapEx blank (financing structure disclosed without USD total). Distinct from CMEC Anillo Norte.",
    "",
    "",
    "2024",
    "-34.480",
    "-56.400",
    "Cardal / Florida–San José corridor, Uruguay (Punta del Tigre interconnection; approximate).",
    "invenergy_cardal_cod_20240216",
    "Invenergy … announced commercial operations have commenced on its landmark high-voltage Tealov Cardal transmission line in Uruguay … Cardal consists of a new 55-kilometer (34-mile), 500 kV high-voltage transmission line, a new 20-kilometer (12-mile), 150 kV transmission line, a new 500 kV substation, and accompanying infrastructure. … The line is operated by … UTE … under a 30-year lease agreement. … Invenergy in partnership with IDB Invest … financed the construction under an innovative A/B Bond structure",
    "https://wwww.invenergy.com/news/invenergy-s-landmark-tealov-cardal-transmission-line-begins-operations-in-uruguay-",
    "Actor: Invenergy (Chicago HQ) — us. Company English primary. CapEx blank. Undersampled Uruguay×US grid transmission.",
    "hunt_energy_power_plants_grid",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Invenergy LLC. “Invenergy’s Landmark Tealov Cardal Transmission Line Begins Operations in Uruguay.” February 16, 2024. https://wwww.invenergy.com/news/invenergy-s-landmark-tealov-cardal-transmission-line-begins-operations-in-uruguay-.',
    annotation="Invenergy primary: Cardal 55 km 500 kV + 20 km 150 kV COD Feb 2024 / 30-year UTE lease. Supports invenergy_tealov_cardal_tx_uruguay_2024.",
    evid_note="Opened Invenergy 16 Feb 2024 (Cardal TX COD).",
)

# 3. solar / us — Invenergy La Jacinta Uruguay 64–65 MW (still owned per 2024 Cardal release)
row_doc(
    "invenergy_la_jacinta_solar_uruguay_64mw",
    "energy",
    "solar",
    "us",
    "Invenergy — La Jacinta Solar Farm (64–65 MW; Salto)",
    "Uruguay",
    "14 Mar 2017 Invenergy: purchases operating La Jacinta Solar Farm from FRV — 64 MW / 216,000 BYD panels; COD Oct 2015. 16 Feb 2024 Invenergy Cardal release confirms continued ownership of 65 MW La Jacinta. CapEx blank (purchase price undisclosed). Distinct from atlas_uruguay_solar_sale_76mwp_2026.",
    "",
    "",
    "2017",
    "-31.450",
    "-57.960",
    "La Jacinta, Salto department, Uruguay (~5 km south of Salto city per prior FRV ESIA).",
    "invenergy_la_jacinta_purchase_20170314",
    "Invenergy LLC (“Invenergy”) announced today that it has purchased the La Jacinta Solar Farm in Uruguay from Fotowatio Renewable Ventures (FRV), the developer of the solar farm which has been operating since October 2015. … La Jacinta has an installed capacity of 64 MW of power from 216,000 solar panels manufactured by BYD.",
    "https://invenergy.com/news/invenergy-closes-purchase-agreement-for-the-la-jacinta-solar-farm-in-uruguay",
    "Actor: Invenergy (Chicago HQ) owner — us. Company English primary; 2024 Cardal release confirms ongoing ownership. CapEx blank. First Uruguay US solar ownership row.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Invenergy LLC. “Invenergy Closes Purchase Agreement for the La Jacinta Solar Farm in Uruguay.” March 14, 2017. https://invenergy.com/news/invenergy-closes-purchase-agreement-for-the-la-jacinta-solar-farm-in-uruguay.',
    annotation="Invenergy primary: purchase of operating 64 MW La Jacinta (BYD modules). Supports invenergy_la_jacinta_solar_uruguay_64mw.",
    evid_note="Opened Invenergy 14 Mar 2017 (La Jacinta purchase); ownership reconfirmed in 2024 Cardal release.",
)

# 4. wind / us — Invenergy Campo Palomas Uruguay 70 MW
row_doc(
    "invenergy_campo_palomas_wind_uruguay_70mw",
    "energy",
    "wind",
    "us",
    "Invenergy — Campo Palomas Wind Farm (70 MW; Salto)",
    "Uruguay",
    "1 Apr 2016 Invenergy: closes acquisition and financing of Campo Palomas Wind Farm — 70 MW from 35 Vestas V110-2.0 MW turbines; expected COD Feb 2017; UTE long-term lease offtaker; IIC financing / DNB MLA. 16 Feb 2024 Cardal release confirms continued ownership of 70 MW Campo Palomas. CapEx blank. Distinct from nordex Uruguay historical OEM rows if any.",
    "",
    "",
    "2016",
    "-31.400",
    "-57.700",
    "Campo Palomas, Salto department, Uruguay (wind farm; departmental pin).",
    "invenergy_campo_palomas_20160401",
    "Invenergy Wind LLC (“Invenergy”) today announced that it has closed on the acquisition and financing of Campo Palomas Wind Farm … The facility will have the capacity to generate 70 MW of power from 35 Vestas V110 - 2.0 MW wind turbines when commercial operation commences in February 2017. The state-owned utility Usinas & Trasmisiones Electricas (UTE) will be the offtaker/lessor",
    "https://wwww.invenergy.com/news/invenergy-purchases-and-closes-financing-on-campo-palomas-wind-farm",
    "Actor: Invenergy (Chicago HQ) — us. Company English primary; ownership reconfirmed 2024. CapEx blank. First Uruguay US wind ownership row.",
    "hunt_energy_wind",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Invenergy Wind LLC. “Invenergy Purchases and Closes Financing on Campo Palomas Wind Farm.” April 1, 2016. https://wwww.invenergy.com/news/invenergy-purchases-and-closes-financing-on-campo-palomas-wind-farm.',
    annotation="Invenergy primary: Campo Palomas 70 MW / 35× Vestas V110 acquisition+financing. Supports invenergy_campo_palomas_wind_uruguay_70mw.",
    evid_note="Opened Invenergy 1 Apr 2016 (Campo Palomas acquisition).",
)

# 5. solar / us — AES Cedro Solar 10 MW Panama
row_doc(
    "aes_panama_cedro_10mw_2021",
    "energy",
    "solar",
    "us",
    "AES Panamá — Cedro Solar (10 MW; Boquerón, Chiriquí)",
    "Panama",
    "14 Feb 2020 AES Panamá: Cedro Solar among four 10 MW parks (Pesé, Mayorca, Cedro, Caoba) in >USD 50m Elecnor EPC portfolio. AES Q2 2026 Fact Sheet lists Cedro Panama Solar 10 MW at 49% AES ownership, COD 2021. CapEx blank at plant level. Distinct from aes_panama_pese_10mw_2021 / aes_panama_mayorca_10mw_2021 / aes_panama_caoba_10mw_2021.",
    "",
    "",
    "2021",
    "8.505",
    "-82.570",
    "Boquerón district, Chiriquí province, Panama (Cedro Solar).",
    "aes_panama_solar40mw_20200214",
    "four smaller projects of 10MW each … Pesé Solar (District of Pesé, Herrera Province), Mayorca Solar (District of Pocrí, Los Santos Province), and Cedro & Caoba Solar (both in the district of Boquerón, Chiriquí Province).",
    "https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables",
    "Actor: AES Panamá (U.S. HQ parent) — us. Same company primary as Pesé/Mayorca. CapEx blank.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Panamá. “AES Panamá aumenta su apuesta a las energías renovables.” February 14, 2020. https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables.',
    annotation="AES Panamá primary: Cedro Solar 10 MW. Supports aes_panama_cedro_10mw_2021; aes_panama_caoba_10mw_2021.",
    evid_note="Opened AES Panamá 14 Feb 2020 (Cedro Solar 10 MW).",
)

# 6. solar / us — AES Caoba Solar 10 MW Panama
row_doc(
    "aes_panama_caoba_10mw_2021",
    "energy",
    "solar",
    "us",
    "AES Panamá — Caoba Solar (10 MW; Boquerón, Chiriquí)",
    "Panama",
    "14 Feb 2020 AES Panamá: Caoba Solar among four 10 MW parks. AES Q2 2026 Fact Sheet lists Caoba Panama Solar 10 MW at 49% AES ownership, COD 2021. CapEx blank. Distinct from aes_panama_cedro_10mw_2021.",
    "",
    "",
    "2021",
    "8.490",
    "-82.550",
    "Boquerón district, Chiriquí province, Panama (Caoba Solar; near Cedro).",
    "aes_panama_solar40mw_20200214",
    "Cedro & Caoba Solar (both in the district of Boquerón, Chiriquí Province).",
    "https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables",
    "Actor: AES Panamá (U.S. HQ parent) — us. CapEx blank. Completes four-park named AES Panama solar set.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Panamá. “AES Panamá aumenta su apuesta a las energías renovables.” February 14, 2020. https://www.aespanama.com/en/press-release/aes-panama-aumenta-su-apuesta-las-energias-renovables.',
    annotation="AES Panamá primary: Caoba Solar 10 MW. Supports aes_panama_caoba_10mw_2021; aes_panama_cedro_10mw_2021.",
    evid_note="Opened AES Panamá 14 Feb 2020 (Caoba Solar 10 MW).",
)

# 7. solar / us — USTDA New Sun Road Guatemala solar DCC pilot
row_doc(
    "ustda_new_sun_road_guatemala_dcc_2023",
    "energy",
    "solar",
    "us",
    "USTDA / New Sun Road — solar-powered digital community centers pilot (10 sites; Guatemala)",
    "Guatemala",
    "30 Aug 2023 USTDA: technical assistance grant to Senacyt; California-based New Sun Road selected to install women-led solar-powered digital community centers (DCCs) with battery storage and microgrids in 10 unconnected communities, aiming to scale to 3,000 sites. Grant USD amount not disclosed on opened page — CapEx blank. Distinct from first_solar_zacapa_exim_guatemala_2021.",
    "",
    "",
    "2023",
    "14.635",
    "-90.508",
    "Rural Guatemala (10 pilot DCC sites TBD; national pin).",
    "ustda_guatemala_new_sun_road_20230830",
    "the U.S. Trade and Development Agency awarded a technical assistance grant to Guatemala’s National Secretariat of Science and Technology (Senacyt) … Senacyt selected California-based New Sun Road … installation of women-led solar-powered digital community centers (DCCs) in 10 unconnected communities, with the goal of scaling the project to 3,000 sites across rural Guatemala. … The DCCs will be powered by solar panels coupled with battery storage and microgrids",
    "https://www.ustda.gov/ustda-advances-sustainable-women-led-rural-connectivity-in-guatemala/",
    "Actor: USTDA grant to U.S. firm New Sun Road — us. USTDA English primary. CapEx blank (grant amount undisclosed). Undersampled Guatemala solar beyond First Solar Zacapa.",
    "hunt_energy_solar",
    investment_type="financing",
    bib_type="government",
    chicago='U.S. Trade and Development Agency. “USTDA Advances Sustainable, Women-Led Rural Connectivity in Guatemala.” August 30, 2023. https://www.ustda.gov/ustda-advances-sustainable-women-led-rural-connectivity-in-guatemala/.',
    annotation="USTDA primary: New Sun Road solar+storage DCC pilot (10 sites / scale to 3,000). Supports ustda_new_sun_road_guatemala_dcc_2023.",
    evid_note="Opened USTDA 30 Aug 2023 (New Sun Road Guatemala solar DCC grant).",
)

# 8. power_plants_grid / us — AES ENADOM 2nd LNG tank USD 253m DR
row_doc(
    "aes_enadom_lng_tank2_253m_dr_2023",
    "energy",
    "power_plants_grid",
    "us",
    "AES Andrés / ENADOM — second LNG storage tank (120,000 m³; Punta Caucedo)",
    "Dominican Republic",
    "AES Dominicana Investor Presentation Q3 2025 (opened): ENADOM JV (Andres BV + Energas) — 2nd LNG storage tank completed construction Oct 2023; capacity 120,000 m³ (~50 TBtu/y); total cost budgeted at USD 253m. Complements Andrés 160,000 m³ tank / regas / pipelines serving Los Mina and Eastern Gas Pipeline. CapEx USD 253m documented. Distinct from aes solar/wind DR rows.",
    "253000000",
    "2023-10-31",
    "2023",
    "18.425",
    "-69.630",
    "AES Andrés / ENADOM LNG terminal, Punta Caucedo, Dominican Republic.",
    "aes_dominicana_ir_q3_2025",
    "The 2 nd LNG storage tank, completed construction in Oct. 2023. Total Cost is budgeted at $253M. • Capacity: 120,000 m 3 (~50 TBTU/year)",
    "https://www.aesdominicana.com/sites/aesvault.com/files/2026-01/AES%20DR%20-%20Investor%20Presentation%202025%20Q3.pdf",
    "Actor: AES Andrés / ENADOM (U.S. HQ parent AES) — us. Company IR PDF primary. USD 253m. Undersampled DR LNG infrastructure beyond generation plants.",
    "hunt_energy_power_plants_grid",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Dominicana. “Investor Presentation 2025 Q3.” January 2026. https://www.aesdominicana.com/sites/aesvault.com/files/2026-01/AES%20DR%20-%20Investor%20Presentation%202025%20Q3.pdf.',
    annotation="AES Dominicana IR: ENADOM 2nd LNG tank 120,000 m³ COD Oct 2023 / USD 253m. Supports aes_enadom_lng_tank2_253m_dr_2023.",
    evid_note="Opened AES Dominicana Q3 2025 IR PDF (ENADOM 2nd tank USD 253m).",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        supports = list(existing.get("supports") or [])
        for s in entry.get("supports") or []:
            if s not in supports:
                supports.append(s)
        existing.update(entry)
        existing["supports"] = supports
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
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
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 161 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
