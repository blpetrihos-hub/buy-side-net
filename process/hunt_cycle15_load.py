#!/usr/bin/env python3
"""Cycle 15 hunt: shuffle_seed=20261015; equal budget across 18 subcategories."""
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


# seed 20261015 order:
# rail, balsa, engineering_epc, port_cranes, wind, building_materials, graphite,
# power_plants_grid, copper, bridges_roads, nickel, water, fission_smr, port_ownership,
# lithium, solar, other_renewables, niobium

# 1 infrastructure/rail — miss
# 2 resources/balsa — miss

# 3 infrastructure/engineering_epc — Sedgman Colossus REE EPCM (MG, Brazil)
A(
    {
        "id": "sedgman_colossus_epcm_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Sedgman (ACS) — preferred EPCM for Viridis Colossus rare-earth project (Minas Gerais)",
        "country": "Brazil",
        "asset": "Preferred EPCM contractor appointment for Colossus ionic adsorption clay rare-earth project; bridging-phase detailed engineering/procurement ahead of FID; delivery with Brazilian partner Blossom Consult after FID",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-18.5",
        "lon": "-44.0",
        "geo_note": "Colossus project, Minas Gerais (Sedgman/HOCHTIEF release; approximate).",
        "evidence": "documented",
        "source_id": "sedgman_colossus_20260915",
        "note": "Actor: Sedgman (ACS Group / Australia–Spain) — allied; owner Viridis Mining & Minerals. HOCHTIEF/Sedgman 15 Sep 2026 press. No contract USD on page. Distinct from Lycopodium San Cristóbal / M3 Panuco / Worley Diablillos. Non-grid mine EPCM.",
    },
    {
        "id": "sedgman_colossus_epcm_2026",
        "retrieved": "2026-10-01",
        "source_id": "sedgman_colossus_20260915",
        "url": "https://www.hochtief.com/news-media/press-releases/press-release/sedgman-appointed-as-the-preferred-epcm-contractor-for-colossus-rare-earth-project",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Sedgman, a member of the ACS Group, has been appointed as the preferred engineering, procurement and construction management (EPCM) contractor for the Colossus Rare Earth Project in Minas Gerais, Brazil, by Viridis Mining & Minerals Limited (Viridis). … Work will commence immediately under a bridging phase to progress critical detailed engineering design and procurement activities ahead of the Project Final Investment Decision (FID).",
        "note": "Opened HOCHTIEF/Sedgman press release.",
    },
    {
        "id": "sedgman_colossus_20260915",
        "type": "official",
        "chicago": "Sedgman / HOCHTIEF. “Sedgman appointed as the preferred EPCM contractor for Colossus Rare Earth Project.” 15 September 2026.",
        "url": "https://www.hochtief.com/news-media/press-releases/press-release/sedgman-appointed-as-the-preferred-epcm-contractor-for-colossus-rare-earth-project",
        "annotation": "Company primary Colossus preferred-EPCM appointment. Supports sedgman_colossus_epcm_2026.",
        "supports": ["sedgman_colossus_epcm_2026", "hunt_infra_engineering_epc"],
    },
)

# 4 infrastructure/port_cranes — ZPMC Tecon Rio Grande (Wilson Sons)
A(
    {
        "id": "zpmc_tecon_rio_grande_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — 3 Super Post-Panamax STS + 6 remote aRTGs for Tecon Rio Grande (Wilson Sons)",
        "country": "Brazil",
        "asset": "Delivery Sep 2026 of 3 STS + 6 automated/remotely operated RTGs ordered Mar 2025 from ZPMC (Shanghai); UNVERIFIED press package ~R$ 290 million within R$ 1.4bn Tecon expansion plan to 2030",
        "investment_type": "equipment_supply",
        "value": "290000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-32.13",
        "lon": "-52.1",
        "geo_note": "Tecon Rio Grande, Port of Rio Grande, Rio Grande do Sul (GaúchaZH citing terminal director).",
        "evidence": "proxy",
        "source_id": "gauchazh_tecon_rg_zpmc_20260918",
        "note": "Actor: ZPMC (PRC) OEM; buyer Wilson Sons / Tecon Rio Grande — prc crane coding. UNVERIFIED proxy: GaúchaZH 18 Sep 2026 names ZPMC and ~R$290m; WorldCargo/Datamar corroborate delivery of 3 STS + 6 RTGs from Shanghai. Distinct from ZPMC Santos Brasil / Portonave / Itapoá rows. Value stored as BRL (no FX).",
    },
    {
        "id": "zpmc_tecon_rio_grande_2026",
        "retrieved": "2026-10-01",
        "source_id": "gauchazh_tecon_rg_zpmc_20260918",
        "url": "https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/09/tecon-rio-grande-recebe-r-290-milhoes-em-equipamentos-para-movimentacao-de-conteineres-cmu738bdl01v1014x2r640dlr.html",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "O Tecon Rio Grande recebeu … nove novos equipamentos … três guindastes de cais e seis equipamentos de pátio … investimento de cerca de R$ 290 milhões. … Os equipamentos foram adquiridos em março de 2025 da fabricante chinesa ZPMC. … três são STSs (Super Post Panamax) … seis são aRTGs (Automated Rubber Tyred Gantry)",
        "note": "Opened GaúchaZH local press naming ZPMC and R$290m (Wilson Sons primary not opened this cycle).",
    },
    {
        "id": "gauchazh_tecon_rg_zpmc_20260918",
        "type": "press",
        "chicago": "GaúchaZH / Zero Hora. “Tecon Rio Grande recebe R$ 290 milhões em equipamentos para movimentação de contêineres.” 18 September 2026.",
        "url": "https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/09/tecon-rio-grande-recebe-r-290-milhoes-em-equipamentos-para-movimentacao-de-conteineres-cmu738bdl01v1014x2r640dlr.html",
        "annotation": "Local press on Tecon Rio Grande ZPMC STS/aRTG delivery. Supports zpmc_tecon_rio_grande_2026 (UNVERIFIED value).",
        "supports": ["zpmc_tecon_rio_grande_2026", "hunt_infra_port_cranes"],
    },
)

