#!/usr/bin/env python3
"""Cycle 93 hunt: shuffle_seed=20261093; equal budget; U.S./PRC split; thin after.

Order: niobium, water, nickel, building_materials, graphite, solar, rail,
bridges_roads, port_ownership, balsa, engineering_epc, copper, port_cranes,
fission_smr, lithium, power_plants_grid, wind, other_renewables.
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


# ---------------------------------------------------------------------------
# energy/power_plants_grid — Quanta / LUMA distribution IDIQ (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "quanta_luma_dist_525m_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Quanta Services Solutions PR — LUMA/PREPA distribution-grid IDIQ",
        "country": "Puerto Rico",
        "asset": "12 Nov 2025: Financial Oversight and Management Board for Puerto Rico approves (with observations) Indefinite Delivery-Indefinite Quantity contract between LUMA Energy ServCo (as PREPA agent) and Quanta Services Solutions PR, LLC for construction/restoration/rebuild of Puerto Rico’s power distribution system — pole/structure/foundation work, stringing, underground installs, hotline work; max payable USD 525 million; 3-year term + two 1-year extensions; competitive RFP 3PPO-1123-01-DL awarded 23 Sep 2024; entirely federal-funded. Distinct from Hostos HVDC corridor.",
        "investment_type": "epc",
        "value": "525000000",
        "currency": "USD",
        "value_usd": "525000000",
        "fx_usd": "1",
        "fx_date": "2025-11-12",
        "year": "2025",
        "status": "active",
        "lat": "18.47",
        "lon": "-66.11",
        "geo_note": "Puerto Rico island-wide distribution system (San Juan process pin; PREPA/LUMA network).",
        "evidence": "documented",
        "source_id": "fomb_quanta_luma_525m_20251112",
        "note": "Actor: Quanta Services Solutions PR (U.S. Quanta Services affiliate) — us. Official FOMB Contract Review letter 12 Nov 2025 states USD 525m ceiling.",
    },
    {
        "id": "quanta_luma_dist_525m_2025",
        "retrieved": "2026-10-02",
        "source_id": "fomb_quanta_luma_525m_20251112",
        "url": "https://docs.oversightboard.pr.gov/n/id6ek3qs8yrm/b/CR_PUBLIC/o/6809_LUMAandQuantaServices(1123-01DL)(November122025).pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "It has a maximum payable amount of $525,000,000 and a 3-year term from its date of execution, with two allowable one-year extensions. … for the provision of construction, restoration, and rebuilding services in connection with Puerto Rico’s power grid distribution system.",
        "note": "Opened FOMB Contract Review PDF approving Quanta–LUMA IDIQ at USD 525m ceiling.",
    },
    {
        "id": "fomb_quanta_luma_525m_20251112",
        "type": "government",
        "chicago": "Financial Oversight and Management Board for Puerto Rico. Letter to LUMA Energy ServCo re Quanta Services Solutions PR, LLC (RFP No. 3PPO-1123-01-DL). 12 November 2025.",
        "url": "https://docs.oversightboard.pr.gov/n/id6ek3qs8yrm/b/CR_PUBLIC/o/6809_LUMAandQuantaServices(1123-01DL)(November122025).pdf",
        "annotation": "FOMB primary: Quanta PR distribution IDIQ max USD 525m. Supports quanta_luma_dist_525m_2025.",
        "supports": ["quanta_luma_dist_525m_2025", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/port_cranes — ZPMC Kingston Freeport STS (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "zpmc_kingston_sts_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — two post-Panamax STS quay cranes for Kingston Freeport Terminal",
        "country": "Jamaica",
        "asset": "Oct 2025 arrival / Dec 2025 commissioning: Shanghai Zhenhua Heavy Industries (ZPMC) delivers two post-Panamax ship-to-shore quay cranes to Kingston Freeport Terminal Limited (Terminal Link / CMA CGM) — 60 m outreach, handle vessels up to ~15,000 TEU; arrival despite Hurricane Melissa; expected to support terminal throughput toward ~2.5m TEU. CapEx USD not on ZPMC page (press cites ~USD 24m UNVERIFIED — leave blank). Distinct from CHEC Kingston yard Phase I EPC.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "17.98",
        "lon": "-76.82",
        "geo_note": "Kingston Freeport Terminal / Kingston Harbour (ZPMC + JIS geography).",
        "evidence": "documented",
        "source_id": "zpmc_kingston_sts_20251215",
        "note": "Actor: ZPMC (PRC SOE) — prc. Company English primary naming delivery to Kingston Freeport. CapEx blank.",
    },
    {
        "id": "zpmc_kingston_sts_2025",
        "retrieved": "2026-10-02",
        "source_id": "zpmc_kingston_sts_20251215",
        "url": "https://www.zpmc.com/content/693f6faf001ae6510000000d",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Jamaican Prime Minister Andrew Holness recently visited the Kingston Freeport Terminal to inspect two post-Panamax quay cranes delivered by … Shanghai Zhenhua Heavy Industries Co., Ltd. (ZPMC). … The two quay cranes from ZPMC feature a 60-meter outreach that enables them to handle ultra-large container vessels of up to 15,000 TEU.",
        "note": "Opened ZPMC English page naming Kingston Freeport two post-Panamax STS delivery.",
    },
    {
        "id": "zpmc_kingston_sts_20251215",
        "type": "company",
        "chicago": "Shanghai Zhenhua Heavy Industries Co., Ltd. (ZPMC). “Jamaican Prime Minister Praises China-Made Port Equipment.” Company news, 15 December 2025.",
        "url": "https://www.zpmc.com/content/693f6faf001ae6510000000d",
        "annotation": "ZPMC primary: two post-Panamax STS quay cranes at Kingston Freeport. Supports zpmc_kingston_sts_2025.",
        "supports": ["zpmc_kingston_sts_2025", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — CHEC Sucre–Yamparáez highway (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "chec_sucre_yamparaez_bolivia_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "CHEC — Sucre–Yamparáez Highway Project (Bolivia)",
        "country": "Bolivia",
        "asset": "24 May 2025: President Luis Arce launches initial inspection of Sucre–Yamparáez Highway Project with China Harbour Engineering Company (CHEC) as contractor; described as largest infrastructure project in Sucre in 30 years — modernize key urban–rural corridor, improve road safety and connectivity. CapEx USD not disclosed on CHEC Americas page.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.05",
        "lon": "-65.26",
        "geo_note": "Sucre–Yamparáez corridor, Chuquisaca (CHEC Americas geography; approximate mid-corridor pin near Sucre).",
        "evidence": "documented",
        "source_id": "chec_sucre_yamparaez_20250524",
        "note": "Actor: CHEC / CCCC (PRC SOE) — prc. Company Americas English primary. CapEx blank. Distinct from CHEC Jamaica SPARK/SCHIP rows.",
    },
    {
        "id": "chec_sucre_yamparaez_bolivia_2025",
        "retrieved": "2026-10-02",
        "source_id": "chec_sucre_yamparaez_20250524",
        "url": "https://www.checamerica.com/blog/2025/05/24/bolivian-president-launches-inspection-of-sucre-highway-project/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "President Luis Arce of Bolivia presided over the official launch of the initial inspection of the Sucre – Yamparáez Highway Project … reflecting China Harbour Engineering Company’s (CHEC) dedication to delivering high-quality projects",
        "note": "Opened CHEC Americas English blog naming CHEC on Sucre–Yamparáez highway inspection launch.",
    },
    {
        "id": "chec_sucre_yamparaez_20250524",
        "type": "company",
        "chicago": "China Harbour Engineering Company (CHEC Americas). “Bolivian President Launches Inspection of Sucre Highway Project.” Blog, 24 May 2025.",
        "url": "https://www.checamerica.com/blog/2025/05/24/bolivian-president-launches-inspection-of-sucre-highway-project/",
        "annotation": "CHEC Americas primary: Sucre–Yamparáez highway inspection launch. Supports chec_sucre_yamparaez_bolivia_2025.",
        "supports": ["chec_sucre_yamparaez_bolivia_2025", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Huawei BESS for Aggreko Amazonas microgrids (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "huawei_aggreko_amazonas_bess_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Huawei Digital Power — BESS supply for Aggreko Amazonas solar+storage microgrids",
        "country": "Brazil",
        "asset": "2 Mar 2026: Huawei will supply batteries to Aggreko for hybrid solar+BESS microgrids across 24 isolated Amazonas locations (incl. Tefé) totaling ~110 MWp solar + 120 MWh storage to cut diesel thermal generation; project cost ~R$850 million (~USD 165.55m at cited FX) with Axia Energia-linked fund ~R$510m and Aggreko remainder; first plants 2027–2028. Huawei battery contract USD not separately disclosed — leave CapEx blank; total project figure is press-cited.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-3.35",
        "lon": "-64.71",
        "geo_note": "Tefé / Amazonas isolated-systems cluster (Reuters geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "essnews_huawei_aggreko_amazonas_20260303",
        "note": "Actor: Huawei (PRC) battery OEM — prc; Aggreko (UK) developer allied not dual-tagged. UNVERIFIED proxy: ESS News citing company executives; R$850m/~USD 165m is total project not Huawei invoice.",
    },
    {
        "id": "huawei_aggreko_amazonas_bess_2026",
        "retrieved": "2026-10-02",
        "source_id": "essnews_huawei_aggreko_amazonas_20260303",
        "url": "https://www.ess-news.com/2026/03/03/huawei-and-aggreko-win-brazils-largest-battery-storage-contract-will-replace-diesel-in-the-amazon/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A consortium formed by Huawei Digital Power and British company Aggreko is set to deploy the largest integrated battery energy storage system (BESS) in Brazil in the Amazon … 110 MWp of photovoltaic plants and 120 MWh of battery capacity distributed across 24 locations, including mid-sized municipalities such as Tefé. Total investment is estimated at $165 million (Brazilian R$850 million)",
        "note": "Opened ESS News (English) naming Huawei Digital Power BESS supply with Aggreko for Amazonas microgrids; Reuters blocked in-session.",
    },
    {
        "id": "essnews_huawei_aggreko_amazonas_20260303",
        "type": "press",
        "chicago": "Neris, Alessandra. “Huawei and Aggreko Win Brazil’s Largest Battery Storage Contract, Will Replace Diesel in the Amazon.” ESS News, 3 March 2026.",
        "url": "https://www.ess-news.com/2026/03/03/huawei-and-aggreko-win-brazils-largest-battery-storage-contract-will-replace-diesel-in-the-amazon/",
        "annotation": "UNVERIFIED proxy: Huawei BESS supply to Aggreko Amazonas microgrids; ~R$850m/~USD 165m project. Supports huawei_aggreko_amazonas_bess_2026.",
        "supports": ["huawei_aggreko_amazonas_bess_2026", "hunt_energy_other_renewables"],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]] = entry
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8"))
    assert isinstance(bib, list)
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
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

    hunt_updates = {
        "hunt_fenb_araxa": "Cycle 93: equal budget; CMOC / CBMM dense (miss). Thin niobium dry after fission/balsa/graphite.",
        "hunt_res_water": "Cycle 93: equal budget; CWE Zapallar / desal / Techint SADDN dense (miss).",
        "hunt_res_nickel": "Cycle 93: equal budget; BRN DFC / Westwin / BNDES already (miss). Thin top-up dry — shift.",
        "hunt_infra_building_materials": "Cycle 93: equal budget; Sinoma Cibao / Cruz Azul / Panam dense (miss).",
        "hunt_res_graphite": "Cycle 93: equal budget; Graphcoa / South Star dense (miss). Thin top-up dry — shift.",
        "hunt_energy_solar": "Cycle 93: equal budget; Seraphim / Array / Nextracker already (miss).",
        "hunt_latam_rail_telecom": "Cycle 93: equal budget; Wabtec TRANSAP / Vale / Progress Rail already (miss).",
        "hunt_infra_bridges_roads": "Cycle 93: logged chec_sucre_yamparaez_bolivia_2025 (PRC; CapEx blank).",
        "hunt_infra_port_ownership": "Cycle 93: equal budget; COSCO / APM / SSA dense (miss).",
        "hunt_res_balsa": "Cycle 93: equal budget; Plantabal / AIMA dense (miss). Thin top-up dry — shift.",
        "hunt_infra_engineering_epc": "Cycle 93: equal budget; CHEXIM–BNDES / Bechtel / CBI already (miss).",
        "hunt_res_copper": "Cycle 93: equal budget; FCX El Abra / Orion Santo Domingo dense (miss).",
        "hunt_infra_port_cranes": "Cycle 93: logged zpmc_kingston_sts_2025 (PRC; two post-Panamax STS).",
        "hunt_energy_fission_smr": "Cycle 93: equal budget; USTDA / CAREM / FIRST dense (miss). Thin top-up dry — shift.",
        "hunt_res_lithium": "Cycle 93: equal budget; Zijin / Atlas / EXIM / PPG dense (miss).",
        "hunt_br_power_equip": "Cycle 93: logged quanta_luma_dist_525m_2025 (U.S.; USD 525m FOMB).",
        "hunt_energy_wind": "Cycle 93: equal budget; Goldwind Jacobina / Envision / Vestas dense (miss).",
        "hunt_energy_other_renewables": "Cycle 93: logged huawei_aggreko_amazonas_bess_2026 (PRC; proxy Reuters).",
    }
    for hid, note in hunt_updates.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
            ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 93 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
