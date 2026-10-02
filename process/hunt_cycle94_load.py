#!/usr/bin/env python3
"""Cycle 94 hunt: shuffle_seed=20261094; equal budget; U.S./PRC split; thin after.

Order: niobium, fission_smr, nickel, wind, solar, other_renewables,
engineering_epc, bridges_roads, port_ownership, rail, graphite, balsa,
building_materials, lithium, copper, water, port_cranes, power_plants_grid.
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
# infrastructure/bridges_roads — CRCC Mackenzie–Wismar Bridge (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "crcc_wismar_mackenzie_guyana_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Railway Construction (Caribbean) — Mackenzie–Wismar Bridge (Guyana)",
        "country": "Guyana",
        "asset": "Jan 2024 contract / Aug 2025 construction advance: Government of Guyana awards USD 35 million contract to China Railway Construction Corporation Limited / China Railway Construction (Caribbean) Co., Ltd. for new four-lane Mackenzie–Wismar Bridge in Linden (Region 10) — ~220 m precast concrete replacement of ageing single-lane crossing; DPI 19 Aug 2025 confirms permanent works progressing (precast anti-collision beams). Distinct from CRCC Demerara River Bridge.",
        "investment_type": "epc",
        "value": "35000000",
        "currency": "USD",
        "value_usd": "35000000",
        "fx_usd": "1",
        "fx_date": "2024-01-05",
        "year": "2024",
        "status": "active",
        "lat": "6.00",
        "lon": "-58.30",
        "geo_note": "Mackenzie–Wismar / Linden Demerara River crossing, Region 10 (DPI geography).",
        "evidence": "documented",
        "source_id": "dpi_wismar_mackenzie_20250819",
        "note": "Actor: China Railway Construction (Caribbean) / CRCC (PRC SOE) — prc. Official DPI Guyana names contractor and USD 35m; Stabroek corroborates Jan 2024 CRCCL signing.",
    },
    {
        "id": "crcc_wismar_mackenzie_guyana_2024",
        "retrieved": "2026-10-02",
        "source_id": "dpi_wismar_mackenzie_20250819",
        "url": "https://dpi.gov.gy/us35-million-mackenzie-wismar-bridge-advancing/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Work on the new US$35 million Mackenzie-Wismar four-lane bridge is now … Regarding permanent works, contractor China Railway Construction (Caribbean) Co., Ltd. has completed the construction and installation of all eight precast anti-collision beams",
        "note": "Opened DPI Guyana naming USD 35m Mackenzie–Wismar bridge and CRCC Caribbean as contractor.",
    },
    {
        "id": "dpi_wismar_mackenzie_20250819",
        "type": "government",
        "chicago": "Department of Public Information (Guyana). “US$35 Million Mackenzie-Wismar Bridge Advancing.” 19 August 2025.",
        "url": "https://dpi.gov.gy/us35-million-mackenzie-wismar-bridge-advancing/",
        "annotation": "DPI primary: USD 35m Mackenzie–Wismar four-lane bridge; CRCC Caribbean contractor. Supports crcc_wismar_mackenzie_guyana_2024.",
        "supports": ["crcc_wismar_mackenzie_guyana_2024", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# energy/solar — Danasun / Texhong Choloma solar+BESS MoU (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "danasun_choloma_solar_honduras_2024",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Danasun Energy Honduras (Texhong) — Choloma 300 MW solar + 60 MW BESS",
        "country": "Honduras",
        "asset": "2024 MoU with ENEE / continuing through 2025–26: Danasun Energy Honduras S.A. de C.V. (subsidiary of Chinese textile conglomerate Texhong International Group / Danasun Energy Hong Kong) develops Choloma (Cortés) solar park described as ~300 MW PV with 60 MW battery storage; authorities cite ~USD 400 million private investment (UNVERIFIED press/NGO figure — leave CapEx blank). Project still in administrative/EIA solicitation phase as of late 2025 per Expediente Público. Distinct from PowerChina ENEE 230 kV transmission.",
        "investment_type": "greenfield_plant",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "15.61",
        "lon": "-87.95",
        "geo_note": "Choloma municipality, Cortés Department (Expediente Público / ENEE geography).",
        "evidence": "proxy",
        "source_id": "expediente_danasun_choloma_2026",
        "note": "Actor: Danasun/Texhong (PRC/HK corporate group) — prc. UNVERIFIED proxy: Expediente Público investigative report citing ~USD 400m and 300 MW+60 MW BESS; contract texts not released. CapEx blank.",
    },
    {
        "id": "danasun_choloma_solar_honduras_2024",
        "retrieved": "2026-10-02",
        "source_id": "expediente_danasun_choloma_2026",
        "url": "https://www.expedientepublico.org/asfura-government-withholds-key-details-of-chinese-solar-megaproject-amid-transparency-concerns/",
        "price_year": "2024",
        "evidence": "proxy",
        "quote": "The project is being developed by Danasun Energy Honduras S.A. de C.V., a subsidiary of the Chinese textile conglomerate Texhong International Group Ltd. … promoting a US$400 million Chinese-backed solar megaproject … plant’s projected capacity—300 MW with 60 MW of battery storage",
        "note": "Opened Expediente Público English report naming Danasun/Texhong Choloma 300 MW+60 MW BESS and ~USD 400m figure; CapEx left blank as UNVERIFIED.",
    },
    {
        "id": "expediente_danasun_choloma_2026",
        "type": "press",
        "chicago": "Expediente Público. “Asfura Government Withholds Key Details of Chinese Solar Megaproject Amid Transparency Concerns.” 2026.",
        "url": "https://www.expedientepublico.org/asfura-government-withholds-key-details-of-chinese-solar-megaproject-amid-transparency-concerns/",
        "annotation": "UNVERIFIED proxy: Danasun/Texhong Choloma ~300 MW solar + 60 MW BESS; ~USD 400m cited. Supports danasun_choloma_solar_honduras_2024.",
        "supports": ["danasun_choloma_solar_honduras_2024", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/port_ownership — APMT Balboa temporary concession (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "apmt_balboa_temp_panama_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "APMT Panamá / APM Terminals — temporary Balboa concession",
        "country": "Panama",
        "asset": "23–24 Feb 2026: After CSJ annulment of Panama Ports Company (Hutchison) concession, Cabinet/AMP awards Contrato No. A-2002-26 transitional concession to APMT Panamá, S.A. (APM Terminals / A.P. Moller–Maersk) to operate, maintain and administer Port of Balboa (Pacific) for up to 18 months; concessionaire contraprestación USD 26.1 million. Distinct from Corozal/Telfers prequalification.",
        "investment_type": "concession",
        "value": "26100000",
        "currency": "USD",
        "value_usd": "26100000",
        "fx_usd": "1",
        "fx_date": "2026-02-23",
        "year": "2026",
        "status": "active",
        "lat": "8.95",
        "lon": "-79.57",
        "geo_note": "Port of Balboa, Pacific entrance Panama Canal (AMP / Infobae geography).",
        "evidence": "documented",
        "source_id": "infobae_panama_balboa_cristobal_20260224",
        "note": "Actor: APM Terminals (Danish Maersk group) — allied. Infobae citing Contraloría/AMP refrendo states USD 26.1m contraprestación for Balboa.",
    },
    {
        "id": "apmt_balboa_temp_panama_2026",
        "retrieved": "2026-10-02",
        "source_id": "infobae_panama_balboa_cristobal_20260224",
        "url": "https://www.infobae.com/panama/2026/02/24/contraloria-avala-contratos-por-419-millones-para-la-operacion-de-los-puertos-de-balboa-y-cristobal-en-panama/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El acuerdo aprobado contempla montos de $26,100,000.00 para la operación del puerto de Balboa y $15,800,000.00 para la administración de Cristóbal. … APMT Panamá S.A. operará el puerto de Balboa durante 18 meses por $26,100,000.00",
        "note": "Opened Infobae Panama citing Contraloría refrendo of AMP–APMT Balboa temporary concession at USD 26.1m.",
    },
    {
        "id": "infobae_panama_balboa_cristobal_20260224",
        "type": "press",
        "chicago": "Infobae. “Contraloría Avala Contratos por $41.9 Millones para la Operación de los Puertos de Balboa y Cristóbal en Panamá.” 24 February 2026.",
        "url": "https://www.infobae.com/panama/2026/02/24/contraloria-avala-contratos-por-419-millones-para-la-operacion-de-los-puertos-de-balboa-y-cristobal-en-panama/",
        "annotation": "Press citing Contraloría/AMP: APMT Balboa USD 26.1m and TIL Cristóbal USD 15.8m temporary concessions. Supports apmt_balboa_temp_panama_2026; til_cristobal_temp_panama_2026.",
        "supports": [
            "apmt_balboa_temp_panama_2026",
            "til_cristobal_temp_panama_2026",
            "hunt_infra_port_ownership",
        ],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/port_ownership — TIL Cristóbal temporary concession (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "til_cristobal_temp_panama_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "TIL Panamá / Terminal Investment Limited — temporary Cristóbal concession",
        "country": "Panama",
        "asset": "23–24 Feb 2026: AMP awards Contrato No. A-2003-26 transitional concession to TIL Panamá, S.A. (Terminal Investment Limited / MSC group) to operate, maintain and administer Port of Cristóbal (Atlantic) for up to 18 months; concessionaire contraprestación USD 15.8 million. Paired with APMT Balboa temporary award after PPC annulment.",
        "investment_type": "concession",
        "value": "15800000",
        "currency": "USD",
        "value_usd": "15800000",
        "fx_usd": "1",
        "fx_date": "2026-02-23",
        "year": "2026",
        "status": "active",
        "lat": "9.35",
        "lon": "-79.90",
        "geo_note": "Port of Cristóbal, Atlantic/Colón (AMP / Infobae geography).",
        "evidence": "documented",
        "source_id": "infobae_panama_balboa_cristobal_20260224",
        "note": "Actor: TIL / MSC (Swiss) — allied. Same Infobae Contraloría refrendo source as Balboa; USD 15.8m contraprestación.",
    },
    {
        "id": "til_cristobal_temp_panama_2026",
        "retrieved": "2026-10-02",
        "source_id": "infobae_panama_balboa_cristobal_20260224",
        "url": "https://www.infobae.com/panama/2026/02/24/contraloria-avala-contratos-por-419-millones-para-la-operacion-de-los-puertos-de-balboa-y-cristobal-en-panama/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "TIL Panamá S.A. asumirá la administración del puerto de Cristóbal por $15,800,000.00 en el mismo periodo … Contrato de … No. A-2003-26 con TIL Panamá",
        "note": "Opened Infobae Panama citing Contraloría refrendo of AMP–TIL Cristóbal temporary concession at USD 15.8m.",
    },
    {
        "id": "infobae_panama_balboa_cristobal_20260224",
        "type": "press",
        "chicago": "Infobae. “Contraloría Avala Contratos por $41.9 Millones para la Operación de los Puertos de Balboa y Cristóbal en Panamá.” 24 February 2026.",
        "url": "https://www.infobae.com/panama/2026/02/24/contraloria-avala-contratos-por-419-millones-para-la-operacion-de-los-puertos-de-balboa-y-cristobal-en-panama/",
        "annotation": "Press citing Contraloría/AMP: APMT Balboa USD 26.1m and TIL Cristóbal USD 15.8m temporary concessions. Supports apmt_balboa_temp_panama_2026; til_cristobal_temp_panama_2026.",
        "supports": [
            "apmt_balboa_temp_panama_2026",
            "til_cristobal_temp_panama_2026",
            "hunt_infra_port_ownership",
        ],
    },
)

# ---------------------------------------------------------------------------
# energy/fission_smr — CONUAR × Terra Innovatum SOLO MMR (allied) thin top-up
# ---------------------------------------------------------------------------
A(
    {
        "id": "terra_conuar_solo_argentina_2025",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "allied",
        "counterpart": "Terra Innovatum × CONUAR — SOLO™ micro-modular reactor components (Argentina)",
        "country": "Argentina",
        "asset": "Sep 2025: CONUAR (Argentine nuclear-fuel/components manufacturer) signs strategic industrial cooperation agreement with Terra Innovatum (Italian SOLO™ MMR developer; later dual-listed / U.S. ops) for CONUAR to develop and supply cooling tubes/plates, control-rod mechanisms, fuel-rod assemblies and specialty alloy components for SOLO; Terra envisions future SOLO assembly lines in South America. CapEx USD not disclosed.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-34.82",
        "lon": "-58.52",
        "geo_note": "CONUAR industrial facilities, Ezeiza / Buenos Aires Province (company geography).",
        "evidence": "documented",
        "source_id": "conuar_terra_solo_20250919",
        "note": "Actor: Terra Innovatum (Italian HQ s.r.l. / Global N.V.) — allied; CONUAR is Argentine state-linked manufacturer (other) not dual-tagged. Company primary. CapEx blank. Thin top-up fission_smr.",
    },
    {
        "id": "terra_conuar_solo_argentina_2025",
        "retrieved": "2026-10-02",
        "source_id": "conuar_terra_solo_20250919",
        "url": "https://conuar.ar/en/conuar-signs-strategic-agreement-with-terra-innovatum-for-the-development-of-the-solo-micro-modular-reactor/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "CONUAR … has signed a strategic industrial cooperation agreement with Terra Innovatum, developer of the innovative SOLO™ Micro-Modular Reactor (MMR). … CONUAR will develop and supply essential nuclear components for the SOLO™ reactor’s operation … future SOLO™ assembly lines are envisioned in South America",
        "note": "Opened CONUAR English release naming Terra Innovatum SOLO industrial cooperation and Argentina component supply.",
    },
    {
        "id": "conuar_terra_solo_20250919",
        "type": "company",
        "chicago": "CONUAR. “CONUAR Signs Strategic Agreement with Terra Innovatum for the Development of the SOLO™ Micro-Modular Reactor.” 19 September 2025.",
        "url": "https://conuar.ar/en/conuar-signs-strategic-agreement-with-terra-innovatum-for-the-development-of-the-solo-micro-modular-reactor/",
        "annotation": "CONUAR primary: SOLO MMR component cooperation with Terra Innovatum; LatAm supply-hub intent. Supports terra_conuar_solo_argentina_2025.",
        "supports": ["terra_conuar_solo_argentina_2025", "hunt_energy_fission_smr"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — Crowley American Energy LNG to Peñuelas (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "crowley_american_energy_lng_pr_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Crowley — American Energy U.S.-flag LNG carrier serving Naturgy Peñuelas (Puerto Rico)",
        "country": "Puerto Rico",
        "asset": "18 Mar 2025: Crowley raises U.S. flag on American Energy (130,400 m³ LNG carrier) and begins multi-year deliveries of U.S. mainland-sourced LNG to Naturgy’s Peñuelas (EcoEléctrica) facility under Crowley–Naturgy agreement; Crowley also operates Peñuelas LNG Loading Terminal (~94 million gallons/year ISO-tank distribution) and Isla Grande cargo terminal. CapEx for vessel/agreement USD not disclosed on Crowley release.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "17.97",
        "lon": "-66.76",
        "geo_note": "Naturgy/EcoEléctrica Peñuelas LNG facility, southern Puerto Rico (Crowley geography).",
        "evidence": "documented",
        "source_id": "crowley_american_energy_20250318",
        "note": "Actor: Crowley Corporation (U.S. HQ Jacksonville) — us. Company primary. CapEx blank. Distinct from Excelerate Jamaica NFE acquisition.",
    },
    {
        "id": "crowley_american_energy_lng_pr_2025",
        "retrieved": "2026-10-02",
        "source_id": "crowley_american_energy_20250318",
        "url": "https://www.crowley.com/news-and-media/press-releases/crowley-and-naturgy-deploy-first-u-s-lng-carrier-american-energy-to-serve-puerto-rico/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Crowley has raised the U.S. flag on American Energy, commencing operations of the first domestic liquified natural gas (LNG) carrier to transport U.S.-sourced natural gas to Puerto Rico. … Crowley and Naturgy have entered into a multi-year agreement that provides for the regular delivery of the U.S. mainland-sourced LNG to Naturgy’s operating facility in Penuelas, Puerto Rico.",
        "note": "Opened Crowley press release naming American Energy U.S.-flag LNG service to Naturgy Peñuelas.",
    },
    {
        "id": "crowley_american_energy_20250318",
        "type": "company",
        "chicago": "Crowley. “Crowley and Naturgy Deploy First U.S. LNG Carrier, American Energy, to Serve Puerto Rico.” 18 March 2025.",
        "url": "https://www.crowley.com/news-and-media/press-releases/crowley-and-naturgy-deploy-first-u-s-lng-carrier-american-energy-to-serve-puerto-rico/",
        "annotation": "Crowley primary: American Energy LNG carrier multi-year Peñuelas deliveries. Supports crowley_american_energy_lng_pr_2025.",
        "supports": ["crowley_american_energy_lng_pr_2025", "hunt_br_power_equip"],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]] = entry
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8"))
    assert isinstance(bib, list)
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
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

    hunt_updates = {
        "hunt_fenb_araxa": "Cycle 94: equal budget; CMOC / CBMM dense (miss).",
        "hunt_energy_fission_smr": "Cycle 94: thin top-up logged terra_conuar_solo_argentina_2025 (allied; CapEx blank).",
        "hunt_res_nickel": "Cycle 94: equal budget; BRN DFC / Westwin / BNDES already (miss). Thin dry — shift.",
        "hunt_energy_wind": "Cycle 94: equal budget; Goldwind Sento Sé / Envision / Jacobina dense (miss).",
        "hunt_energy_solar": "Cycle 94: logged danasun_choloma_solar_honduras_2024 (PRC; CapEx blank proxy).",
        "hunt_energy_other_renewables": "Cycle 94: equal budget; Huawei Amazonas / AES Andes / Fluence LinkedIn-only (miss).",
        "hunt_infra_engineering_epc": "Cycle 94: equal budget; Halliburton Zeus / CHEXIM–BNDES / Fluor unnamed (miss).",
        "hunt_infra_bridges_roads": "Cycle 94: logged crcc_wismar_mackenzie_guyana_2024 (PRC; USD 35m DPI).",
        "hunt_infra_port_ownership": "Cycle 94: logged apmt_balboa_temp_panama_2026 + til_cristobal_temp_panama_2026 (allied).",
        "hunt_latam_rail_telecom": "Cycle 94: equal budget; Wabtec / Progress Rail / PowerChina Chancay dense (miss).",
        "hunt_res_graphite": "Cycle 94: equal budget; Graphcoa Jordânia dense (miss). Thin dry — shift.",
        "hunt_res_balsa": "Cycle 94: equal budget; Plantabal / AIMA dense (miss). Thin dry — shift.",
        "hunt_infra_building_materials": "Cycle 94: equal budget; Sinoma PANAM / CHEC housing dense (miss).",
        "hunt_res_lithium": "Cycle 94: equal budget; Zijin / Atlas / EXIM Argentina dense (miss).",
        "hunt_res_copper": "Cycle 94: equal budget; FCX El Abra / Fluor unnamed Chile (miss).",
        "hunt_res_water": "Cycle 94: equal budget; CWE Zapallar / Sacyr Coquimbo / IDE SADDN dense (miss).",
        "hunt_infra_port_cranes": "Cycle 94: equal budget; ZPMC Kingston / Aguadulce / ICAVE dense (miss).",
        "hunt_br_power_equip": "Cycle 94: logged crowley_american_energy_lng_pr_2025 (U.S.; CapEx blank).",
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
    print("Cycle 94 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
