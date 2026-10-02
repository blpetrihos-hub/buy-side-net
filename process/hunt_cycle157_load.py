#!/usr/bin/env python3
"""Cycle 157 hunt: shuffle_seed=20261157; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: other_renewables, port_cranes, rail, balsa, water,
fission_smr, niobium, bridges_roads, power_plants_grid, wind, graphite, nickel,
copper, port_ownership, engineering_epc, solar, lithium, building_materials.

Weight under-covered: El Salvador, Antigua, Trinidad, Suriname, Bolivia.
PRC ahead by 10 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite then fission_smr/nickel (dry → niobium).
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


# 1. other_renewables / us — AES Nejapa landfill-gas 6 MW (El Salvador)
row_doc(
    "aes_nejapa_biogas_6mw_elsalvador",
    "energy",
    "other_renewables",
    "us",
    "AES El Salvador — Nejapa landfill-gas / biogas plant (6 MW)",
    "El Salvador",
    "13 Aug 2025 AES El Salvador: company continues to operate 16 generation plants including one biogas unit inaugurated 2011 at Nejapa (first Central America landfill-methane plant); companion company Nejapa Plant page states 6 MW installed capacity from sanitary-landfill biogas. CapEx USD not disclosed. Distinct from aes_meanguera_golfo_solar_bess_2023 / aes_santa_ana_iv_55mw_2026.",
    "",
    "",
    "2025",
    "13.814",
    "-89.230",
    "Nejapa municipality, San Salvador department, El Salvador (AES Nejapa landfill-gas plant).",
    "aes_elsalvador_energy_future_20250813",
    "With the firm purpose of contributing to the energy development of the country and the region, AES El Salvador inaugurated the Nejapa plant, the first in Central America capable of generating energy from methane gas captured from a landfill. … AES El Salvador currently has 16 generation plants: one based on biogas and 15 solar plants.",
    "https://www.aes-elsalvador.com/en/press-release/el-salvador-energy-future-built-today",
    "Actor: AES Corporation / AES El Salvador (U.S. HQ) — us. Company English primary (13 Aug 2025) confirming ongoing Nejapa biogas plant among 16 generators; 6 MW capacity opened on companion Nejapa Plant page. CapEx blank. Undersampled El Salvador other_renewables.",
    "hunt_energy_other_renewables",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES El Salvador. “El Salvador: The energy of the future is built today.” August 13, 2025. https://www.aes-elsalvador.com/en/press-release/el-salvador-energy-future-built-today.',
    annotation="AES El Salvador primary: Nejapa biogas among 16 plants (2025). Supports aes_nejapa_biogas_6mw_elsalvador.",
    evid_note="Opened AES El Salvador English 13 Aug 2025; companion Nejapa Plant page for 6 MW capacity.",
)

# 2. water / us — Seven Seas Barnacle Point Antigua 2 IMGD
row_doc(
    "seven_seas_barnacle_point_antigua_2migd_2026",
    "resources",
    "water",
    "us",
    "Seven Seas Water Group — Barnacle Point SWRO desalination (2 IMGD; Antigua)",
    "Antigua and Barbuda",
    "20 Jan 2026 Seven Seas: with APUA opens Barnacle Point SWRO plant (2 million imperial gallons/day) adjacent to existing Ivan Rodrigues facility; northwestern corridor service; production began Nov 2025; second plant under Mar 2024 WaaS BOOT with Ffryes Beach (together up to 3 IMGD). CapEx USD not disclosed. Distinct from seven_seas_ffryes_antigua_1migd_2025.",
    "",
    "",
    "2026",
    "17.142",
    "-61.773",
    "Barnacle Point / Ivan Rodrigues corridor, northwestern Antigua (Maiden Island / Saint George area).",
    "seven_seas_barnacle_point_20260120",
    "The Antigua Public Utilities Authority (APUA) and Seven Seas Water Group (SSWG) … today announced the opening of the Barnacle Point seawater reverse osmosis (SWRO) desalination plant. … has a production capacity of 2 million imperial gallons per day (IMGD) and will serve communities in the island’s northwestern corridor. The plant is located adjacent to APUA’s existing Ivan Rodrigues desalination plant … Water production at the new Barnacle Point plant began in November 2025.",
    "https://sevenseaswater.com/opening-of-barnacle-point-plant/",
    "Actor: Seven Seas Water Group (Tampa/Houston HQ) — us. Company English primary. CapEx blank. Second Antigua desal row after Ffryes Beach.",
    "hunt_res_water",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Seven Seas Water Group. “Seven Seas Water Group and APUA Open Barnacle Point Plant, Antigua’s Second New Water-as-a-Service® Desalination Facility, Adding 2 Million IGPD.” January 20, 2026. https://sevenseaswater.com/opening-of-barnacle-point-plant/.',
    annotation="Seven Seas primary: Barnacle Point 2 IMGD COD / Nov 2025 production. Supports seven_seas_barnacle_point_antigua_2migd_2026.",
    evid_note="Opened Seven Seas English 20 Jan 2026 (Barnacle Point 2 IMGD opening).",
)

# 3. solar / us — AES Metapán Apopa Energy 1.5 MWp
row_doc(
    "aes_metapan_apopa_1p5mwp_2022",
    "energy",
    "solar",
    "us",
    "AES El Salvador Solutions — Apopa Energy Metapán solar (1.5 MWp)",
    "El Salvador",
    "16 Mar 2022 AES El Salvador: Solutions Division constructed 1.5 MWp PV plant for Apopa Energy in Metapán, Santa Ana; >3,400 monocrystalline modules, nine inverters, power substation; output injected to AES CLESA distribution. CapEx USD not disclosed. Distinct from aes_santa_ana_iv_55mw_2026 / aes_meanguera_golfo_solar_bess_2023.",
    "",
    "",
    "2022",
    "14.332",
    "-89.448",
    "Metapán municipality, Santa Ana department, El Salvador (Apopa Energy PV plant).",
    "aes_elsalvador_metapan_apopa_20220316",
    "Recientemente, AES El Salvador a través de su División Soluciones realizó la construcción de la planta fotovoltaica para la empresa Apopa Energy. El nuevo parque fotovoltaico está ubicado en el Municipio de Metapán, Departamento de Santa Ana y cuenta con la capacidad de generar 1.5 megavatios (MWp) de energía. … La energía generada por la nueva planta solar será inyectada a la red de distribución eléctrica de AES CLESA",
    "https://www.aes-elsalvador.com/en/press-release/aes-construye-planta-solar-cliente-comercial",
    "Actor: AES El Salvador Solutions (U.S. HQ parent) — us. Company Spanish/English primary. CapEx blank. Commercial EPC for Apopa Energy offtake into AES CLESA grid.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='AES El Salvador. “AES construye planta solar a cliente comercial.” March 16, 2022. https://www.aes-elsalvador.com/en/press-release/aes-construye-planta-solar-cliente-comercial.',
    annotation="AES El Salvador primary: Metapán Apopa Energy 1.5 MWp construction. Supports aes_metapan_apopa_1p5mwp_2022.",
    evid_note="Opened AES El Salvador Spanish release 16 Mar 2022 (Metapán 1.5 MWp / Apopa Energy).",
)

# 4. bridges_roads / prc — CRCC Diego Martin–Westmoorings interchange Trinidad
row_doc(
    "crcc_diego_martin_westmoorings_tt_2023",
    "infrastructure",
    "bridges_roads",
    "prc",
    "China Railway Construction Corporation — Diego Martin–Westmoorings road bridge / interchange (Trinidad)",
    "Trinidad and Tobago",
    "25 Dec 2023 China Daily: CRCC completed road bridge linking western Port of Spain main road and Diego Martin Highway; PM Rowley attended completion ceremony; main bridge uses post-tensioned prefabricated small box girders (first Caribbean application); two roundabouts, connecting roads, four ramps, two subsidiary roads. CapEx USD not on China Daily (press TT$185–190m figures left UNVERIFIED / not entered). Distinct from powerchina_piarco_trinidad_2024 / powerchina_malabar_wwtp_trinidad_2019.",
    "",
    "",
    "2023",
    "10.714",
    "-61.579",
    "Diego Martin Highway / Western Main Road interchange, Diego Martin, Trinidad.",
    "chinadaily_crcc_diego_martin_20231225",
    "China Railway Construction Corporation recently completed the construction of a road bridge linking a main road and a major freeway in Port of Spain, the capital of Trinidad and Tobago … The bridge links the main road in the western part of Port of Spain and the Diego Martin Highway. … The main components of the project included the main bridge spanning the Diego Martin Highway, two roundabouts, two connecting roads, four ramps and two subsidiary roads.",
    "https://global.chinadaily.com.cn/a/202312/25/WS6589445ba31040ac301a9673.html",
    "Actor: CRCC / China Railway Construction (Caribbean) — prc. China Daily English primary (CRCC-provided). CapEx blank (local-press TT$ figures UNVERIFIED, not entered). Undersampled Trinidad bridges_roads.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    bib_type="press",
    chicago='Luo Wangshu. “Chinese-built road bridge completed in Trinidad and Tobago.” China Daily, December 25, 2023. https://global.chinadaily.com.cn/a/202312/25/WS6589445ba31040ac301a9673.html.',
    annotation="China Daily: CRCC Diego Martin–Westmoorings road bridge completion. Supports crcc_diego_martin_westmoorings_tt_2023.",
    evid_note="Opened China Daily English 25 Dec 2023 (CRCC Diego Martin road bridge).",
)

# 5. water / prc — China Antigua re-piping grant (UNVERIFIED USD 60m)
row_doc(
    "china_antigua_water_repiping_60m_2025",
    "resources",
    "water",
    "prc",
    "PRC government — Antigua and Barbuda national water re-piping grant (USD 60m UNVERIFIED)",
    "Antigua and Barbuda",
    "16 Jun 2025 Antigua News Room: Utilities Minister Melford Nicholas confirms Antigua and Barbuda set to receive a US$60 million grant from China for national re-piping / modernising aging water pipelines (St John’s and rural districts including Villa and Point); follows PM Browne China visit. Face value = press-reported grant (UNVERIFIED). Complements Jan 2024 Water Rehabilitation Project agreement signing (antigua.news). Distinct from seven_seas_ffryes_antigua_1migd_2025 / seven_seas_barnacle_point_antigua_2migd_2026.",
    "60000000",
    "2025-06-16",
    "2025",
    "17.127",
    "-61.847",
    "St John’s / national distribution network, Antigua (re-piping program; urban St John’s pin).",
    "antigua_newsroom_china_repiping_60m_20250616",
    "Utilities Minister Melford Nicholas has confirmed that Antigua and Barbuda is set to receive a US$60 million grant from China to support a national re-piping initiative aimed at modernising the country’s aging water infrastructure. The funding, which was secured following a diplomatic visit by Prime Minister Gaston Browne to China, is expected to accelerate efforts to replace deteriorating underground pipelines",
    "https://antiguanewsroom.com/60-million-chinese-re-piping-grant-to-support-major-infrastructure-overhaul/",
    "Actor: PRC government grant — prc. Press-only USD 60m — evidence=proxy / UNVERIFIED. CapEx = press figure. Complements opened Jan 2024 Water Rehabilitation agreement (antigua.news).",
    "hunt_res_water",
    investment_type="financing",
    evidence="proxy",
    bib_type="press",
    chicago='Antigua News Room. “$60 Million Chinese Re-piping Grant to Support Major Infrastructure Overhaul.” June 16, 2025. https://antiguanewsroom.com/60-million-chinese-re-piping-grant-to-support-major-infrastructure-overhaul/.',
    annotation="Antigua News Room press: USD 60m China re-piping grant (UNVERIFIED). Supports china_antigua_water_repiping_60m_2025.",
    evid_note="Opened Antigua News Room 16 Jun 2025 (USD 60m China re-piping grant; UNVERIFIED).",
)

# 6. solar / prc — POWERCHINA Botopasi Suriname Phase II site
row_doc(
    "powerchina_botopasi_suriname_2025",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Botopasi Microgrid Project (1,020 kW solar; Suriname Phase II site 2)",
    "Suriname",
    "29 Apr 2025 POWERCHINA: Vice-President Ronnie Brunswijk and Minister David Abiamofo attend 25 Apr inauguration/lighting of Botopasi Microgrid Project — second completed site of Suriname Village Microgrid Solar Project Phase II; 1,020 kW solar + 2,580 kWh storage + 800 kVA diesel; ~1,600 MWh/yr; serves 11 forest villages. CapEx blank. Distinct from powerchina_djoemoe_suriname_2026 / powerchina_kajana_guyaba_suriname_2026 / powerchina_suriname_microgrid_p2_2026.",
    "",
    "",
    "2025",
    "4.217",
    "-55.447",
    "Botopasi, Boven Suriname / Sipaliwini, Suriname (Phase II Botopasi microgrid site).",
    "powerchina_botopasi_20250429",
    "On April 25, local time, Suriname's vice-President Ronnie Brunswijk, along with Minister of Natural Resources David Abiamofo, attended the inauguration and lighting ceremony of the Botopasi Microgrid Project. The project is part of the second phase of the Suriname Village Microgrid Solar Project constructed by POWERCHINA. … The Botopasi Microgrid Project is the second site completed under this phase. It includes a solar capacity of 1,020 kW, energy storage of 2,580 kWh, and a diesel generator capacity of 800 KVA, with an annual electricity output of 1,600 MWh.",
    "https://en.powerchina.cn/2025-04/29/c_828922.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English primary for named Botopasi COD. CapEx blank. Named-site presence distinct from Kajana/Guyaba and Djoemoe rows.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “Vice-president attends POWERCHINA\'s inauguration of Suriname Microgrid Project.” April 29, 2025. https://en.powerchina.cn/2025-04/29/c_828922.htm.',
    annotation="POWERCHINA primary: Botopasi Phase II site inauguration (1,020 kW). Supports powerchina_botopasi_suriname_2025.",
    evid_note="Opened POWERCHINA English 29 Apr 2025 (Botopasi 1,020 kW inauguration).",
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
    print(f"Cycle 157 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
