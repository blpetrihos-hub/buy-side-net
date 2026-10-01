#!/usr/bin/env python3
"""Cycle 14 hunt: shuffle_seed=20261014; equal budget across 18 subcategories."""
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


# seed 20261014 order:
# port_ownership, rail, fission_smr, bridges_roads, wind, port_cranes, niobium, balsa,
# solar, graphite, power_plants_grid, copper, nickel, lithium, water, building_materials,
# engineering_epc, other_renewables

# 1 infrastructure/port_ownership — APM Terminals Callao Stage 3B (USD 570m)
A(
    {
        "id": "apm_callao_stage3b_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "APM Terminals Callao — North Terminal Stage 3B modernization",
        "country": "Peru",
        "asset": "Stage 3B expansion of Callao North Multipurpose Terminal: Pier 5C for ULCVs + 3 MalaccaMax quay cranes (OEM unnamed) + container equipment + 16-lane general-cargo gate (2026–2028); three new general-cargo berths (2028–2030); capacity 1.3→1.75m containers and 13.5→18m t general cargo by 2030; UNVERIFIED press USD 570 million citing APM Terminals Callao",
        "investment_type": "concession_capex",
        "value": "570000000",
        "currency": "USD",
        "value_usd": "570000000",
        "fx_usd": "1",
        "fx_date": "2026-07-02",
        "year": "2026",
        "status": "active",
        "lat": "-12.048",
        "lon": "-77.143",
        "geo_note": "Terminal Norte Multipropósito, Port of Callao (DataPortuaria citing APM Terminals Callao).",
        "evidence": "proxy",
        "source_id": "dataportuaria_apm_callao_stage3b_20260702",
        "note": "Actor: APM Terminals (Maersk/Denmark) — allied. UNVERIFIED proxy: DataPortuaria 2 Jul 2026 reprints APM Callao Stage 3B figures (USD 570m; Pier 5C; 3 MalaccaMax). APM Terminals primary URL unreachable this cycle (HTTP 000). Crane OEM unnamed — coded port_ownership not port_cranes. Distinct from DP World Callao South Bicentennial and APM Suape/Lázaro ownership rows.",
    },
    {
        "id": "apm_callao_stage3b_2026",
        "retrieved": "2026-10-01",
        "source_id": "dataportuaria_apm_callao_stage3b_20260702",
        "url": "https://dataportuaria.com/en/peru/ports/apm-terminals-callao-to-invest-usd-570-million-in-modernizat",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "APM Terminals Callao will begin expansion works on the North Pier of the Port of Callao, set to conclude in 2030, with an investment of USD 570 million. The project will increase annual capacity from 1.3 to 1.75 million containers and from 13.5 to 18 million tons in general cargo. … construction of a new Pier 5C … installation of 3 state-of-the-art and largest MalaccaMax cranes on the market",
        "note": "Opened DataPortuaria English report citing APM Terminals Callao Project Director José Carlos Maia; company primary unreachable this cycle.",
    },
    {
        "id": "dataportuaria_apm_callao_stage3b_20260702",
        "type": "press",
        "chicago": "DataPortuaria. “APM Terminals Callao to invest USD 570 million in modernization until 2030.” 2 July 2026.",
        "url": "https://dataportuaria.com/en/peru/ports/apm-terminals-callao-to-invest-usd-570-million-in-modernizat",
        "annotation": "Trade press reprint of APM Callao Stage 3B expansion (primary apmterminals.com unreachable). Supports apm_callao_stage3b_2026 (UNVERIFIED value).",
        "supports": ["apm_callao_stage3b_2026", "hunt_infra_port_ownership"],
    },
)

# 2 infrastructure/rail — miss (PowerChina Chancay–Sierra Central press/IRJ Cloudflare)
# 3 energy/fission_smr — miss (Meitner/FIRST/CAREM/Brazil microreactor already logged)
# 4 infrastructure/bridges_roads — miss (CRBC Arequipa–La Joya logged C13)

