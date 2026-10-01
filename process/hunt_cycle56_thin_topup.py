#!/usr/bin/env python3
"""Cycle 56 thin_topup: 3 thinnest after equal pass.

Post-equal thinnest (active+hunt, evidence documented|proxy|hunt):
balsa ~20, niobium ~20, power_plants_grid ~20.
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
# thin 1 energy/power_plants_grid — GE Vernova Arauco Sucuriú GIS (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ge_vernova_arauco_sucuriu_gis_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "GE Vernova — Arauco Sucuriú 230 kV GIS + transformers (MS)",
        "country": "Brazil",
        "asset": "14 Aug 2025 Megawhat (quoting GE Vernova LatAm Grid Systems Integration): GE Vernova contracted by Arauco Papel e Celulose to supply a 230 kV gas-insulated substation (GIS) for the Sucuriú bleached-eucalyptus pulp mill at Inocência, Mato Grosso do Sul, plus five power transformers, a 230 kV insulated cable transmission segment, and expansion of Ilha Solteira 2 substation to connect industrial loads and the project's captive 432 MW thermal plant (220 MW to SIN). Mill CapEx cited ~USD 4.6bn (Arauco) — not GE contract value. Distinct from ge_vernova_serra_tigre_ais_2023 / ge_vernova_transelec_sync_chile_2024 / ge_vernova_azulao_i_cod_2026.",
        "investment_type": "epc_equipment",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.73",
        "lon": "-51.93",
        "geo_note": "Inocência, Mato Grosso do Sul (Sucuriú mill / GIS site, approximate municipal pin).",
        "evidence": "documented",
        "source_id": "megawhat_ge_arauco_gis_20250814",
        "note": "Actor: GE Vernova (U.S.-listed) Grid Solutions equipment/EPC supply — us. Contract value not disclosed; Arauco mill CapEx USD 4.6bn is plant-level context only (not booked as GE value).",
    },
    {
        "id": "ge_vernova_arauco_sucuriu_gis_2025",
        "retrieved": "2026-10-01",
        "source_id": "megawhat_ge_arauco_gis_20250814",
        "url": "https://megawhat.uol.com.br/economia-e-politica/empresas/ge-vernova-fornecera-subestacao-gis-para-fabrica-de-celulose-da-arauco-no-ms/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "A GE Vernova fechou contrato com a Arauco Papel e Celulose para fornecer uma subestação de energia isolada a gás (GIS) de 230 kV na primeira fábrica de celulose branqueada de eucalipto da companhia no Brasil, localizada no município de Inocência, no Mato Grosso do Sul. … O acordo entre as empresas também inclui o fornecimento de cinco transformadores de potência, além de um trecho de linha de transmissão em cabo isolado 230kV e ampliação da subestação Ilha Solteira 2.",
        "note": "Opened Megawhat with named GE Vernova LatAm executive quote on Sucuriú GIS scope.",
    },
    {
        "id": "megawhat_ge_arauco_gis_20250814",
        "type": "press",
        "chicago": "Souto, Poliana. “GE Vernova Fornecerá Subestação GIS para Fábrica de Celulose da Arauco no MS.” Megawhat / UOL, 14 August 2025.",
        "url": "https://megawhat.uol.com.br/economia-e-politica/empresas/ge-vernova-fornecera-subestacao-gis-para-fabrica-de-celulose-da-arauco-no-ms/",
        "annotation": "Opened Brazilian energy press quoting GE Vernova on Sucuriú 230 kV GIS package. Supports ge_vernova_arauco_sucuriu_gis_2025.",
        "supports": ["ge_vernova_arauco_sucuriu_gis_2025", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# thin 2 resources/balsa — CoreLite Los Ríos 2,500 ha plantation PPP (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "corelite_los_rios_2500ha_plantation_2020",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "CoreLite — Los Ríos Province 2,500 ha balsa plantation PPP",
        "country": "Ecuador",
        "asset": "2 Dec 2020 CoreLite company release: long-term balsa plantation cooperation agreement with Government of Los Ríos Province covering planting and harvesting over five years with a target of 2,500 hectares; framed as wind-energy raw-material supply for CoreLite Balsasud panels. Distinct from corelite_balsasud_ecuador_presence (factory presence only) and plantabal_2025_planting_2951ha (3A/Plantabal).",
        "investment_type": "plantation",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2020",
        "status": "active",
        "lat": "-1.67",
        "lon": "-79.46",
        "geo_note": "Los Ríos Province, Ecuador (Quevedo / provincial plantation program, approximate).",
        "evidence": "documented",
        "source_id": "corelite_los_rios_20201202",
        "note": "Actor: CoreLite (Miami, U.S.) plantation PPP — us. Hectare target documented; CapEx not disclosed.",
    },
    {
        "id": "corelite_los_rios_2500ha_plantation_2020",
        "retrieved": "2026-10-01",
        "source_id": "corelite_los_rios_20201202",
        "url": "https://www.corelitecomposites.com/blogs/post/CoreLite-Signs-Agreement-with-Local-Government-for-Balsa-Wood-Supply",
        "price_year": "2020",
        "evidence": "documented",
        "quote": "CoreLite has signed a long-term Balsa Wood plantation cooperation agreement with the local Government of Los Rios Province in Ecuador during a public ceremony on Wednesday December 2, 2020. This agreement entails the planting and harvesting of Balsa Wood plantations throughout Los Rios Province over a 5-year period with a target number of 2,500 hectares of Balsa Wood plantations.",
        "note": "Opened CoreLite primary on Los Ríos 2,500 ha plantation PPP.",
    },
    {
        "id": "corelite_los_rios_20201202",
        "type": "company",
        "chicago": "CoreLite. “CoreLite Signs Agreement with Local Government for Balsa Wood Supply.” 2 December 2020.",
        "url": "https://www.corelitecomposites.com/blogs/post/CoreLite-Signs-Agreement-with-Local-Government-for-Balsa-Wood-Supply",
        "annotation": "CoreLite primary on Los Ríos Province 2,500 ha balsa plantation agreement. Supports corelite_los_rios_2500ha_plantation_2020.",
        "supports": ["corelite_los_rios_2500ha_plantation_2020", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# thin 3 resources/niobium — Auxico Minastyc mining title / Nb samples (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "auxico_minastyc_title_nb_2023",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "Auxico Resources — Minastyc mining title (Vichada; Nb-bearing)",
        "country": "Colombia",
        "asset": "Auxico Resources Canada (CSE:AUAG) exclusive operating agreement and Mining Registration Certificate (#CRM-202308221848-479897) for Minastyc title LFH-14431X (188 ha), Puerto Carreño, Vichada, valid through 21 Aug 2040; pit-sample concentrates reported up to 8.15%–25.44% Nb alongside Sn/Ta/Ti. Small-scale Phase 1 tin-concentrate plan up to 300 t/month. Distinct from CBMM/CMOC/Taboca Brazil rows. CapEx not disclosed.",
        "investment_type": "permit",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "6.18",
        "lon": "-67.49",
        "geo_note": "Minastyc / ~12 km south of Puerto Carreño, Vichada, Colombia (approximate).",
        "evidence": "documented",
        "source_id": "auxico_minastyc_title_2023",
        "note": "Actor: Auxico Resources (Canada-listed) — allied. Title/operating rights documented; Nb grades from company sampling releases; no CapEx figure on opened pages.",
    },
    {
        "id": "auxico_minastyc_title_nb_2023",
        "retrieved": "2026-10-01",
        "source_id": "auxico_minastyc_title_2023",
        "url": "https://www.newswire.ca/news-releases/auxico-signs-exclusive-operating-agreement-and-receives-mining-title-certificate-for-minastyc-project-in-colombia-852585066.html",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "The Minastyc Project mining title covers a total area of 188 hectares in Puerto Carreño, department of Vichada, Colombia, a prolific critical mineral property with sampled grades up to 62.13% tin, among rare earth elements, tantalum, niobium, and others. … These samples indicated grades up to 62.13% tin, 25.08% tantalum, 15.50% titanium and 8.15% niobium",
        "note": "Opened CNW/newswire on Auxico Minastyc title and Nb-bearing sample grades.",
    },
    {
        "id": "auxico_minastyc_title_2023",
        "type": "company",
        "chicago": "Auxico Resources Canada Inc. “Auxico Signs Exclusive Operating Agreement and Receives Mining Title Certificate for Minastyc Project in Colombia.” CNW Newswire, 2023.",
        "url": "https://www.newswire.ca/news-releases/auxico-signs-exclusive-operating-agreement-and-receives-mining-title-certificate-for-minastyc-project-in-colombia-852585066.html",
        "annotation": "Auxico primary/newswire on Minastyc title and Nb sample grades. Supports auxico_minastyc_title_nb_2023.",
        "supports": ["auxico_minastyc_title_nb_2023", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# equal overflow — ISA ENERGIA Serra Dourada R$ 3.2bn CapEx (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "isa_energia_serra_dourada_3p2bn_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "ISA ENERGIA BRASIL — Serra Dourada transmission CapEx (ANEEL)",
        "country": "Brazil",
        "asset": "9 Dec 2025 ISA ENERGIA BRASIL: Projeto Serra Dourada (ANEEL Transmission Auction 01/2023 Lot 1) CapEx ANEEL R$ 3.2 billion; five 500 kV lines totaling 1,097 km (Bahia–Norte de Minas) plus substations Campo Formoso II, Barra II, and Correntina; RAP R$ 322 million (2025/2026 cycle); energization target Mar 2029. Colombian-controlled ISA is controlling shareholder. Distinct from GE Vernova equipment deliveries into Barra II sync condenser (separate actor/row if logged).",
        "investment_type": "capex",
        "value": "3200000000",
        "currency": "BRL",
        "value_usd": "580000000",
        "fx_usd": "0.18125",
        "fx_date": "2025-12-09",
        "year": "2025",
        "status": "active",
        "lat": "-11.09",
        "lon": "-43.14",
        "geo_note": "Barra II substation area, western Bahia (approximate Barra pin among project SEs).",
        "evidence": "proxy",
        "source_id": "isa_serra_dourada_20251209",
        "note": "Actor: ISA ENERGIA BRASIL (Colombian ISA control) — allied. CapEx ANEEL R$ 3.2bn documented; USD ~580m is UNVERIFIED FX proxy at ~5.52 BRL/USD on announcement date.",
    },
    {
        "id": "isa_energia_serra_dourada_3p2bn_2025",
        "retrieved": "2026-10-01",
        "source_id": "isa_serra_dourada_20251209",
        "url": "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/projeto-serra-dourada-isa-energia-brasil-avanca-com-o-maior-investimento-em-transmissao-de-energia-renovavel-em-construcao-no-estado-da-bahia/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "Com investimento de R$ 3,2 bilhões (Capex ANEEL), o empreendimento é considerado um projeto prioritário do Programa de Aceleração do Crescimento (PAC) … O projeto contempla a construção de cinco linhas de transmissão aérea em 500 kV, com 1.097 km de extensão … três novas subestações (Campo Formoso II, Barra II e Correntina)",
        "note": "Opened ISA ENERGIA BRASIL primary; USD conversion UNVERIFIED proxy.",
    },
    {
        "id": "isa_serra_dourada_20251209",
        "type": "company",
        "chicago": "ISA ENERGIA BRASIL. “Projeto Serra Dourada: ISA ENERGIA BRASIL Avança com o Maior Investimento em Transmissão de Energia Renovável em Construção no Estado da Bahia.” 9 December 2025.",
        "url": "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/projeto-serra-dourada-isa-energia-brasil-avanca-com-o-maior-investimento-em-transmissao-de-energia-renovavel-em-construcao-no-estado-da-bahia/",
        "annotation": "ISA primary on Serra Dourada R$ 3.2bn Capex ANEEL. Supports isa_energia_serra_dourada_3p2bn_2025.",
        "supports": ["isa_energia_serra_dourada_3p2bn_2025", "hunt_br_power_equip"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None and k != "supports":
                existing[k] = v
        supports = list(
            dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or []))
        )
        existing["supports"] = supports
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added = []

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
        "hunt_br_power_equip": "Cycle 56 thin_topup: logged ge_vernova_arauco_sucuriu_gis_2025 (U.S.) + isa_energia_serra_dourada_3p2bn_2025 (allied overflow).",
        "hunt_res_balsa": "Cycle 56 thin_topup: logged corelite_los_rios_2500ha_plantation_2020 (U.S.; 2,500 ha Los Ríos PPP).",
        "hunt_fenb_araxa": "Cycle 56 thin_topup: logged auxico_minastyc_title_nb_2023 (allied; Colombia Minastyc Nb-bearing title).",
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
    print("Cycle 56 thin_topup rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