# 5 energy/wind — miss (Esquina do Vento / Sento Sé logged C14)
# 6 infrastructure/building_materials — miss (CSN Cimentos sale not closed)
# 7 resources/graphite — miss (Jordânia / South Star already logged)
# 8 energy/power_plants_grid — miss (thick)
# 9 resources/copper — miss
# 10 infrastructure/bridges_roads — miss

# 11 resources/nickel — Centaurus Jaguar BNDES LOI R$1bn
A(
    {
        "id": "centaurus_jaguar_bndes_loi_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "BNDES FINEM LOI — R$1 billion debt funding for Centaurus Jaguar Nickel Project (Pará)",
        "country": "Brazil",
        "asset": "Non-binding Letter of Intent from BNDES for R$1 billion (~US$190 million per company) FINEM long-term project finance for 100%-owned Jaguar Ni sulphide project (Carajás, Pará); subject to credit analysis and board approvals",
        "investment_type": "financing",
        "value": "1000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-6.65",
        "lon": "-49.0",
        "geo_note": "Jaguar Nickel Project, Carajás Mineral Province, Pará (Centaurus ASX 23 Mar 2026).",
        "evidence": "documented",
        "source_id": "centaurus_jaguar_bndes_loi_20260323",
        "note": "Actor: Centaurus Metals (Australian) borrower — allied; lender BNDES (Brazilian DFI). Company ASX 23 Mar 2026. LOI non-binding / not closed. Distinct from centaurus_jaguar_nickel_lease_2025 and Brazilian Nickel DFC LOI. Value stored as BRL (company ~US$190m paraphrase not entered as FX).",
    },
    {
        "id": "centaurus_jaguar_bndes_loi_2026",
        "retrieved": "2026-10-01",
        "source_id": "centaurus_jaguar_bndes_loi_20260323",
        "url": "https://centaurusmetals.com/pdf/464fb39b-afc4-467c-9317-33f1c3870c73/LOI-for-US190M-from-Brazils-National-Development-Bank.pdf?Platform=ListPage",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Centaurus Metals Limited … has received a Letter of Intent (LOI) from BNDES for R$1 billion (~US$190 million) in debt funding for its 100%-owned Jaguar Nickel Project located in the Carajás Mineral Province in the State of Pará, Brazil. The non-binding LOI confirms BNDES’ intent to support the development of the Jaguar Project, through its Financiamento a Empreendimentos (FINEM) long-term project finance facility",
        "note": "Opened Centaurus ASX PDF announcement.",
    },
    {
        "id": "centaurus_jaguar_bndes_loi_20260323",
        "type": "official",
        "chicago": "Centaurus Metals Limited. “Centaurus Receives Letter of Intent for R$1 Billion in Debt Funding from the Brazilian National Development Bank.” ASX announcement, 23 March 2026.",
        "url": "https://centaurusmetals.com/pdf/464fb39b-afc4-467c-9317-33f1c3870c73/LOI-for-US190M-from-Brazils-National-Development-Bank.pdf?Platform=ListPage",
        "annotation": "Company primary BNDES FINEM LOI for Jaguar. Supports centaurus_jaguar_bndes_loi_2026.",
        "supports": ["centaurus_jaguar_bndes_loi_2026", "hunt_res_nickel"],
    },
)