# 5 energy/wind — Vestas Esquina do Vento 230 MW (Equinor/Rio Energy)
A(
    {
        "id": "vestas_esquina_do_vento_230mw_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Vestas — Esquina do Vento 230 MW for Equinor / Rio Energy (Rio Grande do Norte)",
        "country": "Brazil",
        "asset": "230 MW Esquina do Vento wind project: supply/install 51 × V163-4.5 MW turbines; install Mar–end 2027; 30-year AOM 5000 service; first Equinor/Rio Energy–Vestas collaboration in Brazil (fully developed by Vestas Energy Solutions)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-5.2",
        "lon": "-36.9",
        "geo_note": "Rio Grande do Norte, northeast Brazil (Vestas company news; approximate RN wind belt).",
        "evidence": "documented",
        "source_id": "vestas_esquina_do_vento_2026",
        "note": "Actor: Vestas (Danish) — allied; customer Equinor/Rio Energy. Company news: 230 MW / 51 V163-4.5 MW; no contract USD on page. Distinct from Vestas Dom Inocêncio / Casa dos Ventos 2023 / Cimarrón / Chile 128 MW rows.",
    },
    {
        "id": "vestas_esquina_do_vento_230mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "vestas_esquina_do_vento_2026",
        "url": "https://www.vestas.com/en/media/company-news/2026/equinor-and-rio-energy-order-vestas-turbines-for-the-23-c4325164",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Equinor and Rio Energy … signs a turbine supply agreement with Vestas for the project, which is located in the state of Rio Grande do Norte, northeast of Brazil. Vestas will supply 51 V163-4.5 MW turbines to the project. Installation of the turbines is expected to begin in March 2027, and all turbines are to be installed by end of 2027. In addition to supplying and installing the turbines, Vestas will also be responsible for operation and maintenance services for 30 years under an Active Output Management 5000 (AOM 5000) service agreement.",
        "note": "Opened Vestas company news page.",
    },
    {
        "id": "vestas_esquina_do_vento_2026",
        "type": "official",
        "chicago": "Vestas. “Equinor and Rio Energy order Vestas turbines for the 230 MW Esquina do Vento Wind Project in Brazil, fully developed by Vestas.” Company news, 2026.",
        "url": "https://www.vestas.com/en/media/company-news/2026/equinor-and-rio-energy-order-vestas-turbines-for-the-23-c4325164",
        "annotation": "Company primary Esquina do Vento turbine order. Supports vestas_esquina_do_vento_230mw_2026.",
        "supports": ["vestas_esquina_do_vento_230mw_2026", "hunt_energy_wind"],
    },
)

# 5b energy/wind — Goldwind Sento Sé 872 MW (Casa dos Ventos)
A(
    {
        "id": "goldwind_sento_se_872mw_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "Goldwind — Sento Sé 872 MW turbine supply for Casa dos Ventos (Bahia)",
        "country": "Brazil",
        "asset": "Definitive agreements for 872 MW Sento Sé wind project (northern Bahia): supply/transport/install/commission 109 × GWH182-8.0 MW turbines + 30-year O&M; company states largest single turbine order volume for Goldwind in Brazil",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-10.46",
        "lon": "-41.59",
        "geo_note": "Sento Sé municipality, northern Bahia (PR Newswire Goldwind/Casa dos Ventos release).",
        "evidence": "documented",
        "source_id": "prnewswire_goldwind_sento_se_20260916",
        "note": "Actor: Goldwind (PRC) — prc; customer Casa dos Ventos. PR Newswire PT 16 Sep 2026. No contract USD on page. Distinct from Goldwind Touros/SPIC, Goldwind Pemuco Chile, and Envision Casa dos Ventos 630 MW rows.",
    },
    {
        "id": "goldwind_sento_se_872mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "prnewswire_goldwind_sento_se_20260916",
        "url": "https://www.prnewswire.com/br/comunicados-para-a-imprensa/goldwind-e-casa-dos-ventos-assinam-acordo-para-o-projeto-eolico-sento-se-de-872-mw-no-brasil-302880123.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "A Goldwind e a Casa dos Ventos … assinaram os acordos definitivos para o projeto eólico Sento Sé, de 872 MW, localizado no norte da Bahia. … a Goldwind se responsabilizará por fornecer, transportar, instalar e colocar em funcionamento 109 turbinas eólicas GWH182-8.0 MW. A Goldwind também oferecerá serviços completos de operação e manutenção por 30 anos",
        "note": "Opened PR Newswire Brazil Goldwind/Casa dos Ventos release.",
    },
    {
        "id": "prnewswire_goldwind_sento_se_20260916",
        "type": "official",
        "chicago": "Goldwind / Casa dos Ventos. “Goldwind e Casa dos Ventos assinam acordo para o projeto eólico Sento Sé, de 872 MW, no Brasil.” PR Newswire, 16 September 2026.",
        "url": "https://www.prnewswire.com/br/comunicados-para-a-imprensa/goldwind-e-casa-dos-ventos-assinam-acordo-para-o-projeto-eolico-sento-se-de-872-mw-no-brasil-302880123.html",
        "annotation": "Company PR (PT) on Sento Sé 872 MW / 109 GWH182-8.0 MW order. Supports goldwind_sento_se_872mw_2026.",
        "supports": ["goldwind_sento_se_872mw_2026", "hunt_energy_wind"],
    },
)

