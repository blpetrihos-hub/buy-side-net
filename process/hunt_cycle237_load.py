#!/usr/bin/env python3
"""Cycle 237 hunt: shuffle_seed=20261237; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261237).shuffle):
other_renewables, water, nickel, niobium, port_cranes, lithium, bridges_roads,
port_ownership, rail, balsa, graphite, fission_smr, building_materials,
engineering_epc, solar, power_plants_grid, copper, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes Greentegra cumulative >USD 4bn Chile;
  honest residual Freeport/EXIM/Bechtel/Fluence/Wabtec/Nextracker/USTDA sweeps
  (US blank-USD CapEx residual exhausted after cycle 235).
PRC equal-budget: NEW PowerChina NENCOL 5 LSTK USD 195.2m (Colombia LNG-to-power).
NEW allied: EDP Brazil transmission R$3.7bn 2026–28; EDP Goiás tx R$450m (nested
  within national tx program); EDP São Paulo distribution R$5bn 2025–2030;
  ANDRITZ COPEL Foz do Areia/Segredo mid-three-digit EUR floor EUR 300m.
Skipped: RAP-as-CapEx; Huaxin–CSN; Xinhai MoU; Aldesa EUR; Sungrow–BHP CapEx
  undisclosed; COP/CLP/PEN (no Fed H.10); holdovers unsigned.
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

EUR_USD = "1.1400"
EUR_FX_DATE = "2026-09-25"
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


# 1. NEW power_plants_grid / allied — EDP Brazil transmission ~R$3.7bn 2026–28
row_doc(
    "edp_brazil_tx_3p7bn_brl_2026_2028",
    "energy", "power_plants_grid", "allied",
    "EDP — Brazil transmission CapEx program 2026–2028",
    "Brazil",
    "15 Sep 2026 EDP: between 2026 and 2028 the company plans to invest about R$3.7 billion in developing new projects and expanding its transmission activities in Brazil; cumulative transmission CapEx since 2017 already exceeds R$8.5 billion across 12 states; operating + under-construction network ~3,001 km. CapEx: Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~712.62m. Distinct from edp_south_america_7bn_brl_2025_2026 (broader SA plan) and edp_goias_tx_450m_brl_2026_2028 (Goiás portion nested within this program).",
    "3700000000", BRL_FX_DATE, "2026", "-15.78", "-47.93",
    "EDP Brazil transmission footprint (Brasília pin; multi-state program).",
    "edp_brazil_tx_3p7bn_20260915",
    "Entre 2026 e 2028, a empresa prevê investir cerca de R$ 3,7 bilhões no desenvolvimento de novos projetos e na expansão de sua atuação em Transmissão.",
    "https://edp.com/pt-br/america-do-sul/brasil/imprensa/noticias/edp-energiza-maior-linha-e-subestacao-de-sua-historia-34",
    "Actor: EDP (Portugal) — allied. NEW row: company Portuguese ~R$3.7bn Brazil transmission 2026–28. CapEx USD via Fed H.10 Sep 25 2026 5.1921. Shuffle power_plants_grid.",
    "hunt_cycle237", investment_type="capex_program", evidence="documented", currency="BRL",
    value_usd=str(round(3700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='EDP. “EDP energiza maior linha e subestação de sua história 34 meses antes do prazo.” September 15, 2026. https://edp.com/pt-br/america-do-sul/brasil/imprensa/noticias/edp-energiza-maior-linha-e-subestacao-de-sua-historia-34.',
    annotation="EDP Brazil tx NEW ~USD 712.62m via Fed H.10. Supports edp_brazil_tx_3p7bn_brl_2026_2028.",
    evid_note="Opened EDP Portuguese; R$3.7bn 2026–28 transmission program confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. NEW power_plants_grid / allied — EDP Goiás transmission ~R$450m 2026–28 (nested)
row_doc(
    "edp_goias_tx_450m_brl_2026_2028",
    "energy", "power_plants_grid", "allied",
    "EDP — Goiás transmission expansion/modernization 2026–2028",
    "Brazil",
    "25 Aug 2026 EDP: between 2026 and 2028 will allocate about R$450 million to expansion and modernization of transmission lines and substations in Goiás (capacity, reliability, digitalization; datacenter/agribusiness demand). Nested geographic portion of the national ~R$3.7bn 2026–28 transmission program (edp_brazil_tx_3p7bn_brl_2026_2028); do not sum both as independent CapEx. CapEx: Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~86.67m.",
    "450000000", BRL_FX_DATE, "2026", "-16.68", "-49.25",
    "EDP Goiás transmission (Goiânia pin; statewide CELG-T footprint).",
    "edp_goias_tx_450m_20260825",
    "Entre 2026 e 2028, a companhia vai destinar cerca de R$ 450 milhões à ampliação e modernização de linhas de transmissão e subestações, fortalecendo a capacidade, a confiabilidade e a digitalização da rede.",
    "https://edp.com/pt-br/america-do-sul/brasil/imprensa/noticias/edp-investe-r-450-milhoes-e-consolida-goias",
    "Actor: EDP (Portugal) — allied. NEW row: company Portuguese ~R$450m Goiás tx 2026–28 (nested in national R$3.7bn). CapEx USD via Fed H.10. Shuffle power_plants_grid.",
    "hunt_cycle237", investment_type="capex_program", evidence="documented", currency="BRL",
    value_usd=str(round(450000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='EDP. “EDP investe R$ 450 milhões e consolida Goiás como centro estratégico da Transmissão de energia.” August 25, 2026. https://edp.com/pt-br/america-do-sul/brasil/imprensa/noticias/edp-investe-r-450-milhoes-e-consolida-goias.',
    annotation="EDP Goiás tx NEW ~USD 86.67m via Fed H.10 (nested). Supports edp_goias_tx_450m_brl_2026_2028.",
    evid_note="Opened EDP Portuguese; R$450m Goiás 2026–28 tx confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. NEW power_plants_grid / allied — EDP São Paulo distribution R$5bn 2025–2030
row_doc(
    "edp_sp_dist_5bn_brl_2025_2030",
    "energy", "power_plants_grid", "allied",
    "EDP — São Paulo distribution concession CapEx 2025–2030",
    "Brazil",
    "8 May 2026 EDP: signed 30-year renewal of São Paulo distribution concession (28 municipalities — Guarulhos, Alto Tietê, Vale do Paraíba, Litoral Norte) through 2058; investing R$5 billion from 2025 to 2030 in concession area (~30% above 2019–2024 cycle) for customer service, energy infrastructure, digitalization/automation, and distribution-network resilience. CapEx: Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~962.99m. Distinct from edp_brazil_tx_3p7bn (transmission) and neoenergia_dist_50bn (Iberdrola).",
    "5000000000", BRL_FX_DATE, "2026", "-23.45", "-46.53",
    "EDP São Paulo distribution concession (Guarulhos / Alto Tietê pin).",
    "edp_sp_dist_5bn_20260508",
    "Com o compromisso da qualidade de serviço e expansão da infraestrutura, a companhia está investindo R$ 5 bilhões de 2025 a 2030 em sua área de concessão, um crescimento de cerca de 30% na comparação com os investimentos realizados entre 2019 e 2024.",
    "https://www.edp.com.br/noticias/artigo/edp-assina-renovacao-da-sua-concessao-de-distribuicao-no-estado-de-sao-paulo-e-investira-r-5-bilhoes-ate-2030/",
    "Actor: EDP (Portugal) — allied. NEW row: company Portuguese R$5bn SP distribution 2025–2030. CapEx USD via Fed H.10. Shuffle power_plants_grid.",
    "hunt_cycle237", investment_type="capex_program", evidence="documented", currency="BRL",
    value_usd=str(round(5000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='EDP Brasil. “EDP assina renovação da sua concessão de Distribuição no estado de São Paulo e investirá R$ 5 bilhões até 2030.” May 8, 2026. https://www.edp.com.br/noticias/artigo/edp-assina-renovacao-da-sua-concessao-de-distribuicao-no-estado-de-sao-paulo-e-investira-r-5-bilhoes-ate-2030/.',
    annotation="EDP SP dist NEW ~USD 962.99m via Fed H.10. Supports edp_sp_dist_5bn_brl_2025_2030.",
    evid_note="Opened EDP Brasil Portuguese; R$5bn 2025–2030 SP distribution / 30-year renewal confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. NEW power_plants_grid / allied — ANDRITZ COPEL Foz do Areia / Segredo mid-three-digit EUR
row_doc(
    "andritz_copel_foz_segredo_2026",
    "energy", "power_plants_grid", "allied",
    "ANDRITZ — COPEL Foz do Areia + Segredo hydropower expansion (Paraná)",
    "Brazil",
    "27 May 2026 ANDRITZ: COPEL awards two turnkey contracts for additional generating units at Foz do Areia and Segredo HPPs on the Iguaçu River (Paraná); combined order value in the mid three-digit million-euro range (Q1 2026 order intake); adds >2.1 GW to the two plants (current combined 2.9 GW); construction from 2026; COD planned 2030; part of Brazil 2nd Capacity Reserve Auction (LRCAP). CapEx: enter EUR 300m floor of mid-three-digit million-euro range; Fed H.10 Sep 25 2026 EUR 1.1400 → USD 342.00m.",
    "300000000", EUR_FX_DATE, "2026", "-26.00", "-51.67",
    "Foz do Areia / Segredo HPPs on Iguaçu River, Paraná (Foz do Areia pin).",
    "andritz_copel_foz_segredo_20260527",
    "The combined order value is in the mid three-digit million-euro range and was included in ANDRITZ’s order intake for the first quarter of 2026.",
    "https://www.andritz.com/newsroom-en/hydro/2026-05-27-copel-group",
    "Actor: ANDRITZ (Austria) — allied. NEW row: company English mid-three-digit EUR floor EUR 300m for COPEL Foz/Segredo. CapEx USD via Fed H.10. Shuffle power_plants_grid.",
    "hunt_cycle237", investment_type="epc", evidence="documented", currency="EUR",
    value_usd=str(round(300000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='ANDRITZ. “Powering Brazil’s clean energy future: ANDRITZ secures major hydropower capacity expansion contracts with COPEL.” May 27, 2026. https://www.andritz.com/newsroom-en/hydro/2026-05-27-copel-group.',
    annotation="ANDRITZ COPEL NEW USD 342.00m via Fed H.10 (EUR 300m floor). Supports andritz_copel_foz_segredo_2026.",
    evid_note="Opened ANDRITZ English; mid-three-digit million-euro / >2.1 GW / Foz do Areia+Segredo confirmed. CapEx USD via Fed H.10 Sep 25 2026 1.1400 on EUR 300m floor.",
)

# 5. NEW power_plants_grid / prc — PowerChina NENCOL 5 LSTK USD 195.2m
row_doc(
    "powerchina_nencol5_lstk_195p2m_2026",
    "energy", "power_plants_grid", "prc",
    "PowerChina — NENCOL 5 / TermoInduEnergy Phase 1 LSTK EPC (282 MW)",
    "Colombia",
    "Project developer Nencol Energia (2026): PowerChina holds Lump-Sum Turnkey (LSTK) EPC contract valued at USD 195.2 million for three 94 MW dual-fuel modules (Termobonda, Termocosta, Termogaira) aggregating 282 MW Phase 1 of TermoInduEnergy–NENCOL 5 LNG-to-power on Colombia’s northern coast; NENCOL 5 awarded 20-year Firm Energy Obligation (OEF) in XM Fifth Long-Term Energy Auction (award 22 May 2026). CapEx: enter stated LSTK USD 195.2m.",
    "195200000", "2026-05-22", "2026", "11.00", "-74.80",
    "NENCOL 5 northern Colombia coast modules (Santa Marta / Caribbean coast pin).",
    "nencol_powerchina_lstk_2026",
    "with EPC execution by PowerChina under a Lump-Sum Turnkey (LSTK) contract valued at $195.2 million for the three 94 MW modules.",
    "https://nencolenergia.com/",
    "Actor: PowerChina (PRC) EPC — prc; developer ZeuzCorp/POWERCOL via Nodo Energético de Norte de Colombia. NEW row: developer English LSTK USD 195.2m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle237", investment_type="epc", evidence="documented", currency="USD",
    value_usd="195200000", fx_usd="1", bib_type="company",
    chicago='Nencol Energia. “TermoInduEnergy – NENCOL 5: Colombia’s Only Firm Energy Awarded LNG-to-Power Project.” 2026. https://nencolenergia.com/.',
    annotation="PowerChina NENCOL LSTK NEW USD 195.2m. Supports powerchina_nencol5_lstk_195p2m_2026.",
    evid_note="Opened Nencol Energia English; PowerChina LSTK $195.2M / three 94 MW modules / OEF award May 22 2026 confirmed.",
)

# 6. NEW other_renewables / us — AES Andes Greentegra cumulative >USD 4bn Chile
row_doc(
    "aes_andes_greentegra_4bn_chile_2026",
    "energy", "other_renewables", "us",
    "AES Andes — Greentegra renewable + BESS CapEx cumulative (Chile)",
    "Chile",
    "23 Jan 2026 AES Andes: by 2027 will have completed renewable growth exceeding 4,500 MW, investing over US$4 billion in Chile since launch of Greentegra; focus on Andes Solar III and Bolero BESS COD 1H2026 plus construction of Arenales, Cristales, Pampas, and Atacama BESS (together adding 2,363 MW). CapEx: enter USD 4bn floor of stated “over US$4 billion” cumulative Greentegra Chile investment. Distinct from project-level aes_andes_pampas_cristales_2025 / aes_andes_solar_iii_hub_2026 rows.",
    "4000000000", "2026-01-23", "2026", "-23.65", "-70.40",
    "AES Andes Chile Greentegra renewable/BESS portfolio (Antofagasta / northern Chile pin).",
    "aes_andes_greentegra_4bn_20260123",
    "Together, these projects will add 2,363 MW to the portfolio. This means that by 2027, AES Andes will have completed renewable growth exceeding 4,500 MW, investing over US$4 billion in the country since the launch of Greentegra — reaffirming its position as a regional leader in the energy transition.",
    "https://www.aesandes.com/en/press-release/aes-andes-focus-renewables-and-storage-discontinues-green-hydrogen-development",
    "Actor: AES Andes (AES Corp, U.S.) — us. NEW row: company English >USD 4bn Greentegra Chile cumulative floor. Shuffle other_renewables / U.S. ≥1/3 budget.",
    "hunt_cycle237", investment_type="capex_program", evidence="documented", currency="USD",
    value_usd="4000000000", fx_usd="1",
    chicago='AES Andes. “AES Andes Focuses on Renewables and Discontinues Green Hydrogen Development.” January 23, 2026. https://www.aesandes.com/en/press-release/aes-andes-focus-renewables-and-storage-discontinues-green-hydrogen-development.',
    annotation="AES Andes Greentegra NEW USD 4bn floor. Supports aes_andes_greentegra_4bn_chile_2026.",
    evid_note="Opened AES Andes English; over US$4 billion Greentegra Chile / >4,500 MW by 2027 / 2,363 MW under construction confirmed. CapEx enter USD 4bn floor.",
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
    print(f"cycle237 added {len(added)}: {added}")
    print(f"cycle237 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
