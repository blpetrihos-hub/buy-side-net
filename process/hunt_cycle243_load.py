#!/usr/bin/env python3
"""Cycle 243 hunt: shuffle_seed=20261243; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261243).shuffle):
port_ownership, lithium, bridges_roads, port_cranes, other_renewables, niobium,
graphite, engineering_epc, fission_smr, balsa, water, copper, nickel, wind, solar,
building_materials, power_plants_grid, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes Chile construction+development CapEx
  >USD 1.9bn (2024–2027 company face); honest residual.
PRC equal-budget: NEW Envision Brazil SAF/net-zero park USD 1bn (Planalto/press).
Allied: NEW Neoenergia Coelba Oeste Baiano ~R$2bn nested; NEW Generadora
  Metropolitana Dune Plus USD 629m (Latham citing sponsor).
Skipped: Microsoft Chile IDC ecosystem USD 3.3bn; Envision company PR without
  dollar face (CapEx from Planalto/press only); ENGIE 2026 CapEx plan figure not
  cleanly extractable from IR PDF text; holdovers unsigned; thin dry.
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

BRL_USD = "5.1921"
BRL_FX_DATE = "2026-09-25"


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid, "layer": layer, "subcategory": subcategory, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": currency,
            "value_usd": value_usd, "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "", "year": year, "status": "active",
            "lat": lat, "lon": lon, "geo_note": geo, "evidence": evidence,
            "source_id": source_id, "note": note, "pair_id": "", "counterpart_side": "",
            "counterpart_actor": "", "counterpart_value": "", "counterpart_currency": "",
            "counterpart_value_usd": "", "gap": "",
        },
        {
            "id": rid, "retrieved": "2026-10-05", "source_id": source_id, "url": url,
            "price_year": year, "evidence": evidence, "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id, "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url, "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. other_renewables / us — NEW AES Andes Chile construction CapEx >USD 1.9bn 2024–2027
row_doc(
    "aes_andes_chile_capex_1p9bn_2024_2027",
    "energy", "other_renewables", "us",
    "AES Andes — Chile renewable construction + advanced-development CapEx (2024–2027)",
    "Chile",
    "22 Oct 2024 AES Andes Spanish: Andes Solar IV COD release — Chile has initiatives under construction totaling 572 MW renewable capacity plus an advanced-development portfolio >1,300 MW, with investment exceeding US$1.9 billion to be executed between 2024 and 2027. CapEx: enter USD 1.9bn floor face (company “superior a”). Distinct from aes_andes_solar_iii_hub_2026 cumulative hub >USD 1.3bn and from Altos/Llanos/Oriente SEA package rows.",
    "1900000000", "2024-10-22", "2024", "-23.65", "-70.40",
    "AES Andes Chile renewable hub / construction portfolio (Antofagasta regional pin).",
    "aes_andes_solar_iv_cod_1p9bn_capex_20241022",
    "En Chile, cuenta con iniciativas en construcción por 572 MW de capacidad renovable, además de una cartera de proyectos en etapa avanzada de desarrollo con más de 1.300 MW, todo esto con una inversión superior a los US$1.900 millones a ser realizada entre 2024 y 2027.",
    "https://www.aesandes.com/es/press-release/aes-andes-inicia-operacion-comercial-de-andes-solar-iv-y-ratifica-su-liderazgo-en",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW row: company Spanish CapEx floor >USD 1.9bn for Chile construction+advanced development 2024–2027. Envelope for construction-phase renewables/BESS (nested vs project-level COD/SEA rows). Shuffle other_renewables / U.S. ≥1/3 budget.",
    "hunt_cycle243", investment_type="greenfield_storage", evidence="documented", currency="USD",
    value_usd="1900000000", fx_usd="1", bib_type="company",
    chicago='AES Andes. “AES Andes inicia operación comercial de Andes Solar IV y ratifica su liderazgo en almacenamiento en baterías en Latinoamérica.” October 22, 2024. https://www.aesandes.com/es/press-release/aes-andes-inicia-operacion-comercial-de-andes-solar-iv-y-ratifica-su-liderazgo-en.',
    annotation="AES Chile CapEx NEW >USD 1.9bn 2024–2027. Supports aes_andes_chile_capex_1p9bn_2024_2027.",
    evid_note="Opened AES Andes Spanish; >US$1.900m 2024–2027 / 572 MW construction / >1,300 MW advanced development confirmed.",
)

# 2. other_renewables / prc — NEW Envision Brazil SAF / net-zero park USD 1bn
row_doc(
    "envision_brazil_saf_1bn_2025",
    "energy", "other_renewables", "prc",
    "Envision Energy — Brazil SAF / Net-Zero Industrial Park (sugarcane SAF + green H2/NH3)",
    "Brazil",
    "12 May 2025 Planalto/Agência Brasil coverage (via DATAGRO English paraphrase): Envision Energy to invest USD 1 billion in sustainable aviation fuel (SAF) from sugarcane in Brazil plus renewable-energy R&D center, announced during President Lula’s China visit; company PRNewswire same day confirms Net-Zero Industrial Park collaboration without stating the dollar face. CapEx: enter USD 1bn (UNVERIFIED press citing Planalto). Leave lat/lon empty (site not named).",
    "1000000000", "2025-05-12", "2025", "", "",
    "Brazil SAF / Net-Zero Industrial Park (site not named in sources; lat/lon blank).",
    "datagro_envision_saf_1bn_20250512",
    "According to the Planalto Palace, the recent meetings have contributed to further expanding Chinese investments in Brazil. The new agreements provide for an investment of US$1 billion in the production of renewable aviation fuel (SAF) from sugarcane, and the creation of a Research and Development (R&D) Center in the area of renewable energy.",
    "https://portal.datagro.com/en/12/agribusiness/979254/china-to-invest-usdollar1-billion-in-brazil-to-produce-sustainable-aviation-fuel-saf-from-sugarcane",
    "Actor: Envision Energy (PRC) — prc. NEW row: USD 1bn SAF CapEx via DATAGRO citing Planalto/Agência Brasil (UNVERIFIED press); company PR confirms park collaboration without dollar. Distinct from envision_casa_ventos_630mw_2026 turbine supply. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle243", investment_type="greenfield", evidence="press", currency="USD",
    value_usd="1000000000", fx_usd="1", bib_type="press",
    chicago='DATAGRO. “China to invest US$1 billion in Brazil to produce sustainable aviation fuel (SAF) from sugarcane.” May 12, 2025. https://portal.datagro.com/en/12/agribusiness/979254/china-to-invest-usdollar1-billion-in-brazil-to-produce-sustainable-aviation-fuel-saf-from-sugarcane.',
    annotation="Envision Brazil SAF NEW USD 1bn (press citing Planalto). Supports envision_brazil_saf_1bn_2025.",
    evid_note="Opened DATAGRO English citing Planalto; US$1bn SAF sugarcane + R&D center confirmed. CapEx enter USD 1bn UNVERIFIED press face.",
)

# 3. power_plants_grid / allied — NEW Neoenergia Coelba Oeste Baiano ~R$2bn
row_doc(
    "neoenergia_oeste_baiano_2bn_brl_2026",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Coelba — Oeste Baiano distribution expansion (~R$2bn nested)",
    "Brazil",
    "8 May 2026 Neoenergia company: within R$50bn 2026–2030 distribution cycle, Oeste Baiano (major irrigation/agribusiness pole) will receive about R$ 2 billion for electrical system expansion — 10 new substations and capacity expansion of 14 others, doubling installed capacity. CapEx: enter R$2bn nested face. Distinct from neoenergia_dist_50bn envelope and neoenergia_coelba_litoral_7bn_brl_2026.",
    "2000000000", "2026-05-08", "2026", "-12.15", "-45.00",
    "Oeste Baiano agribusiness / irrigation pole (Barreiras regional pin).",
    "neoenergia_coelba_oeste_baiano_2bn_20260508",
    "Já no Oeste baiano, um dos maiores polos de irrigação do Brasil e motor do agronegócio nacional, serão investidos cerca de R$ 2 bilhões na expansão do sistema elétrico da região, em continuidade a um plano robusto que já vem sendo executado nos últimos anos. O projeto prevê a construção de 10 novas subestações e a ampliação da capacidade de outras 14, duplicando a capacidade instalada",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia (Iberdrola Spain) — allied. NEW nested CapEx ~R$2bn Oeste Baiano within R$50bn cycle. Shuffle power_plants_grid.",
    "hunt_cycle243", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(2000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia Oeste Baiano NEW ~R$2bn ~USD 385.20m via Fed H.10. Supports neoenergia_oeste_baiano_2bn_brl_2026.",
    evid_note="Opened Neoenergia Portuguese; ~R$2bn Oeste Baiano / 10 new + 14 expanded substations confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. other_renewables / allied — NEW Generadora Metropolitana Dune Plus USD 629m
row_doc(
    "gen_metro_dune_plus_629m_2025",
    "energy", "other_renewables", "allied",
    "Generadora Metropolitana (AME / EDF) — Dune Plus hybrid BESS + PV (María Elena)",
    "Chile",
    "21 Nov 2025 Latham & Watkins (sponsor counsel): Generadora Metropolitana (AME + EDF power solutions Chile) begins construction of Dune Plus — total investment US$629 million; integrates Dune 333 MW / 4h BESS + La Pampina 186 MWp PV + 175 MW / 4h BESS at María Elena, Antofagasta; Codelco 15-year / 1,000 GWh offtake. CapEx: enter USD 629m. Distinct from powerchina_dune_plus_epc_chile_2025 (blank CapEx; Sungrow later named EPC in trade press).",
    "629000000", "2025-11-21", "2025", "-22.35", "-69.66",
    "María Elena commune, Antofagasta Region (company geography; municipal pin).",
    "latham_gen_metro_dune_plus_629m_20251121",
    "Generadora Metropolitana, a leading electricity generation company in Chile owned by AME and EDF power solutions Chile, announced it has officially begun construction on Dune Plus, one of the largest energy storage projects in Chile. With a total investment of US$629 million and financing secured from leading international banks, Dune Plus represents a large-scale hybrid project which combines photovoltaic generation with battery storage.",
    "https://www.lw.com/en/news/2025/11/latham-watkins-advises-generadora-metropolitana-on-construction-financing-for-dune-plus-energy",
    "Actor: Generadora Metropolitana — AME (Chile) + EDF (France) — allied. NEW row: Latham counsel release CapEx USD 629m (company Generadora page confirms construction without dollar; CapEx from counsel). Shuffle other_renewables.",
    "hunt_cycle243", investment_type="greenfield_storage", evidence="documented", currency="USD",
    value_usd="629000000", fx_usd="1", bib_type="company",
    chicago='Latham & Watkins LLP. “Latham & Watkins Advises Generadora Metropolitana on Construction Financing for Dune Plus Energy Storage Project.” November 21, 2025. https://www.lw.com/en/news/2025/11/latham-watkins-advises-generadora-metropolitana-on-construction-financing-for-dune-plus-energy.',
    annotation="Generadora Metropolitana Dune Plus NEW USD 629m. Supports gen_metro_dune_plus_629m_2025.",
    evid_note="Opened Latham English; US$629m / Dune+La Pampina / AME+EDF / María Elena confirmed. Companion company page https://www.generadora.cl/noticias/iniciamos-la-construccion-de-dune-plus-proyecto-de-almacenamiento-a-gran-escala/ (no CapEx).",
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
    added, updated = [], []
    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            existing = rows[by_id[rid]]
            for k, v in full.items():
                if k != "id" and v != "" and v is not None:
                    existing[k] = v
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
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
    print(f"cycle243 added {len(added)}: {added}")
    print(f"cycle243 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
