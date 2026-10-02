#!/usr/bin/env python3
"""Cycle 134 hunt: shuffle_seed=20261134; equal budget; U.S./PRC split; thin after.

Order: port_cranes, engineering_epc, wind, building_materials, nickel,
port_ownership, other_renewables, balsa, lithium, water, bridges_roads, rail,
fission_smr, solar, graphite, niobium, copper, power_plants_grid.

PRC push (still slightly behind US). Thin top-up: balsa/graphite/nickel.
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


# 1. wind / prc — Goldwind turbines at Cuba Herradura 1 installation milestone
row_doc(
    "goldwind_herradura1_cuba_51mw_2026",
    "energy",
    "wind",
    "prc",
    "Goldwind — Herradura 1 wind farm turbine supply (Cuba / UNE)",
    "Cuba",
    "May 2026 POWER magazine report on Cuba’s Herradura 1 wind farm (Las Tunas): installation of Chinese Goldwind GW77/1500 turbines underway; original design 34 × 1.5 MW = 51 MW; first phase 22 turbines (~34 MW); complementary substation and maintenance center complete after decade of delays. Distinct from Goldwind Brazil / Chile rows.",
    "",
    "",
    "2026",
    "21.30",
    "-76.70",
    "Herradura 1 wind farm, northern coast Las Tunas Province, Cuba (approximate coastal pin).",
    "powermag_goldwind_herradura1_2026",
    "As originally designed, the project comprises 34 Goldwind GW77/1500 turbines from China—each rated at 1.5 MW with a 76.9-meter rotor diameter—for a combined nameplate capacity of 51 MW.",
    "https://www.powermag.com/cuba-begins-installing-turbines-at-herradura-1-its-largest-wind-farm/",
    "Actor: Goldwind (Beijing HQ) turbine OEM — prc; Cuban state utility developer. CapEx blank (press does not disclose project CapEx). Cross-check Cubadebate/ACN installation milestone (22 turbines / 34 MW first phase).",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    bib_type="press",
    chicago='Pérez Sánchez, Amaury. “Cuba Begins Installing Turbines at Herradura 1, Its Largest Wind Farm.” POWER Magazine, May 18, 2026. https://www.powermag.com/cuba-begins-installing-turbines-at-herradura-1-its-largest-wind-farm/.',
    annotation="Goldwind GW77/1500 named; CapEx blank. Supports goldwind_herradura1_cuba_51mw_2026.",
    evid_note="Opened POWER Magazine article naming Goldwind GW77/1500; Cubadebate cross-check on first-phase installation.",
)

# 2. port_ownership / prc — COFCO STS11 Santos terminal
row_doc(
    "cofco_sts11_santos_port_2023",
    "infrastructure",
    "port_ownership",
    "prc",
    "COFCO International — STS11 agriculture solid-bulk terminal lease (Port of Santos)",
    "Brazil",
    "14 Aug 2023 COFCO International newsroom: groundbreaking for STS11 agriculture terminal at Port of Santos; expands company-owned Brazil port capacity from 3 to 14 million tonnes; operations phased 2025–2026. Cross-checked Brazilian COFCO Stories page (20 Aug 2024): 98,000 m², two dedicated berths, >490,000 t static storage, 480 direct jobs; largest COFCO LatAm export terminal when complete. Distinct from CMPort Açu / other Santos crane rows.",
    "",
    "",
    "2023",
    "-23.95",
    "-46.31",
    "STS11 / Paquetá right bank, Port of Santos, São Paulo, Brazil (approximate quay pin).",
    "cofco_sts11_construction_start_2023",
    "COFCO International has marked the start of construction on the STS11 agriculture terminal at the Port of Santos in Brazil at a groundbreaking ceremony. The new terminal will expand the company’s own port capacity in Brazil from 3 to 14 million tonnes with operations scheduled to commence in phases between 2025 and 2026.",
    "https://www.cofcointernational.com/newsroom/cofco-international-starts-construction-on-santos-port-terminal-expansion/",
    "Actor: COFCO International (PRC SOE trading arm / Geneva-listed group) — prc. CapEx blank on company English primary (press USD 285m / lease R$764.8m figures treated as UNVERIFIED proxies, not stored). Cross-check br.cofcointernational.com STS-11 story.",
    "hunt_infra_port_ownership",
    investment_type="concession",
    bib_type="company",
    chicago='COFCO International. “COFCO International starts construction on Santos port terminal expansion.” Newsroom, August 14, 2023. https://www.cofcointernational.com/newsroom/cofco-international-starts-construction-on-santos-port-terminal-expansion/.',
    annotation="Company construction-start primary; CapEx blank. Supports cofco_sts11_santos_port_2023.",
    evid_note="Opened COFCO International English newsroom construction-start page; Brazilian Stories page cross-check for site specs.",
)

# 3. other_renewables / prc — CWE Rucalhue 90 MW Chile
row_doc(
    "cwe_rucalhue_hydro_chile_90mw_2025",
    "energy",
    "other_renewables",
    "prc",
    "China International Water & Electric (CWE / CCCC) — Rucalhue Hydropower Project",
    "Chile",
    "28 Jul 2025 CWE English release on Rucalhue Hydropower Station (Biobío River, Region VIII): total installed capacity 90 MW; designed average generation 441 million kWh/year; community firewood donation during construction. CWE wholly owned by CCCC. CapEx blank on company primary (press USD 350m UNVERIFIED, not stored). Distinct from CWE Zapallar / other Chile hydro rows.",
    "",
    "",
    "2025",
    "-37.72",
    "-71.93",
    "Rucalhue run-of-river site, Biobío River near Santa Bárbara / Quilaco, Biobío Region, Chile (approximate dam-site pin).",
    "cwe_rucalhue_firewood_2025",
    "Located on the Biobío River in the south-central Region VIII of Chile, the Project has a total installed capacity of 90 MW and is designed to generate an average of 441 million kWh of electricity annually.",
    "https://english.cwe.cn/shzr/shzr/202508/t20250821_276497.html",
    "Actor: CWE (CCCC subsidiary; PRC SOE) — prc. Company English primary opened; CapEx blank (USD 350m press figure UNVERIFIED, not stored).",
    "hunt_energy_other_renewables",
    investment_type="greenfield",
    bib_type="company",
    chicago='China International Water & Electric Corp. “Rucalhue Hydropower Station Project in Chile Donates Winter Firewood to Local Indigenous Community.” July 28, 2025. https://english.cwe.cn/shzr/shzr/202508/t20250821_276497.html.',
    annotation="CWE primary 90 MW / 441 GWh; CapEx blank. Supports cwe_rucalhue_hydro_chile_90mw_2025.",
    evid_note="Opened CWE English CSR/project page confirming 90 MW Rucalhue capacity.",
)

# 4. lithium / prc — Tsingshan Perico electrochemical plant USD 120m
row_doc(
    "tsingshan_perico_jujuy_120m_2026",
    "resources",
    "lithium",
    "prc",
    "Tsingshan South America — Perico Industrial Park electrochemical plant (HCl / NaOH for lithium chain)",
    "Argentina",
    "Tsingshan South America company site: USD 120 million electrochemical plant at Parque Industrial Perico, Jujuy; 100,000 t/y HCl 32% and 35,000 t/y NaOH 98%; mission explicitly supplies northern Argentina lithium industry / Lithium Triangle. Cross-checked Jujuy government press (16 Jan 2026): operational start-up phase with Governor Sadir / Jing Li. Distinct from Eramet Centenario / Ganfeng brine rows.",
    "120000000",
    "2026-01-16",
    "2026",
    "-24.38",
    "-65.12",
    "Parque Industrial Perico, Jujuy, Argentina (approximate industrial-park pin).",
    "tsingshan_south_america_perico",
    "With a total investment of USD 120 million, our electrochemical plant in Jujuy establishes a strategic base for supplying key inputs to the region’s mining, agro-industrial, and manufacturing operations. … Output: 100,000 t/year HCl and 35,000 t/year NaOH",
    "http://www.ts-southamerica.com/",
    "Actor: Tsingshan Group (PRC; Wenzhou HQ) via Tsingshan South America — prc. CapEx USD 120m from opened company site. Lithium-chain chemical inputs supporting brine processing.",
    "hunt_res_lithium",
    investment_type="greenfield",
    bib_type="company",
    chicago='Tsingshan South America. “USD 120M Investment | 100,000 t/y HCl | 35,000 t/y NaOH.” Company site. http://www.ts-southamerica.com/.',
    annotation="Company CapEx USD 120m; Jujuy press COD-phase cross-check. Supports tsingshan_perico_jujuy_120m_2026.",
    evid_note="Opened Tsingshan South America site (USD 120m) and Jujuy government operational-start press.",
)

# 5. copper / prc — Zijin Río Blanco CapEx USD 2,792m (MINEM)
row_doc(
    "zijin_rio_blanco_peru_2792m",
    "resources",
    "copper",
    "prc",
    "Zijin Mining (51%) / Tongling (35%) / Xiamen C&D (14%) — Río Blanco copper-molybdenum mine",
    "Peru",
    "Zijin Mining Key Projects page: Río Blanco Copper-Molybdenum Mine, Piura Region, Peru; Zijin 51% / Tongling 35% / Xiamen C&D 14%; status In Preparation for construction; open-pit porphyry; contained Cu 11.3189 Mt @ 0.47%. CapEx US$ 2,792 million from MINEM Portfolio of Mining Investment Projects 2024 (English) — feasibility stage, operator Río Blanco Copper S.A. Distinct from Zijin La Arena / Tres Quebradas rows.",
    "2792000000",
    "2024-12-19",
    "2024",
    "-5.05",
    "-79.55",
    "Río Blanco project area, Ayabaca / Huancabamba provinces, Piura Region, Peru (approximate concession pin).",
    "minem_cpim_2024_rio_blanco",
    "TBD Rio Blanco Rio Blanco Copper S.A. Piura Copper FEASIBILITY 2792",
    "https://cdn.www.gob.pe/uploads/document/file/6762263/5325671-cpim-2024-english-ver.pdf",
    "Actor: Zijin Mining Group (PRC) controlling 51% — prc. CapEx from opened MINEM CPIM 2024 English PDF (US$ 2792m). Ownership/status cross-checked on opened Zijin Key Projects page (https://www.zijinmining.com/global/program-detail-71780.htm).",
    "hunt_res_copper",
    investment_type="greenfield",
    bib_type="government",
    chicago='Peru Ministry of Energy and Mines (MINEM). Portfolio of Mining Investment Projects 2024 (English). Río Blanco CapEx US$ 2,792 million (feasibility). https://cdn.www.gob.pe/uploads/document/file/6762263/5325671-cpim-2024-english-ver.pdf.',
    annotation="MINEM CapEx US$2792m; Zijin ownership cross-check. Supports zijin_rio_blanco_peru_2792m.",
    evid_note="Opened MINEM CPIM 2024 English PDF (2792) and Zijin Key Projects page (51% ownership).",
)

# 6. copper / prc — Tongling / CRCC Tongguan Mirador Phase II built; COD delayed
row_doc(
    "tongling_mirador_phase2_ecuador_2026",
    "resources",
    "copper",
    "prc",
    "Tongling Nonferrous / China Railway Construction Tongguan (CRCTG) — Mirador Phase II (ECSA)",
    "Ecuador",
    "5 Jan 2026 Tongling Nonferrous cninfo announcement 2026-001: Mirador Phase II (Ecuador) main works started Aug 2023, basically completed May 2025 (22 months); system linkage Jun 2025; heavy-load trials Dec 2025. Phase II adds 26.20 Mt/y ore processing to Phase I 20 Mt/y for combined 46.20 Mt/y (~200 kt/y Cu metal in concentrate). Formal COD awaits Mining Contract signature with Ecuador government (timing uncertain). CapEx blank (feasibility CapEx not restated in this delay notice). Distinct from CMOC Cangrejos.",
    "",
    "",
    "2026",
    "-3.56",
    "-78.43",
    "Mirador mine, Zamora Chinchipe, Ecuador (approximate Phase II / north orebody pin).",
    "tongling_mirador_delay_cninfo_2026",
    "米拉多铜矿二期工程于 2023 年 8 月启动主体工程建设，2025 年 5 月基本建成，用时 22 个月……扩建后米拉多铜矿采选工程对铜矿石的处理能力合计达到 4,620 万吨/年，预计每年产出约 20 万吨铜金属量对应的铜精矿。",
    "http://static.cninfo.com.cn/finalpage/2026-01-05/1224913878.PDF",
    "Actor: Tongling Nonferrous (70% of CRCTG) / CRCC Tongguan (30%) — prc; operator ECSA. Company cninfo primary opened. CapEx blank.",
    "hunt_res_copper",
    investment_type="expansion",
    bib_type="company",
    chicago='Tongling Nonferrous Metals Group Co., Ltd. “关于控股子公司项目延期的公告.” Announcement 2026-001, January 5, 2026. http://static.cninfo.com.cn/finalpage/2026-01-05/1224913878.PDF.',
    annotation="Cninfo primary on Phase II build complete / COD delayed; CapEx blank. Supports tongling_mirador_phase2_ecuador_2026.",
    evid_note="Opened Tongling cninfo PDF 2026-001 (Mirador Phase II completion and contract delay).",
)

# 7. copper / prc — Minmetals / Lumina El Galeno USD 3,500m
row_doc(
    "minmetals_el_galeno_peru_3500m",
    "resources",
    "copper",
    "prc",
    "China Minmetals / Lumina Copper S.A.C. — El Galeno copper project (Cajamarca)",
    "Peru",
    "MINEM Cartera de Proyectos de Inversión Minera 2025 (Oct update): P.D. El Galeno, Lumina Copper S.A.C., Cajamarca, copper, PRE-FACTIBILIDAD, CapEx 3,500 (US$ million). Cross-checked MINEM CPIM 2024 English: China Minmetals among lead Chinese investors with El Galeno US$ 3,500 million. Distinct from Río Blanco / Conga / Yanacocha rows.",
    "3500000000",
    "2025-10-01",
    "2025",
    "-7.05",
    "-78.35",
    "El Galeno concessions, Celendín / La Encañada, Cajamarca, Peru (approximate project pin).",
    "minem_cpim_2025_el_galeno",
    "P.D. El Galeno Lumina Copper S.A.C. Cajamarca Cobre PRE-FACTIBILIDAD 3500",
    "https://cdn.www.gob.pe/uploads/document/file/9060040/6722917-cpim-2025-actualizacion-oct.pdf?v=1764185093",
    "Actor: China Minmetals Corporation via Lumina Copper S.A.C. — prc. CapEx US$ 3,500m from opened MINEM CPIM 2025 Oct PDF. Pre-feasibility / greenfield.",
    "hunt_res_copper",
    investment_type="greenfield",
    bib_type="government",
    chicago='Peru Ministry of Energy and Mines (MINEM). Cartera de Proyectos de Inversión Minera 2025 — actualización octubre. El Galeno CapEx US$ 3,500 million. https://cdn.www.gob.pe/uploads/document/file/9060040/6722917-cpim-2025-actualizacion-oct.pdf.',
    annotation="MINEM CapEx US$3500m El Galeno. Supports minmetals_el_galeno_peru_3500m.",
    evid_note="Opened MINEM CPIM 2025 Oct PDF listing El Galeno PRE-FACTIBILIDAD 3500.",
)

# 8. power_plants_grid / us — NFE Puerto Sandino LNG-to-power
row_doc(
    "nfe_puerto_sandino_lng_power_2026",
    "energy",
    "power_plants_grid",
    "us",
    "New Fortress Energy — Puerto Sandino LNG terminal + gas power plant (Nicaragua)",
    "Nicaragua",
    "NFE Form 10-Q for quarter ended 30 Jun 2026 (filed 6 Aug 2026): developing offshore LNG receiving/regas facility at Puerto Sandino plus pipeline to Puerto Sandino Power Plant; 25-year PPA with Nicaragua distributors; ~57,000 MMBtu/day LNG to plant; power plant construction substantially complete; expect to complete terminal and commission both terminal and power plant in first half of 2027. Holdover sandino cleared. CapEx blank (historical press USD 700m UNVERIFIED, not stored). Distinct from NFE CELBA2 / Barcarena rows.",
    "",
    "",
    "2026",
    "12.20",
    "-86.76",
    "Puerto Sandino, León Department, Nicaragua (approximate terminal/power-plant complex pin).",
    "nfe_10q_2026q2_sandino",
    "We are developing an offshore liquefied natural gas receiving, transloading and regasification facility in Puerto Sandino, Nicaragua, as well as a pipeline connecting the facility with our Puerto Sandino Power Plant. We have entered into a 25-year PPA with Nicaragua’s electricity distribution companies, and we expect to utilize approximately 57,000 MMBtu from LNG per day to provide natural gas to the Puerto Sandino Power Plant in connection with the 25-year power purchase agreement. Construction of the power plant is substantially complete, and we expect to complete the construction of the terminal and commission both the terminal and the power plant during first half of 2027.",
    "https://www.sec.gov/Archives/edgar/data/1749723/000174972326000106/nfe-20260630.htm",
    "Actor: New Fortress Energy Inc. (NYSE: NFE; U.S. HQ) — us. CapEx blank on 10-Q. Clears sandino holdover.",
    "hunt_energy_power_plants_grid",
    investment_type="greenfield",
    bib_type="sec",
    chicago='New Fortress Energy Inc. Form 10-Q for the quarterly period ended June 30, 2026. “Puerto Sandino Facility.” https://www.sec.gov/Archives/edgar/data/1749723/000174972326000106/nfe-20260630.htm.',
    annotation="SEC 10-Q primary on Sandino LNG+power; CapEx blank. Supports nfe_puerto_sandino_lng_power_2026.",
    evid_note="Opened NFE 10-Q (period ended 2026-06-30) Puerto Sandino Facility section.",
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
    print(f"Cycle 134 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