# 11b resources/nickel — Centaurus Glencore offtake
A(
    {
        "id": "centaurus_glencore_offtake_jaguar_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Glencore AG — binding offtake for Jaguar nickel concentrate (Sudbury destination)",
        "country": "Brazil",
        "asset": "Binding 5-year offtake from production start: 20,000 dmt/y high-grade (~32%) Ni concentrate (~6,400 tpa Ni) to Glencore Sudbury (Canada); ~1/3 of Jaguar 65,000 tpa concentrate; LME-linked payability; conditional on FID by 30 Sep 2026 and other milestones; company estimates contract value exceeds US$450m at announcement prices",
        "investment_type": "offtake",
        "value": "450000000",
        "currency": "USD",
        "value_usd": "450000000",
        "fx_usd": "1",
        "fx_date": "2026-03-16",
        "year": "2026",
        "status": "active",
        "lat": "-6.65",
        "lon": "-49.0",
        "geo_note": "Jaguar Nickel Project, Pará (Centaurus ASX 16 Mar 2026); concentrate destined Sudbury, Canada.",
        "evidence": "documented",
        "source_id": "centaurus_glencore_offtake_20260316",
        "note": "Actors: Centaurus (Australian producer) + Glencore AG (Swiss) — allied offtake coding. Company ASX 16 Mar 2026. Value = company estimated offtake contract value at then nickel prices (not fixed offtake price). Distinct from BNDES LOI and Jaguar mining-lease rows.",
    },
    {
        "id": "centaurus_glencore_offtake_jaguar_2026",
        "retrieved": "2026-10-01",
        "source_id": "centaurus_glencore_offtake_20260316",
        "url": "https://centaurusmetals.com/PDF/26affd46-2e70-40ee-a903-3e3098301ac8/MaidenNickelOfftakeforJaguarSecuredfromGlencore",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Centaurus … has executed a binding Offtake Agreement with Glencore for the supply of nickel concentrate from the Company’s Jaguar Nickel Sulphide Project in Brazil … supply of 20,000 dry metric tonnes per annum of high-grade nickel concentrate to Glencore, with the base destination of Canada for treatment at Glencore’s Sudbury smelting operations … The estimated value of the Offtake Agreement, at current nickel prices, exceeds US$450 million over the life of the initial 5-year contract.",
        "note": "Opened Centaurus ASX PDF announcement.",
    },
    {
        "id": "centaurus_glencore_offtake_20260316",
        "type": "official",
        "chicago": "Centaurus Metals Limited. “Centaurus Secures Maiden Nickel Offtake with Glencore for the Jaguar Nickel Project, Brazil.” ASX announcement, 16 March 2026.",
        "url": "https://centaurusmetals.com/PDF/26affd46-2e70-40ee-a903-3e3098301ac8/MaidenNickelOfftakeforJaguarSecuredfromGlencore",
        "annotation": "Company primary Glencore Jaguar offtake. Supports centaurus_glencore_offtake_jaguar_2026.",
        "supports": ["centaurus_glencore_offtake_jaguar_2026", "hunt_res_nickel"],
    },
)

# 12 resources/water — miss
# 13 energy/fission_smr — miss (Meitner/FIRST/CAREM/Brazil microreactor already logged)
# 14 infrastructure/port_ownership — miss (APM Callao Stage 3B logged C14)
# 15 resources/lithium — miss (Ganfeng LAAC note logged C14)
# 16 energy/solar — miss
# 17 energy/other_renewables — miss
# 18 resources/niobium — miss (CMOC Catalão production already logged; CBMM R$13bn overlaps prior)


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
        "hunt_latam_rail_telecom": "Cycle 15: equal budget; no new rail award beyond prior CRRC/Alstom/Siemens/CAF set (miss).",
        "hunt_res_balsa": "Cycle 15: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_infra_engineering_epc": "Cycle 15: logged sedgman_colossus_epcm_2026.",
        "hunt_infra_port_cranes": "Cycle 15: logged zpmc_tecon_rio_grande_2026.",
        "hunt_energy_wind": "Cycle 15: equal budget; Vestas Esquina / Goldwind Sento Sé logged C14 (miss).",
        "hunt_infra_building_materials": "Cycle 15: equal budget; CSN Cimentos sale not closed (Huaxin/Votorantim bids — miss).",
        "hunt_res_graphite": "Cycle 15: equal budget; Graphcoa Jordânia / South Star already logged (miss).",
        "hunt_br_power_equip": "Cycle 15: equal budget; thick subcategory — miss.",
        "hunt_res_copper": "Cycle 15: equal budget; no new copper beyond FCX/FQM/Teck/Chinalco (miss).",
        "hunt_infra_bridges_roads": "Cycle 15: equal budget; CRBC Arequipa–La Joya logged C13 (miss).",
        "hunt_res_nickel": "Cycle 15: logged centaurus_jaguar_bndes_loi_2026 + centaurus_glencore_offtake_jaguar_2026.",
        "hunt_res_water": "Cycle 15: equal budget; Cox Rosarito logged C13 (miss).",
        "hunt_energy_fission_smr": "Cycle 15: equal budget; Meitner/FIRST/CAREM/Brazil microreactor already logged (miss).",
        "hunt_infra_port_ownership": "Cycle 15: equal budget; APM Callao Stage 3B logged C14 (miss).",
        "hunt_res_lithium": "Cycle 15: equal budget; Ganfeng LAAC convertible logged C14 (miss).",
        "hunt_energy_solar": "Cycle 15: equal budget; thick set — miss.",
        "hunt_energy_other_renewables": "Cycle 15: equal budget; Acciona La Gina / Ormat Dominica logged C12 (miss).",
        "hunt_fenb_araxa": "Cycle 15: equal budget; CMOC Catalão production already logged; CBMM R$13bn overlaps prior (miss).",
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
    print("Cycle 15 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
