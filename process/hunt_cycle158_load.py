#!/usr/bin/env python3
"""Cycle 158 hunt: shuffle_seed=20261158; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: rail, niobium, water, wind, bridges_roads, balsa,
other_renewables, building_materials, solar, lithium, nickel, engineering_epc,
port_ownership, power_plants_grid, graphite, copper, fission_smr, port_cranes.

Weight under-covered: Honduras, Panama, Bolivia, El Salvador.
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


# 1. water / prc — POWERCHINA Panama City Water Pipeline (~USD 148.9m)
row_doc(
    "powerchina_panama_city_water_148p9m",
    "resources",
    "water",
    "prc",
    "POWERCHINA — Panama City Water Pipeline Project (~USD 148.9m)",
    "Panama",
    "10 Oct 2022 POWERCHINA country page: Americas regional HQ office in Panama (2016) carrying out Panama City Water Pipeline Project under construction; contract value approximately USD 148.9 million. Face value = stated contract value.",
    "148900000",
    "2022-10-10",
    "2022",
    "8.971",
    "-79.534",
    "Panama City, Panama (potable-water pipeline project; city pin).",
    "powerchina_panama_country_20221010",
    "POWERCHINA Americas regional headquarters established an office in Panama in 2016 and carried out a project—Panama City Water Pipeline Project, which is under construction so far and the contract value is approximately USD 148.9 million.",
    "https://en.powerchina.cn/2022-10/10/c_818779.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English primary. Contract value ~USD 148.9m. Undersampled Panama water.",
    "hunt_res_water",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “Panama.” October 10, 2022. https://en.powerchina.cn/2022-10/10/c_818779.htm.',
    annotation="POWERCHINA Panama country page: City Water Pipeline ~USD 148.9m. Supports powerchina_panama_city_water_148p9m.",
    evid_note="Opened POWERCHINA English Panama page 10 Oct 2022 (Water Pipeline ~USD 148.9m).",
)

# 2. wind / us — AES Panamá Penonomé I 55 MW acquisition
row_doc(
    "aes_panama_penonome_i_55mw_2020",
    "energy",
    "wind",
    "us",
    "AES Panamá — Penonomé I wind farm acquisition (55 MW; 22 Goldwind turbines)",
    "Panama",
    "28 Apr 2020 AES Panamá: agreed to acquire 55 MW Penonomé I / UEP wind project in Coclé Province from Goldwind Americas; 22 Goldwind GW109/2500 turbines; operating since 2014; 300 ha. CapEx USD not on AES Panama release (SEC 10-Q cites USD 80m acquisition — UNVERIFIED here / not dual-entered as price). Distinct from aes_panama_corotu_10mw_2025 / Los Santos.",
    "",
    "",
    "2020",
    "8.403",
    "-80.351",
    "El Coco / Penonomé district, Coclé Province, Panama (Penonomé I / Nuevo Chagres Phase I wind site).",
    "aes_panama_penonome_acq_20200428",
    "AES Panamá S.R.L … has agreed to acquire the 55-megawatt Penonomé I (one) Wind Project from Goldwind Americas (“Goldwind”) … The UEP wind project, located in the Coclé Province on Panama’s southern coast, is comprised of 22 Goldwind GW109/2500 permanent magnet direct-drive turbines. … With an installed capacity of 55 MW, the project brings AES Panamá ́s total operating capacity up to 609 MW.",
    "https://www.aespanama.com/en/press-release/aes-panama-will-continue-strengthen-its-energy-portfolio-through-acquisition-55mw",
    "Actor: AES Corporation / AES Panamá (U.S. HQ parent) — us. Company English primary for 55 MW acquisition. CapEx blank on primary. Undersampled Panama wind.",
    "hunt_energy_wind",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES Panamá. “AES Panama will continue to strengthen its energy portfolio through the acquisition of a 55MW wind farm.” April 28, 2020. https://www.aespanama.com/en/press-release/aes-panama-will-continue-strengthen-its-energy-portfolio-through-acquisition-55mw.',
    annotation="AES Panamá primary: Penonomé I 55 MW acquisition from Goldwind. Supports aes_panama_penonome_i_55mw_2020.",
    evid_note="Opened AES Panamá English 28 Apr 2020 (Penonomé I 55 MW acquisition).",
)

# 3. bridges_roads / prc — POWERCHINA El Sillar Highway Bolivia
row_doc(
    "powerchina_el_sillar_bolivia_2023",
    "infrastructure",
    "bridges_roads",
    "prc",
    "POWERCHINA / Sinohydro — El Sillar Highway (RN-4 Cochabamba–Santa Cruz; 30.3 km)",
    "Bolivia",
    "28 Nov 2023 POWERCHINA: El Sillar Highway Project temporarily accepted by Bolivia National Road Administration Bureau and fully opened to traffic; built by POWERCHINA; 30.3 km / 20.6 m wide on National Route 4 Cochabamba–Santa Cruz; four tunnels, 17 bridges, retaining walls, anti-slide piles, 139 culverts. CapEx USD not on company primary (ANF Mar 2026 press cites USD 426.1m Sinohydro contract — UNVERIFIED, not entered). Distinct from chec_sucre_yamparaez_bolivia_2025 / crec_espino_highway_bolivia_2023.",
    "",
    "",
    "2023",
    "-17.637",
    "-65.216",
    "El Sillar double-lane segment on RN-4 Cochabamba–Santa Cruz corridor (Epizana / Totora area pin).",
    "powerchina_el_sillar_20231128",
    "Following a temporary acceptance by Bolivia's National Road Administration Bureau, the El Sillar Highway Project, the largest ongoing road construction project in Bolivia, recently fully opened to traffic. It was built by POWERCHINA. … The El Sillar Highway Project winds its way through the Andes Mountains, serving as a crucial part of National Route 4, which connects Cochabamba and Santa Cruz, two major Bolivian cities. The highway spans a total length of 30.3 kilometers, with the road surface 20.6 meters wide. The highway features four separate tunnels, 17 bridges, 6.1 kilometers of reinforced concrete retaining walls, 21,000 meters of anti-slide piles, and 139 culverts.",
    "https://en.powerchina.cn/2023-11/28/c_828626.htm",
    "Actor: POWERCHINA / Sinohydro (PRC SOE) — prc. Company English primary for temporary acceptance / opening. CapEx blank (press USD 426.1m UNVERIFIED). Undersampled Bolivia bridges_roads.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “Bolivian president praises highway project built by POWERCHINA.” November 28, 2023. https://en.powerchina.cn/2023-11/28/c_828626.htm.',
    annotation="POWERCHINA primary: El Sillar Highway temporary acceptance / opening. Supports powerchina_el_sillar_bolivia_2023.",
    evid_note="Opened POWERCHINA English 28 Nov 2023 (El Sillar 30.3 km opening).",
)

# 4. other_renewables / us — Ormat Platanares geothermal Honduras 35 MW
row_doc(
    "ormat_platanares_honduras_35mw",
    "energy",
    "other_renewables",
    "us",
    "Ormat Technologies — Geoplatanares / Platanares geothermal plant (35 MW; Copán)",
    "Honduras",
    "Geoplatanares company site (opened 2026-10-02): first geothermal plant in Honduras; 35 MW generation capacity; located San Andrés Minas, municipio La Unión, departamento Copán; Ormat experience cited. CapEx blank. Distinct from ormat_amatitlan_guatemala / ormat_zunil_guatemala / ormat_dominica rows. Continuous U.S.-HQ Ormat ownership presence.",
    "",
    "",
    "2025",
    "14.659",
    "-88.896",
    "San Andrés Minas / La Unión municipality, Copán department, Honduras (Platanares geothermal; municipal pin).",
    "geoplatanares_hn_platanares",
    "Geoplatanares es la primera planta de energía geotérmica en Honduras la cual hace uso del recurso geotérmico, con una capacidad de generación de 35 Mw. Se encuentra ubicada en la Comunidad de San Andrés Minas, municipio de La Unión, departamento de Copan. … Es la experiencia que ORMAT posee en generación electrica mediante Geotermia.",
    "https://www.geoplatanares.hn/",
    "Actor: Ormat Technologies (NYSE:ORA; Reno HQ) via Geoplatanares — us. Company Spanish primary for 35 MW named site. CapEx blank. Undersampled Honduras other_renewables.",
    "hunt_energy_other_renewables",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Geoplatanares. “Inicio.” Accessed October 2, 2026. https://www.geoplatanares.hn/.',
    annotation="Geoplatanares primary: Platanares 35 MW Ormat geothermal Honduras. Supports ormat_platanares_honduras_35mw.",
    evid_note="Opened Geoplatanares Spanish site (35 MW Platanares / Ormat; Copán).",
)

# 5. solar / us — AES El Ronco / Holcim Metapán 21.4 MW (Banco Cuscatlán USD 14.8m)
row_doc(
    "aes_holcim_el_ronco_21p4mw_2023",
    "energy",
    "solar",
    "us",
    "AES El Salvador — Holcim El Ronco Metapán solar park (21.4 MW; Banco Cuscatlán USD 14.8m financing)",
    "El Salvador",
    "14 Mar 2023 AES El Salvador: Banco Cuscatlán financing of USD 14.8 million to AES for construction of 21.4 MW PV park at Holcim El Ronco plant, Metapán; three solar plants; 20-year PPA with Holcim (17 MW to Holcim); expected COD last quarter 2023. Face value = stated bank financing to AES. Press total CapEx ~USD 21m left UNVERIFIED / not entered as total. Distinct from aes_metapan_apopa_1p5mwp_2022 / aes_santa_ana_iv_55mw_2026.",
    "14800000",
    "2023-03-14",
    "2023",
    "14.332",
    "-89.448",
    "Holcim El Ronco plant, Metapán municipality, Santa Ana, El Salvador (on-site PV park).",
    "aes_elsalvador_banco_cuscatlan_ronco_20230314",
    "El Banco Cuscatlán reconoció a AES El Salvador y a Holcim por su apuesta por la sostenibilidad energética del país, a través de la construcción de un nuevo parque solar fotovoltaico de 21.4 MW, ubicado en la planta de Holcim “El Ronco”, en el Municipio de Metapán. La construcción del proyecto será posible gracias al financiamiento de US$ 14.8 millones, otorgado por el Banco Cuscatlán a AES. … El nuevo parque estará conformado por tres plantas solares que en conjunto generarán 21.4 MW de energía renovable, de los cuales 17 MW serán destinados al suministro energético de Holcim",
    "https://www.aes-elsalvador.com/es/press-release/aes-recibe-reconocimiento-de-banco-cuscatlan-por-impulsar-la-sostenibilidad",
    "Actor: AES El Salvador (U.S. HQ parent) — us. Company Spanish primary for 21.4 MW park + USD 14.8m Banco Cuscatlán financing. Value = financing figure on primary (not unverified total CapEx).",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='AES El Salvador. “AES recibe reconocimiento de Banco Cuscatlán por impulsar la sostenibilidad energética.” March 14, 2023. https://www.aes-elsalvador.com/es/press-release/aes-recibe-reconocimiento-de-banco-cuscatlan-por-impulsar-la-sostenibilidad.',
    annotation="AES El Salvador primary: El Ronco 21.4 MW / Banco Cuscatlán USD 14.8m. Supports aes_holcim_el_ronco_21p4mw_2023.",
    evid_note="Opened AES El Salvador Spanish 14 Mar 2023 (El Ronco 21.4 MW; USD 14.8m financing).",
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
    print(f"Cycle 158 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
