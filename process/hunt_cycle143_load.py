#!/usr/bin/env python3
"""Cycle 143 hunt: shuffle_seed=20261143; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: copper, fission_smr, rail, bridges_roads, engineering_epc,
building_materials, port_cranes, power_plants_grid, balsa, solar, other_renewables,
port_ownership, graphite, water, lithium, niobium, nickel, wind.

PRC ahead by 8 after 142 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite then fission_smr/nickel (dry → niobium).
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
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
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


# 1. solar / us — AES Colombia Solar 3 ANLA environmental license (100 MW)
row_doc(
    "aes_colombia_solar3_anla_100mw_2025",
    "energy",
    "solar",
    "us",
    "AES Colombia — Parque Fotovoltaico AES Solar 3 (Armero Guayabal, Tolima)",
    "Colombia",
    "11 Sep 2025 ANLA: environmental license for Parque Fotovoltaico AES Solar 3 — 100 MW in Armero Guayabal (Tolima), developed by AES Colombia & Cía S.C.A. E.S.P.; 227.10 ha; 212,464 PV modules on 2,781 trackers; 230 kV connection (~402 m) to San Felipe substation; approved compensation plan 154.30 ha. CapEx blank on ANLA notice (permitting milestone).",
    "",
    "",
    "2025",
    "5.030",
    "-74.885",
    "Armero Guayabal municipality, Tolima Department, Colombia (ANLA project geography).",
    "anla_aes_solar3_tolima_20250911",
    "El Parque Fotovoltaico AES Solar 3 contará con una capacidad instalada de 100 MW (megavatios) y será desarrollado por AES Colombia & Cía S.C.A. E.S.P. Contará con… 212.464 módulos fotovoltaicos instalados en 2.781 estructuras con seguimiento solar (trackers).",
    "https://www.anla.gov.co/noticias-anla/luz-verde-al-parque-fotovoltaico-aes-solar-3-y-a-la-subestacion-huila-230-kv-con-sus-lineas-de-conexion",
    "Actor: AES Colombia (AES Corporation, Arlington VA — us). ANLA government primary. CapEx blank. Distinct from aes_jk* Guajira wind cluster.",
    "hunt_energy_solar",
    investment_type="greenfield_generation",
    bib_type="government",
    chicago='Autoridad Nacional de Licencias Ambientales (ANLA). “Luz verde al Parque Fotovoltaico AES Solar 3 y a la Subestación Huila 230 kV con sus líneas de conexión.” September 11, 2025. https://www.anla.gov.co/noticias-anla/luz-verde-al-parque-fotovoltaico-aes-solar-3-y-a-la-subestacion-huila-230-kv-con-sus-lineas-de-conexion.',
    annotation="ANLA primary: AES Solar 3 100 MW environmental license Tolima. Supports aes_colombia_solar3_anla_100mw_2025.",
    evid_note="Opened ANLA release 11 Sep 2025 (AES Solar 3 100 MW license).",
)

# 2. other_renewables / prc — POWERCHINA SEPCO1 + CEEC Northwest Barueri WtE
row_doc(
    "powerchina_barueri_wte_brazil_2025",
    "energy",
    "other_renewables",
    "prc",
    "POWERCHINA SEPCO1 + CEEC Northwest Electric Power Design — URE Barueri waste-to-energy",
    "Brazil",
    "4 Nov 2025 Xinhua via Belt and Road Portal: Barueri (São Paulo) waste-to-energy plant jointly built by POWERCHINA Shandong Electric Power Construction No.1 (SEPCO1) and China Energy Engineering Group Northwest Electric Power Design Institute; ~37,000 m²; design 870 t/day MSW; installed capacity 19.1 MW; entered installation mid-2025; COD expected 2027 — among first LatAm WtE incineration plants. CapEx blank on Xinhua/Yidaiyilu page (owner Orizon CapEx separate; not EPC-attributed here).",
    "",
    "",
    "2025",
    "-23.511",
    "-46.876",
    "Barueri, São Paulo state, Brazil (project site / municipal geography).",
    "yidaiyilu_powerchina_barueri_wte_20251104",
    "作为巴西乃至拉美首批垃圾发电站之一的巴鲁埃里垃圾发电站即将完成建设。项目占地约3.7万平方米，由中国电建集团山东电力建设第一工程有限公司…与中国能建集团中国电力工程顾问集团西北电力设计院有限公司联合承建。…项目设计日处理固体垃圾870吨，装机容量19.1兆瓦。",
    "https://www.yidaiyilu.gov.cn/p/070OB3ME.html",
    "Actor: POWERCHINA SEPCO1 + CEEC Northwest Design (PRC SOEs) — prc. BRI portal / Xinhua primary. CapEx blank. WtE coded other_renewables. Distinct from biogas landfill rows.",
    "hunt_energy_other_renewables",
    investment_type="epc",
    bib_type="government",
    chicago='Belt and Road Portal (citing Xinhua). “中企承建垃圾发电站助力巴西‘变废为能’.” November 4, 2025. https://www.yidaiyilu.gov.cn/p/070OB3ME.html.',
    annotation="BRI/Xinhua primary: POWERCHINA Barueri WtE 19.1 MW / 870 t/day under construction. Supports powerchina_barueri_wte_brazil_2025.",
    evid_note="Opened yidaiyilu.gov.cn Xinhua feature 4 Nov 2025 (Barueri WtE POWERCHINA EPC).",
)

# 3. wind / prc — CTG Luz del Sur acquires San Juan de Marcona (Red Coral) 135.7 MW
row_doc(
    "ctg_lds_red_coral_marcona_256m_2025",
    "energy",
    "wind",
    "prc",
    "CTG / Luz del Sur — San Juan de Marcona (Red Coral) wind farm equity acquisition",
    "Peru",
    "16 Dec 2025 ACCIONA Energía: closed sale of San Juan de Marcona wind farm (135.7 MW) in Peru to Luz del Sur S.A.A. (CTG subsidiary) for US$256 million (€218 million); INDECOPI approvals completed. CTG English (22 Dec 2025) confirms LDS equity transfer of Red Coral Wind Power Project — third LDS renewable acquisition; LDS becomes Peru’s largest wind operator. CapEx = transaction value from ACCIONA seller primary.",
    "256000000",
    "2025-12-16",
    "2025",
    "-15.360",
    "-75.160",
    "San Juan de Marcona, Ica Region, Peru (ACCIONA / asset geography; CTG note cites Lima closing).",
    "acciona_energia_san_juan_marcona_sale_20251216",
    "ACCIONA Energía has closed today the sale of San Juan de Marcona wind farm (135.7 MW) in Peru to Luz del Sur S.A.A., one of the country's leading energy companies. … The value of the transaction amounts to US$256 million (€218 million).",
    "https://www.acciona-energia.com/updates/news/acciona-energia-completes-sale-san-juan-marcona-wind-farm-peru",
    "Actor: buyer Luz del Sur (CTG / China Three Gorges subsidiary) — prc. Seller ACCIONA Energía primary for USD 256m / 135.7 MW. CTG English corroborates Red Coral equity transfer. Distinct from prior LDS Tres Hermanas/Marcona USD 170m (2024) sapphire cluster.",
    "hunt_energy_wind",
    investment_type="acquisition",
    chicago='ACCIONA Energía. “ACCIONA Energía completes the sale of San Juan de Marcona wind farm in Perú.” December 16, 2025. https://www.acciona-energia.com/updates/news/acciona-energia-completes-sale-san-juan-marcona-wind-farm-peru.',
    annotation="ACCIONA Energía primary: San Juan de Marcona 135.7 MW sold to CTG Luz del Sur for USD 256m. Supports ctg_lds_red_coral_marcona_256m_2025.",
    evid_note="Opened ACCIONA Energía release 16 Dec 2025 (Marcona/Red Coral sale to LDS USD 256m).",
)

# 4. wind / us — AES Andes San Matías COD
row_doc(
    "aes_andes_san_matias_cod_2024",
    "energy",
    "wind",
    "us",
    "AES Andes — San Matías Wind Farm COD (Los Ángeles, Biobío)",
    "Chile",
    "27 Jun 2024 AES Andes: San Matías Wind Farm in Los Ángeles, Biobío Region, commenced commercial operation after National Electric Coordinator authorization — 78 MW; fifth AES Andes wind farm; construction began late 2022; part of Biobío renewable hub. CapEx blank on COD release (portfolio Greentegra >USD 1.8bn narrative not project-attributed).",
    "",
    "",
    "2024",
    "-37.470",
    "-72.350",
    "Los Ángeles / Laja communes, Biobío Region, Chile (company geography).",
    "aes_andes_san_matias_cod_20240627",
    "AES Andes announced that its San Matías Wind Farm, located in Los Ángeles, Biobío region, has commenced commercial operation following authorization from the National Electric Coordinator. … San Matías, with a capacity of 78 MW, began construction in late 2022…",
    "https://www.aesandes.com/en/press-release/aes-andes-initiates-commercial-operation-san-matias-and-consolidates-its-wind",
    "Actor: AES Andes / AES Corporation — us. Company English primary. CapEx blank. Distinct from aes_jk* Colombia and aes_andes_solar_* Chile solar/BESS rows.",
    "hunt_energy_wind",
    investment_type="greenfield_generation",
    chicago='AES Andes. “AES Andes initiates commercial operation of San Matías and consolidates its wind generation in Biobío.” June 27, 2024. https://www.aesandes.com/en/press-release/aes-andes-initiates-commercial-operation-san-matias-and-consolidates-its-wind.',
    annotation="AES Andes primary: San Matías 78 MW wind COD Jun 2024. Supports aes_andes_san_matias_cod_2024.",
    evid_note="Opened AES Andes English release 27 Jun 2024 (San Matías COD 78 MW).",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        supports = list(existing.get("supports") or [])
        for s in entry.get("supports") or []:
            if s not in supports:
                supports.append(s)
        existing.update(entry)
        existing["supports"] = supports
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

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

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 143 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