# 6 infrastructure/port_cranes — miss (Portonave/Arica/Cartagena/Yucatán already logged)
# 7 resources/niobium — miss (CBMM R$13bn overlaps prior capex proxy)
# 8 resources/balsa — miss
# 9 energy/solar — miss (thick set)
# 10 resources/graphite — miss (South Star PO logged C12)
# 11 energy/power_plants_grid — miss (thick)
# 12 resources/copper — miss (El Abra mill already logged; Continuidad USD press not distinct new equity)
# 13 resources/nickel — miss (IFC/Appian Santa Rita already logged)

# 14 resources/lithium — Ganfeng USD 180m convertible into Lithium Argentina
A(
    {
        "id": "ganfeng_laac_convertible_180m_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Ganfeng Lithium — USD 180m convertible note investment in Lithium Argentina AG",
        "country": "Argentina",
        "asset": "Closing of USD 180 million six-year unsecured convertible note (4.0% coupon; convert at USD 12.50/share) to strengthen Lithium Argentina balance sheet for Cauchari-Olaroz Stage 2 and PPG; Ganfeng ~9.6% current stake → ~16.1% fully diluted if converted; PPG JV with Ganfeng on track end-Sep 2026",
        "investment_type": "financing",
        "value": "180000000",
        "currency": "USD",
        "value_usd": "180000000",
        "fx_usd": "1",
        "fx_date": "2026-09-15",
        "year": "2026",
        "status": "active",
        "lat": "-23.7",
        "lon": "-66.7",
        "geo_note": "Cauchari-Olaroz / PPG Argentina lithium footprint (Lithium Argentina GlobeNewswire; approximate Jujuy/Salta pin).",
        "evidence": "documented",
        "source_id": "globenewswire_laac_ganfeng_180m_20260915",
        "note": "Actor: Ganfeng Lithium Group (PRC) — prc. Lithium Argentina AG GlobeNewswire 15 Sep 2026. Distinct from ganfeng_pastos_grandes_stake_2024 / Lithea PPG acquisition / Mariana production rows (corporate convertible financing event).",
    },
    {
        "id": "ganfeng_laac_convertible_180m_2026",
        "retrieved": "2026-10-01",
        "source_id": "globenewswire_laac_ganfeng_180m_20260915",
        "url": "https://www.globenewswire.com/news-release/2026/09/15/3361860/0/en/lithium-argentina-announces-closing-of-180m-strategic-investment-from-ganfeng.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Lithium Argentina AG … today announced the closing of the $180 million strategic investment from Ganfeng Lithium Group Co., Ltd. (“Ganfeng”) through the issuance of a six-year unsecured convertible note … The Note bears a coupon of 4.0% per annum, matures six years from issuance and is convertible into common shares of the Company at $12.50 per share",
        "note": "Opened Lithium Argentina GlobeNewswire release (curl blocked; content retrieved via fetch).",
    },
    {
        "id": "globenewswire_laac_ganfeng_180m_20260915",
        "type": "official",
        "chicago": "Lithium Argentina AG. “Lithium Argentina Announces Closing of $180M Strategic Investment from Ganfeng.” GlobeNewswire, 15 September 2026.",
        "url": "https://www.globenewswire.com/news-release/2026/09/15/3361860/0/en/lithium-argentina-announces-closing-of-180m-strategic-investment-from-ganfeng.html",
        "annotation": "Company primary convertible-note close. Supports ganfeng_laac_convertible_180m_2026.",
        "supports": ["ganfeng_laac_convertible_180m_2026", "hunt_res_lithium"],
    },
)

