#!/usr/bin/env python3
"""Cycle 92 hunt: shuffle_seed=20261092; equal budget; U.S./PRC split; thin after.

Order: lithium, engineering_epc, copper, solar, niobium, port_cranes, nickel,
building_materials, fission_smr, other_renewables, bridges_roads,
power_plants_grid, balsa, wind, graphite, water, port_ownership, rail.
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
# energy/power_plants_grid — CTDC / Atabey Project Hostos HVDC+CCGT (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ctdc_hostos_hvdc_dr_pr_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Caribbean Transmission Development Company / Atabey Capital — Project Hostos (DR–PR HVDC)",
        "country": "Dominican Republic",
        "asset": "27 Feb 2026: CTDC receives U.S. DOE Presidential Permit for Project Hostos — privately financed ~USD 2.5 billion corridor: 500 MW combined-cycle plant at San Pedro de Macorís (DR), 90 km 345 kV AC overhead, 150 km subsea 320 kV HVDC across Mona Passage, Mayagüez landing to Mayagüez Substation; COD targeted 2031; Siemens Energy OEM for plant + converters (allied, not dual-sided). Distinct from Lindsayca Manzanillo Block 2.",
        "investment_type": "greenfield_plant",
        "value": "2500000000",
        "currency": "USD",
        "value_usd": "2500000000",
        "fx_usd": "1",
        "fx_date": "2026-02-27",
        "year": "2026",
        "status": "active",
        "lat": "18.45",
        "lon": "-69.30",
        "geo_note": "San Pedro de Macorís combined-cycle plant site (CTDC/PR Newswire geography; approximate pin).",
        "evidence": "documented",
        "source_id": "ctdc_hostos_permit_20260227",
        "note": "Actor: CTDC founding investor Atabey Capital (Puerto Rico / U.S. territory) — us. Company PR Newswire 27 Feb 2026 states USD 2.5bn total project cost and DOE Presidential Permit. Siemens Energy is allied OEM not dual-tagged.",
    },
    {
        "id": "ctdc_hostos_hvdc_dr_pr_2026",
        "retrieved": "2026-10-02",
        "source_id": "ctdc_hostos_permit_20260227",
        "url": "https://www.prnewswire.com/news-releases/caribbean-transmission-secures-us-presidential-permit-for-hostos-energy-interconnection-between-the-dominican-republic-and-puerto-rico-302699653.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Caribbean Transmission Development Company (CTDC) today announced it has received the Presidential Permit from the U.S. Department of Energy for Project Hostos … The total project cost of $2.5 billion is allocated across key components: 500MW combined-cycle power plant … 150 km of subsea 320kv HVDC transmission line",
        "note": "Opened CTDC PR Newswire naming Presidential Permit, USD 2.5bn cost, San Pedro de Macorís plant, and Atabey Capital as founding investor.",
    },
    {
        "id": "ctdc_hostos_permit_20260227",
        "type": "company",
        "chicago": "Caribbean Transmission Development Company. “Caribbean Transmission Secures U.S. Presidential Permit for Hostos Energy Interconnection Between the Dominican Republic and Puerto Rico.” PR Newswire, 27 February 2026.",
        "url": "https://www.prnewswire.com/news-releases/caribbean-transmission-secures-us-presidential-permit-for-hostos-energy-interconnection-between-the-dominican-republic-and-puerto-rico-302699653.html",
        "annotation": "CTDC/Atabey primary: DOE Presidential Permit; USD 2.5bn Hostos CCGT+HVDC corridor DR–PR. Supports ctdc_hostos_hvdc_dr_pr_2026.",
        "supports": ["ctdc_hostos_hvdc_dr_pr_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — CHEXIM–BNDES bilateral fund (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "chexim_bndes_fund_600m_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "prc",
        "counterpart": "Export-Import Bank of China (CEXIM) — Brazil bilateral investment fund with BNDES",
        "country": "Brazil",
        "asset": "Oct 2025: BNDES and CEXIM structure a bilateral investment fund targeting up to USD 1 billion for Brazilian capital-markets investments (debt securities and equity stakes), with intended CEXIM contribution ~USD 600 million and BNDES ~USD 400 million; ops targeted 2026; priority sectors cited as mining and infrastructure (also energy transition / agriculture / AI). MoU/commitment term signed Sep 2025. Fund-level financing presence — no single named plant pin.",
        "investment_type": "financing",
        "value": "600000000",
        "currency": "USD",
        "value_usd": "600000000",
        "fx_usd": "1",
        "fx_date": "2025-10-06",
        "year": "2025",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Nationwide Brazil fund (no single named site on opened CNN Brasil / BNDES-confirmed figures).",
        "evidence": "proxy",
        "source_id": "cnnbrasil_chexim_bndes_20251006",
        "note": "Actor: CEXIM (PRC policy bank) — prc. UNVERIFIED proxy: CNN Brasil 6 Oct 2025 cites BNDES confirmation of CEXIM ~USD 600m / BNDES ~USD 400m; BNDES Agência primary offline (electoral blackout). Value = CEXIM intended contribution only (not dual-entered BNDES share).",
    },
    {
        "id": "chexim_bndes_fund_600m_2025",
        "retrieved": "2026-10-02",
        "source_id": "cnnbrasil_chexim_bndes_20251006",
        "url": "https://www.cnnbrasil.com.br/economia/macroeconomia/bndes-e-banco-chines-avancam-em-fundo-de-investimentos-bilionario/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "O BNDES … e o CEXIM … concordaram em criar um fundo bilateral de investimentos que deve atingir cerca de US$ 1 bilhão em aportes. A informação foi confirmada pelo BNDES. Segundo o banco, a proposta é que o CEXIM aporte cerca de US$ 600 milhões e o BNDES contribua com aproximadamente US$ 400 milhões.",
        "note": "Opened CNN Brasil citing BNDES confirmation of CEXIM ~USD 600m bilateral fund; BNDES Agência archive offline during electoral blackout.",
    },
    {
        "id": "cnnbrasil_chexim_bndes_20251006",
        "type": "press",
        "chicago": "Garcia, Gabriel. “BNDES e banco chinês avançam em fundo de investimentos bilionário.” CNN Brasil, 6 October 2025.",
        "url": "https://www.cnnbrasil.com.br/economia/macroeconomia/bndes-e-banco-chines-avancam-em-fundo-de-investimentos-bilionario/",
        "annotation": "UNVERIFIED proxy confirming BNDES+CEXIM up to USD 1bn fund with CEXIM ~USD 600m. Supports chexim_bndes_fund_600m_2025.",
        "supports": ["chexim_bndes_fund_600m_2025", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# energy/wind — Goldwind Brazil TSI Parque Eólico Jacobina 02/03/04 (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "goldwind_jacobina_02_04_tsi_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "Goldwind Brazil — turbine supply & installation Jacobina 02/03/04",
        "country": "Brazil",
        "asset": "15 Aug 2025 (SZSE/cninfo 19 Aug): Goldwind Equipamentos e Soluções em Energia Renovável Ltda. signs turbine supply-and-installation agreements with Parque Eólico Jacobina 02, 03, and 04 S.A. (supply, inland transport, erection, commissioning, warranty). Parent Goldwind International issues parent guarantees totaling USD 48,500,393.76 + BRL 190,826,090.46 (guarantees ≠ CapEx — leave contract value blank). Warranty end ~Feb 2031. Distinct from Goldwind Jacobina tower-factory reactivation and EDF Diana Jacobina farm.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-11.18",
        "lon": "-40.51",
        "geo_note": "Jacobina wind complex, Bahia (company/project geography; approximate pin).",
        "evidence": "documented",
        "source_id": "goldwind_szse_jacobina0204_20250819",
        "note": "Actor: Goldwind (PRC; SZSE 002202) via Goldwind Brazil — prc. Official cninfo/SZSE parent-guarantee notice discloses TSI contracts; guarantee face amounts are not CapEx.",
    },
    {
        "id": "goldwind_jacobina_02_04_tsi_2025",
        "retrieved": "2026-10-02",
        "source_id": "goldwind_szse_jacobina0204_20250819",
        "url": "http://static.cninfo.com.cn/finalpage/2025-08-19/1224502733.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "金风巴西与PARQUE EÓLICO JACOBINA 02 S.A.…JACOBINA 03…JACOBINA 04 S.A.…分别签署《风机供货和安装协议》…担保金额均为16,166,797.92美元及63,608,696.82雷亚尔，总计为48,500,393.76美元及190,826,090.46雷亚尔",
        "note": "Opened Goldwind SZSE/cninfo PDF naming Jacobina 02/03/04 TSI contracts and parent-guarantee totals.",
    },
    {
        "id": "goldwind_szse_jacobina0204_20250819",
        "type": "regulator",
        "chicago": "Goldwind Science & Technology Co., Ltd. “关于全资子公司金风国际为全资子公司金风巴西提供担保的公告.” SZSE / cninfo announcement 2025-061, 19 August 2025.",
        "url": "http://static.cninfo.com.cn/finalpage/2025-08-19/1224502733.pdf",
        "annotation": "Official Goldwind filing: TSI contracts for Parque Eólico Jacobina 02/03/04; parent guarantees. Supports goldwind_jacobina_02_04_tsi_2025.",
        "supports": ["goldwind_jacobina_02_04_tsi_2025", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# energy/wind — Goldwind Brazil TSI Parque Eólico Jacobina 05 (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "goldwind_jacobina_05_tsi_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "Goldwind Brazil — turbine supply & installation Jacobina 05",
        "country": "Brazil",
        "asset": "16 Mar 2026 (SZSE/cninfo 18 Mar): Goldwind Brazil signs turbine supply-and-installation agreement with Parque Eólico Jacobina 05 S.A.; Goldwind International parent guarantee ~CNY 162,462,530.94 (guarantee ≠ CapEx — leave contract value blank); warranty end including extension ~Feb 2031. Distinct from Jacobina 02–04 TSI row and Jacobina tower-factory reactivation.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "CNY",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-11.18",
        "lon": "-40.51",
        "geo_note": "Jacobina wind complex, Bahia (company/project geography; approximate pin).",
        "evidence": "documented",
        "source_id": "goldwind_szse_jacobina05_20260318",
        "note": "Actor: Goldwind (PRC) — prc. Official cninfo/SZSE parent-guarantee notice; CNY guarantee face is not CapEx.",
    },
    {
        "id": "goldwind_jacobina_05_tsi_2026",
        "retrieved": "2026-10-02",
        "source_id": "goldwind_szse_jacobina05_20260318",
        "url": "http://static.cninfo.com.cn/finalpage/2026-03-18/1225014289.PDF",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "金风巴西与PARQUE EÓLICO JACOBINA 05 S.A.签署《风机供货和安装协议》…担保金额折合人民币约162,462,530.94元…签署日期为2026年3月16日",
        "note": "Opened Goldwind SZSE/cninfo PDF naming Jacobina 05 TSI and ~CNY 162.46m parent guarantee.",
    },
    {
        "id": "goldwind_szse_jacobina05_20260318",
        "type": "regulator",
        "chicago": "Goldwind Science & Technology Co., Ltd. “关于全资子公司金风国际为全资子公司金风巴西提供担保的公告.” SZSE / cninfo announcement 2026-021, 18 March 2026.",
        "url": "http://static.cninfo.com.cn/finalpage/2026-03-18/1225014289.PDF",
        "annotation": "Official Goldwind filing: TSI contract for Parque Eólico Jacobina 05; parent guarantee ~CNY 162.46m. Supports goldwind_jacobina_05_tsi_2026.",
        "supports": ["goldwind_jacobina_05_tsi_2026", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/rail — Wabtec C30ACi for TRANSAP Chile (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "wabtec_transap_c30aci_chile_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "us",
        "counterpart": "Wabtec — four C30ACi locomotives for TRANSAP (Chile)",
        "country": "Chile",
        "asset": "23 Jan 2025: Wabtec finalizes order from TRANSAP for four C30ACi AC-traction locomotives — first AC units in TRANSAP fleet; to haul ARAUCO freight on EFE network; deliveries expected 2026. CapEx USD not disclosed.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-33.45",
        "lon": "-70.66",
        "geo_note": "TRANSAP / EFE Chile freight network (company geography; Santiago process pin).",
        "evidence": "documented",
        "source_id": "wabtec_transap_20250123",
        "note": "Actor: Wabtec Corporation (U.S.; NYSE:WAB) — us. Company primary. Distinct from Wabtec Vale / MRS / Progress Rail VLI rows.",
    },
    {
        "id": "wabtec_transap_c30aci_chile_2025",
        "retrieved": "2026-10-02",
        "source_id": "wabtec_transap_20250123",
        "url": "https://www.wabteccorp.com/newsroom/press-releases/wabtec-finalizes-locomotive-order-with-transap",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Wabtec Corporation (NYSE: WAB) announced today that TRANSAP, a leading rail-based logistics company in Chile, ordered four of its advanced C30ACi locomotives. … Wabtec is expected to deliver the new locomotives in 2026.",
        "note": "Opened Wabtec primary naming TRANSAP four-unit C30ACi order for Chile EFE/ARAUCO freight.",
    },
    {
        "id": "wabtec_transap_20250123",
        "type": "company",
        "chicago": "Wabtec Corporation. “Wabtec Finalizes Locomotive Order with TRANSAP.” Newsroom, 23 January 2025.",
        "url": "https://www.wabteccorp.com/newsroom/press-releases/wabtec-finalizes-locomotive-order-with-transap",
        "annotation": "Wabtec primary: four C30ACi locomotives for TRANSAP Chile; 2026 delivery. Supports wabtec_transap_c30aci_chile_2025.",
        "supports": ["wabtec_transap_c30aci_chile_2025", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# energy/solar — Seraphim modules for SPIC-Zuma Santa María / Orejana (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "seraphim_spic_zuma_module_replace_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Seraphim — module replacement supply for SPIC-Zuma Santa María + Orejana",
        "country": "Mexico",
        "asset": "Jul 2025: Seraphim and SPIC-Zuma Energía announce initial 12 MW polycrystalline module supply/installation for replacement at Santa María (Galeana, Chihuahua) and Orejana (Hermosillo, Sonora) solar parks (combined ~344 MW); Seraphim leads supply/installation, SPIC-Zuma operational coordination. CapEx USD not disclosed.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "25.70",
        "lon": "-106.60",
        "geo_note": "Santa María solar park, Galeana, Chihuahua (first-phase shipment site; Orejana Sonora not dual-pinned).",
        "evidence": "documented",
        "source_id": "spic_zuma_seraphim_20250723",
        "note": "Actor: Seraphim Energy Group (PRC) — prc; plant owner SPIC-Zuma (PRC SOE affiliate) — same side. Company SPIC-Zuma English press. CapEx blank.",
    },
    {
        "id": "seraphim_spic_zuma_module_replace_2025",
        "retrieved": "2026-10-02",
        "source_id": "spic_zuma_seraphim_20250723",
        "url": "https://zumaenergia.com/en/press-center-view?id=105",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Seraphim and SPIC-Zuma Energía … have announced the launch of a joint project for the supply and installation of solar modules in … Santa María … and Orejana … This cooperation agreement includes an initial supply of 12MW of solar modules",
        "note": "Opened SPIC-Zuma English press naming Seraphim 12 MW replacement supply at Santa María and Orejana.",
    },
    {
        "id": "spic_zuma_seraphim_20250723",
        "type": "company",
        "chicago": "SPIC-Zuma Energía. “Seraphim and SPIC-Zuma Energía Consolidate Strategic Alliance for Module Replacement in Key Solar Parks in Mexico.” Press center, July 2025.",
        "url": "https://zumaenergia.com/en/press-center-view?id=105",
        "annotation": "SPIC-Zuma primary: Seraphim 12 MW module replacement at Santa María and Orejana. Supports seraphim_spic_zuma_module_replace_2025.",
        "supports": ["seraphim_spic_zuma_module_replace_2025", "hunt_energy_solar"],
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
        "hunt_res_lithium": "Cycle 92: equal budget; Zijin 3Q / Atlas Neves / EXIM Argentina dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 92: logged chexim_bndes_fund_600m_2025 (PRC; ~USD 600m CEXIM fund face; proxy).",
        "hunt_res_copper": "Cycle 92: equal budget; FCX El Abra / Zijin La Arena dense (miss).",
        "hunt_energy_solar": "Cycle 92: logged seraphim_spic_zuma_module_replace_2025 (PRC; 12 MW replacement).",
        "hunt_fenb_araxa": "Cycle 92: equal budget; CMOC / CBMM / St George dense (miss).",
        "hunt_infra_port_cranes": "Cycle 92: equal budget; ZPMC / Kalmar / Konecranes dense (miss).",
        "hunt_res_nickel": "Cycle 92: equal budget; DFC Piauí / Brazilian Nickel dense (miss). Thin top-up dry — shift.",
        "hunt_infra_building_materials": "Cycle 92: equal budget; Holcim / Sinoma dense (miss).",
        "hunt_energy_fission_smr": "Cycle 92: equal budget; USTDA / CAREM / FIRST dense (miss). Thin top-up dry — shift.",
        "hunt_energy_other_renewables": "Cycle 92: equal budget; SolarMax / Stem / Trina BESS already (miss).",
        "hunt_infra_bridges_roads": "Cycle 92: equal budget; CRBC / CHEC / POWERCHINA Catac dense (miss).",
        "hunt_br_power_equip": "Cycle 92: logged ctdc_hostos_hvdc_dr_pr_2026 (U.S.; USD 2.5bn CTDC/Atabey).",
        "hunt_res_balsa": "Cycle 92: equal budget; Plantabal / AIMA dense (miss). Thin top-up dry — shift.",
        "hunt_energy_wind": "Cycle 92: logged goldwind_jacobina_02_04_tsi_2025 + goldwind_jacobina_05_tsi_2026 (PRC TSI; CapEx blank).",
        "hunt_res_graphite": "Cycle 92: equal budget; Graphcoa / South Star dense (miss). Thin top-up dry — shift.",
        "hunt_res_water": "Cycle 92: equal budget; CWE Zapallar / desal dense (miss).",
        "hunt_infra_port_ownership": "Cycle 92: equal budget; COSCO / APM / SSA dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 92: logged wabtec_transap_c30aci_chile_2025 (U.S.; four C30ACi).",
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
    print("Cycle 92 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
