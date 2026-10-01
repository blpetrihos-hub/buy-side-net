#!/usr/bin/env python3
"""Cycle 24 hunt: shuffle_seed=20261024; equal budget across 18 subcategories."""
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


# seed 20261024 order:
# water, solar, wind, power_plants_grid, niobium, lithium, building_materials,
# other_renewables, port_cranes, balsa, fission_smr, copper, bridges_roads,
# port_ownership, graphite, nickel, rail, engineering_epc

# 1 resources/water — Techint Collahuasi C20+ seawater impulse aqueduct EPC
A(
    {
        "id": "techint_collahuasi_c20_impulse_2022",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Techint E&C — Collahuasi C20+ seawater impulse / aqueduct EPC (Patache–Ujina)",
        "country": "Chile",
        "asset": "EPC for 195 km seawater transport system from Puerto Patache to Ujina (>4,000 masl): 1,100 l/s capacity (expandable); 5 pump stations (25 × 5,000 hp pumps) + 6 drainage stations + terminal energy-recovery turbines; detail engineering through commissioning + 2-year O&M assist",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2022",
        "status": "active",
        "lat": "-20.8",
        "lon": "-70.18",
        "geo_note": "Puerto Patache intake / start of Collahuasi impulse line, Tarapacá (Techint release).",
        "evidence": "documented",
        "source_id": "techint_collahuasi_impulse_20220729",
        "note": "Actor: Techint Engineering & Construction (Italian-Argentine Techint Group) — allied. Company news 29 Jul 2022. Companion to Acciona Patache desal (acciona_collahuasi_desal_chile); distinct from techint_saddn_epc_chile (Codelco Northern District SADDN). No contract USD on opened page.",
    },
    {
        "id": "techint_collahuasi_c20_impulse_2022",
        "retrieved": "2026-10-01",
        "source_id": "techint_collahuasi_impulse_20220729",
        "url": "https://www.techint.com/es/noticias/2022/mineria-sustentable-para-collahuasi",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Techint E&C fue adjudicada con un contrato EPC … para construir un sistema de impulsión de agua desde el Puerto Patache … hasta Ujina … El sistema de transporte de agua de mar para Collahuasi tendrá una capacidad de 1.100 litros/seg … Un ducto de 195 km de longitud",
        "note": "Opened Techint company news 29 Jul 2022.",
    },
    {
        "id": "techint_collahuasi_impulse_20220729",
        "type": "company",
        "chicago": "Techint Engineering & Construction. “Minería sustentable para Collahuasi.” 29 July 2022.",
        "url": "https://www.techint.com/es/noticias/2022/mineria-sustentable-para-collahuasi",
        "annotation": "Company primary on Collahuasi seawater impulse EPC. Supports techint_collahuasi_c20_impulse_2022.",
        "supports": ["techint_collahuasi_c20_impulse_2022", "hunt_res_water"],
    },
)

# 2 energy/solar — miss (Jinko Casa dos Ventos logged C23)
# 3 energy/wind — miss (Statkraft Emma / Vestas Esquina / Goldwind Sento Sé already logged)
# 4 energy/power_plants_grid — miss (State Grid NE UHV / thick)
# 5 resources/niobium — miss (CBMM R$13bn press overlaps prior capex proxy)

# 6 resources/lithium — Eni 25% of EnergyX Black Giant SpA (Chile)
A(
    {
        "id": "eni_energyx_black_giant_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Eni — 25% stake in EnergyX Black Giant SpA lithium project (Salar de Punta Negra area)",
        "country": "Chile",
        "asset": "Agreement to acquire 25% of Black Giant SpA (EnergyX Chile subsidiary) for phased investment USD 225 million; DLE closed-loop with full brine reinjection; target 52.5 ktpa LCE (Train 1 7.5 ktpa ~2028 + 45 ktpa ~2030); Eni board seat + option to offtake up to 25% of LCE",
        "investment_type": "ownership_equity",
        "value": "225000000",
        "currency": "USD",
        "value_usd": "225000000",
        "fx_usd": "1",
        "fx_date": "2026-07-06",
        "year": "2026",
        "status": "active",
        "lat": "-24.6",
        "lon": "-69.0",
        "geo_note": "Northern Chile near Salar de Punta Negra (Eni release; approximate).",
        "evidence": "documented",
        "source_id": "eni_black_giant_20260706",
        "note": "Actors: Eni (Italian) — allied investor; project developer EnergyX (U.S.) via Black Giant SpA. Company Eni press 6 Jul 2026. Distinct from Rio Tinto Rincon / Eramet Centenario / Ganfeng / Zijin lithium rows.",
    },
    {
        "id": "eni_energyx_black_giant_2026",
        "retrieved": "2026-10-01",
        "source_id": "eni_black_giant_20260706",
        "url": "https://www.eni.com/en-IT/media/press-release/2026/07/eni-invests-in-energyxs-black-giant-project-to-develop-lithium-business-in-chile.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Eni announces that it has signed an agreement to acquire a 25% stake in EnergyX’s Chilean subsidiary company Black Giant SpA … Eni’s total phased investment amounts to $225 million. … The project targets production of 52.5 kton/year of lithium carbonate equivalent (“LCE”) at full capacity",
        "note": "Opened Eni English company press release 6 Jul 2026.",
    },
    {
        "id": "eni_black_giant_20260706",
        "type": "company",
        "chicago": "Eni. “Eni invests in EnergyX’s Black Giant project to develop lithium business in Chile.” 6 July 2026.",
        "url": "https://www.eni.com/en-IT/media/press-release/2026/07/eni-invests-in-energyxs-black-giant-project-to-develop-lithium-business-in-chile.html",
        "annotation": "Company primary on Eni 25% / USD 225m Black Giant Chile lithium stake. Supports eni_energyx_black_giant_2026.",
        "supports": ["eni_energyx_black_giant_2026", "hunt_res_lithium"],
    },
)