# 15 resources/water — miss (Cox Rosarito logged C13)
# 16 infrastructure/building_materials — miss (Heidelberg Inka / Holcim Colombia already logged)

# 17 infrastructure/engineering_epc — Lycopodium San Cristóbal silver oxide EPCM (Bolivia)
A(
    {
        "id": "lycopodium_san_cristobal_epcm_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Lycopodium — EPCM for San Cristóbal silver oxide plant (Minera San Cristóbal, Bolivia)",
        "country": "Bolivia",
        "asset": "EPCM contract ~A$37 million for new 15,000 tpd silver oxide plant adjacent to existing 52,000 tpd sulphide plant at San Cristóbal (Potosí); still subject to FID; works commence immediately; completion anticipated 2030; ~4,000 masl site",
        "investment_type": "epc",
        "value": "37000000",
        "currency": "AUD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-21.08",
        "lon": "-67.2",
        "geo_note": "San Cristóbal Mine, southwestern Potosí Department, Bolivia (Lycopodium ASX announcement).",
        "evidence": "documented",
        "source_id": "lycopodium_san_cristobal_20260818",
        "note": "Actor: Lycopodium (Australian ASX:LYL) — allied. Company 18 Aug 2026 ASX PDF. Value stored as AUD (no FX). Distinct from Worley Diablillos / Bechtel EIMISA / Fluor/Hatch EPC rows. Non-grid mine plant EPCM.",
    },
    {
        "id": "lycopodium_san_cristobal_epcm_2026",
        "retrieved": "2026-10-01",
        "source_id": "lycopodium_san_cristobal_20260818",
        "url": "https://www.lycopodium.com/wp-content/uploads/2026/08/San-Cristobal-Announcement_FINAL.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Lycopodium … has been awarded the Engineering, Procurement and Construction Management (EPCM) contract for the development of a new silver oxide plant, adjacent to the existing sulphides plant, at the San Cristóbal Mine in Bolivia. The EPCM contract is valued at approximately A$37 million. … Lycopodium will provide EPCM services for a new 15,000 tonnes per day (tpd) plant to treat oxidised material and produce silver doré.",
        "note": "Opened Lycopodium ASX PDF announcement.",
    },
    {
        "id": "lycopodium_san_cristobal_20260818",
        "type": "official",
        "chicago": "Lycopodium Limited. “Lycopodium Awarded EPCM Contract for San Cristóbal Silver Oxide Project in Bolivia.” ASX announcement, 18 August 2026.",
        "url": "https://www.lycopodium.com/wp-content/uploads/2026/08/San-Cristobal-Announcement_FINAL.pdf",
        "annotation": "Company primary San Cristóbal oxide-plant EPCM award. Supports lycopodium_san_cristobal_epcm_2026.",
        "supports": ["lycopodium_san_cristobal_epcm_2026", "hunt_infra_engineering_epc"],
    },
)

