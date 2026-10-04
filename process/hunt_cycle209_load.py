#!/usr/bin/env python3
"""Cycle 209 hunt: shuffle_seed=20261209; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261209).shuffle):
bridges_roads, rail, lithium, water, wind, port_cranes, niobium, port_ownership,
engineering_epc, other_renewables, graphite, building_materials, power_plants_grid,
copper, solar, fission_smr, balsa, nickel.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES Andes Hub/EXIM Argentina/DFC Patria/AquaCapital/
EnergyX/Nextracker/Array/Wabtec/Progress Rail/SSA/Glenfarne/Bechtel/Fluence/
USTDA/GE Vernova/Equinix/Microsoft/Freeport El Abra sweeps (0 new U.S. rows —
catalog dense; Freeport El Abra mill / Wabtec MRS / Equinix SP6 already logged).
PRC equal-budget: CRRC México-Pachuca / CHEC Fourth Bridge / CAMCE Punta Huete /
Envision Casa already logged; holdovers unsigned.
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
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
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
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
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


# 1. bridges_roads / other — EPR Régis Bittencourt BR-116/SP/PR concession R$7.2bn
row_doc(
    "epr_regis_bittencourt_7p2bn_2026",
    "infrastructure",
    "bridges_roads",
    "other",
    "EPR Participações S.A. — Autopista Régis Bittencourt (BR-116/SP/PR) concession transfer",
    "Brazil",
    "23 Jul 2026 ANTT: EPR Participações S.A. wins competitive process for Autopista Régis Bittencourt (BR-116/SP/PR, 383 km) with 22.53% discount on basic toll tariff; contract contemplates estimated investments of R$7.2 billion for capacity expansion, pavement recovery, conservation, maintenance, monitoring and operation through 2041. ANTT board homologated result 10 Sep 2026 (CNN Brasil / Agência iNFRA); CCVA signature and control transfer still pending post-homologation conditions. CapEx face = ANTT estimated R$7.2bn. Distinct from ecorodovias_rota_gerais_13bn_2026 and azevedo_rota_mogiana_9p4bn_brl_2026.",
    "7200000000",
    "",
    "2026",
    "",
    "",
    "BR-116/SP/PR Régis Bittencourt corridor São Paulo–Paraná (383 km multi-municipality; lat/lon blank).",
    "antt_epr_regis_bittencourt_20260723",
    "A EPR Participações S.A. venceu o leilão da concessão da BR-116/SP/PR (Régis Bittencourt) ao apresentar deságio de 22,53% sobre a tarifa básica de pedágio. … o contrato prevê investimentos estimados em R$ 7,2 bilhões destinados à ampliação da capacidade da rodovia, recuperação da infraestrutura e prestação dos serviços previstos no edital. … O novo contrato terá vigência até 2041",
    "https://www.gov.br/antt/pt-br/assuntos/noticias-defeso-eleitoral/epr-vence-o-leilao-da-concessao-da-regis-bittencourt-com-desagio-de-22-53",
    "Actor: EPR Participações S.A. (Brazilian concessionaire group) — other. Opened ANTT Portuguese primary 23 Jul 2026. CapEx face = R$7.2bn estimated investments; USD blank (Fed H.10 unreachable). Homologation Sep 2026; contract signature pending. Shuffle bridges_roads.",
    "hunt_cycle209",
    investment_type="concession",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='Agência Nacional de Transportes Terrestres (ANTT). “EPR vence o leilão da concessão da Régis Bittencourt com deságio de 22,53%.” July 23, 2026. https://www.gov.br/antt/pt-br/assuntos/noticias-defeso-eleitoral/epr-vence-o-leilao-da-concessao-da-regis-bittencourt-com-desagio-de-22-53.',
    annotation="ANTT EPR Régis Bittencourt R$7.2bn. Supports epr_regis_bittencourt_7p2bn_2026.",
    evid_note="Opened ANTT Portuguese primary 2026-10-04; R$7.2bn / 22.53% deságio / BR-116/SP/PR 383 km / vigência até 2041 confirmed.",
)

# 2. wind / allied — CapEx fill: Vestas Dom Inocêncio >BRL 5bn (floor)
row_doc(
    "vestas_dom_inocencio_br_2025",
    "energy",
    "wind",
    "allied",
    "Vestas / Casa dos Ventos — Dom Inocêncio Wind Complex (Piauí)",
    "Brazil",
    "828 MW order: 184 × V150-4.5 MW turbines + construction management + 25-year AOM 5000; project investment over BRL 5 billion (CapEx face filled as BRL 5.0bn floor from Vestas company primary); COD targeted 2028. Distinct from vestas_casa_dos_ventos_br_2023 (1,310 MW).",
    "5000000000",
    "",
    "2025",
    "-8.9",
    "-42.5",
    "South-central Piauí (Vestas release; approximate).",
    "vestas_dom_inocencio_20251217",
    "Casa dos Ventos ... and Vestas ... announce ... the 828 MW order for the Dom Inocêncio wind complex. ... The project will feature 184 V150-4.5 MW turbines ... The project represents a total investment of over BRL 5 billion",
    "https://www.vestas.com/en/media/company-news/2025/casa-dos-ventos-and-vestas-announce-new-partnership-for-c4283083",
    "Actor: Vestas (Danish) — allied; customer Casa dos Ventos (Brazilian). CapEx-fill upgrade: Vestas company primary states total investment over BRL 5 billion — face filled as BRL 5.0bn floor (was blank). USD blank (Fed H.10 unreachable). Shuffle wind.",
    "hunt_cycle209",
    investment_type="equipment_supply",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Vestas. “Casa dos Ventos and Vestas announce new partnership for the 828 MW Dom Inocêncio Wind Complex in Brazil.” December 17, 2025. https://www.vestas.com/en/media/company-news/2025/casa-dos-ventos-and-vestas-announce-new-partnership-for-c4283083.',
    annotation="Vestas Dom Inocêncio CapEx fill >BRL 5bn floor. Supports vestas_dom_inocencio_br_2025.",
    evid_note="Re-opened Vestas company primary 2026-10-04; CapEx-fill upgrade — over BRL 5 billion confirmed; face = BRL 5.0bn floor.",
)

# 3. other_renewables / other — Casa dos Ventos US private placement USD 1.1bn
row_doc(
    "casa_dos_ventos_us_pp_1p1bn_2026",
    "energy",
    "other_renewables",
    "other",
    "Casa dos Ventos S.A. — U.S. private debt placement (Ventos DC 1 + PAR-DOM IV notes)",
    "Brazil",
    "18 Jun 2026 Casa dos Ventos company: completes U.S. private debt raise totaling USD 1.1 billion (~R$5.6bn) via two simultaneous wholly-owned-subsidiary issuances — USD 825m 24-year fully amortizing notes and USD 252m 17-year partially amortizing notes — to finance part of wind and solar complexes in Ceará, Piauí and Mato Grosso do Sul plus Dom Inocêncio solar (Piauí) under dollar PPAs with Ascenty, Omnia and ByteDance. Placement agents: BNP Paribas, Goldman Sachs, MUFG. Issuer = Brazilian generator (TotalEnergies shareholder since 2022) — side other (U.S. market debt, not U.S. project owner). Distinct from vestas_dom_inocencio_br_2025 (OEM/CapEx) and nextracker_casa_dos_ventos_1p5gw_2025.",
    "1100000000",
    "2026-06-18",
    "2026",
    "",
    "",
    "Multi-state Brazil renewables package (CE/PI/MS); lat/lon blank.",
    "casa_dos_ventos_us_pp_20260618",
    "Casa dos Ventos has completed a private debt raise in the United States, totaling US$1.1 billion, equivalent to approximately R$5.6 billion. … The funds will finance part of the company's wind and solar complexes in Ceará, Piauí, and Mato Grosso do Sul, in addition to the Dom Inocêncio solar project in Piauí. … one for US$825 million, with a 24-year term, and another for US$252 million, with a 17-year term.",
    "https://casadosventos.com.br/en/news/captacao-nos-estados-unidos",
    "Actor: Casa dos Ventos S.A. (Brazilian renewables; TotalEnergies shareholder) — other. Company English primary 18 Jun 2026. CapEx/financing face = USD 1.1bn. U.S. private placement market / Goldman-BNP-MUFG agents do not re-side the issuer to us. Shuffle other_renewables.",
    "hunt_cycle209",
    investment_type="financing",
    evidence="documented",
    currency="USD",
    value_usd="1100000000",
    fx_usd="1",
    bib_type="company",
    chicago='Casa dos Ventos. “Casa dos Ventos raises US$ 1.1 billion in the United States.” June 18, 2026. https://casadosventos.com.br/en/news/captacao-nos-estados-unidos.',
    annotation="Casa dos Ventos US private placement USD 1.1bn. Supports casa_dos_ventos_us_pp_1p1bn_2026.",
    evid_note="Opened Casa dos Ventos English company primary 2026-10-04; USD 1.1bn / USD 825m + USD 252m / CE-PI-MS + Dom Inocêncio solar / Ascenty-Omnia-ByteDance PPAs / BNP-Goldman-MUFG confirmed.",
)

# 4. copper / allied — McEwen Los Azules FS initial CapEx USD 3.168bn
row_doc(
    "mcewen_los_azules_fs_3p17bn_2025",
    "resources",
    "copper",
    "allied",
    "McEwen Copper Inc. — Los Azules copper project Feasibility Study initial CapEx (San Juan)",
    "Argentina",
    "7 Oct 2025 McEwen Copper FS: Los Azules (San Juan) initial capital cost USD 3,168 million (~USD 3.17bn); after-tax NPV(8%) USD 2.9bn; IRR 19.8%; 21-year LOM average 148,200 t Cu/yr cathode; RIGI acceptance Sep 2025. Distinct from mcewen_los_azules_240m_2026 (USD 240m term loan toward FID).",
    "3168000000",
    "2025-10-07",
    "2025",
    "-31.2",
    "-70.0",
    "Los Azules, Calingasta, San Juan Province, Argentina (company geography; approximate pin).",
    "mcewen_los_azules_fs_20251007",
    "Initial Capital Cost | USD Millions | $3,168 … Initial capital expenditure $3.17 billion … Accepted into Argentina’s Large Investment Incentive Regime (RIGI) in September, 2025",
    "https://www.mcewenmining.com/investor-relations/press-releases/press-release-details/2025/Los-Azules-Feasibility-Study-Confirms-Economically-Robust-Copper-Project-With-Leading-ESG-Performance/",
    "Actor: McEwen Copper Inc. (46.3% McEwen Inc. NYSE/TSX:MUX — Canada/US-listed parent) — allied. Company FS primary 7 Oct 2025. CapEx face = USD 3,168m initial capital. Shuffle copper.",
    "hunt_cycle209",
    investment_type="greenfield_mine",
    evidence="documented",
    currency="USD",
    value_usd="3168000000",
    fx_usd="1",
    bib_type="company",
    chicago='McEwen Copper Inc. / McEwen Inc. “Los Azules Feasibility Study Confirms Economically Robust Copper Project With Leading ESG Performance.” October 7, 2025. https://www.mcewenmining.com/investor-relations/press-releases/press-release-details/2025/Los-Azules-Feasibility-Study-Confirms-Economically-Robust-Copper-Project-With-Leading-ESG-Performance/.',
    annotation="McEwen Los Azules FS initial CapEx USD 3.168bn. Supports mcewen_los_azules_fs_3p17bn_2025.",
    evid_note="Opened McEwen company FS primary 2026-10-04; Initial Capital Cost USD 3,168m / RIGI Sep 2025 confirmed.",
)

# 5. copper / allied — CapEx/source upgrade: McEwen Los Azules USD 240m term loan (company primary)
row_doc(
    "mcewen_los_azules_240m_2026",
    "resources",
    "copper",
    "allied",
    "McEwen Copper Inc. — Los Azules USD 240m senior secured term loan (toward FID)",
    "Argentina",
    "27 Aug 2026 McEwen Inc.: McEwen Copper closes USD 240 million senior secured 4-year term loan (Sprott NRIP USD 112m; Rob McEwen USD 85m; other lenders USD 43m) to advance engineering and early works at Los Azules (San Juan) toward FID targeted mid-2027 and commercial cathode production targeted 2030. Distinct from mcewen_los_azules_fs_3p17bn_2025 (FS initial CapEx USD 3.168bn).",
    "240000000",
    "2026-08-27",
    "2026",
    "-31.2",
    "-70.0",
    "Los Azules, Calingasta, San Juan Province, Argentina (company geography; approximate pin).",
    "mcewen_los_azules_termloan_20260827",
    "McEwen Copper Inc. … has closed a $240 million senior secured 4-year term loan facility with a syndicate of lenders (the “Term Loan”). Participants include Sprott Natural Resource Investment Partners for $112 million, and Rob McEwen … for $85 million; and other lenders for a total of $43 million. The proceeds of the Term Loan will be used to continue advancing engineering and early works of the Los Azules copper project in San Juan, Argentina",
    "https://www.mcewenmining.com/investor-relations/press-releases/press-release-details/2026/McEwen-Copper-Completes-US240-Million-Term-Loan-to-Advance-Los-Azules-Toward-Final-Investment-Decision/",
    "Actor: McEwen Copper Inc. (46.3% McEwen Inc. NYSE/TSX:MUX) — allied. Source upgrade from Bloomberg Línea UNVERIFIED proxy to McEwen company primary 27 Aug 2026. CapEx/financing face = USD 240m term loan. Shuffle copper.",
    "hunt_cycle209",
    investment_type="financing",
    evidence="documented",
    currency="USD",
    value_usd="240000000",
    fx_usd="1",
    bib_type="company",
    chicago='McEwen Inc. “McEwen Copper Completes US$240 Million Term Loan to Advance Los Azules Toward Final Investment Decision.” August 27, 2026. https://www.mcewenmining.com/investor-relations/press-releases/press-release-details/2026/McEwen-Copper-Completes-US240-Million-Term-Loan-to-Advance-Los-Azules-Toward-Final-Investment-Decision/.',
    annotation="McEwen Los Azules USD 240m term loan company primary. Supports mcewen_los_azules_240m_2026.",
    evid_note="Opened McEwen company primary 2026-10-04; USD 240m / Sprott USD 112m / Rob McEwen USD 85m / San Juan early works toward FID mid-2027 confirmed. Source upgrade from Bloomberg Línea proxy.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []
    updated = []

    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle209 added {len(added)}: {added}")
    print(f"cycle209 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