# 7 infrastructure/building_materials — miss (CSN Cimentos still open; Holcim Colombia / Heidelberg Inka / Pacasmayo already logged)
# 8 energy/other_renewables — miss (CATL Alegria logged C23)

# 9 infrastructure/port_cranes — Kalmar 5 electric reachstackers for Portonave
A(
    {
        "id": "kalmar_portonave_ers_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Kalmar — five electric reachstackers for Portonave (Navegantes / TiL)",
        "country": "Brazil",
        "asset": "Order for five Kalmar electric reachstackers booked Q2 2026; delivery completion targeted Q4 2026 at Portonave Navegantes terminal (complements existing Kalmar empty handlers / Eco reachstacker fleet)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-26.89",
        "lon": "-48.65",
        "geo_note": "Portonave, Navegantes, Santa Catarina (Kalmar release).",
        "evidence": "documented",
        "source_id": "kalmar_portonave_ers_20260729",
        "note": "Actor: Kalmar (Finnish; Nasdaq Helsinki) — allied. Company trade press 29 Jul 2026. Yard cargo-handling equipment (reachstackers) under port_cranes equipment map. Distinct from konecranes_portonave_rtg_2025 and zpmc_portonave_sts_2025 on same terminal. No USD on opened page.",
    },
    {
        "id": "kalmar_portonave_ers_2026",
        "retrieved": "2026-10-01",
        "source_id": "kalmar_portonave_ers_20260729",
        "url": "https://www.kalmarglobal.com/news--insights/press_releases/2026/kalmar-and-portonave-to-enhance/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Kalmar has concluded an agreement with Brazilian terminal operator Portonave … to supply five Kalmar electric reachstackers. The machines will be deployed at the Navegantes terminal in Santa Catarina State, Brazil. The large order was booked in Kalmar’s Q2 2026 order intake, with delivery scheduled to be completed during Q4 2026.",
        "note": "Opened Kalmar company trade press release 29 Jul 2026.",
    },
    {
        "id": "kalmar_portonave_ers_20260729",
        "type": "company",
        "chicago": "Kalmar Corporation. “Kalmar and Portonave to enhance cargo-handling sustainability in Brazil with large order for electric reachstackers.” Trade press release, 29 July 2026.",
        "url": "https://www.kalmarglobal.com/news--insights/press_releases/2026/kalmar-and-portonave-to-enhance/",
        "annotation": "Company primary on Portonave electric reachstacker order. Supports kalmar_portonave_ers_2026.",
        "supports": ["kalmar_portonave_ers_2026", "hunt_infra_port_cranes"],
    },
)

# 10 resources/balsa — miss

