#!/usr/bin/env python3
"""Cycle 130 hunt: shuffle_seed=20261130; equal budget; U.S./PRC split; thin after.

Order: copper, nickel, bridges_roads, niobium, lithium, balsa, fission_smr,
port_ownership, water, rail, wind, power_plants_grid, other_renewables,
engineering_epc, solar, graphite, port_cranes, building_materials.

Holdovers from C96/C97 + CMEC Lima water primary.
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
        fx_usd = "1" if value_usd else ""
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


# 1. water / prc — CMEC Lima Three Districts
row_doc(
    "cmec_lima_three_districts_water_2025",
    "resources",
    "water",
    "prc",
    "CMEC — Lima Three Districts Water Project (first drainage section handover)",
    "Peru",
    "1 Sep 2025 Sinomach/CMEC: Lima Three Districts Water Project reaches major milestone — first handover section (324-block drainage) passes acceptance and is delivered to the client; covers ~1 km² including household connections for 4,579 households, 423 new sewer manholes, and primary/secondary drainage upgrades; project to serve >400,000 low- and middle-income residents. CapEx USD not disclosed on opened Sinomach page. Distinct from CRSEG Barbados / PowerChina Barbados water rows.",
    "",
    "",
    "2025",
    "-12.046",
    "-77.043",
    "Lima Three Districts Water Project drainage section, Lima, Peru (CMEC geography; approximate Lima pin).",
    "sinomach_cmec_lima_water_20250901",
    "The Lima Three Districts Water Project, undertaken by CMEC, has reached a major milestone. The first handover section — the 324-block drainage project — has successfully passed acceptance and was officially delivered to the client",
    "https://www.sinomach.com.cn/en/MediaCenter/News/202509/t20250905_576128.html",
    "Actor: China National Machinery Engineering Corporation / CMEC (PRC SOE) — prc. Sinomach English primary. CapEx blank.",
    "hunt_res_water",
    investment_type="epc",
    bib_type="company",
    chicago="Sinomach / China National Machinery Engineering Corporation (CMEC). “CMEC projects deliver benefits to local communities.” 1 September 2025. https://www.sinomach.com.cn/en/MediaCenter/News/202509/t20250905_576128.html.",
    annotation="Sinomach/CMEC English primary on Lima Three Districts water handover. Supports cmec_lima_three_districts_water_2025.",
)

# 2. rail / allied — Alstom Panama Metro maintenance
row_doc(
    "alstom_panama_metro_maint_90m_2026",
    "infrastructure",
    "rail",
    "allied",
    "Alstom — Panama Metro Lines 1–2 long-term Metropolis maintenance (USD 90m)",
    "Panama",
    "24 Sep 2026 Alstom: signs USD 90 million (~EUR 80m) contract with Metro de Panamá S.A. for long-term maintenance of 235 Metropolis cars on Lines 1 and 2; scheduled interventions at 5/6/8/10/12-year intervals covering bogies, traction, brakes, pneumatics, wheels, auxiliaries. Distinct from prior Alstom train supply for Lines 1–2.",
    "90000000",
    "2026-09-24",
    "2026",
    "8.982",
    "-79.520",
    "Panama Metro Lines 1–2 fleet maintenance, Panama City (Alstom geography; approximate pin).",
    "alstom_panama_metro_maint_20260924",
    "Alstom… has signed a US$90 million contract (approximately 80 million euro) with Metro de Panamá S.A. (MPSA) to provide long-term maintenance services for the Metropolis trains operating on Lines 1 and 2… Covering 235 metro cars",
    "https://www.alstom.com/press-releases-news/2026/9/alstom-signs-contract-long-term-maintenance-panama-metro",
    "Actor: Alstom (France) — allied; counterparty Metro de Panamá. Company English press.",
    "hunt_latam_rail_telecom",
    investment_type="epc",
    bib_type="company",
    chicago="Alstom. “Alstom signs contract for long-term maintenance of the Panama Metro.” 24 September 2026. https://www.alstom.com/press-releases-news/2026/9/alstom-signs-contract-long-term-maintenance-panama-metro.",
    annotation="Alstom primary: USD 90m Panama Metro Lines 1–2 maintenance. Supports alstom_panama_metro_maint_90m_2026.",
)

# 3. other_renewables / us — Tesla Genera PR BESS
row_doc(
    "tesla_genera_pr_bess_430mw_2025",
    "energy",
    "other_renewables",
    "us",
    "Tesla / Genera PR — 430 MW Megapack BESS (FEMA/CDBG-DR USD 767m)",
    "Puerto Rico",
    "29 Jan 2026 PRFAA: Governor González-Colón / Genera PR announce construction progress on island BESS; Feb 2025 Genera PR and Tesla contracted Megapacks at Cambalache (Arecibo), Vega Baja, Palo Seco (Toa Baja), Yabucoa (Humacao), Aguirre (Salinas), and Costa Sur (Guayanilla) totaling 430 MW; federal investment USD 767 million ($533.5m equipment + $235.7m installation); $404.7m of equipment funds already disbursed/reimbursed FEMA 90% / CDBG-DR 10%. Distinct from Pattern Amanecer DOE EDF and AES Marahu LPO packages.",
    "767000000",
    "2025-02-01",
    "2025",
    "18.444",
    "-66.388",
    "Multi-site Genera PR Tesla Megapack BESS (Cambalache/Vega Baja/Palo Seco/Yabucoa/Aguirre/Costa Sur); Arecibo approximate pin.",
    "prfaa_tesla_genera_bess_20260129",
    "In February 2025, Genera PR and Tesla entered a contract for the installation of Megapacks at the Cambalache (Arecibo), Vega Baja, Palo Seco (Toa Baja), Yabucoa (Humacao), Aguirre (Salinas), and Costa Sur (Guayanilla) power plants, adding a total of 430 MW of energy storage capacity… The total federal investment for the island-wide project amounts to $767 million",
    "https://www.prfaa.pr.gov/recent-press-releases/governor-gonzalez-colon-administration-advances-initiatives-to-reduce-load-shedding-and-increase-energy-reserves",
    "Actor: Tesla (U.S.) equipment + Genera PR operator — us; FEMA/CDBG-DR financing. Official PRFAA English primary.",
    "hunt_energy_other_renewables",
    investment_type="greenfield_storage",
    bib_type="government",
    chicago="Puerto Rico Federal Affairs Administration. “Governor González-Colón Administration Advances Initiatives to Reduce Load Shedding and Increase Energy Reserves.” 29 January 2026. https://www.prfaa.pr.gov/recent-press-releases/governor-gonzalez-colon-administration-advances-initiatives-to-reduce-load-shedding-and-increase-energy-reserves.",
    annotation="PRFAA primary: Tesla/Genera 430 MW BESS / USD 767m federal. Supports tesla_genera_pr_bess_430mw_2025.",
)

# 4. solar / us — Convergent DOE LPO
row_doc(
    "convergent_doe_lpo_584m_pr_2025",
    "energy",
    "solar",
    "us",
    "Convergent Energy and Power — DOE LPO USD 584.5m solar+storage (Coamo / Caguas / Peñuelas / Ponce)",
    "Puerto Rico",
    "17 Jan 2025 Convergent: closes USD 584.5 million DOE LPO guaranteed loan facility ($559.4m principal + $25.1m capitalized interest) for 100 MW solar PV + 55 MW/55 MWh BESS in Coamo plus three stand-alone BESS in Caguas, Peñuelas, and Ponce. Distinct from AES Marahu and Pattern Amanecer DOE packages.",
    "584500000",
    "2025-01-17",
    "2025",
    "18.080",
    "-66.358",
    "Coamo solar+storage and Caguas/Peñuelas/Ponce BESS sites, Puerto Rico (Convergent geography; Coamo approximate pin).",
    "convergent_doe_lpo_20250117",
    "Convergent Energy and Power… announced the closing of its $584.5 million guaranteed loan facility from the U.S. Department of Energy (DOE) Loan Programs Office (LPO) to build a solar photovoltaic (PV) system with an integrated battery storage system and three stand-alone battery storage systems across Puerto Rico… Coamo will be a 100 MW solar PV system paired with a 55 MW/55 MWh battery",
    "https://convergentep.com/news/convergent-energy-and-power-closes-584-5-million-guaranteed-loan-from-the-u-s-department-of-energy",
    "Actor: Convergent Energy and Power (U.S.) — us; DOE LPO lender. Company English primary.",
    "hunt_energy_solar",
    investment_type="greenfield_generation",
    bib_type="company",
    chicago="Convergent Energy and Power. “Convergent Energy and Power Closes $584.5 Million Guaranteed Loan from the U.S. Department of Energy.” 17 January 2025. https://convergentep.com/news/convergent-energy-and-power-closes-584-5-million-guaranteed-loan-from-the-u-s-department-of-energy.",
    annotation="Convergent company primary: USD 584.5m DOE LPO solar+storage PR. Supports convergent_doe_lpo_584m_pr_2025.",
)

# 5. port_cranes / allied — Liebherr Antigua (proxy)
row_doc(
    "liebherr_antigua_lhm420_2025",
    "infrastructure",
    "port_cranes",
    "allied",
    "Liebherr — LHM 420 MHC for Antigua and Barbuda Port Authority (St. John’s)",
    "Antigua and Barbuda",
    "25 Sep 2025 Antigua News Room summarizing Cabinet briefing: Government procured Liebherr LHM 420 mobile harbour crane for Antigua and Barbuda Port Authority at USD 6.2 million; arrival/assembly at St. John’s Port with German engineer commissioning team. UNVERIFIED proxy (cabinet briefing via local press; CapEx from press).",
    "6200000",
    "2025-09-25",
    "2025",
    "17.122",
    "-61.850",
    "St. John’s / Deep Water Harbour, Antigua and Barbuda (press geography; approximate pin).",
    "anr_liebherr_antigua_lhm420_20250925",
    "Government recently procured the Liebherr LHM 420 for the Antigua and Barbuda Port Authority at a cost of US$6.2 million",
    "https://antiguanewsroom.com/cabinet-briefed-on-arrival-of-new-liebherr-mobile-harbour-crane/",
    "Actor: Liebherr (Germany/Switzerland) equipment — allied; buyer Antigua and Barbuda Port Authority. UNVERIFIED proxy: local press summarizing Cabinet briefing.",
    "hunt_infra_port_cranes",
    investment_type="equipment_supply",
    evidence="proxy",
    bib_type="press",
    chicago="Antigua News Room. “Cabinet Briefed on Arrival of New Liebherr Mobile Harbour Crane.” 25 September 2025. https://antiguanewsroom.com/cabinet-briefed-on-arrival-of-new-liebherr-mobile-harbour-crane/.",
    annotation="UNVERIFIED proxy press on Cabinet briefing of Liebherr LHM 420 / USD 6.2m. Supports liebherr_antigua_lhm420_2025.",
)

# 6. engineering_epc / us — Jose Carro Morovis National Cemetery
row_doc(
    "jose_carro_morovis_cemetery_2018",
    "infrastructure",
    "engineering_epc",
    "us",
    "Construcciones Jose Carro, S.E. — VA Morovis National Cemetery construction",
    "Puerto Rico",
    "29 Oct 2018: Department of Veterans Affairs awards contract 36C10F19C3371 to Construcciones Jose Carro, S.E. for construction of Morovis National Cemetery; obligated USD 68,585,227.27; place of performance Morovis, Puerto Rico. Distinct from Jose Carro Arecibo FHWA Branch 2 package.",
    "68585227.27",
    "2018-10-29",
    "2018",
    "18.327",
    "-66.407",
    "Morovis National Cemetery, Morovis Municipality, Puerto Rico (USASpending PoP Morovis).",
    "usaspending_jose_carro_morovis_20181029",
    "CONSTRUCTION OF MOROVIS NATIONAL CEMETERY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_36C10F19C3371_3600_-NONE-_-NONE-/",
    "Actor: Construcciones Jose Carro, S.E. (Puerto Rico / U.S.) under VA — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
    investment_type="epc",
    bib_type="government",
    chicago="U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_36C10F19C3371_3600_-NONE-_-NONE- to Construcciones Jose Carro, S.E. for Morovis National Cemetery. Signed 2018-10-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_36C10F19C3371_3600_-NONE-_-NONE-/.",
    annotation="USASpending primary. Supports jose_carro_morovis_cemetery_2018.",
    evid_note="Opened USASpending Award API; USD 68585227.27; date_signed 2018-10-29.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]].update(entry)
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

    hunt_updates = {
        "hunt_res_copper": "Cycle 130: equal budget; CMOC dense (miss).",
        "hunt_res_nickel": "Cycle 130: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 130: equal budget; FHWA/CRBC dense (miss).",
        "hunt_fenb_araxa": "Cycle 130: equal budget; CBMM dense (miss).",
        "hunt_res_lithium": "Cycle 130: equal budget; Ganfeng dense (miss).",
        "hunt_res_balsa": "Cycle 130: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_energy_fission_smr": "Cycle 130: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_infra_port_ownership": "Cycle 130: equal budget; COSCO/APM dense (miss).",
        "hunt_res_water": "Cycle 130: logged cmec_lima_three_districts_water_2025.",
        "hunt_latam_rail_telecom": "Cycle 130: logged alstom_panama_metro_maint_90m_2026.",
        "hunt_energy_wind": "Cycle 130: equal budget; Windey/Vergnet just logged C129 (miss).",
        "hunt_br_power_equip": "Cycle 130: equal budget; grid EPC dense (miss).",
        "hunt_energy_other_renewables": "Cycle 130: logged tesla_genera_pr_bess_430mw_2025.",
        "hunt_infra_engineering_epc": "Cycle 130: logged jose_carro_morovis_cemetery_2018.",
        "hunt_energy_solar": "Cycle 130: logged convergent_doe_lpo_584m_pr_2025.",
        "hunt_res_graphite": "Cycle 130: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 130: logged liebherr_antigua_lhm420_2025 (proxy).",
        "hunt_infra_building_materials": "Cycle 130: equal budget; Caribbean Lumber dense (miss).",
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
    print("Cycle 130 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
