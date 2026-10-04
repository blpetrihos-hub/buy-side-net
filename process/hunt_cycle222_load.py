#!/usr/bin/env python3
"""Cycle 222 hunt: shuffle_seed=20261222; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261222).shuffle):
building_materials, port_ownership, fission_smr, nickel, water, engineering_epc,
graphite, port_cranes, power_plants_grid, other_renewables, balsa, solar, lithium,
bridges_roads, copper, rail, niobium, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry; next-thinnest niobium CapEx-fill (St George Araxá ~R$3bn).
≥1/3 U.S. hunt budget spent on new SSA Lázaro TEA Polígono 5 CapEx row + NADBank
San Quintín CapEx-fill + Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/SSA sweeps (1 new US + 1 US CapEx-fill; catalog dense).
PRC equal-budget: CPFL FY2025 CapEx + CTG Brasil H2V CapEx-fills; Huaxin CSN bid
still pre-close M&A (skipped); holdovers unsigned (CHEC San Carlos Contraloría
aval but contract not yet signed).
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
MXN_USD = "17.6932"
MXN_FX_DATE = "2026-09-25"


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


# 1. NEW port_ownership / us — SSA Lázaro TEA Polígono 5 MXN 54.2m
row_doc(
    "ssa_lazaro_tea_poligono5_mxn54m_2025",
    "infrastructure", "port_ownership", "us",
    "SSA Marine México — TEA Polígono 5 vehicle-terminal expansion (Lázaro Cárdenas)",
    "Mexico",
    "2025 (Alera SCI 18 Mar 2026 roundup): SSA Marine México expands Terminal Especializada de Automóviles (TEA) at Polígono 5, Lázaro Cárdenas — 36,616.32 m² area; +1,500-unit capacity; investment MXN 54.2 million. Distinct from ssa_lazaro_isla_palma_mxn143m_2025 external yard CapEx-fill.",
    "54200000", MXN_FX_DATE, "2025", "17.96", "-102.17",
    "TEA Polígono 5, Puerto Lázaro Cárdenas, Michoacán (press geography).",
    "alerasci_ssa_mexico_20260318",
    "En Lázaro Cárdenas, Michoacán, SSA Marine México fortaleció su operación en el manejo de vehículos con la expansión de la Terminal Especializada de Autos (TEA), en el Polígono 5, con un área de 36,616.32 m². Esta ampliación incrementa la capacidad de la terminal en 1,500 unidades… La inversión realizada para esta expansión ascendió a 54.2 millones de pesos.",
    "https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/",
    "Actor: SSA Marine / Carrix (U.S.) via SSA Marine México — us. CapEx MXN 54.2m; Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~3.06m. ≥1/3 U.S. hunt / shuffle port_ownership.",
    "hunt_cycle222", investment_type="terminal_expansion", evidence="documented", currency="MXN",
    value_usd=str(round(54200000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='Alera SCI. “Crecimiento estratégico y operación responsable.” March 18, 2026. https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/.',
    annotation="SSA TEA Polígono 5 CapEx ~USD 3.06m via Fed H.10. Supports ssa_lazaro_tea_poligono5_mxn54m_2025.",
    evid_note="Opened Alera SCI Spanish; MXN 54.2m / TEA Polígono 5 / +1,500 units confirmed. CapEx USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 2. water / us — CapEx-fill NADBank San Quintín ≤MXN 665m
row_doc(
    "nadbank_san_quintin_desal_665m_mxn_2026",
    "resources", "water", "us",
    "NADBank — proposed up to MXN 665m loan for San Quintín desalination (Desaladora Kenton)",
    "Mexico",
    "12 May 2026 NADBank certification/financing proposal: loan for up to MXN 665 million for San Quintín Valley seawater RO desalination plant (250 lps / 5.7 mgd). CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~37.59m for stored MXN 665m ceiling face.",
    "665000000", MXN_FX_DATE, "2026", "30.56", "-115.94",
    "San Quintín Valley / former Ejido Chapala area, Baja California (NADBank proposal geography).",
    "nadbank_san_quintin_proposal_20260512",
    "NADBank is requesting authorization to provide a loan for up to $665 million pesos to the Project Sponsor. … desalination plant with a capacity of 250 liters per second (lps) or 5.7 million gallons per day (mgd)",
    "https://nadbank.org/hubfs/proposals-open-for-public-comment/Planta%20Desaladora%20en%20San%20Quintin%20(Eng)_published.pdf?hsLang=en",
    "Actor: NADBank (U.S.–Mexico binational) — us financing. CapEx-fill: retain ≤MXN 665m loan ceiling; add Fed H.10 Sep 25 2026 FX to USD ~37.59m. ≥1/3 U.S. hunt / shuffle water.",
    "hunt_cycle222", investment_type="financing", evidence="documented", currency="MXN",
    value_usd=str(round(665000000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="government",
    chicago='North American Development Bank. “Certification and Financing Proposal — Desalination Plant in San Quintín, Baja California.” May 12, 2026. https://nadbank.org/hubfs/proposals-open-for-public-comment/Planta%20Desaladora%20en%20San%20Quintin%20(Eng)_published.pdf?hsLang=en.',
    annotation="NADBank San Quintín CapEx-fill ~USD 37.59m via Fed H.10. Supports nadbank_san_quintin_desal_665m_mxn_2026.",
    evid_note="Opened NADBank English proposal PDF; ≤MXN 665m / 250 lps confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 3. building_materials / allied — CapEx-fill Holcim Geocycle Tecomán ~MXN 200m
row_doc(
    "holcim_geocycle_tecoman_mxn200m_2026",
    "infrastructure", "building_materials", "allied",
    "Holcim México / Geocycle — Tecomán biomass co-processing plant",
    "Mexico",
    "4 Aug 2026: Holcim México announces investment of nearly MXN 200 million via Geocycle for biomass (sugarcane bagasse) drying/grinding infrastructure at Tecomán, Colima. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~11.30m for stored MXN 200m face.",
    "200000000", MXN_FX_DATE, "2026", "18.92", "-103.87",
    "Tecomán, Colima (company release).",
    "holcim_mx_geocycle_tecoman_20260804",
    "Holcim México anunció una reciente inversión cercana a 200 millones de pesos para poner en marcha infraestructura innovadora en Tecomán, Colima. Desarrollada a través de Geocycle … la nueva planta permitirá resolver la problemática de residuos de bagazo de caña.",
    "https://www.holcim.com.mx/holcim-mexico-invierte-cerca-de-200-millones-de-pesos-para-acelerar-la-economia-circular",
    "Actor: Holcim México (Switzerland Holcim) — allied. CapEx-fill: retain ~MXN 200m; add Fed H.10 Sep 25 2026 FX to USD ~11.30m. Shuffle building_materials.",
    "hunt_cycle222", investment_type="plant_capex", evidence="documented", currency="MXN",
    value_usd=str(round(200000000 / float(MXN_USD), 2)), fx_usd=MXN_USD,
    chicago='Holcim México. “Holcim México invierte cerca de 200 millones de pesos para acelerar la economía circular.” August 4, 2026. https://www.holcim.com.mx/holcim-mexico-invierte-cerca-de-200-millones-de-pesos-para-acelerar-la-economia-circular.',
    annotation="Holcim Geocycle Tecomán CapEx-fill ~USD 11.30m via Fed H.10. Supports holcim_geocycle_tecoman_mxn200m_2026.",
    evid_note="Opened Holcim México Spanish; ~MXN 200m / Tecomán Geocycle confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 4. port_cranes / allied — CapEx-fill Portonave e-RTG ~R$210m
row_doc(
    "portonave_ertg_210m_brl_2026",
    "infrastructure", "port_cranes", "allied",
    "Portonave (TIL) — 14 Konecranes electric RTG CapEx (Navegantes)",
    "Brazil",
    "8 Jul 2026 Portonave: first seven of 14 new electric Rubber Tyred Gantry (e-RTG) cranes arrive Navegantes; Konecranes design (Finland) / China assembly; acquisition investment approximately R$ 210 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~40.45m for stored R$210m face.",
    "210000000", BRL_FX_DATE, "2026", "-26.89", "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina, Brazil (company geography).",
    "portonave_ertg_arrival_20260708",
    "A aquisição destes RTGs representa um investimento de aproximadamente R$ 210 milhões. … Da marca Konecranes, projetados na Finlândia e fabricados na China",
    "https://www.portonave.com.br/pt/todas-as-noticias/portonave-amplia-frota-de-patio-com-sete-novos-guindastes-eletricos",
    "Actor: Portonave under TIL (MSC/Swiss) — allied; equipment Konecranes (Finland). CapEx-fill: retain ~R$210m; add Fed H.10 Sep 25 2026 FX to USD ~40.45m. Shuffle port_cranes.",
    "hunt_cycle222", investment_type="equipment_supply", evidence="documented", currency="BRL",
    value_usd=str(round(210000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Portonave. “Portonave amplia frota de pátio com sete novos guindastes elétricos.” July 8, 2026. https://www.portonave.com.br/pt/todas-as-noticias/portonave-amplia-frota-de-patio-com-sete-novos-guindastes-eletricos.',
    annotation="Portonave e-RTG CapEx-fill ~USD 40.45m via Fed H.10. Supports portonave_ertg_210m_brl_2026.",
    evid_note="Opened Portonave Portuguese; ~R$210m / 14 Konecranes e-RTG confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. power_plants_grid / prc — CapEx-fill CPFL FY2025 R$6.1bn
row_doc(
    "cpfl_fy2025_capex_6p1bn_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — FY2025 record CapEx",
    "Brazil",
    "6 Mar 2026 CPFL Energia: executed R$ 6.1 billion CapEx in 2025 (+5.5% YoY), described as the company’s largest investment cycle. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1174.86m for stored R$6.1bn face. Distinct from cpfl_capex_plan_31p1bn_2026_2030 forward plan.",
    "6100000000", BRL_FX_DATE, "2025", "", "",
    "CPFL Energia Brazil distribution/transmission CapEx (national multi-concession footprint; no single-site pin).",
    "cpfl_fy2025_results_20260306",
    "Em 2025, a CPFL executou R$ 6,1 bilhões em CAPEX, avanço de 5,5% frente ao ano anterior. O Conselho de Administração aprovou ainda o novo plano de investimentos para o período de 2026 a 2030, que totaliza R$ 31,1 bilhões.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61",
    "Actor: CPFL Energia — controlled by State Grid Corporation of China — prc. CapEx-fill: retain R$6.1bn FY2025; add Fed H.10 Sep 25 2026 FX to USD ~1174.86m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle222", investment_type="capex_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(6100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CPFL Energia. “CPFL Energia registra EBITDA de R$ 13,5 bilhões em 2025 e investimento recorde de R$ 6,1 bilhões.” March 6, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61.',
    annotation="CPFL FY2025 CapEx-fill ~USD 1174.86m via Fed H.10. Supports cpfl_fy2025_capex_6p1bn_brl.",
    evid_note="Opened CPFL Portuguese; R$6.1bn FY2025 CapEx confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. other_renewables / prc — CapEx-fill CTG Brasil H2V ~R$60m
row_doc(
    "ctg_brasil_h2v_pilot_60m_brl_2025",
    "energy", "other_renewables", "prc",
    "CTG Brasil — green hydrogen (H2V) pilot plant (Aneel-regulated spend)",
    "Brazil",
    "CTG Brasil Relatório Anual 2025: Hidrogênio Verde (H2V) pilot plant inside a client industrial site; investment about R$ 60 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~11.56m for stored R$60m face. Site unnamed — lat/lon left blank.",
    "60000000", BRL_FX_DATE, "2025", "", "",
    "CTG Brasil H2V pilot at unnamed client industrial site (company; site not named — coordinates blank).",
    "ctg_brasil_relatorio_anual_2025",
    "O projeto de Hidrogênio Verde (H2V) vai desenvolver uma planta-piloto dentro do site industrial de um cliente para validar o modelo de negócio de produção e venda do hidrogênio verde. O investimento de cerca de R$ 60 milhões.",
    "https://www.ctgbr.com.br/relatorioanual2025/",
    "Actor: CTG Brasil (China Three Gorges) — prc. CapEx-fill: retain ~R$60m; add Fed H.10 Sep 25 2026 FX to USD ~11.56m. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle222", investment_type="pilot_plant", evidence="documented", currency="BRL",
    value_usd=str(round(60000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CTG Brasil. Relatório Anual 2025. https://www.ctgbr.com.br/relatorioanual2025/.',
    annotation="CTG Brasil H2V CapEx-fill ~USD 11.56m via Fed H.10. Supports ctg_brasil_h2v_pilot_60m_brl_2025.",
    evid_note="Opened CTG Brasil Relatório Anual 2025; ~R$60m H2V pilot confirmed (site unnamed). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. niobium / allied — CapEx-fill St George Araxá ~R$3bn (thin next-thinnest)
row_doc(
    "st_george_araxa_capex_brl3bn_2026",
    "resources", "niobium", "allied",
    "St George Mining Brasil — Araxá Nb-REE planned investment",
    "Brazil",
    "16 Sep 2026: St George Mining Brasil DG Thiago Amaral (Rádio Imbiara / The Mining) states company maintains approximately R$ 3 billion planned investment at Araxá Nb-REE project, Minas Gerais. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~577.80m for stored R$3bn face (UNVERIFIED proxy CapEx retained).",
    "3000000000", BRL_FX_DATE, "2026", "-19.59", "-46.94",
    "Araxá Project, Minas Gerais (company geography).",
    "the_mining_sgq_araxa_3bn_20260916",
    "A St George Mining Brasil mantém investimentos de aproximadamente R$ 3 bilhões no Projeto Araxá, em Minas Gerais, enquanto avança em uma parceria voltada ao processamento de terras raras no Brasil.",
    "https://themining.com.br/2026/09/16/projeto-araxa-mantem-quase-r-3-bilhoes-em-investimentos/",
    "Actor: St George Mining (Australia) — allied. CapEx-fill: retain UNVERIFIED proxy ~R$3bn; add Fed H.10 Sep 25 2026 FX to USD ~577.80m. Thin next-thinnest niobium (balsa/nickel/fission_smr dry).",
    "hunt_cycle222", investment_type="capex_plan", evidence="proxy", currency="BRL",
    value_usd=str(round(3000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='The Mining Brasil. “Projeto Araxá mantém quase R$ 3 bilhões em investimentos.” September 16, 2026. https://themining.com.br/2026/09/16/projeto-araxa-mantem-quase-r-3-bilhoes-em-investimentos/.',
    annotation="St George Araxá CapEx-fill ~USD 577.80m via Fed H.10. Supports st_george_araxa_capex_brl3bn_2026.",
    evid_note="Opened The Mining Brasil; ~R$3bn Araxá plan confirmed (UNVERIFIED proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle222 added {len(added)}: {added}")
    print(f"cycle222 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