# 11 energy/fission_smr — CNEN–INVAP MoU toward RMB EPC (Iperó)
A(
    {
        "id": "cnen_invap_rmb_mou_2025",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "allied",
        "counterpart": "INVAP — MoU with CNEN toward EPC for Brazilian Multipurpose Reactor (RMB) complex",
        "country": "Brazil",
        "asset": "Memorandum of Understanding setting terms for negotiation of an EPC contract for the technological complex housing the Brazilian Multipurpose Reactor (RMB) including labs, operational infrastructure and logistics; construction start targeted 2026, delivery 2030, operations 2031 (~30 MWt open-pool research reactor class; radioisotope / materials testing mission)",
        "investment_type": "mou_epc_negotiation",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.43",
        "lon": "-47.62",
        "geo_note": "RMB site Iperó / Sorocaba area, São Paulo (CNEN project geography).",
        "evidence": "documented",
        "source_id": "cnen_invap_rmb_20250919",
        "note": "Actor: INVAP S.A.U. (Argentine state technology company) — allied; counterpart CNEN (Brazilian nuclear authority). Official CNEN news 19 Sep 2025 (MoU signed 18 Sep at IAEA GC). Pre-EPC MoU — no CAPEX USD on opened page (WNN secondary cites ~USD 500m estimate — not entered). Distinct from Candu PIAP MoU, CAREM/Meitner/Nuclearis power-SMR rows; multipurpose research reactor / radioisotope complex.",
    },
    {
        "id": "cnen_invap_rmb_mou_2025",
        "retrieved": "2026-10-01",
        "source_id": "cnen_invap_rmb_20250919",
        "url": "https://www.gov.br/cnen/pt-br/assunto/ultimas-noticias/cnen-e-invap-assinam-contrato-para-o-rmb",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "O presidente da CNEN, Francisco Rondinelli Junior, e o CEO da INVAP S.A.U., Darío Sergio Giussi, assinaram um Memorando de Entendimento (MoU), tendo como objetivo estabelecer os termos, as condições e premissas que nortearão as tratativas e negociações … para a celebração do Contrato de EPC … A iniciativa é voltada à implantação do complexo tecnológico que abrigará o Reator Multipropósito Brasileiro (RMB)",
        "note": "Opened CNEN (gov.br) official news 19 Sep 2025.",
    },
    {
        "id": "cnen_invap_rmb_20250919",
        "type": "government",
        "chicago": "Brazil. Comissão Nacional de Energia Nuclear. “CNEN e INVAP assinam contrato para o RMB.” 19 September 2025.",
        "url": "https://www.gov.br/cnen/pt-br/assunto/ultimas-noticias/cnen-e-invap-assinam-contrato-para-o-rmb",
        "annotation": "Official CNEN notice of INVAP MoU toward RMB EPC. Supports cnen_invap_rmb_mou_2025.",
        "supports": ["cnen_invap_rmb_mou_2025", "hunt_energy_fission_smr"],
    },
)

# 12 resources/copper — miss (Toromocho ITS-3 logged C23)
# 13 infrastructure/bridges_roads — miss (CRBC Arequipa / Salvador–Itaparica already logged)
# 14 infrastructure/port_ownership — miss (ICTSI Aratu logged C23)
# 15 resources/graphite — miss (South Star PO / Graphcoa already logged)
# 16 resources/nickel — miss (BNDES Piauí / Centaurus Jaguar already logged)
# 17 infrastructure/rail — miss
# 18 infrastructure/engineering_epc — miss (STRACON / Worley Diablillos already logged)


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
        "hunt_res_water": "Cycle 24: logged techint_collahuasi_c20_impulse_2022.",
        "hunt_energy_solar": "Cycle 24: equal budget; Jinko Casa dos Ventos logged C23 (miss).",
        "hunt_energy_wind": "Cycle 24: equal budget; Statkraft Emma / Vestas Esquina / Goldwind Sento Sé already logged (miss).",
        "hunt_br_power_equip": "Cycle 24: equal budget; State Grid NE UHV construction logged C22 (miss).",
        "hunt_fenb_araxa": "Cycle 24: equal budget; CBMM R$13bn press overlaps prior capex proxy (miss).",
        "hunt_res_lithium": "Cycle 24: logged eni_energyx_black_giant_2026.",
        "hunt_infra_building_materials": "Cycle 24: equal budget; CSN Cimentos still not closed; Holcim Colombia / Heidelberg Inka / Pacasmayo already logged (miss).",
        "hunt_energy_other_renewables": "Cycle 24: equal budget; CATL CIP La Alegría logged C23 (miss).",
        "hunt_infra_port_cranes": "Cycle 24: logged kalmar_portonave_ers_2026.",
        "hunt_res_balsa": "Cycle 24: equal budget; no new named exporter/importer stake beyond WITS years (miss).",
        "hunt_energy_fission_smr": "Cycle 24: logged cnen_invap_rmb_mou_2025.",
        "hunt_res_copper": "Cycle 24: equal budget; Chinalco Toromocho ITS-3 logged C23 (miss).",
        "hunt_infra_bridges_roads": "Cycle 24: equal budget; CRBC Arequipa / Salvador–Itaparica already logged (miss).",
        "hunt_infra_port_ownership": "Cycle 24: equal budget; ICTSI Aratu logged C23 (miss).",
        "hunt_res_graphite": "Cycle 24: equal budget; South Star PO / Graphcoa set already logged (miss).",
        "hunt_res_nickel": "Cycle 24: equal budget; BNDES Piauí / Centaurus Jaguar set already logged (miss).",
        "hunt_latam_rail_telecom": "Cycle 24: equal budget; Alstom/CRRC/Siemens rail set already logged (miss).",
        "hunt_infra_engineering_epc": "Cycle 24: equal budget; STRACON / Worley Diablillos already logged (miss).",
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
    print("Cycle 24 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
