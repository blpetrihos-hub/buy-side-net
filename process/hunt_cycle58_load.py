#!/usr/bin/env python3
"""Cycle 58 hunt: shuffle_seed=20261058; equal budget; U.S. ≥1/3; thin after.

Order: building_materials, other_renewables, engineering_epc, copper, niobium,
power_plants_grid, bridges_roads, port_cranes, water, wind, rail, fission_smr,
nickel, balsa, lithium, solar, graphite, port_ownership.
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
# 1 building_materials — Sinoma CBMI PANAM grind plant (DR) (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sinoma_panam_grind_dr_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "prc",
        "counterpart": "Sinoma CBMI Latin America — Cemento Panam grinding plant (Dominican Republic)",
        "country": "Dominican Republic",
        "asset": "2 May 2025 International Cement Review: Sinoma CBMI Latin America SRL (CNBM) nearing completion of modern cement grinding plant for Cemento Panam (Grupo Estrella) in Dominican Republic; planned capacity 1.23 Mtpa; Gebr Pfeiffer VRM ~155 tph mixed cement. Distinct from sinoma_cibao_clinker_line_2026.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "18.49",
        "lon": "-69.93",
        "geo_note": "Dominican Republic Cemento Panam / Grupo Estrella grinding site (national pin; plant municipality not named on ICR page).",
        "evidence": "documented",
        "source_id": "cemnet_sinoma_panam_20250502",
        "note": "Actor: Sinoma CBMI / CNBM (PRC) — prc. Company-trade press; CapEx USD not disclosed on opened page.",
    },
    {
        "id": "sinoma_panam_grind_dr_2025",
        "retrieved": "2026-10-01",
        "source_id": "cemnet_sinoma_panam_20250502",
        "url": "https://www.cemnet.com/News/story/179075/sinoma-cbmi-latin-america-close-to-completing-panam-project.html",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Sinoma CBMI Latin America, a subsidiary of China National Building Material Group, is completing the construction of the modern cement grinding plant for Cemento Panam, part of Grupo Estrella, in the Dominican Republic. With a planned production capacity of 1.23Mta, the project integrates advanced, carbon-neutral technologies… One of the key components is a Gebr Pfeiffer vertical roller mill, capable of producing 155tph of mixed cement.",
        "note": "Opened International Cement Review / CemNet 2 May 2025.",
    },
    {
        "id": "cemnet_sinoma_panam_20250502",
        "type": "press",
        "chicago": "International Cement Review. “Sinoma CBMI Latin America Close to Completing PANAM Project.” 2 May 2025.",
        "url": "https://www.cemnet.com/News/story/179075/sinoma-cbmi-latin-america-close-to-completing-panam-project.html",
        "annotation": "Trade press on Sinoma CBMI Cemento Panam DR grinding plant near completion. Supports sinoma_panam_grind_dr_2025.",
        "supports": ["sinoma_panam_grind_dr_2025", "hunt_infra_building_materials"],
    },
)

# ---------------------------------------------------------------------------
# 3 engineering_epc — Pumpco (U.S.) / Bonatti / Contreras Argentina LNG pipelines (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "pumpco_bonatti_argentina_lng_epc_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Pumpco (MasTec) / Bonatti / Contreras Hermanos — Argentina LNG dual pipelines EPC",
        "country": "Argentina",
        "asset": "30 Jul 2026 Bonatti: JV with U.S. pipeline contractor Pumpco (plus Contreras Hermanos) awarded EPC for complete Argentina LNG pipeline system — 48-inch gas + parallel liquids pipelines, each ~527 km from Meseta Buena Esperanza (Vaca Muerta) to Sierra Grande (Río Negro). Client thanks ENI/YPF/XRG. Contract USD not on Bonatti primary; BNamericas/Il Sole cite ~USD 1.2bn total JV — not entered. Distinct from Southern Energy / other Vaca Muerta midstream rows.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-38.60",
        "lon": "-68.30",
        "geo_note": "Meseta Buena Esperanza / Vaca Muerta corridor start toward Sierra Grande, Río Negro (approximate basin pin).",
        "evidence": "documented",
        "source_id": "bonatti_argentina_lng_20260730",
        "note": "Actor: Pumpco (U.S.; MasTec) in JV with Bonatti (Italy) and Contreras (AR) — coded us for U.S. pipeline EPC lead. Company primary; USD blank (press USD 1.2bn UNVERIFIED, not booked).",
    },
    {
        "id": "pumpco_bonatti_argentina_lng_epc_2026",
        "retrieved": "2026-10-01",
        "source_id": "bonatti_argentina_lng_20260730",
        "url": "https://www.bonattinternational.com/bonatti-argentina-lng-project",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Bonatti, in joint venture with Pumpco, has been awarded the Engineering, Procurement and Construction (EPC) contract for the complete pipeline system of the Argentina LNG project… The scope of work includes the construction of a 48-inch natural gas pipeline and a parallel liquids pipeline, each extending approximately 527 kilometers from Meseta Buena Esperanza, in the Vaca Muerta basin, to Sierra Grande, in Río Negro Province… Pumpco, a leading U.S. pipeline contractor… The joint venture also includes Contreras Hermanos…",
        "note": "Opened Bonatti company page 30 Jul 2026.",
    },
    {
        "id": "bonatti_argentina_lng_20260730",
        "type": "company",
        "chicago": "Bonatti S.p.A. “Bonatti, in Joint Venture with Pumpco, Has Been Awarded the EPC Contract for the Complete Pipeline System of the Argentina LNG Project.” 30 July 2026.",
        "url": "https://www.bonattinternational.com/bonatti-argentina-lng-project",
        "annotation": "Bonatti primary on Pumpco JV Argentina LNG dual 527 km pipelines. Supports pumpco_bonatti_argentina_lng_epc_2026.",
        "supports": ["pumpco_bonatti_argentina_lng_epc_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 4a copper — Zijin La Arena / La Arena II Peru acquisition (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "zijin_la_arena_peru_245m_2024",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "Zijin Mining / Jinteng — La Arena gold mine + La Arena II Cu-Au (Peru)",
        "country": "Peru",
        "asset": "6 Nov 2024 Zijin HKEX/company PDF: Jinteng (Singapore) to acquire 100% of La Arena S.A. from Pan American Silver for USD 245 million cash at closing + USD 50 million contingent on La Arena II commercial production + 1.5% gold NSR; La Arena II porphyry Cu-Au (La Libertad) designed ~33 Mtpa / ~100 ktpa Cu + 3.8 tpa Au after 3-year build. Closing announced Dec 2024. Distinct from Río Blanco / other Zijin Peru rows.",
        "investment_type": "ownership_equity",
        "value": "245000000",
        "currency": "USD",
        "value_usd": "245000000",
        "fx_usd": "1",
        "fx_date": "2024-11-06",
        "year": "2024",
        "status": "active",
        "lat": "-7.83",
        "lon": "-78.45",
        "geo_note": "La Arena project, Department of La Libertad, northern Peru (~3,000–3,600 m; ~150 km from Trujillo per Zijin).",
        "evidence": "documented",
        "source_id": "zijin_la_arena_acquisition_20241106",
        "note": "Actor: Zijin Mining (PRC) — prc. Value = upfront cash consideration USD 245m from company announcement (contingent USD 50m not summed into value).",
    },
    {
        "id": "zijin_la_arena_peru_245m_2024",
        "retrieved": "2026-10-01",
        "source_id": "zijin_la_arena_acquisition_20241106",
        "url": "https://www.zijinmining.com/upload/file/2024/11/07/381ddb152af942a78df2ca710cfaf4e3.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Jinteng (Singapore) Mining Pte. Ltd. … proposed to acquire 100% interest of the La Arena Gold Mine and La Arena II copper-gold project in Peru … for a cash consideration of USD$245 million, plus a USD$50 million contingent payment and a 1.5% NSR payable on commercial production from La Arena II… Based on a design with an annual mining and processing scale of 33 million tonnes… expected annual production… approximately 100 thousand tonnes of copper and 3.8 tonnes of gold.",
        "note": "Opened Zijin company PDF announcement 6/7 Nov 2024.",
    },
    {
        "id": "zijin_la_arena_acquisition_20241106",
        "type": "company",
        "chicago": "Zijin Mining Group Co., Ltd. “Announcement in Relation to Acquisition of the La Arena Gold Mine and La Arena II Project in Peru.” 6 November 2024.",
        "url": "https://www.zijinmining.com/upload/file/2024/11/07/381ddb152af942a78df2ca710cfaf4e3.pdf",
        "annotation": "Zijin primary on La Arena / La Arena II Peru acquisition terms and Cu production design. Supports zijin_la_arena_peru_245m_2024.",
        "supports": ["zijin_la_arena_peru_245m_2024", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 4b copper — Southern Copper El Pilar Sonora USD 551m (other)
# ---------------------------------------------------------------------------
A(
    {
        "id": "southern_copper_el_pilar_551m_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "other",
        "counterpart": "Southern Copper (Grupo México) — El Pilar SX-EW copper (Sonora)",
        "country": "Mexico",
        "asset": "21 Jul 2026 Southern Copper 2Q26 release: El Pilar (Sonora, ~45 km from Cananea/Buenavista) obtained environmental permits; early site prep Sep 2026; construction 1Q27; production 2H29; open-pit SX-EW 36 ktpa Cu cathode; P&P reserves 317 Mt @ 0.249% Cu; LOM 18 years; investment USD 551 million; 450 construction / 300 ops jobs. Distinct from Tía María / El Arco / Buenavista rows.",
        "investment_type": "greenfield_mine",
        "value": "551000000",
        "currency": "USD",
        "value_usd": "551000000",
        "fx_usd": "1",
        "fx_date": "2026-07-21",
        "year": "2026",
        "status": "active",
        "lat": "30.95",
        "lon": "-110.15",
        "geo_note": "El Pilar, Sonora (~45 km from Cananea/Buenavista; approximate municipal pin).",
        "evidence": "documented",
        "source_id": "scc_2q26_el_pilar_20260721",
        "note": "Actor: Southern Copper / Grupo México (Mexican) — other. Company primary CapEx USD 551m.",
    },
    {
        "id": "southern_copper_el_pilar_551m_2026",
        "retrieved": "2026-10-01",
        "source_id": "scc_2q26_el_pilar_20260721",
        "url": "https://southerncoppercorp.com/wp-content/uploads/2026/07/pr260721.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El Pilar - Sonora. This new copper project has obtained the necessary environmental permits and will begin early site preparation works in September 2026… Project construction will commence in the first quarter of 2027, and production is expected to begin in the second half of 2029… With an investment of $551 million, this project will employ a direct workforce of 450 people during the construction phase and 300 during the operational phase.",
        "note": "Opened Southern Copper 2Q26 results PDF 21 Jul 2026.",
    },
    {
        "id": "scc_2q26_el_pilar_20260721",
        "type": "company",
        "chicago": "Southern Copper Corporation. “Southern Copper Corporation Reports Second Quarter and Six Months 2026 Results.” 21 July 2026.",
        "url": "https://southerncoppercorp.com/wp-content/uploads/2026/07/pr260721.pdf",
        "annotation": "SCC primary on El Pilar permits, schedule, and USD 551m investment. Supports southern_copper_el_pilar_551m_2026.",
        "supports": ["southern_copper_el_pilar_551m_2026", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 6 power_plants_grid — Hitachi Energy Chile mobile digital HV substation (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "hitachi_chile_mobile_digital_substation_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Hitachi Energy — Grid-eXpand mobile digital HV substation (Chile mining client)",
        "country": "Chile",
        "asset": "11 Mar 2026 Hitachi Energy Chile: first mobile digital high-voltage substation in Chile (Grid-eXpand) for a major mining operator — HV trailer with 25/33 MVA transformer + 69 kV GIS and digital protection; second trailer MV switchgear/electrical room; >5,000 man-hours; relocatable with mine plant commissioning. Client unnamed. CapEx USD not disclosed. Distinct from Hitachi Dosquebradas/Brazil transformer CapEx and Garabi/Rio Madeira HVDC rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-33.45",
        "lon": "-70.67",
        "geo_note": "Chile mining client site undisclosed; Santiago metro pin for Hitachi Chile delivery announcement.",
        "evidence": "documented",
        "source_id": "hitachi_chile_mobile_sub_20260311",
        "note": "Actor: Hitachi Energy (Swiss HQ / global) — allied. Company primary; contract USD not disclosed.",
    },
    {
        "id": "hitachi_chile_mobile_digital_substation_2026",
        "retrieved": "2026-10-01",
        "source_id": "hitachi_chile_mobile_sub_20260311",
        "url": "https://www.hitachienergy.com/news-and-events/press-releases/2026/05/hitachi-energy-marca-un-hito-con-la-implementaci-n-de-la-primera-subestaci-n-digital-m-vil-de-alta-tensi-n-en-chile",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Hitachi Energy has presented its Grid-eXpand™ solution, an advanced technology mobile digital substation… The first high-voltage trailer houses a 25 and 33 MVA power transformer, along with 69 kV GIS equipment and a digital protection and control system… the second trailer, composed of an electrical room and a medium-voltage switchgear…",
        "note": "Opened Hitachi Energy Chile press release 11 Mar 2026 (ES/EN page).",
    },
    {
        "id": "hitachi_chile_mobile_sub_20260311",
        "type": "company",
        "chicago": "Hitachi Energy. “Hitachi Energy Marks Milestone with Implementation of Chile’s First Mobile Digital High-Voltage Substation.” 11 March 2026.",
        "url": "https://www.hitachienergy.com/news-and-events/press-releases/2026/05/hitachi-energy-marca-un-hito-con-la-implementaci-n-de-la-primera-subestaci-n-digital-m-vil-de-alta-tensi-n-en-chile",
        "annotation": "Hitachi primary on Chile Grid-eXpand mobile HV substation delivery. Supports hitachi_chile_mobile_digital_substation_2026.",
        "supports": ["hitachi_chile_mobile_digital_substation_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 7 bridges_roads — Aldesa/Proacon Chiapas tunnels MXN 659m (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aldesa_chiapas_tunnels_659m_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Aldesa / Proacon México — Palenque–Ocosingo road tunnels (Chiapas)",
        "country": "Mexico",
        "asset": "27 Aug 2026 Aldesa: SICT awards >MXN 659 million (~EUR 33m) for two tunnels on Palenque–Ocosingo segment of Palenque–San Cristóbal de las Casas highway, Chiapas — 320 m tunnel by Proacon México + 200 m tunnel with Constructora de Caminos Chiapas and Consorcio de Ingenieros; ~17-month execution; portals, terracerías, drainage, paving, lighting. Aldesa CRCC-controlled. Distinct from Aldesa Querétaro–Irapuato rail and Mexico hybrid solar EPC.",
        "investment_type": "epc",
        "value": "659000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "17.15",
        "lon": "-92.05",
        "geo_note": "Palenque–Ocosingo highway corridor, Chiapas (approximate mid-corridor pin).",
        "evidence": "documented",
        "source_id": "aldesa_chiapas_tuneles_20260827",
        "note": "Actor: Aldesa (CRCC-controlled) — prc. Company primary MXN 659m; EUR 33m paraphrase not used as FX. Value stored as MXN.",
    },
    {
        "id": "aldesa_chiapas_tunnels_659m_2026",
        "retrieved": "2026-10-01",
        "source_id": "aldesa_chiapas_tuneles_20260827",
        "url": "https://aldesa.com/aldesa-se-adjudica-la-construccion-de-dos-tuneles-en-mexico-por-33-millones-de-euros/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Aldesa… ha sido adjudicataria para la construcción de dos túneles en México en el tramo entre Palenque y Ocosingo, perteneciente a la carretera Palenque-San Cristóbal de las Casas, en el estado de Chiapas… adjudicadas por la Secretaría de Infraestructura, Comunicaciones y Transporte por más de 659 millones de pesos mexicanos (unos 33 millones de euros)… El primero de los túneles tendrá una longitud de 320 metros… Proacon México… El segundo… 200 metros…",
        "note": "Opened Aldesa company Spanish release 27 Aug 2026.",
    },
    {
        "id": "aldesa_chiapas_tuneles_20260827",
        "type": "company",
        "chicago": "Aldesa Construcción. “Aldesa Se Adjudica la Construcción de Dos Túneles en México por 33 Millones de Euros.” 27 August 2026.",
        "url": "https://aldesa.com/aldesa-se-adjudica-la-construccion-de-dos-tuneles-en-mexico-por-33-millones-de-euros/",
        "annotation": "Aldesa primary on SICT Chiapas twin-tunnel award MXN 659m. Supports aldesa_chiapas_tunnels_659m_2026.",
        "supports": ["aldesa_chiapas_tunnels_659m_2026", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# 9 water — USACE / Ferrovial Río Puerto Nuevo Contract 3 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "usace_ferrovial_rio_puerto_nuevo_1079m_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "USACE Caribbean District — Ferrovial Construcción PR Río Puerto Nuevo Contract 3",
        "country": "Puerto Rico",
        "asset": "8 Jun 2026 Ferrovial: awarded ~USD 1.079 billion USACE contract to expand/upgrade Río Piedras channel section (San Juan) under Río Puerto Nuevo flood-risk program — widen channel ~80 ft to >160 ft; deep concrete pile floodwalls; second USACE Puerto Nuevo contract for Ferrovial. SAM.gov award notice lists USD 1,078,991,952 to Ferrovial Construcción PR LLC (30 Apr 2026). Distinct from other Caribbean flood-control rows.",
        "investment_type": "epc",
        "value": "1078991952",
        "currency": "USD",
        "value_usd": "1078991952",
        "fx_usd": "1",
        "fx_date": "2026-04-30",
        "year": "2026",
        "status": "active",
        "lat": "18.41",
        "lon": "-66.07",
        "geo_note": "Río Piedras / Río Puerto Nuevo channel, San Juan, Puerto Rico (José de Diego–Roosevelt corridor approximate).",
        "evidence": "documented",
        "source_id": "ferrovial_rio_puerto_nuevo_20260608",
        "note": "Actor: U.S. Army Corps of Engineers award (U.S. federal Civil Works) to Ferrovial PR — coded us for USACE financing/award. Company primary rounded USD 1.079bn; value uses SAM total USD 1,078,991,952 when cross-checked.",
    },
    {
        "id": "usace_ferrovial_rio_puerto_nuevo_1079m_2026",
        "retrieved": "2026-10-01",
        "source_id": "ferrovial_rio_puerto_nuevo_20260608",
        "url": "https://newsroom.ferrovial.com/en/press-releases/ferrovial-to-build-new-flood-control-canal-section-in-san-juan-puerto-rico/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Ferrovial… has been awarded a $1,079 billion contract by the U.S. Army Corps of Engineers (USACE) to expand and improve a section of the Río Piedras channel in San Juan, Puerto Rico. This marks Ferrovial’s second contract with USACE under the Puerto Nuevo flood control project… This project will widen the waterway from 80 feet to more than 160 feet…",
        "note": "Opened Ferrovial newsroom 8 Jun 2026; SAM.gov award notice corroborates ~USD 1.079bn.",
    },
    {
        "id": "ferrovial_rio_puerto_nuevo_20260608",
        "type": "company",
        "chicago": "Ferrovial. “Ferrovial to Build New Flood Control Canal Section in San Juan, Puerto Rico.” 8 June 2026.",
        "url": "https://newsroom.ferrovial.com/en/press-releases/ferrovial-to-build-new-flood-control-canal-section-in-san-juan-puerto-rico/",
        "annotation": "Ferrovial primary on USACE Río Puerto Nuevo Contract 3 (~USD 1.079bn). Supports usace_ferrovial_rio_puerto_nuevo_1079m_2026.",
        "supports": ["usace_ferrovial_rio_puerto_nuevo_1079m_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 16 solar — Nextracker Casa dos Ventos 1.5 GW trackers (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "nextracker_casa_dos_ventos_1p5gw_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "Nextracker — Casa dos Ventos 1.5 GW hybrid solar tracker portfolio (Brazil)",
        "country": "Brazil",
        "asset": "12 Aug 2025 PV Tech / Canal Solar citing Nextracker: supply 1.5 GW NX Horizon-XTR / NX Horizon trackers for four Casa dos Ventos utility-scale solar / solar-wind hybrid projects — Babilônia Sul 117 MW, Babilônia Centro 226 MW, Seriemas 540 MW, Rio Brilhante 680 MW (Morro do Chapéu / Várzea Nova BA; Rio Brilhante / Seriemas MS). TrueCapture on all sites. Tracker contract USD not disclosed. Distinct from nextracker_libelula_engie_chile_2025 and Vestas Casa dos Ventos wind rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-11.55",
        "lon": "-41.15",
        "geo_note": "Babilônia Sul / Morro do Chapéu, Bahia (largest Bahia cluster pin; MS sites not dual-pinned).",
        "evidence": "documented",
        "source_id": "pvtech_nextracker_casa_ventos_20250812",
        "note": "Actor: Nextracker (U.S.) — us. Equipment-supply observation; plant CapEx not attributed to Nextracker.",
    },
    {
        "id": "nextracker_casa_dos_ventos_1p5gw_2025",
        "retrieved": "2026-10-01",
        "source_id": "pvtech_nextracker_casa_ventos_20250812",
        "url": "https://www.pv-tech.org/nextracker-to-supply-1-5gw-brazil-hybrid-solar-portfolio-with-trackers/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "US solar tracker manufacturer Nextracker will supply 1.5GW of its products to a Brazilian solar PV hybrid project portfolio… The projects are the Babilônia Sul (117MW), Babilônia Centro (226MW), Seriemas (540MW), and Rio Brilhante (680MW) sites, located in the municipalities of Morro do Chapéu and Várzea Nova in Bahia, and Rio Brilhante and Seriemas in Mato Grosso do Sul.",
        "note": "Opened PV Tech 12 Aug 2025; Canal Solar corroborates named parks and NX Horizon-XTR scope.",
    },
    {
        "id": "pvtech_nextracker_casa_ventos_20250812",
        "type": "press",
        "chicago": "Norman, Will. “Nextracker to Supply 1.5GW Brazil Hybrid Solar Portfolio with Trackers.” PV Tech, 12 August 2025.",
        "url": "https://www.pv-tech.org/nextracker-to-supply-1-5gw-brazil-hybrid-solar-portfolio-with-trackers/",
        "annotation": "Opened trade press on Nextracker 1.5 GW Casa dos Ventos Brazil tracker award. Supports nextracker_casa_dos_ventos_1p5gw_2025.",
        "supports": ["nextracker_casa_dos_ventos_1p5gw_2025", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 18 port_ownership — Jan De Nul / Servimagnus Vía Navegable Troncal (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "jan_de_nul_via_navegable_troncal_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "Jan De Nul N.V. / Servimagnus — Vía Navegable Troncal (Hidrovía) concession",
        "country": "Argentina",
        "asset": "ANPYN Resolución 36/2026 (Boletín Oficial 19 Jun 2026): awards LPNI 1/2025 dredging/signaling concession for Vía Navegable Troncal (Paraná km 1238 Confluencia to Río de la Plata / Canal Punta Indio km 239.1) to JAN DE NUL N.V. – SERVIMAGNUS S.A.; Argentina gob.ar notes Vía Navegable Argentina S.A. SPV and private ops start with peaje cut. Distinct from port terminal concessions (Callao/Chancay).",
        "investment_type": "concession",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-33.95",
        "lon": "-58.40",
        "geo_note": "Vía Navegable Troncal / Canal Punta Indio outer Río de la Plata approach (approximate).",
        "evidence": "documented",
        "source_id": "anpyn_res_36_20260619",
        "note": "Actor: Jan De Nul (Belgian) + Servimagnus (AR) — allied. Official award; CapEx/toll NPV not quantified on opened Res. 36 page.",
    },
    {
        "id": "jan_de_nul_via_navegable_troncal_2026",
        "retrieved": "2026-10-01",
        "source_id": "anpyn_res_36_20260619",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/343322/20260619",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ARTÍCULO 2°.- Adjudíquese la Licitación Pública Nacional e Internacional N° 1/2025, Proceso N° 508-0002-LPU25, a la firma JAN DE NUL N.V. - SERVIMAGNUS S.A. (CUIT 30717268640)… para la modernización, ampliación, operación y mantenimiento del sistema de señalización y tareas de dragado, redragado y mantenimiento de la Vía Navegable Troncal comprendida entre el kilómetro 1238 del Río Paraná… hasta… kilómetro 239,1 del canal Punta Indio…",
        "note": "Opened Boletín Oficial ANPYN Resolución 36/2026.",
    },
    {
        "id": "anpyn_res_36_20260619",
        "type": "government",
        "chicago": "Agencia Nacional de Puertos y Navegación (Argentina). “Resolución 36/2026.” Boletín Oficial de la República Argentina, 19 June 2026.",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/343322/20260619",
        "annotation": "Official award of Vía Navegable Troncal concession to Jan De Nul–Servimagnus. Supports jan_de_nul_via_navegable_troncal_2026.",
        "supports": ["jan_de_nul_via_navegable_troncal_2026", "hunt_infra_port_ownership"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None and k != "supports":
                existing[k] = v
        supports = list(
            dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or []))
        )
        existing["supports"] = supports
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added = []

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
        "hunt_infra_building_materials": "Cycle 58: logged sinoma_panam_grind_dr_2025 (PRC).",
        "hunt_energy_other_renewables": "Cycle 58: equal budget; Ormat Guadeloupe out of LatAm geography list — miss.",
        "hunt_infra_engineering_epc": "Cycle 58: logged pumpco_bonatti_argentina_lng_epc_2026 (U.S. Pumpco JV).",
        "hunt_res_copper": "Cycle 58: logged zijin_la_arena_peru_245m_2024 (PRC) + southern_copper_el_pilar_551m_2026 (other).",
        "hunt_fenb_araxa": "Cycle 58: equal budget; CBMM 13bn/St George A$60m/Taboca 100m already (miss).",
        "hunt_br_power_equip": "Cycle 58: logged hitachi_chile_mobile_digital_substation_2026 (allied).",
        "hunt_infra_bridges_roads": "Cycle 58: logged aldesa_chiapas_tunnels_659m_2026 (PRC).",
        "hunt_infra_port_cranes": "Cycle 58: equal budget; ZPMC Santos Brasil / Itapoá / ICAVE already (miss).",
        "hunt_res_water": "Cycle 58: logged usace_ferrovial_rio_puerto_nuevo_1079m_2026 (U.S. USACE).",
        "hunt_energy_wind": "Cycle 58: equal budget; Vestas Esquina do Vento / AES Villagrán already (miss).",
        "hunt_latam_rail_telecom": "Cycle 58: equal budget; CRCC QI / Siemens Trivia already (miss).",
        "hunt_energy_fission_smr": "Cycle 58: equal budget; Argentina FIRST / Meitner ACR-300 already (miss).",
        "hunt_res_nickel": "Cycle 58: equal budget; Jervois SMP / MMG Anglo Ni / DFC Piauí already (miss).",
        "hunt_res_balsa": "Cycle 58: equal budget; WITS 2025 / AIMA manufactures / Plantabal already (miss).",
        "hunt_res_lithium": "Cycle 58: equal budget; EnergyX/Eni / Zijin 3Q / Galan already (miss).",
        "hunt_energy_solar": "Cycle 58: logged nextracker_casa_dos_ventos_1p5gw_2025 (U.S.).",
        "hunt_res_graphite": "Cycle 58: equal budget; South Star PO / Graphcoa already (miss).",
        "hunt_infra_port_ownership": "Cycle 58: logged jan_de_nul_via_navegable_troncal_2026 (allied).",
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
    print("Cycle 58 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
