#!/usr/bin/env python3
"""Cycle 284 hunt: shuffle_seed=20261284; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261284).shuffle):
graphite, bridges_roads, copper, building_materials, solar, engineering_epc, niobium,
other_renewables, port_cranes, nickel, fission_smr, wind, lithium, rail, water,
port_ownership, balsa, power_plants_grid.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Brasil 2025E / 2027E / 2028E Total Investments CapEx
  nested within 2024–2028 Material Fact plan; Freeport 2Q company-wide CapEx not
  LatAm-separable; Equinix/Ascenty/SSA CapEx blanks; EXIM/USTDA probes.
PRC equal-budget: NEW CPFL Transmissão 2028 R$1.059bn + 2029 R$799m (company FR
  nested within 2026–2030 R$4.540bn); Goldwind Jacobina 05 CNY guarantee ≠ CapEx
  (left blank).
Allied: NEW Antamina SENACE-approved ITS ~USD300m (28 Mar 2025) + Segundo ITS
  presented CapEx ~USD729m (2 Jan 2026; pending SENACE approval).
Other: NEW Motiva frota eletrificada ~R$50m; Rumo Contêiner Recorrente 6M26 R$8m.
Skipped: thin dry; graphite/niobium/solar/etc. dense misses; holdovers unsigned.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
    status="active",
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
            "fx_date": fx_date if value_usd else "", "year": year, "status": status,
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


# 1. bridges_roads / other — NEW Motiva frota eletrificada ~R$50m
row_doc(
    "motiva_frota_eletrificada_50m_brl_2026",
    "infrastructure", "bridges_roads", "other",
    "Motiva — frota operacional eletrificada CapEx ~R$50m (rodovias + trilhos)",
    "Brazil",
    "17 Aug 2026 Motiva company news: investing around R$ 50 million to expand the operational fleet of electric and hybrid vehicles across highway and rail concessions (inspection cars, light tow trucks, rescue vehicles); 59 electric + 67 hybrid planned toward 125 vehicles by end-2026. CapEx: enter R$50m frota face. Distinct from Motiva 1S26/2T26 roads/rails CapEx spent rows and 2026 CapEx plan envelopes (not additive).",
    "50000000", "2026-08-17", "2026", "-23.55", "-46.63",
    "Motiva Brazil highway+rail concessions (São Paulo HQ pin; AutoBan Anhanguera cited).",
    "motiva_frota_eletrificada_20260817",
    "está investindo em torno de R$ 50 milhões na expansão de sua frota operacional de veículos elétricos e híbridos",
    "https://www.motiva.com.br/noticias/motiva-investe-frota-eletrificada-rodovias-trilhos/",
    "Actor: Motiva S.A. (ex-CCR; Brazilian mobility concessionaire) — other. NEW frota eletrificada CapEx ~R$50m. Shuffle bridges_roads.",
    "hunt_cycle284", investment_type="equipment_procurement", evidence="documented", currency="BRL",
    value_usd=str(round(50000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva investe R$ 50 milhões para ampliar a frota operacional de veículos eletrificados em suas rodovias e ativos de trilhos.” August 17, 2026. https://www.motiva.com.br/noticias/motiva-investe-frota-eletrificada-rodovias-trilhos/.',
    annotation="Motiva frota eletrificada ~R$50m via Fed H.10. Supports motiva_frota_eletrificada_50m_brl_2026.",
    evid_note="Opened Motiva company news 17 Aug 2026; frota CapEx ~R$50m confirmed.",
)

# 2. copper / allied — NEW Antamina SENACE-approved ITS ~USD300m
row_doc(
    "antamina_its_300m_2025",
    "resources", "copper", "allied",
    "Antamina — SENACE-approved ITS CapEx ~USD300m (Áncash)",
    "Peru",
    "28 Mar 2025 Antamina company Spanish: SENACE approved a new Informe Técnico Sustentatorio (ITS) presented in January of that year; modifications imply approximately USD 300 million investment to optimize the productive process under environmental standards, within the MEIA life-extension approved Feb 2024. CapEx: enter USD300m ITS face. Nested vs antamina_meia_2bn_2024 envelope (not additive); distinct from Segundo ITS ~USD729m presentation.",
    "300000000", "2025-03-28", "2025", "-9.53", "-77.05",
    "Antamina mine, Áncash Region (company geography; approximate pin).",
    "antamina_its_senace_20250328",
    "Modificaciones significarán una inversión aproximada de US$ 300 millones para optimizar el proceso productivo",
    "https://www.antamina.com/noticias/senace-aprueba-nuevo-informe-tecnico-sustentatorio-its/",
    "Actor: Compañía Minera Antamina (BHP/Glencore/Teck/Mitsubishi JV) — allied. NEW SENACE-approved ITS CapEx ~USD300m. Shuffle copper.",
    "hunt_cycle284", investment_type="brownfield_expansion", evidence="documented", currency="USD",
    chicago='Compañía Minera Antamina. “SENACE aprueba nuevo Informe Técnico Sustentatorio (ITS).” March 28, 2025. https://www.antamina.com/noticias/senace-aprueba-nuevo-informe-tecnico-sustentatorio-its/.',
    annotation="Antamina ITS CapEx ~USD300m company Spanish. Supports antamina_its_300m_2025.",
    evid_note="Opened Antamina company news 28 Mar 2025; ITS CapEx ~USD300m confirmed.",
)

# 3. copper / allied — NEW Antamina Segundo ITS presented ~USD729m (pending approval)
row_doc(
    "antamina_its2_729m_2026",
    "resources", "copper", "allied",
    "Antamina — Segundo ITS presented CapEx ~USD729m (pending SENACE)",
    "Peru",
    "2 Jan 2026 Antamina company Spanish: presents Segundo Informe Técnico Sustentatorio (ITS) to SENACE as part of the Feb 2024 MEIA life-extension plan; if approved by SENACE and company governance, implies approximately USD 729 million investment over remaining operating life (open-pit/waste/commingling optimizations). CapEx: enter USD729m proposed face (pending approval). Distinct from antamina_its_300m_2025 approved ITS and antamina_meia_2bn_2024 envelope (not additive).",
    "729000000", "2026-01-02", "2026", "-9.53", "-77.05",
    "Antamina mine, Áncash Region (company geography; approximate pin).",
    "antamina_its2_presented_20260102",
    "De ser aprobado el ITS por el SENACE y por el proceso de gobernanza de la compañía, supondrá una inversión aproximada de 729 millones de dólares",
    "https://www.antamina.com/noticias/antaminapresento-its-ante-senace/",
    "Actor: Compañía Minera Antamina — allied. NEW Segundo ITS presented CapEx ~USD729m (pending SENACE). Shuffle copper.",
    "hunt_cycle284", investment_type="brownfield_expansion", evidence="documented", currency="USD",
    chicago='Compañía Minera Antamina. “Antamina presentó ITS ante el Senace.” January 2, 2026. https://www.antamina.com/noticias/antaminapresento-its-ante-senace/.',
    annotation="Antamina Segundo ITS proposed CapEx ~USD729m (pending). Supports antamina_its2_729m_2026.",
    evid_note="Opened Antamina company news 2 Jan 2026; Segundo ITS ~USD729m pending-approval face confirmed.",
)

# 4. rail / other — NEW Rumo Contêiner Recorrente 6M26 R$8m
row_doc(
    "rumo_conteiner_recorrente_6m26_8m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Contêiner Recorrente CapEx 6M26 R$8m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Contêiner Recorrente R$8 million in 6M26 (2T26 R$2m). CapEx: enter R$8m Contêiner Recorrente 6M26 face. Nested vs rumo_conteiner_6m26_40m_brl total Contêiner / rumo_conteiner_expansao_6m26_32m_brl Expansão (not additive).",
    "8000000", "2026-06-30", "2026", "-23.95", "-46.30",
    "Rumo/Brado container ops (Santos corridor pin).",
    "rumo_2t26_release_20260812",
    "2 6 -69,7 % Recorrente 8 8 -1,8 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Contêiner Recorrente 6M26 CapEx R$8m. Shuffle rail.",
    "hunt_cycle284", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(8000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Contêiner Recorrente 6M26 CapEx R$8m via Fed H.10. Supports rumo_conteiner_recorrente_6m26_8m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Contêiner Recorrente Capex 6M26 R$8m confirmed.",
)

# 5. power_plants_grid / us — NEW AES Brasil 2025E CapEx R$214.2m
row_doc(
    "aes_brasil_2025e_capex_214p2m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2025E Total Investments CapEx R$214.2m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact (English): investment projections 2024–2028 table shows 2025E Total Investments R$214.2 million (Modernization and Maintenance R$213.9m; Pipeline Development R$0.3m). CapEx: enter R$214.2m 2025E face. Nested vs aes_brasil_capex_plan_1348m_brl_2024_2028 multi-year envelope / aes_brasil_2026e_capex_136p7m_brl (not additive).",
    "214200000", "2024-02-26", "2025", "-23.55", "-46.63",
    "AES Brasil generation portfolio (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Total Investments 712.7 214.2 136.7 125.5 159.5 1,348.4",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil (AES Corp U.S.–controlled) — us. NEW nested 2025E CapEx R$214.2m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle284", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(214200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2025E CapEx R$214.2m via Fed H.10. Supports aes_brasil_2025e_capex_214p2m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2025E Total Investments R$214.2m confirmed.",
)

# 6. power_plants_grid / us — NEW AES Brasil 2027E CapEx R$125.5m
row_doc(
    "aes_brasil_2027e_capex_125p5m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2027E Total Investments CapEx R$125.5m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: 2027E Total Investments R$125.5 million (Modernization and Maintenance R$125.5m; pipeline/expansion zero). CapEx: enter R$125.5m 2027E face. Nested vs aes_brasil_capex_plan_1348m_brl_2024_2028 / 2025E/2026E faces (not additive).",
    "125500000", "2024-02-26", "2027", "-23.55", "-46.63",
    "AES Brasil generation portfolio (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Total Investments 712.7 214.2 136.7 125.5 159.5 1,348.4",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil (AES Corp U.S.–controlled) — us. NEW nested 2027E CapEx R$125.5m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle284", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(125500000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2027E CapEx R$125.5m via Fed H.10. Supports aes_brasil_2027e_capex_125p5m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2027E Total Investments R$125.5m confirmed.",
)

# 7. power_plants_grid / us — NEW AES Brasil 2028E CapEx R$159.5m
row_doc(
    "aes_brasil_2028e_capex_159p5m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2028E Total Investments CapEx R$159.5m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: 2028E Total Investments R$159.5 million (Modernization and Maintenance R$159.5m). CapEx: enter R$159.5m 2028E face. Nested vs aes_brasil_capex_plan_1348m_brl_2024_2028 / prior year faces (not additive).",
    "159500000", "2024-02-26", "2028", "-23.55", "-46.63",
    "AES Brasil generation portfolio (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Total Investments 712.7 214.2 136.7 125.5 159.5 1,348.4",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil (AES Corp U.S.–controlled) — us. NEW nested 2028E CapEx R$159.5m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle284", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(159500000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2028E CapEx R$159.5m via Fed H.10. Supports aes_brasil_2028e_capex_159p5m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2028E Total Investments R$159.5m confirmed.",
)

# 8. power_plants_grid / prc — NEW CPFL TX 2028 CapEx R$1.059bn
row_doc(
    "cpfl_tx_2028_capex_1059m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — 2028 CapEx plan R$1.059bn",
    "Brazil",
    "28 May 2026 CPFL Transmissão Formulário de Referência: CapEx projection table CPFL-T shows 2028*=1.059 (R$1.059 billion) within 2026–2030 sequence 856 / 1.221 / 1.059 / 799 / 605. CapEx: enter R$1.059bn 2028 face. Nested vs cpfl_tx_2026_2030_4540m_brl / 2026 R$856m / 2027 R$1.221bn (not additive).",
    "1059000000", "2026-05-28", "2028", "-22.91", "-47.06",
    "CPFL Transmissão Brazil footprint (Campinas / São Paulo pin).",
    "cpfl_tx_fr_2026_20260528",
    "CPFL-T 804 856 1.221 1.059 799 605",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D",
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW nested 2028 TX CapEx plan R$1.059bn. Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle284", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(1059000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Transmissão. “Formulário de Referência 2026” (FR_CPFL Transmissão 2026). May 28, 2026. https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D.',
    annotation="CPFL TX 2028 CapEx R$1.059bn via Fed H.10. Supports cpfl_tx_2028_capex_1059m_brl.",
    evid_note="Opened CPFL Transmissão FR 2026 PDF; 2028*=1.059 CapEx projection confirmed.",
)

# 9. power_plants_grid / prc — NEW CPFL TX 2029 CapEx R$799m
row_doc(
    "cpfl_tx_2029_capex_799m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — 2029 CapEx plan R$799m",
    "Brazil",
    "28 May 2026 CPFL Transmissão Formulário de Referência: CapEx projection table CPFL-T shows 2029*=799 (R$799 million) within 2026–2030 sequence. CapEx: enter R$799m 2029 face. Nested vs cpfl_tx_2026_2030_4540m_brl / 2028 R$1.059bn (not additive).",
    "799000000", "2026-05-28", "2029", "-22.91", "-47.06",
    "CPFL Transmissão Brazil footprint (Campinas / São Paulo pin).",
    "cpfl_tx_fr_2026_20260528",
    "CPFL-T 804 856 1.221 1.059 799 605",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D",
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW nested 2029 TX CapEx plan R$799m. Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle284", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(799000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Transmissão. “Formulário de Referência 2026” (FR_CPFL Transmissão 2026). May 28, 2026. https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D.',
    annotation="CPFL TX 2029 CapEx R$799m via Fed H.10. Supports cpfl_tx_2029_capex_799m_brl.",
    evid_note="Opened CPFL Transmissão FR 2026 PDF; 2029*=799 CapEx projection confirmed.",
)


def upsert_bib(bib, bib_by, entry):
    sid = entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        old = existing.get("supports") or []
        new = entry["supports"] or []
        merged = list(dict.fromkeys(list(old) + list(new)))
        existing.update({k: v for k, v in entry.items() if k != "supports"})
        existing["supports"] = merged
    else:
        bib.append(entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("entries") or bib.get("sources") or []
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
    print(f"cycle284 added {len(added)}: {added}")
    print(f"cycle284 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
