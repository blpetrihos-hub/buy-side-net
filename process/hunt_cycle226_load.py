#!/usr/bin/env python3
"""Cycle 226 hunt: shuffle_seed=20261226; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261226).shuffle):
other_renewables, rail, lithium, balsa, port_ownership, solar, wind, nickel,
power_plants_grid, port_cranes, niobium, graphite, copper, water, building_materials,
fission_smr, bridges_roads, engineering_epc.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    fission CapEx-fill (FINEP Diamante MRN R$50m); balsa/nickel dry.
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty sweeps (US blank-USD residual exhausted;
0 US CapEx-fills — honest residual).
PRC equal-budget: CRRC Motiva Line 4 + CRRC Salvador Metro + State Grid Mantiqueira
CapEx-fills; holdovers unsigned.
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
EUR_USD = "1.1400"


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
            "id": rid, "retrieved": "2026-10-04", "source_id": source_id, "url": url,
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


# 1. other_renewables / other — CapEx-fill WEG Itajaí BESS factory R$280m
row_doc(
    "weg_itajai_bess_280m_brl_2026",
    "energy", "other_renewables", "other",
    "WEG — Itajaí BESS systems factory (BNDES Mais Inovação)",
    "Brazil",
    "4 Feb 2026 WEG: announces new BESS systems factory; R$ 280 million BNDES Mais Inovação financing approved. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~53.93m for stored R$280m face.",
    "280000000", BRL_FX_DATE, "2026", "-26.91", "-48.66",
    "Itajaí, Santa Catarina (company geography).",
    "weg_itajai_bess_20260204",
    "Para viabilizar o projeto, a WEG contou com financiamento de R$ 280 milhões do programa BNDES Mais Inovação, aprovado no âmbito da chamada pública voltada à transformação de minerais estratégicos.",
    "https://www.weg.net/institutional/BR/pt/news/resultados-e-investimentos/weg-anuncia-nova-fabrica-de-sistemas-de-armazenamento-de-energia-em-baterias-bess-em-itajai-sc",
    "Actor: WEG (Brazil) — other. CapEx-fill: retain R$280m BNDES financing face; add Fed H.10 Sep 25 2026 FX to USD ~53.93m. Shuffle other_renewables.",
    "hunt_cycle226", investment_type="greenfield_plant", evidence="documented", currency="BRL",
    value_usd=str(round(280000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='WEG. “WEG anuncia nova fábrica de sistemas de armazenamento de energia em baterias (BESS) em Itajaí (SC).” February 4, 2026. https://www.weg.net/institutional/BR/pt/news/resultados-e-investimentos/weg-anuncia-nova-fabrica-de-sistemas-de-armazenamento-de-energia-em-baterias-bess-em-itajai-sc.',
    annotation="WEG Itajaí BESS CapEx-fill ~USD 53.93m via Fed H.10. Supports weg_itajai_bess_280m_brl_2026.",
    evid_note="Opened WEG Portuguese; R$280m BNDES Mais Inovação / Itajaí BESS factory confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. rail / prc — CapEx-fill CRRC Motiva Line 4 ~R$600m
row_doc(
    "crrc_motiva_line4_6trains_2026",
    "infrastructure", "rail", "prc",
    "CRRC Changchun — six trains for São Paulo Metro Line 4-Amarela (Motiva)",
    "Brazil",
    "31 Mar 2026 Metro CPTM: Motiva signs in China for six new trains for Line 4-Amarela from CRRC Changchun; planned investment about R$ 600 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~115.56m for stored R$600m face.",
    "600000000", BRL_FX_DATE, "2026", "-23.586", "-46.682",
    "São Paulo Metro Line 4-Amarela (press geography; metro line pin).",
    "metrocptm_crrc_line4_20260331",
    "A Motiva … assinou na China o contrato para a compra de seis novos trens destinados à Linha 4-Amarela … com a fabricante CRRC Changchun Railway Vehicles … O investimento previsto é de cerca de R$ 600 milhões",
    "https://www.metrocptm.com.br/motiva-fecha-compra-de-seis-novos-trens-para-a-linha-4-amarela-na-china/",
    "Actor: CRRC Changchun (PRC) — prc. CapEx-fill: retain ~R$600m; add Fed H.10 Sep 25 2026 FX to USD ~115.56m. Shuffle rail / PRC equal-budget.",
    "hunt_cycle226", investment_type="equipment", evidence="documented", currency="BRL",
    value_usd=str(round(600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Metrô CPTM. “Motiva fecha compra de seis novos trens para a Linha 4-Amarela na China.” March 31, 2026. https://www.metrocptm.com.br/motiva-fecha-compra-de-seis-novos-trens-para-a-linha-4-amarela-na-china/.',
    annotation="CRRC Motiva Line 4 CapEx-fill ~USD 115.56m via Fed H.10. Supports crrc_motiva_line4_6trains_2026.",
    evid_note="Opened Metro CPTM Portuguese; ~R$600m / six CRRC trains confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. rail / prc — CapEx-fill CRRC Salvador Metro R$490.4m
row_doc(
    "crrc_salvador_metro_2026",
    "infrastructure", "rail", "prc",
    "CRRC Changchun / CRRC Brasil — 10 four-car trainsets for Salvador metro",
    "Brazil",
    "17 Jul 2026 Railway Gazette: Bahia selects CRRC Changchun + CRRC Brasil consortium to supply 10 four-car metro trainsets for Salvador; contract value R$490.4m. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~94.45m for stored R$490.4m face.",
    "490400000", BRL_FX_DATE, "2026", "-12.97", "-38.51",
    "Salvador metro, Bahia (press geography).",
    "railwaygazette_salvador_crrc_20260717",
    "The Bahia state government has selected a consortium of CRRC Changchun Railway Vehicles and CRRC Brasil Equipamentos Ferroviários to supply 10 four-car metro trainsets for use in the city of Salvador. The contract has a value of R$490.4m ... CRRC’s bid beat rival Alstom’s R$614.4m offer.",
    "https://www.railwaygazette.com/metro-metro-categories/2026/07/17/crrc-wins-salvador-metro-train-order/",
    "Actor: CRRC (PRC) — prc. CapEx-fill: retain R$490.4m; add Fed H.10 Sep 25 2026 FX to USD ~94.45m. Shuffle rail / PRC equal-budget.",
    "hunt_cycle226", investment_type="equipment", evidence="documented", currency="BRL",
    value_usd=str(round(490400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Railway Gazette. “CRRC wins Salvador metro train order.” July 17, 2026. https://www.railwaygazette.com/metro-metro-categories/2026/07/17/crrc-wins-salvador-metro-train-order/.',
    annotation="CRRC Salvador CapEx-fill ~USD 94.45m via Fed H.10. Supports crrc_salvador_metro_2026.",
    evid_note="Opened Railway Gazette; R$490.4m / 10 four-car sets confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. power_plants_grid / prc — CapEx-fill State Grid Mantiqueira ~R$7bn
row_doc(
    "state_grid_mantiqueira_tx_2025",
    "energy", "power_plants_grid", "prc",
    "State Grid — Mantiqueira transmission line acquisition (from Quantum)",
    "Brazil",
    "28 Nov 2025 CNN Brasil: MME ceremony formalizes State Grid purchase of Mantiqueira transmission line from Quantum Participações; deal estimated at R$ 7 billion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1348.20m for stored R$7bn face.",
    "7000000000", BRL_FX_DATE, "2025", "-19.92", "-43.94",
    "Mantiqueira transmission corridor, Minas Gerais / Southeast Brazil (press geography; approximate).",
    "cnnbrasil_state_grid_mantiqueira_20251128",
    "O MME … cerimônia de assinatura do contrato que formaliza a compra da linha de transmissão Mantiqueira, atualmente pertencente à Quantum Participações, pela chinesa State Grid. … O negócio é estimado em R$ 7 bilhões.",
    "https://www.cnnbrasil.com.br/economia/investimentos/state-grid-assina-contrato-para-compra-da-linha-de-transmissao-mantiqueira-2/",
    "Actor: State Grid Corporation of China — prc. CapEx-fill: retain ~R$7bn deal estimate; add Fed H.10 Sep 25 2026 FX to USD ~1348.20m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle226", investment_type="mna_acquisition", evidence="documented", currency="BRL",
    value_usd=str(round(7000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='CNN Brasil. “State Grid assina contrato para compra da linha de transmissão Mantiqueira.” November 28, 2025. https://www.cnnbrasil.com.br/economia/investimentos/state-grid-assina-contrato-para-compra-da-linha-de-transmissao-mantiqueira-2/.',
    annotation="State Grid Mantiqueira CapEx-fill ~USD 1348.20m via Fed H.10. Supports state_grid_mantiqueira_tx_2025.",
    evid_note="Opened CNN Brasil Portuguese; ~R$7bn Mantiqueira acquisition confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. power_plants_grid / allied — CapEx-fill EDP South America R$7bn 2025–2026
row_doc(
    "edp_south_america_7bn_brl_2025_2026",
    "energy", "power_plants_grid", "allied",
    "EDP South America — 2025–2026 energy-transition CapEx plan",
    "Brazil",
    "18 Jun 2025 EDP: plans to invest R$ 7 billion between 2025 and 2026 to accelerate energy transition (solar/wind + grid). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1348.20m for stored R$7bn face.",
    "7000000000", BRL_FX_DATE, "2025", "", "",
    "EDP South America Brazil footprint (national multi-asset; no single-site pin).",
    "edp_sa_7bn_20250618",
    "The company plans to invest R$ 7 billion between 2025 and 2026 to accelerate the energy transition, consolidating its operations in solar and wind projects and expanding its presence in the grid segment.",
    "https://edp.com/en/south-america/brazil/media/news/edp-reinforces-energy-transition-actions-investment-r-7-billion",
    "Actor: EDP (Portugal) — allied. CapEx-fill: retain R$7bn 2025–2026 plan; add Fed H.10 Sep 25 2026 FX to USD ~1348.20m. Shuffle power_plants_grid.",
    "hunt_cycle226", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(7000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='EDP. “EDP reinforces energy transition actions with investment of R$ 7 billion.” June 18, 2025. https://edp.com/en/south-america/brazil/media/news/edp-reinforces-energy-transition-actions-investment-r-7-billion.',
    annotation="EDP SA CapEx-fill ~USD 1348.20m via Fed H.10. Supports edp_south_america_7bn_brl_2025_2026.",
    evid_note="Opened EDP English; R$7bn 2025–2026 plan confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. building_materials / other — CapEx-fill Votorantim Nobres/Cuiabá R$330m
row_doc(
    "votorantim_nobres_cuiaba_330m_2025",
    "infrastructure", "building_materials", "other",
    "Votorantim Cimentos — Cuiabá and Nobres plant expansion/modernization (Mato Grosso)",
    "Brazil",
    "4 Aug 2025 Votorantim Cimentos: R$330 million investment in Mato Grosso including expansions and modernization of Cuiabá and Nobres sites. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~63.56m for stored R$330m face.",
    "330000000", BRL_FX_DATE, "2025", "-14.72", "-56.33",
    "Cuiabá / Nobres, Mato Grosso (company geography; approximate regional pin).",
    "votorantim_nobres_cuiaba_20250804",
    "We announced today a R$330 million investment in the state of Mato Grosso, including expansions and the modernization of its sites located in the towns of Cuiabá and Nobres",
    "https://www.votorantimcimentos.com/news/we-announced-r330-million-investment-to-expand-and-modernize-cuiaba-and-nobres-plants-in-brazil/",
    "Actor: Votorantim Cimentos (Brazil) — other. CapEx-fill: retain R$330m; add Fed H.10 Sep 25 2026 FX to USD ~63.56m. Shuffle building_materials.",
    "hunt_cycle226", investment_type="plant_capex", evidence="documented", currency="BRL",
    value_usd=str(round(330000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Votorantim Cimentos. “We announced R$330 million investment to expand and modernize Cuiabá and Nobres plants in Brazil.” August 4, 2025. https://www.votorantimcimentos.com/news/we-announced-r330-million-investment-to-expand-and-modernize-cuiaba-and-nobres-plants-in-brazil/.',
    annotation="Votorantim Nobres/Cuiabá CapEx-fill ~USD 63.56m via Fed H.10. Supports votorantim_nobres_cuiaba_330m_2025.",
    evid_note="Opened Votorantim English; R$330m / Cuiabá+Nobres confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. fission_smr / other — CapEx-fill FINEP Diamante MRN R$50m (thin)
row_doc(
    "finep_diamante_mrn_50m_brl_2025",
    "energy", "fission_smr", "other",
    "MCTI / FINEP — Diamante microreactor program (R$50m total)",
    "Brazil",
    "17 Jun 2025 MCTI/FINEP: Diamante microreactor project total investment R$ 50 million (R$ 30m economic subsidy + R$ 20m counterpart from participating companies). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~9.63m for stored R$50m face. Distinct from brazil_microreactor_cnen_2025 dual-quote row.",
    "50000000", BRL_FX_DATE, "2025", "", "",
    "Brazil Diamante MRN program (national; site unnamed — coordinates blank).",
    "mcti_finep_mrn_20250617",
    "O projeto representa um investimento total de R$ 50 milhões, sendo R$ 30 milhões em subvenção econômica e R$ 20 milhões de contrapartida das empresas participantes.",
    "https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias/2025/06/mcti-e-finep-investem-r-30-milhoes-para-projeto-de-microrreator-nuclear",
    "Actor: MCTI/FINEP Brazilian public program — other. CapEx-fill: retain R$50m total; add Fed H.10 Sep 25 2026 FX to USD ~9.63m. Thin fission_smr top-up.",
    "hunt_cycle226", investment_type="rd_program", evidence="documented", currency="BRL",
    value_usd=str(round(50000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="government",
    chicago='Ministério da Ciência, Tecnologia e Inovação. “MCTI e Finep investem R$ 30 milhões para projeto de microrreator nuclear.” June 17, 2025. https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias/2025/06/mcti-e-finep-investem-r-30-milhoes-para-projeto-de-microrreator-nuclear.',
    annotation="FINEP Diamante CapEx-fill ~USD 9.63m via Fed H.10. Supports finep_diamante_mrn_50m_brl_2025.",
    evid_note="Opened MCTI Portuguese; R$50m total / R$30m subsidy + R$20m counterpart confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle226 added {len(added)}: {added}")
    print(f"cycle226 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