# 17b infrastructure/engineering_epc — M3 Engineering Panuco EPCM (Mexico)
A(
    {
        "id": "m3_vizsla_panuco_epcm_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "M3 Engineering & Technology — EPCM for Vizsla Silver Panuco process plant (Sinaloa)",
        "country": "Mexico",
        "asset": "EPCM award for Panuco silver-gold process plant and surface infrastructure valued at approximately US$170 million; definitive EPCM agreement terms still being finalized; Mining Plus mine-design contract also announced (separate scope)",
        "investment_type": "epc",
        "value": "170000000",
        "currency": "USD",
        "value_usd": "170000000",
        "fx_usd": "1",
        "fx_date": "2026-04-23",
        "year": "2026",
        "status": "active",
        "lat": "23.4",
        "lon": "-105.9",
        "geo_note": "Panuco district, Sinaloa, Mexico (Vizsla Silver PR Newswire).",
        "evidence": "documented",
        "source_id": "prnewswire_vizsla_m3_panuco_20260423",
        "note": "Actor: M3 Engineering & Technology Corp. (U.S.) — us; owner Vizsla Silver (Canadian). Company PR 23 Apr 2026. Distinct from Lycopodium San Cristóbal / Worley Diablillos. Value = stated EPCM process-plant/surface-infrastructure scope (definitive agreement still finalizing).",
    },
    {
        "id": "m3_vizsla_panuco_epcm_2026",
        "retrieved": "2026-10-01",
        "source_id": "prnewswire_vizsla_m3_panuco_20260423",
        "url": "https://www.prnewswire.com/news-releases/vizsla-silver-awards-epcm-and-mine-design-contracts-for-the-development-of-the-panuco-silver-gold-project-302750621.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Vizsla Silver … announced that it has awarded the Engineering, Procurement and Construction Management (the “EPCM”) contract to M3 Engineering & Technology Corp. … The EPCM scope of work covers the process plant and surface infrastructure, valued at approximately US$170 million. The Company and M3 Engineering are currently finalizing the terms and conditions of the definitive EPCM agreement.",
        "note": "Opened Vizsla Silver PR Newswire release.",
    },
    {
        "id": "prnewswire_vizsla_m3_panuco_20260423",
        "type": "official",
        "chicago": "Vizsla Silver Corp. “Vizsla Silver Awards EPCM and Mine Design Contracts for the Development of the Panuco Silver-Gold Project.” PR Newswire, 23 April 2026.",
        "url": "https://www.prnewswire.com/news-releases/vizsla-silver-awards-epcm-and-mine-design-contracts-for-the-development-of-the-panuco-silver-gold-project-302750621.html",
        "annotation": "Company primary Panuco EPCM award to M3 Engineering. Supports m3_vizsla_panuco_epcm_2026.",
        "supports": ["m3_vizsla_panuco_epcm_2026", "hunt_infra_engineering_epc"],
    },
)

# 18 energy/other_renewables — miss (Acciona La Gina / Ormat Dominica logged C12)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]] = full
        else:
            by_id[rid] = len(rows)
            rows.append(full)
        added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            supports = set(existing.get("supports") or [])
            supports.update(bib_entry.get("supports") or [])
            existing["supports"] = sorted(supports)
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    hunt_updates = {
        "hunt_infra_port_ownership": "Cycle 14: logged apm_callao_stage3b_2026.",
        "hunt_latam_rail_telecom": "Cycle 14: equal budget; PowerChina Chancay–Sierra Central press/IRJ Cloudflare (miss).",
        "hunt_energy_fission_smr": "Cycle 14: equal budget; Meitner/FIRST/CAREM/Brazil microreactor already logged (miss).",
        "hunt_infra_bridges_roads": "Cycle 14: equal budget; CRBC Arequipa–La Joya logged C13 (miss).",
        "hunt_energy_wind": "Cycle 14: logged vestas_esquina_do_vento_230mw_2026 + goldwind_sento_se_872mw_2026.",
        "hunt_infra_port_cranes": "Cycle 14: equal budget; Portonave/Arica/Cartagena/Yucatán already logged (miss).",
        "hunt_fenb_araxa": "Cycle 14: equal budget; CBMM R$13bn press overlaps prior capex proxy (miss).",
        "hunt_res_balsa": "Cycle 14: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_energy_solar": "Cycle 14: equal budget; thick set — miss.",
        "hunt_res_graphite": "Cycle 14: equal budget; South Star PO logged C12 (miss).",
        "hunt_br_power_equip": "Cycle 14: equal budget; thick subcategory — miss.",
        "hunt_res_copper": "Cycle 14: equal budget; El Abra mill already logged; no distinct new Cu equity (miss).",
        "hunt_res_nickel": "Cycle 14: equal budget; IFC/Appian Santa Rita already logged (miss).",
        "hunt_res_lithium": "Cycle 14: logged ganfeng_laac_convertible_180m_2026.",
        "hunt_res_water": "Cycle 14: equal budget; Cox Rosarito logged C13 (miss).",
        "hunt_infra_building_materials": "Cycle 14: equal budget; Heidelberg Inka / Holcim Colombia already logged (miss).",
        "hunt_infra_engineering_epc": "Cycle 14: logged lycopodium_san_cristobal_epcm_2026 + m3_vizsla_panuco_epcm_2026.",
        "hunt_energy_other_renewables": "Cycle 14: equal budget; Acciona La Gina / Ormat Dominica logged C12 (miss).",
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
    print("Cycle 14 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
