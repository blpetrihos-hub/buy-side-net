#!/usr/bin/env python3
"""Cycle 221 hunt: shuffle_seed=20261221; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261221).shuffle):
wind, nickel, graphite, fission_smr, lithium, niobium, engineering_epc,
building_materials, balsa, port_ownership, power_plants_grid, water,
bridges_roads, other_renewables, copper, solar, rail, port_cranes.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    nickel CapEx-fill (BNDES Piauí Níquel R$100m); balsa/fission_smr dry.
≥1/3 U.S. hunt budget spent on Amazon Brazil 2025 + Microsoft Brazil cloud/AI
+ SSA Lázaro Isla Palma CapEx-fills + Freeport/EnergyX/EXIM/Bechtel/Fluor/
USTDA/Nextracker/Jervois/Wabtec sweeps (3 US CapEx-fills; catalog dense).
PRC equal-budget: ZPMC MultiRio dual-quote US$21m + ZPMC Tecon Rio Grande
CapEx-fills; Goldwind/Envision/Sungrow/PowerChina already logged; holdovers
unsigned.
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
MXN_USD = "17.6932"  # Fed H.10 Sep 25 2026 Mexico peso
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


# 1. engineering_epc / us — CapEx-fill Amazon Brazil 2025 >R$19bn
row_doc(
    "amazon_brazil_invest_19bn_brl_2025",
    "infrastructure", "engineering_epc", "us",
    "Amazon — Brazil 2025 investments (infra / logistics / cloud / tech)",
    "Brazil",
    "4 Aug 2026 About Amazon Brasil: since 2012 Amazon invested more than R$ 75 billion in Brazil; in 2025 investments surpassed R$19 billion — nearly five times the annual average of the prior decade. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~3659.41m for stored R$19bn floor face.",
    "19000000000", BRL_FX_DATE, "2025", "", "",
    "Brazil nationwide Amazon ops (company geography; no single-site pin).",
    "amazon_brasil_invest_20260804",
    "Desde sua chegada ao país, em 2012, a Amazon investiu mais de R$ 75 bilhoes no Brasil em infraestrutura, logística, tecnologia, serviços de nuvem, qualificação profissional e fomento ao empreendedorismo. Somente em 2025, os investimentos ultrapassaram R$19 bilhões — quase cinco vezes a média anual da década anterior.",
    "https://www.aboutamazon.com.br/noticias/noticias-da-empresa/amazon-reforca-compromisso-com-o-brasil-com-operacao-crescente-alinhada-a-estrategia-global",
    "Actor: Amazon.com Inc. (U.S.) — us. CapEx-fill: retain >R$19bn 2025 floor; add Fed H.10 Sep 25 2026 FX to USD ~3659.41m. ≥1/3 U.S. hunt / shuffle engineering_epc.",
    "hunt_cycle221", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(19000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Amazon. “Amazon reforça compromisso com o Brasil com operação crescente alinhada à estratégia global.” About Amazon Brasil, August 4, 2026. https://www.aboutamazon.com.br/noticias/noticias-da-empresa/amazon-reforca-compromisso-com-o-brasil-com-operacao-crescente-alinhada-a-estrategia-global.',
    annotation="Amazon Brazil 2025 CapEx-fill ~USD 3659.41m via Fed H.10. Supports amazon_brazil_invest_19bn_brl_2025.",
    evid_note="Opened About Amazon Brasil Portuguese; >R$19bn 2025 investments confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. engineering_epc / us — CapEx-fill Microsoft Brazil cloud/AI R$14.7bn
row_doc(
    "microsoft_brazil_cloud_ai_14p7bn_brl_2024",
    "infrastructure", "engineering_epc", "us",
    "Microsoft — Brazil cloud and AI infrastructure package (3 years)",
    "Brazil",
    "26 Sep 2024 Microsoft News Center Brasil: largest single Microsoft investment in Brazil — plans to spend 14.7 billion Reais in cloud and AI infrastructure over three years across São Paulo-state datacenter campuses. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~2831.22m for stored R$14.7bn face.",
    "14700000000", BRL_FX_DATE, "2024", "", "",
    "São Paulo state Microsoft datacenter campuses (company geography; no single-site pin).",
    "microsoft_brazil_14p7bn_20240926",
    "Today, Microsoft announced its largest single investment in Brazil, with plans to spend 14.7 billion Reais in cloud and artificial intelligence (AI) infrastructure over three years. … Microsoft will expand its cloud and AI infrastructure across several datacenter campuses in the state of São Paulo.",
    "https://news.microsoft.com/pt-br/microsoft-announces-14-7-billion-reais-investment-over-three-years-in-cloud-and-ai-infrastructure-and-provide-ai-training-at-scale-to-upskill-5-million-people-in-brazil/",
    "Actor: Microsoft Corporation (U.S.) — us. CapEx-fill: retain R$14.7bn; add Fed H.10 Sep 25 2026 FX to USD ~2831.22m. ≥1/3 U.S. hunt / shuffle engineering_epc.",
    "hunt_cycle221", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(14700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Microsoft. “Microsoft announces 14.7 billion Reais investment over three years in Cloud and AI infrastructure and provide AI training at scale to upskill 5 million people in Brazil.” September 26, 2024. https://news.microsoft.com/pt-br/microsoft-announces-14-7-billion-reais-investment-over-three-years-in-cloud-and-ai-infrastructure-and-provide-ai-training-at-scale-to-upskill-5-million-people-in-brazil/.',
    annotation="Microsoft Brazil CapEx-fill ~USD 2831.22m via Fed H.10. Supports microsoft_brazil_cloud_ai_14p7bn_brl_2024.",
    evid_note="Opened Microsoft News Center Brasil; R$14.7bn / 3-year cloud+AI package confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. port_ownership / us — CapEx-fill SSA Isla de la Palma MXN 142.6m
row_doc(
    "ssa_lazaro_isla_palma_mxn143m_2025",
    "infrastructure", "port_ownership", "us",
    "SSA Marine México — Isla de la Palma vehicle distribution yard (Lázaro Cárdenas)",
    "Mexico",
    "2025 (Alera SCI 18 Mar 2026 roundup): SSA Marine México enables an external vehicle patio on Isla de la Palma (10.5 ha, ~2.5 km from port; 4,918-unit capacity); investment MXN 142.6 million. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~8.06m for stored MXN 142.6m face.",
    "142600000", MXN_FX_DATE, "2025", "17.96", "-102.17",
    "Isla de la Palma / Lázaro Cárdenas, Michoacán (press geography).",
    "alerasci_ssa_mexico_20260318",
    "Complementando esta acción, se habilitó un patio externo en la Isla de la Palma con un área de 10.5 hectáreas, a solo 2.5 km del puerto, con capacidad para 4,918 unidades. … La inversión en este proyecto fue de 142.6 millones de pesos.",
    "https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/",
    "Actor: SSA Marine / Carrix (U.S.) via SSA Marine México — us. CapEx-fill: retain MXN 142.6m; add Fed H.10 Sep 25 2026 FX to USD ~8.06m. ≥1/3 U.S. hunt / shuffle port_ownership.",
    "hunt_cycle221", investment_type="terminal_expansion", evidence="documented", currency="MXN",
    value_usd=str(round(142600000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='Alera SCI. “Crecimiento estratégico y operación responsable.” March 18, 2026. https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/.',
    annotation="SSA Isla de la Palma CapEx-fill ~USD 8.06m via Fed H.10. Supports ssa_lazaro_isla_palma_mxn143m_2025.",
    evid_note="Opened Alera SCI Spanish; MXN 142.6m / Isla de la Palma confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 4. port_cranes / prc — CapEx-fill ZPMC MultiRio dual-quote US$21m
row_doc(
    "zpmc_multirio_sts_2026",
    "infrastructure", "port_cranes", "prc",
    "ZPMC — two Super Post-Panamax STS for MultiRio (Port of Rio de Janeiro)",
    "Brazil",
    "Delivery Jun 2026 of two ZPMC STS quay cranes (arrived erected on Zhen Hua 15) for MultiRio; HMT News values investment at about R$110 million, or $21 million. CapEx-fill: enter company/press dual-quoted US$21 million as value_usd (retain R$110m face).",
    "110000000", "2026-06-23", "2026", "-22.89", "-43.2",
    "MultiRio / Port of Rio de Janeiro (press geography).",
    "hmt_multirio_zpmc_20260623",
    "Multiterminais has received two new ZPMC ship-to-shore cranes for MultiRio … The ZPMC-built cranes arrived fully assembled on 10 June aboard Zhen Hua 15 … The investment is valued at about R$110 million, or $21 million.",
    "https://hmt-news.com/multiterminais-adds-sts-cranes-at-rio-terminal/",
    "Actor: ZPMC (PRC) OEM; buyer Multiterminais MultiRio — prc. CapEx-fill: dual-quote US$21m alongside R$110m — store both. Shuffle port_cranes / PRC equal-budget.",
    "hunt_cycle221", investment_type="equipment", evidence="proxy", currency="BRL",
    value_usd="21000000", fx_usd=str(round(110000000 / 21000000, 4)), bib_type="press",
    chicago='HMT News. “Multiterminais Adds STS Cranes at Rio Terminal.” June 23, 2026. https://hmt-news.com/multiterminais-adds-sts-cranes-at-rio-terminal/.',
    annotation="ZPMC MultiRio CapEx-fill company/press dual-quote US$21m. Supports zpmc_multirio_sts_2026.",
    evid_note="Opened HMT News; ~R$110m / US$21m dual-quote / two ZPMC STS / Zhen Hua 15 confirmed. CapEx-fill uses press USD.",
)

# 5. port_cranes / prc — CapEx-fill ZPMC Tecon Rio Grande ~R$290m
row_doc(
    "zpmc_tecon_rio_grande_2026",
    "infrastructure", "port_cranes", "prc",
    "ZPMC — 3 Super Post-Panamax STS + 6 remote aRTGs for Tecon Rio Grande (Wilson Sons)",
    "Brazil",
    "Delivery Sep 2026 of 3 STS + 6 automated/remotely operated RTGs ordered Mar 2025 from ZPMC; investment about R$ 290 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~55.85m for stored R$290m face (UNVERIFIED proxy CapEx retained).",
    "290000000", BRL_FX_DATE, "2026", "-32.13", "-52.1",
    "Tecon Rio Grande, Rio Grande do Sul (press geography).",
    "gauchazh_tecon_rg_zpmc_20260918",
    "O Tecon Rio Grande recebeu … nove novos equipamentos … três guindastes de cais e seis equipamentos de pátio … investimento de cerca de R$ 290 milhões. … Os equipamentos foram adquiridos em março de 2025 da fabricante chinesa ZPMC.",
    "https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/09/tecon-rio-grande-recebe-r-290-milhoes-em-equipamentos-para-movimentacao-de-conteineres-cmu738bdl01v1014x2r640dlr.html",
    "Actor: ZPMC (PRC) OEM; buyer Wilson Sons / Tecon Rio Grande — prc. CapEx-fill: retain UNVERIFIED proxy ~R$290m; add Fed H.10 Sep 25 2026 FX to USD ~55.85m. Shuffle port_cranes / PRC equal-budget.",
    "hunt_cycle221", investment_type="equipment", evidence="proxy", currency="BRL",
    value_usd=str(round(290000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='GaúchaZH / Zero Hora. “Tecon Rio Grande recebe R$ 290 milhões em equipamentos para movimentação de contêineres.” September 18, 2026. https://gauchazh.clicrbs.com.br/zona-sul/economia/noticia/2026/09/tecon-rio-grande-recebe-r-290-milhoes-em-equipamentos-para-movimentacao-de-conteineres-cmu738bdl01v1014x2r640dlr.html.',
    annotation="ZPMC Tecon Rio Grande CapEx-fill ~USD 55.85m via Fed H.10. Supports zpmc_tecon_rio_grande_2026.",
    evid_note="Opened GaúchaZH; ~R$290m / 3 STS + 6 aRTG / ZPMC confirmed (UNVERIFIED proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. nickel / allied — CapEx-fill BNDES Piauí Níquel R$100m (thin)
row_doc(
    "bndes_piaui_nickel_maq_100m_2026",
    "resources", "nickel", "allied",
    "BNDES Máquinas e Serviços — R$100 million financing to Piauí Níquel Metais (Brazilian Nickel)",
    "Brazil",
    "BNDES approved R$100 million financing for Piauí Níquel Metais S/A to acquire machines/equipment/services supporting high-purity Ni/Co precipitate production at Capitão Gervásio Oliveira (Piauí). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~19.26m for stored R$100m face.",
    "100000000", BRL_FX_DATE, "2026", "-8.1", "-42.5",
    "Capitão Gervásio Oliveira, Piauí (BNDES geography).",
    "bndes_piaui_niquel_20260713",
    "O Banco Nacional de Desenvolvimento Econômico e Social (BNDES) aprovou financiamento no valor de R$ 100 milhões para a Piauí Níquel Metais S/A adquirir máquinas, equipamentos ou serviços industriais para apoiar a produção de precipitados de níquel e cobalto de alta pureza, em Capitão Gervásio Oliveira (PI).",
    "https://agenciadenoticias.bndes.gov.br/noticia/BNDES-aprova-R$-100-mi-para-apoiar-processamento-de-niquel-no-Piaui/",
    "Actor: Piauí Níquel Metais (Brazilian Nickel Ltd, UK) — allied; lender BNDES. CapEx-fill: retain R$100m; add Fed H.10 Sep 25 2026 FX to USD ~19.26m. Thin nickel top-up / shuffle nickel.",
    "hunt_cycle221", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="government",
    chicago='Banco Nacional de Desenvolvimento Econômico e Social. “BNDES aprova R$ 100 mi para apoiar processamento de níquel no Piauí.” July 13, 2026. https://agenciadenoticias.bndes.gov.br/noticia/BNDES-aprova-R$-100-mi-para-apoiar-processamento-de-niquel-no-Piaui/.',
    annotation="BNDES Piauí Níquel CapEx-fill ~USD 19.26m via Fed H.10. Supports bndes_piaui_nickel_maq_100m_2026.",
    evid_note="Opened BNDES Portuguese primary; R$100m / Capitão Gervásio Oliveira confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. power_plants_grid / allied — CapEx-fill ENGIE Jaguara modernization R$500m
row_doc(
    "engie_jaguara_modernization_500m_brl_2026",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil Energia — UHE Jaguara modernization (4 units / 424 MW)",
    "Brazil",
    "18 Mar 2026 ENGIE Brasil LRCAP release: Jaguara modernization began Jul 2023 with investment of R$ 500 million, of which R$ 130 million already expended. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~96.30m for stored R$500m face. Distinct from engie_jaguara_expansion_1p2bn_brl_2026 LRCAP expansion row.",
    "500000000", BRL_FX_DATE, "2026", "-20.02", "-47.28",
    "UHE Jaguara, Minas Gerais / São Paulo border (ENGIE geography).",
    "engie_brasil_jaguara_lrcap_20260318",
    "Work on the modernization of the hydropower plant began in July 2023 and involves an investment of R$ 500 million, of which R$ 130 million has already been expended.",
    "https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-vence-leilao-de-reserva-de-capacidade-e-vai-ampliar-potencia-da-usina-hidreletrica-jaguara/",
    "Actor: ENGIE Brasil Energia (France ENGIE) — allied. CapEx-fill: retain R$500m modernization; add Fed H.10 Sep 25 2026 FX to USD ~96.30m. Shuffle power_plants_grid.",
    "hunt_cycle221", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ENGIE Brasil Energia. “ENGIE Brasil wins the Capacity Reserve Auction and will increase the power output of the Jaguara Hydropower Plant.” March 18, 2026. https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-vence-leilao-de-reserva-de-capacidade-e-vai-ampliar-potencia-da-usina-hidreletrica-jaguara/.',
    annotation="ENGIE Jaguara modernization CapEx-fill ~USD 96.30m via Fed H.10. Supports engie_jaguara_modernization_500m_brl_2026.",
    evid_note="Opened ENGIE Brasil English; R$500m modernization / Jul 2023 start confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle221 added {len(added)}: {added}")
    print(f"cycle221 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
