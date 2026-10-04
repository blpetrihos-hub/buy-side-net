#!/usr/bin/env python3
"""Cycle 178 hunt: shuffle_seed=20261178; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261178)):
power_plants_grid, lithium, balsa, port_cranes, solar, nickel, bridges_roads,
other_renewables, copper, rail, fission_smr, niobium, graphite, water,
engineering_epc, port_ownership, building_materials, wind.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (AIMA/WITS/Plantabal Ecuador balsa; Centaurus/BRN/Atlantic/
Fenix nickel already logged; Meitner/Colombia/Peru FIRST fission already logged).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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
VALUE_FILLS: list[tuple[str, dict]] = []


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
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
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
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
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


# 1. power_plants_grid / miss (USTDA CNEL ADMS + PowerChina Chile Decree 4 already logged)
# 2. lithium / miss (Sigma bank-guarantee page blocked; Atlas/Yahua/Ganfeng dense)
# 3. balsa / miss (thin; Plantabal/AIMA/WITS/CoreLite already logged)
# 4. port_cranes / miss (ZPMC MultiRio / Konecranes Cartagena / TCP Montevideo already logged)

# 5. solar / allied — IFC + IDB Invest Solengy Haiti package
row_doc(
    "ifc_idb_solengy_haiti_13p5m_2025",
    "energy",
    "solar",
    "allied",
    "IFC / IDB Invest — Solengy Haiti solar+storage financing package (USD 13.5m)",
    "Haiti",
    "18 Mar 2025 (IFC): IFC and IDB Invest announce USD 13.5 million long-term financing for Solengy Haiti S.A. to support installation of 10 MWp solar PV and 20 MWh storage for households, schools, hospitals, and C&I customers. Package: USD 3m IFC senior loan + USD 3m IDB Invest-mobilized senior loan + USD 6m Canada-IFC Blended Climate Finance subordinated loan + USD 1.5m Korea K-GRID grant. CapEx/financing face = USD 13.5m. Distinct from ssangyong_caracol_solar_13p4mw_haiti_57m.",
    "13500000",
    "2025-03-18",
    "2025",
    "",
    "",
    "Solengy distributed solar footprint (Haiti national C&I/household installations) — lat/lon blank (multi-site package).",
    "ifc_solengy_haiti_20250318",
    "IFC… and IDB Invest… announced a US$13.5 million investment in projects by Solengy Haiti S.A.… The project aims to support the installation of 10 MWp of solar PV and 20 MWh of storage… Structured by IFC, the long-term financing package consists of a US$3 million senior loan from IFC’s own account, a US$3 million senior loan mobilized by IDB Invest, a US$6 million subordinated loan from the Canada-IFC Blended Climate Finance Program, and a US$1.5 million grant from the Korea Green, Resilient and Innovative Development (K-GRID) program.",
    "https://www.ifc.org/en/pressroom/2025/ifc-and-idb-invest-partner-to-expand-solar-energy-solutions-in-haiti",
    "Actor: IFC (WBG) + IDB Invest (multilateral) financing Solengy Haiti (local SME) — allied. Opened IFC English release 18 Mar 2025. Haiti under-covered priority cell.",
    "hunt_cycle178",
    investment_type="financing",
    evidence="documented",
    bib_type="official",
    chicago='International Finance Corporation. “IFC and IDB Invest Partner to Expand Solar Energy Solutions in Haiti.” March 18, 2025. https://www.ifc.org/en/pressroom/2025/ifc-and-idb-invest-partner-to-expand-solar-energy-solutions-in-haiti.',
    annotation="IFC/IDB Invest: Solengy Haiti USD 13.5m solar+storage package. Supports ifc_idb_solengy_haiti_13p5m_2025.",
    evid_note="Opened IFC pressroom page 2026-10-04.",
)

# 6. nickel / miss (thin; BRN/Centaurus/Fenix/Atlantic already logged)

# 7a. bridges_roads / allied — World Bank IDA Haiti Resilient Corridors
row_doc(
    "wb_haiti_resilient_corridors_80m_2025",
    "infrastructure",
    "bridges_roads",
    "allied",
    "World Bank / IDA — Haiti Resilient Corridors Project grant (USD 80m)",
    "Haiti",
    "22 Oct 2025 PAD / Board approval window Nov 2025 (World Bank IDA): Resilient Corridors Project (P510851) — proposed IDA grant SDR 58.5 million (USD 80 million equivalent) to Haiti. Components include Resilient Rural Accessibility (USD 37m), Strategic Road Corridors (USD 30m) reconstructing La Digue, Cote-de-Fer and Mahot bridges plus strategic corridor upgrades, and Bridge Asset Management (USD 7m); also rehabilitate/upgrade ~100 km tertiary/rural roads. Financing face = USD 80m. Distinct from trigon_cap_haitien_port_cm_43m.",
    "80000000",
    "2025-10-22",
    "2025",
    "",
    "",
    "Haiti South/North resilient corridors (La Digue / Cote-de-Fer / Mahot bridges + rural network) — lat/lon blank (multi-corridor package).",
    "wb_haiti_resilient_corridors_pad_20251022",
    "PROJECT APPRAISAL DOCUMENT ON A PROPOSED GRANT IN THE AMOUNT OF SDR 58.5 MILLION (US$80 MILLION EQUIVALENT) TO THE REPUBLIC OF HAITI FOR THE RESILIENT CORRIDORS PROJECT… Component 1: Resilient Rural Accessibility (US$37 million equivalent)… Component 2. Strategic Road Corridors (US$30 million equivalent)… reconstruction of three major bridges (La Digue, Cote-de-Fer and Mahot bridges)… This sub-component will rehabilitate and upgrade 100 kilometers of tertiary and rural road networks… Component 3: Bridge Asset Management (US$7 million equivalent).",
    "https://documents1.worldbank.org/curated/en/099102425125518596/pdf/BOSIB-c74e1914-9ebb-4f99-9007-b2afac8158c5.pdf",
    "Actor: World Bank / IDA (multilateral) — allied. Opened IDA PAD PDF 22 Oct 2025 (Report No. PADHI01236). Haiti under-covered bridges_roads cell.",
    "hunt_cycle178",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='World Bank / International Development Association. “Resilient Corridors Project (P510851) Project Appraisal Document.” Report No. PADHI01236, October 22, 2025. https://documents1.worldbank.org/curated/en/099102425125518596/pdf/BOSIB-c74e1914-9ebb-4f99-9007-b2afac8158c5.pdf.',
    annotation="IDA PAD: Haiti Resilient Corridors USD 80m grant. Supports wb_haiti_resilient_corridors_80m_2025.",
    evid_note="Opened World Bank PAD PDF 2026-10-04.",
)

# 7b. bridges_roads / prc — Salvador–Itaparica sondagem CapEx (distinct from blank concession row)
# Fed H.10 2025-04-14 BRL 5.8649 → fx_usd=0.17050589097853333
row_doc(
    "cpsi_itaparica_sondagem_200m_2025",
    "infrastructure",
    "bridges_roads",
    "prc",
    "CPSI (CCECC/CCCC) — Salvador–Itaparica Bay marine sondagem package (R$200m)",
    "Brazil",
    "Apr 2025 (Bahia gov.br Projeto page, updated Apr 2026): marine sondagem in Baía de Todos os Santos for Ponte Salvador–Itaparica PPP — 105 boreholes to ~200 m depth; three barges + drill platform; Chinese wave-compensation system; >20 Bahian firms contracted; 300 direct jobs; total investment R$ 200 million. Results presented Apr 2025 by Seinfra/CPSI. CapEx = R$200m / USD 34,101,178.20 via Fed H.10 2025-04-14. Distinct from ccecc_cccc_salvador_itaparica_2025 concession row and caf_salvador_itaparica_150m_2024.",
    "200000000",
    "2025-04-14",
    "2025",
    "-12.97",
    "-38.62",
    "Baía de Todos os Santos bridge alignment (Vera Cruz–Salvador ferry corridor; approximate mid-bay pin).",
    "ba_gov_ponte_salvador_itaparica_projeto",
    "As sondagens marítimas realizadas na Baía de Todos os Santos começaram em 31 de janeiro de 2024, com duração de 14 meses… No total, foram realizados 105 furos ao longo do traçado da ponte… O projeto também impulsionou a economia local, com a contratação de mais de 20 empresas baianas, geração de 300 empregos diretos e um investimento total de R$ 200 milhões. Os resultados da sondagem… foram apresentados em abril de 2025…",
    "https://www.ba.gov.br/pontesalvadoritaparica/projeto",
    "Actor: Concessionária Ponte Salvador–Itaparica (CCECC/CCCC Chinese consortium) — prc. Opened Bahia state project page. FX: Fed H.10 BRL 5.8649 on 2025-04-14.",
    "hunt_cycle178",
    investment_type="epc",
    evidence="documented",
    currency="BRL",
    value_usd="34101178.20",
    fx_usd="0.1705058910",
    bib_type="government",
    chicago='Governo do Estado da Bahia. “Projeto | Ponte Salvador Itaparica.” Updated April 29, 2026. https://www.ba.gov.br/pontesalvadoritaparica/projeto.',
    annotation="Bahia.gov.br: Itaparica sondagem R$200m. Supports cpsi_itaparica_sondagem_200m_2025.",
    evid_note="Opened ba.gov.br project page 2026-10-04; Fed H.10 BRL 2025-04-14.",
)

# 7c. VALUE FILL — prior Itaparica concession CapEx blank → R$10.42bn (A Tarde / TCE-adjusted)
# Fed H.10 2025-06-04 BRL 5.6396 → fx_usd=0.17731754025108165
VALUE_FILLS.append(
    (
        "ccecc_cccc_salvador_itaparica_2025",
        {
            "value": "10420000000",
            "currency": "BRL",
            "value_usd": "1847648769.42",
            "fx_usd": "0.1773175403",
            "fx_date": "2025-06-04",
            "evidence": "proxy",
            "source_id": "atarde_itaparica_1042bn_20250608",
            "note_append": " Cycle 178 value fill: A Tarde 8 Jun 2025 reports TCE-adjusted works cost redefined to R$10.42 billion after 4 Jun 2025 aditivo; UNVERIFIED proxy vs blank prior concession row (ba.gov.br confirms aditivo date but not R$10.42bn face). FX Fed H.10 BRL 5.6396 on 2025-06-04.",
        },
    )
)

# 8. other_renewables / miss (CIP Esperanza FC / CATL Alegría BESS already logged)

# 9a. copper / us — Caterpillar DET pilot at Codelco Radomiro Tomic
row_doc(
    "caterpillar_codelco_det_rt_2025",
    "resources",
    "copper",
    "us",
    "Caterpillar / Finning — Cat Dynamic Energy Transfer pilot (Codelco Radomiro Tomic)",
    "Chile",
    "2 Oct 2025 (Codelco): pilot of Cat Dynamic Energy Transfer (DET) system at División Radomiro Tomic — electrified rails on one haul ramp feeding Cat 798 AC diesel-electric trucks while moving; ~1-year test starting Q2 2026; preliminary emission cut estimate 60–70%; collaboration Codelco–Finning–Caterpillar. CapEx USD not disclosed — blank. Distinct from caterpillar_andina_798ac_18_2026 fleet delivery.",
    "",
    "",
    "2025",
    "-22.18",
    "-68.90",
    "Codelco Radomiro Tomic open-pit, Antofagasta Region (company geography; approximate pin).",
    "codelco_cat_det_rt_20251002",
    "Codelco anunció sus planes para probar el sistema Cat® Dynamic Energy Transfer (DET) con su flota de camiones de extracción diésel-eléctricos en la División Radomiro Tomic… El piloto está programado para comenzar en el segundo trimestre de 2026… involucrará camiones Cat® 798 AC y la instalación de rieles en una de las rampas… “Este programa piloto es el resultado de una extensa colaboración entre Codelco, Finning S.A. y Caterpillar,” asegura Marc Cameron, vicepresidente senior de Caterpillar.",
    "https://www.codelco.com/codelco-testeara-innovador-sistema-de-cat-para-transferir-energia",
    "Actor: Caterpillar (U.S.) + Finning (Cat dealer) for Codelco RT — us. Opened Codelco Spanish release 2 Oct 2025. CapEx blank. U.S. side-balance copper equipment.",
    "hunt_cycle178",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="company",
    chicago='Codelco. “Codelco testeará innovador sistema de CAT para transferir energía eléctrica a camiones en movimiento.” October 2, 2025. https://www.codelco.com/codelco-testeara-innovador-sistema-de-cat-para-transferir-energia.',
    annotation="Codelco: Cat DET pilot at Radomiro Tomic. Supports caterpillar_codelco_det_rt_2025.",
    evid_note="Opened Codelco company page 2026-10-04.",
)

# 9b. copper / allied — Komatsu 930E-5 fleet Gabriela Mistral
row_doc(
    "komatsu_gaby_930e5_6_2025",
    "resources",
    "copper",
    "allied",
    "Komatsu — Codelco Gabriela Mistral 6× 930E-5 haul trucks (4 autonomous-capable)",
    "Chile",
    "20 Aug 2025 (Electrominería citing Codelco DGM): División Gabriela Mistral incorporates six Komatsu 930E-5 haul trucks — four already in autonomous operation — replacing >100,000-hour units; further 10-unit renewal evaluated for 2027–28. CapEx USD not disclosed — blank. Distinct from caterpillar_andina_798ac_18_2026.",
    "",
    "",
    "2025",
    "-22.95",
    "-69.08",
    "Codelco Gabriela Mistral, Antofagasta Region (press geography; approximate pin).",
    "electromineria_gaby_komatsu_20250820",
    "La División Gabriela Mistral (DGM) de Codelco… renovar parte de su flota de camiones de extracción… La inversión, que contempla seis camiones Komatsu modelo 930E-5 —cuatro de ellos ya en operación autónoma—… “Los nuevos camiones reemplazan a equipos con más de 100 mil horas de uso,”… ya se evalúa una nueva renovación de 10 equipos adicionales entre 2027 y 2028.",
    "https://electromineria.cl/codelco-gabriela-mistral-impulsa-la-electromovilidad-minera-con-nueva-flota-autonoma-y-eficiente-en-energia/",
    "Actor: Komatsu (Japan) equipment for Codelco Gaby — allied. Opened Electrominería 20 Aug 2025 citing division officials. CapEx blank.",
    "hunt_cycle178",
    investment_type="equipment_supply",
    evidence="documented",
    bib_type="trade_press",
    chicago='Electrominería. “Codelco: Gabriela Mistral impulsa la electromovilidad minera con nueva flota autónoma y eficiente en energía.” August 20, 2025. https://electromineria.cl/codelco-gabriela-mistral-impulsa-la-electromovilidad-minera-con-nueva-flota-autonoma-y-eficiente-en-energia/.',
    annotation="Electrominería/Codelco DGM: 6× Komatsu 930E-5. Supports komatsu_gaby_930e5_6_2025.",
    evid_note="Opened Electrominería page 2026-10-04.",
)

# 10. rail / miss (Wabtec MRS / Progress Rail VLI / Vestas Dom Inocêncio already logged)
# 11. fission_smr / miss (thin; Meitner ACR-300 / FIRST MoUs already logged)
# 12. niobium / miss (CBMM R$13bn / Taboca / St George already logged)
# 13. graphite / miss (South Star restart / Graphcoa Jordânia already logged)
# 14. water / miss (Cox Rosarito / Sacyr Coquimbo / Antofagasta Zaldívar already logged)
# 15. engineering_epc / miss (Halliburton YPF / Baker Hughes Petrobras already logged)

# 16. port_ownership / us — SSA México Cozumel cruise pier expansion MIA CapEx
# Fed H.10 2025-04-14 MXN 20.1255 → fx_usd=0.04968820650418623
row_doc(
    "ssa_cozumel_cruise_pier_882mdp_2025",
    "infrastructure",
    "port_ownership",
    "us",
    "SSA México — Cozumel International Cruise Pier expansion (MXN 882.3m MIA)",
    "Mexico",
    "14–15 Apr 2025 (Yucatan Times citing Semarnat Ecological Gazette / DGIRA): SSA México International Cruise Pier Cozumel expansion MIA under evaluation — +412 m length × 24 m width to berth up to four cruise ships simultaneously; required investment MXN 882,325,996 (incl. MXN 5,543,458 mitigation). CapEx = MXN 882.325996m / USD 43,841,196.29 via Fed H.10 2025-04-14. UNVERIFIED proxy (trade press citing gazette figures). Distinct from ssa_progreso_cruise_54m_2026 / ssa_guaymas_tum_concession_2025.",
    "882325996",
    "2025-04-14",
    "2025",
    "20.51",
    "-86.95",
    "SSA México cruise pier, Cozumel, Quintana Roo (press geography; approximate pin).",
    "yucatan_times_ssa_cozumel_20250415",
    "The Ecological Gazette of the Ministry of Environment and Natural Resources (Semarnat) published the request for authorization of the Environmental Impact Statement (EIS) for the project to expand the SSA México International Cruise Pier in Cozumel by 412 meters in length and 24 meters in width, to accommodate up to four cruise ships simultaneously… The required investment is 882,325,996 pesos, of which 5,543,458 pesos correspond to the amount allocated for the implementation of mitigation measures…",
    "https://theyucatantimes.com/2025/04/authorization-requested-for-expansion-of-ssa-mexico-pier-in-cozumel/",
    "UNVERIFIED proxy. Actor: SSA México (Carrix/SSA Marine U.S.) — us. Opened Yucatan Times 15 Apr 2025 citing Semarnat gazette MIA figures. FX: Fed H.10 MXN 20.1255 on 2025-04-14. U.S. side-balance port_ownership.",
    "hunt_cycle178",
    investment_type="concession",
    evidence="proxy",
    currency="MXN",
    value_usd="43841196.29",
    fx_usd="0.0496882065",
    bib_type="trade_press",
    chicago='Yucatan Times. “Authorization Requested for Expansion of SSA México Pier in Cozumel.” April 15, 2025. https://theyucatantimes.com/2025/04/authorization-requested-for-expansion-of-ssa-mexico-pier-in-cozumel/.',
    annotation="Yucatan Times/Semarnat MIA: SSA Cozumel pier MXN 882.3m. Supports ssa_cozumel_cruise_pier_882mdp_2025.",
    evid_note="Opened Yucatan Times page 2026-10-04; Fed H.10 MXN 2025-04-14.",
)

# 17. building_materials / miss (Holcim Colombia Cemex acquisition / Argos 50m already logged)

# 18. wind / allied — Equinor/Rio Energy acquires Esquina do Vento (distinct from Vestas OEM row)
row_doc(
    "equinor_esquina_do_vento_acq_2026",
    "energy",
    "wind",
    "allied",
    "Equinor / Rio Energy — acquisition of ready-to-build Esquina do Vento 230 MW wind complex",
    "Brazil",
    "23 Mar 2026 (Equinor): Equinor via wholly owned Rio Energy acquires ready-to-build 230 MW Esquina do Vento onshore wind complex in Rio Grande do Norte from Vestas — 51× V163 turbines; construction start Q2 2026; COD planned 2028; ~1 TWh/y potential; Vestas 30-year service/energy-based availability agreement. Acquisition price / CapEx USD not disclosed — blank. Distinct from vestas_esquina_do_vento_230mw_2026 turbine-supply row.",
    "",
    "",
    "2026",
    "-5.20",
    "-35.46",
    "Esquina do Vento / Touros–Pureza area, Rio Grande do Norte (Equinor geography; approximate regional pin).",
    "equinor_esquina_vento_20260323",
    "Equinor has acquired the ready to build 230 MW Esquina do Vento onshore wind complex from Vestas… The acquisition, conducted by Equinor’s fully owned subsidiary Rio Energy… Location: State of Rio Grande do Norte, Brazil… 51 Vestas V163 wind turbines… Installed capacity: 230 MW… Start construction Q2 2026… Commercial operations planned for 2028… Vestas will be the WTG O&M responsible, with a 30-year Service and Energy-Based Availability Agreement.",
    "https://www.equinor.com/news/20260323-strengthens-integrated-power-portfolio-brazil",
    "Actor: Equinor (Norway) via Rio Energy — allied. Opened Equinor English release 23 Mar 2026. CapEx/price blank (not disclosed).",
    "hunt_cycle178",
    investment_type="ownership_equity",
    evidence="documented",
    bib_type="company",
    chicago='Equinor. “Equinor strengthens integrated power portfolio in Brazil.” March 23, 2026. https://www.equinor.com/news/20260323-strengthens-integrated-power-portfolio-brazil.',
    annotation="Equinor: Esquina do Vento 230 MW acquisition. Supports equinor_esquina_do_vento_acq_2026.",
    evid_note="Opened Equinor company page 2026-10-04.",
)

FX_BIBS = [
    {
        "id": "fed_h10_20250421",
        "type": "government",
        "chicago": 'Board of Governors of the Federal Reserve System. “Foreign Exchange Rates — H.10.” Release dated April 21, 2025 (rates for Apr. 14–18, 2025). https://www.federalreserve.gov/releases/h10/20250421/.',
        "url": "https://www.federalreserve.gov/releases/h10/20250421/",
        "annotation": "Fed H.10 MXN 20.1255 and BRL 5.8649 on 2025-04-14. Supports Cozumel and Itaparica sondagem FX.",
        "supports": [
            "ssa_cozumel_cruise_pier_882mdp_2025",
            "cpsi_itaparica_sondagem_200m_2025",
            "hunt_cycle178",
        ],
    },
    {
        "id": "fed_h10_20250609",
        "type": "government",
        "chicago": 'Board of Governors of the Federal Reserve System. “Foreign Exchange Rates — H.10.” Release dated June 9, 2025 (rates for Jun. 2–6, 2025). https://www.federalreserve.gov/releases/h10/20250609/.',
        "url": "https://www.federalreserve.gov/releases/h10/20250609/",
        "annotation": "Fed H.10 BRL 5.6396 on 2025-06-04. Supports Itaparica R$10.42bn value fill FX.",
        "supports": ["ccecc_cccc_salvador_itaparica_2025", "hunt_cycle178"],
    },
    {
        "id": "atarde_itaparica_1042bn_20250608",
        "type": "trade_press",
        "chicago": 'Rodrigues, Alan. “Ponte Salvador-Itaparica avança e promete mudar o mapa da Bahia.” A Tarde, June 8, 2025. https://atarde.com.br/bahia/ponte-salvador-itaparica-avanca-e-promete-mudar-o-mapa-da-bahia-1330156.',
        "url": "https://atarde.com.br/bahia/ponte-salvador-itaparica-avanca-e-promete-mudar-o-mapa-da-bahia-1330156",
        "annotation": "A Tarde: TCE-adjusted Itaparica cost R$10.42bn. Supports ccecc_cccc_salvador_itaparica_2025 value fill.",
        "supports": ["ccecc_cccc_salvador_itaparica_2025", "hunt_cycle178"],
    },
]


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
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        if not row.get("id"):
            continue
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

    for rid, patch in VALUE_FILLS:
        if rid not in by_id:
            raise SystemExit(f"value-fill target missing: {rid}")
        r = rows[by_id[rid]]
        for k, v in patch.items():
            if k == "note_append":
                r["note"] = (r.get("note") or "") + v
            else:
                r[k] = v
        # evidence json touch
        evid_path = EVID / f"{rid}.json"
        if evid_path.exists():
            ev = json.loads(evid_path.read_text(encoding="utf-8"))
            ev["note"] = (ev.get("note") or "") + " Cycle 178 value fill applied."
            ev["source_id"] = patch.get("source_id", ev.get("source_id"))
            evid_path.write_text(
                json.dumps(ev, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )

    for entry in FX_BIBS:
        upsert_bib(bib, bib_by, entry)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print("added", added)
    print("value_fills", [rid for rid, _ in VALUE_FILLS])


if __name__ == "__main__":
    main()
