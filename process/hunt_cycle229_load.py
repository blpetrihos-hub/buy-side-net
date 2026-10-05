#!/usr/bin/env python3
"""Cycle 229 hunt: shuffle_seed=20261229; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261229).shuffle):
niobium, wind, rail, fission_smr, copper, water, building_materials, port_ownership,
port_cranes, nickel, power_plants_grid, solar, bridges_roads, other_renewables,
graphite, engineering_epc, balsa, lithium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
    (niobium CapEx-fill already in shuffle slot via St George A$60m).
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted; 0 new US CapEx — honest residual).
PRC equal-budget: CTG Serra da Palmeira CapEx-fill; holdovers unsigned.
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
EUR_FX_DATE = "2026-09-25"
AUD_USD = "0.7033"  # Fed H.10 Sep 25 2026 USD per AUD
AUD_FX_DATE = "2026-09-25"


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


# 1. NEW port_ownership / allied — CMPC Rio Grande TUP ~R$1.5bn
row_doc(
    "cmpc_rio_grande_tup_1p5bn_brl_2026",
    "infrastructure", "port_ownership", "allied",
    "CMPC / Neltume Ports — Terminal Rio Grande do Sul S.A. (TUP)",
    "Brazil",
    "14 Sep 2026 CMPC: on 11 Sep 2026 signed onerous assignment contract for Union area to install Terminal Rio Grande do Sul S.A. (private-use pulp terminal) at Porto de Rio Grande; port infrastructure investment approximately R$ 1.5 billion; ~400,000 m²; 25-year concession renewable; planned capacity up to 9 million tonnes/year (barge unload + ship load). JV with Neltume Ports / Sagres operations.",
    "1500000000", BRL_FX_DATE, "2026", "-32.13", "-52.10",
    "Porto de Rio Grande, Rio Grande do Sul (company geography).",
    "cmpc_rio_grande_tup_20260914",
    "O investimento na infraestrutura portuária será de cerca de R$ 1,5 bilhão, e a área será concedida por 25 anos, com possibilidade de renovação.",
    "https://www.cmpc.com/pt-br/assinamos-contrato-para-a-instalacao-do-terminal-rio-grande-do-sul-s-a/",
    "Actor: CMPC (Chilean pulp/paper) with Neltume Ports — allied. Company Portuguese primary. CapEx face ≈R$1.5bn; Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~288.90m. Shuffle port_ownership.",
    "hunt_cycle229", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CMPC. “Assinamos contrato para a instalação do Terminal Rio Grande do Sul S.A.” September 14, 2026. https://www.cmpc.com/pt-br/assinamos-contrato-para-a-instalacao-do-terminal-rio-grande-do-sul-s-a/.',
    annotation="CMPC Rio Grande TUP ~USD 288.90m via Fed H.10. Supports cmpc_rio_grande_tup_1p5bn_brl_2026.",
    evid_note="Opened CMPC Portuguese 2026-10-05; ~R$1.5bn / 25-year / up to 9 Mt/y / Neltume Ports confirmed.",
)

# 2. niobium / allied — CapEx-fill St George A$60m raise
row_doc(
    "st_george_araxa_raise_aud60m_2026",
    "resources", "niobium", "allied",
    "St George Mining — A$60m equity raise for Araxá rare earths/niobium project",
    "Brazil",
    "17 Jun 2026 ASX: St George Mining Limited received firm commitments to raise A$60 million (before costs) via two-tranche placement for Araxá Rare Earths & Niobium Project. CapEx-fill: Fed H.10 Sep 25 2026 Australia dollar 0.7033 USD/AUD → USD ~42.20m for stored A$60m face.",
    "60000000", AUD_FX_DATE, "2026", "-19.59", "-46.94",
    "Araxá project area, Minas Gerais (company geography).",
    "stgm_asx_aud60m_20260617",
    "St George Mining Limited (ASX: SGQ) (“St George” or “the Company”) is pleased to announce it has received firm commitments to raise A$60 million (before costs)",
    "https://www.stgm.com.au/pdf/daec3170-d1c5-4743-b8f8-3c6c12f7dd90/Platform/ListPage/A60M-secured-for-Araxa-Rare-EarthsNiobium-Project.pdf",
    "Actor: St George Mining (Australia ASX) — allied. CapEx-fill: retain A$60m raise face; add Fed H.10 Sep 25 2026 AUD FX to USD ~42.20m. Shuffle niobium (thin).",
    "hunt_cycle229", investment_type="equity_raise", evidence="documented", currency="AUD",
    value_usd=str(round(60000000 * float(AUD_USD), 2)), fx_usd=AUD_USD,
    chicago='St George Mining Limited. “A$60M Secured for Araxá Rare Earths & Niobium Project.” June 17, 2026. https://www.stgm.com.au/pdf/daec3170-d1c5-4743-b8f8-3c6c12f7dd90/Platform/ListPage/A60M-secured-for-Araxa-Rare-EarthsNiobium-Project.pdf.',
    annotation="St George Araxá CapEx-fill ~USD 42.20m via Fed H.10 AUD. Supports st_george_araxa_raise_aud60m_2026.",
    evid_note="Opened St George ASX PDF; A$60m firm commitments for Araxá REE/Nb confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 0.7033 USD/AUD.",
)

# 3. wind / prc — CapEx-fill CTG Serra da Palmeira R$4.327bn
row_doc(
    "ctg_serra_da_palmeira_2025",
    "energy", "wind", "prc",
    "CTG Brasil — Serra da Palmeira 648 MW wind (NDB total project cost)",
    "Brazil",
    "NDB project page: Serra da Palmeira 648-MW wind power project in Paraíba; total project cost BRL 4,327 million (NDB financing approval 17 Sep 2025); Goldwind Science & Technology named turbine supplier. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~833.38m for stored R$4.327bn face.",
    "4327000000", BRL_FX_DATE, "2025", "-7.12", "-35.88",
    "Serra da Palmeira wind project, Paraíba (NDB geography).",
    "ndb_serra_da_palmeira_2025",
    "NDB will finance the construction of the Serra da Palmeira power project, a 648-MW wind power project in the State of Paraíba, Brazil.",
    "https://www.ndb.int/project/serra-da-palmeira-wind-power-project/",
    "Actor: CTG Brasil / China Three Gorges — prc. CapEx-fill: retain NDB total project cost R$4.327bn; add Fed H.10 Sep 25 2026 FX to USD ~833.38m. Shuffle wind.",
    "hunt_cycle229", investment_type="ownership_equity", evidence="documented", currency="BRL",
    value_usd=str(round(4327000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='New Development Bank. “Serra da Palmeira Wind Power Project.” https://www.ndb.int/project/serra-da-palmeira-wind-power-project/.',
    annotation="CTG Serra da Palmeira CapEx-fill ~USD 833.38m via Fed H.10. Supports ctg_serra_da_palmeira_2025.",
    evid_note="Opened NDB project page; 648 MW / BRL 4,327m total cost confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. wind / allied — CapEx-fill Statkraft/WEG Seabra R$130m
row_doc(
    "weg_statkraft_seabra_7mw_2025",
    "energy", "wind", "allied",
    "Statkraft / WEG / Petrobras — Seabra 7 MW onshore wind innovation project",
    "Brazil",
    "18 Sep 2025 Statkraft: Petrobras–WEG–Statkraft put into operation a 7 MW WEG onshore aerogenerator at Seabra; project is result of Petrobras R$130 million innovation investment. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~25.04m for stored R$130m face.",
    "130000000", BRL_FX_DATE, "2025", "-12.42", "-41.77",
    "Seabra, Bahia (company geography).",
    "statkraft_weg_seabra_20250918",
    "O projeto é resultado de um investimento de R$130 milhões da Petrobrás ... E como parte do investimento em inovação tecnológica, o aerogerador",
    "https://www.statkraft.com.br/sala-de-comunicacao/ultimas-noticias/2025/parceria-inovadora-entre-petrobras-weg-e-statkraft-coloca-em-operacao-o-maior-aerogerador-onshore-das-americas/",
    "Actor: Statkraft (Norway — allied) with WEG OEM; Petrobras innovation spend. CapEx-fill: retain R$130m; add Fed H.10 Sep 25 2026 FX to USD ~25.04m. Shuffle wind.",
    "hunt_cycle229", investment_type="innovation_capex", evidence="documented", currency="BRL",
    value_usd=str(round(130000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Statkraft Brasil. “Parceria inovadora entre Petrobras, WEG e Statkraft coloca em operação o maior aerogerador onshore das Américas.” September 18, 2025. https://www.statkraft.com.br/sala-de-comunicacao/ultimas-noticias/2025/parceria-inovadora-entre-petrobras-weg-e-statkraft-coloca-em-operacao-o-maior-aerogerador-onshore-das-americas/.',
    annotation="Statkraft/WEG Seabra CapEx-fill ~USD 25.04m via Fed H.10. Supports weg_statkraft_seabra_7mw_2025.",
    evid_note="Opened Statkraft Portuguese; R$130m / 7 MW Seabra confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. rail / allied — CapEx-fill VLI FCA ~R$1.2bn 2026
row_doc(
    "vli_fca_capex_1p2bn_brl_2026",
    "infrastructure", "rail", "allied",
    "VLI — Ferrovia Centro-Atlântica 2026 CapEx (~R$1.2bn)",
    "Brazil",
    "5 Feb 2026 VLI: prepara investimento de cerca de R$ 1,2 bilhão na malha FCA em 2026 (fourth consecutive year >R$1bn); 2023–2026 cumulative ~R$4.8bn. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~231.12m for stored R$1.2bn face.",
    "1200000000", BRL_FX_DATE, "2026", "", "",
    "FCA network (MG/ES/GO/BA/SP); no single-site pin.",
    "vli_fca_1p2bn_20260205",
    "a VLI – companhia de soluções logísticas que opera ferrovias, portos e terminais – prepara investimento de cerca de R$ 1,2 bilhão nesta malha ferroviária",
    "https://www.vli-logistica.com.br/vli-mantem-investimento-na-fca-acima-de-r-1-bilhao-pelo-quarto-ano-consecutivo/",
    "Actor: VLI (Vale/Brookfield/Mitsui logistics) — allied. CapEx-fill: retain ~R$1.2bn 2026 FCA CapEx; add Fed H.10 Sep 25 2026 FX to USD ~231.12m. Shuffle rail.",
    "hunt_cycle229", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(1200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='VLI Logística. “VLI mantém investimento na FCA acima de R$ 1 bilhão pelo quarto ano consecutivo.” February 5, 2026. https://www.vli-logistica.com.br/vli-mantem-investimento-na-fca-acima-de-r-1-bilhao-pelo-quarto-ano-consecutivo/.',
    annotation="VLI FCA CapEx-fill ~USD 231.12m via Fed H.10. Supports vli_fca_capex_1p2bn_brl_2026.",
    evid_note="Opened VLI Portuguese; ~R$1.2bn 2026 FCA CapEx confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. rail / allied — CapEx-fill Alstom Mexico DMU (company EUR 920m dual)
row_doc(
    "alstom_mexico_dmu_2025",
    "infrastructure", "rail", "allied",
    "Alstom — 47 DMU trains + 5-year maintenance (Mexico Trenes del Norte)",
    "Mexico",
    "26 Dec 2025 Alstom: contract with ARTF for 47 DMU passenger trains + 5-year maintenance/depots for Mexico City–Querétaro–Irapuato and Saltillo–Monterrey–Nuevo Laredo corridors; valued at approximately MXN 20.2 billion (approximately EUR 920 million). CapEx-fill: enter company dual EUR 920m × Fed H.10 Sep 25 2026 EUR 1.1400 → USD 1,048.80m (retain MXN 20.2bn face).",
    "20200000000", "2025-12-26", "2025", "19.4326", "-99.1332",
    "Alstom Mexico Trenes del Norte corridors (CDMX pin; manufacture Ciudad Sahagún).",
    "alstom_mexico_47trains_20251226",
    "The contract is valued at approximately 20,2 billion Mexican pesos (approximately 920 million euros)",
    "https://www.alstom.com/press-releases-news/2025/12/alstom-supply-47-trains-and-associated-maintenance-new-rail-corridors-mexico",
    "Actor: Alstom (France) — allied. CapEx-fill: company dual EUR 920m → USD 1,048.80m via Fed H.10 EUR. Shuffle rail.",
    "hunt_cycle229", investment_type="equipment_supply", evidence="documented", currency="MXN",
    value_usd=str(round(920000000 * float(EUR_USD), 2)),
    fx_usd=str(round(20200000000 / (920000000 * float(EUR_USD)), 4)),
    chicago='Alstom. “Alstom to supply 47 trains and associated maintenance for new rail corridors in Mexico.” December 26, 2025. https://www.alstom.com/press-releases-news/2025/12/alstom-supply-47-trains-and-associated-maintenance-new-rail-corridors-mexico.',
    annotation="Alstom Mexico DMU CapEx-fill company EUR 920m → ~USD 1048.80m via Fed H.10. Supports alstom_mexico_dmu_2025.",
    evid_note="Opened Alstom English; MXN 20.2bn / EUR 920m dual / 47 DMU confirmed. CapEx-fill uses company EUR × Fed H.10 Sep 25 2026 1.1400.",
)

# 7. rail / allied — CapEx-fill Sacyr Fortaleza Metro Leste ~R$1.231bn
row_doc(
    "sacyr_fortaleza_metro_leste_1230m_brl_2026",
    "infrastructure", "rail", "allied",
    "Sacyr — Fortaleza Metro Leste integrated construction (three stations package)",
    "Brazil",
    "Ceará government award notice: Sacyr Construccion S/A do Brasil declared winner for integrated construction of three Metro Leste stations package; stored face R$1,230,612,738. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~237.02m for stored face.",
    "1230612738", BRL_FX_DATE, "2026", "-3.73", "-38.52",
    "Fortaleza Metro Leste, Ceará (award geography).",
    "atlas_publico_sacyr_fortaleza_20260918",
    "A empresa Sacyr Construccion S/A do Brasil foi declarada vencedora da licitação para a contratação integrada da construção de três",
    "https://atlaspublico.com.br/noticias/governo-do-ceara-declara-sacyr-vencedora-de-licitacao-para-87968",
    "Actor: Sacyr (Spain) — allied. CapEx-fill: retain R$1.2306bn award face; add Fed H.10 Sep 25 2026 FX to USD ~237.02m. Shuffle rail.",
    "hunt_cycle229", investment_type="epc", evidence="documented", currency="BRL",
    value_usd=str(round(1230612738 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Atlas Público / Governo do Ceará. “Governo do Ceará declara Sacyr vencedora de licitação” (Metro Leste). 2026. https://atlaspublico.com.br/noticias/governo-do-ceara-declara-sacyr-vencedora-de-licitacao-para-87968.',
    annotation="Sacyr Fortaleza Metro CapEx-fill ~USD 237.02m via Fed H.10. Supports sacyr_fortaleza_metro_leste_1230m_brl_2026.",
    evid_note="Opened Atlas Público award notice; Sacyr winner / stored R$1.2306bn face CapEx-filled via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 8. water / allied — CapEx-fill ACCIONA BRK Pernambuco (company EUR 2.68bn dual)
row_doc(
    "acciona_brk_pernambuco_sanitation_2026",
    "resources", "water", "allied",
    "ACCIONA / BRK — Pernambuco sanitation concession (153 municipalities)",
    "Brazil",
    "29 Apr 2026 ACCIONA: 35-year concession with BRK for basic sanitation in 153 municipalities + district in Pernambuco; investment of BRL 15.4 billion (€2.68 billion). CapEx-fill: enter company dual EUR 2.68bn × Fed H.10 Sep 25 2026 EUR 1.1400 → USD 3,055.20m (retain BRL 15.4bn face).",
    "15400000000", "2026-04-29", "2026", "-8.05", "-34.90",
    "Pernambuco state sanitation concession (Recife metro pin).",
    "acciona_pernambuco_20260429",
    "The 35-year agreement includes an investment of BRL 15.4 billion (€2.68 billion) to expand and modernize the region’s water supply and urban sanitation infrastructure.",
    "https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-153-municipalities-pernambuco-brazil",
    "Actor: ACCIONA (Spain) with BRK — allied. CapEx-fill: company dual EUR 2.68bn → USD 3,055.20m via Fed H.10 EUR. Shuffle water.",
    "hunt_cycle229", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(2680000000 * float(EUR_USD), 2)),
    fx_usd=str(round(15400000000 / (2680000000 * float(EUR_USD)), 4)),
    chicago='ACCIONA. “ACCIONA signs sanitation contract for 153 municipalities in Pernambuco (Brazil).” April 29, 2026. https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-153-municipalities-pernambuco-brazil.',
    annotation="ACCIONA BRK Pernambuco CapEx-fill company EUR 2.68bn → ~USD 3055.20m via Fed H.10. Supports acciona_brk_pernambuco_sanitation_2026.",
    evid_note="Opened ACCIONA English; BRL 15.4bn / EUR 2.68bn dual / 153 municipalities confirmed. CapEx-fill uses company EUR × Fed H.10 Sep 25 2026 1.1400.",
)

# 9. power_plants_grid / other — CapEx-fill WEG Brazil transformers R$543m
row_doc(
    "weg_brazil_xfmr_543m_brl_2024",
    "energy", "power_plants_grid", "other",
    "WEG — Brazil transformer capacity expansion (~R$543m)",
    "Brazil",
    "25 Sep 2024 WEG: investment plan of approximately R$ 543 million to increase transformer production capacity in Brazil over next two years (Betim MG ~R$370m; Gravataí RS ~R$128m). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~104.58m for stored R$543m face.",
    "543000000", BRL_FX_DATE, "2024", "-19.968", "-44.198",
    "WEG Betim (MG) primary expansion pin; also Gravataí RS.",
    "weg_brazil_xfmr_20240925",
    "WEG announces an investment plan of approximately R$ 543 million to increase transformer production capacity in Brazil. The investments will be made over the next two years in manufacturing units located in Minas Gerais and Rio Grande do Sul.",
    "https://www.weg.net/institutional/GE/en/news/result-and-investiments/weg-announces-investments-to-expand-transformer-production-capacity-in-brazil",
    "Actor: WEG (Brazilian) — other (host-country industrial). CapEx-fill: retain R$543m; add Fed H.10 Sep 25 2026 FX to USD ~104.58m. Shuffle power_plants_grid.",
    "hunt_cycle229", investment_type="capex_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(543000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='WEG. “WEG announces investments to expand transformer production capacity in Brazil.” September 25, 2024. https://www.weg.net/institutional/GE/en/news/result-and-investiments/weg-announces-investments-to-expand-transformer-production-capacity-in-brazil.',
    annotation="WEG Brazil transformer CapEx-fill ~USD 104.58m via Fed H.10. Supports weg_brazil_xfmr_543m_brl_2024.",
    evid_note="Opened WEG English; R$543m / Betim+Gravataí confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle229 added {len(added)}: {added}")
    print(f"cycle229 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
