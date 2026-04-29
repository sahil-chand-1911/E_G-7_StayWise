# NST DVA Capstone 2 — E_G-7_StayWise

> **Newton School of Technology | Data Visualization & Analytics**
> A industry simulation capstone using Python, GitHub, and Tableau to convert raw Airbnb listing data into actionable market intelligence for European hosts.

---

## Before You Start

1. Repository is named using the format `SectionName_TeamID_ProjectName` → `E_G-7_StayWise`.
2. Project details and team table are filled in below.
3. Raw dataset is placed in `data/raw/`.
4. Notebooks are completed in order from `01` to `05`.
5. Final dashboard is published — public link is in `tableau/dashboard_links.md`.
6. Final report and presentation are exported as PDFs into `reports/`.

### Quick Start

If you are working locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

If you are working in Google Colab:

- Upload or sync the notebooks from `notebooks/`
- Keep the final `.ipynb` files committed to GitHub
- Export any cleaned datasets into `data/processed/`

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | StayWise — Airbnb Market Intelligence Dashboard |
| **Sector** | Consumer Discretionary (Travel & Hospitality) |
| **Team ID** | E G-7 |
| **Section** | E G |
| **Faculty Mentor** | Newton School of Technology |
| **Institute** | Newton School of Technology |
| **Submission Date** | 29th April 2026 |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | Sahil Chand | https://github.com/sahil-chand-1911 |
| Data Lead | Pranjal Shukla | https://github.com/Pranjal9005 |
| ETL and Analysis Lead | Shyam Verma | https://github.com/ishyverma |
| Visualization Lead | Akshat Agrawal | https://github.com/Akshuu1 |
| Strategy Lead | Vikrant Yadav | https://github.com/vikgenix |
| PPT and Quality Lead | Trishit Swarnakar | https://github.com/Trishix |

---

## Business Problem

The Travel & Hospitality sector has been reshaped by short-term rental platforms like Airbnb. Europe is one of Airbnb's most active markets, with millions of listings generating income for individual hosts and property management firms. Post-pandemic recovery has intensified competition, raising the stakes for intelligent property management. Without data-driven guidance, hosts misprice listings, over-invest in low-impact amenities, and lose competitive advantage across 94,000+ listings.

**Core Business Question**

> What are the key drivers of revenue and occupancy for Airbnb listings in Europe, and how can hosts use this information to improve pricing, amenity investment, and market positioning?

**Decision Supported**

> This analysis enables hosts to make evidence-based decisions about which amenities to invest in, how to price dynamically across seasons, and which markets to prioritise for property acquisition — directly improving annual revenue and occupancy rates.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Airbnb Market Data — Europe (Kaggle — Jason Airroi) |
| **Direct Access Link** | https://www.kaggle.com/datasets/jasonairroi/airbnb-market-data-europe |
| **Row Count** | Listings: 95,898 · Past Rates: 1,115,174 |
| **Column Count** | Listings: 61 columns · Past Rates: 17 columns |
| **Time Period Covered** | Trailing Twelve Months (TTM) + historical monthly data |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `ttm_revenue` | Trailing 12-month revenue in USD | Primary KPI — core profitability measure |
| `ttm_occupancy` | Occupancy rate over trailing 12 months (0–1 scale) | Primary KPI — demand and pricing signal |
| `amenities` | Comma-separated list of listing amenities | Amenity impact analysis — revenue and occupancy drivers |
| `listing_type` | Property type (Entire home, Villa, Condo, etc.) | Segmentation — revenue tier predictor |
| `room_type` | Room configuration (entire home, private room, shared) | Segmentation — occupancy and revenue comparison |
| `city` | City location (e.g., Bodrum, Istanbul) | Geographic segmentation — market benchmarking |
| `rating_overall` | Overall listing rating | Quality signal — guest satisfaction proxy |
| `cleaning_fee` | Cleaning fee charged in USD | Pricing component — ADR computation |
| `latitude` / `longitude` | Geographic coordinates | Map visualisation — geographic distribution |
| `rev_perf_index` | Derived: listing revenue ÷ market mean revenue | Competitive positioning signal |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| TTM Revenue | Core measure of listing profitability over a trailing year | Sum of revenue over trailing 12 months (USD) · `notebooks/05_final_load_prep.ipynb` |
| TTM Occupancy Rate | Indicates demand and pricing competitiveness | Reserved days ÷ Total available days · `notebooks/03_eda.ipynb` |
| RevPAR | Industry-standard cross-market efficiency metric | Total Revenue ÷ Total Available Room-Nights · `notebooks/05_final_load_prep.ipynb` |
| Average Daily Rate (ADR) | Pricing position vs. competitors | Total Revenue ÷ Total Reserved Days · `notebooks/04_statistical_analysis.ipynb` |
| Revenue Tier | Quartile benchmarking classification | Quartile split → Bronze / Silver / Gold / Platinum · `notebooks/05_final_load_prep.ipynb` |
| Occupancy Tier | Operational improvement classification | Binned rate → Low / Mid / High / Optimal · `notebooks/05_final_load_prep.ipynb` |
| Revenue Performance Index | Competitive positioning signal vs. market mean | Listing TTM Revenue ÷ Market Mean Revenue · `notebooks/05_final_load_prep.ipynb` |
| Amenity Count | Inventory completeness proxy | Count of amenities listed per property · `notebooks/02_cleaning.ipynb` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | https://public.tableau.com/app/profile/akshat.agrawal2260/viz/Airbnb_17773079392460/MarketIntelligence |
| **Executive View** | Market Intelligence view — high-level KPI summary, geographic distribution of listings, revenue tier breakdown (Bronze → Platinum), and city-level performance comparison for CEO or policy-maker audiences |
| **Operational View** | Pricing & Performance and Optimisation views — pricing trends by city, revenue by property type, amenity gap analysis, and Revenue Performance Index drill-down for property managers |
| **Main Filters** | City · Property Type · Date Range · Revenue Tier |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

1. **Premium amenities equal higher revenue.** Private pool, sea view, and hot tub are strongly correlated with above-average revenue. Hosts who can add even one of these features should prioritise it over multiple mid-tier improvements.
2. **Property type is the single strongest predictor of revenue tier.** Entire homes and villas consistently occupy the Gold and Platinum tiers; private rooms trail significantly in total earnings.
3. **Coastal markets outperform inland cities by 2–3×.** Cities like Bodrum deliver materially higher per-unit revenue potential despite lower listing density, driven by premium leisure demand.
4. **WiFi is non-negotiable for sustained occupancy.** High-speed internet is the top occupancy-driving amenity across all market segments. Listings without it consistently underperform, especially outside peak season.
5. **Kitchen amenities drive longer stays and higher total revenue.** Fully stocked kitchens correlate with longer average booking durations, reducing marketing cost per booking and improving overall yield.
6. **Self check-in enables off-peak bookings.** Flexible check-in reduces friction for last-minute and independent travellers, sustaining occupancy during shoulder and off-peak seasons.
7. **Climate control is now expected, not premium.** Air conditioning and heating appear in the top occupancy-driving amenity sets. In Mediterranean markets, year-round climate control is an occupancy baseline.
8. **Revenue Performance Index exposes benchmarking gaps.** Listings with a `rev_perf_index` above 1.0 consistently outperform the market; this metric pinpoints when pricing or occupancy is underperforming.
9. **Seasonal pricing is massively under-utilised.** Historical data confirms sharp seasonal demand variation, yet many hosts apply flat pricing. Peak-season surcharges and shoulder discounts can unlock 10–20% additional annual revenue.
10. **The Gold-to-Platinum upgrade path is accessible.** The revenue gap between Silver and Gold tiers is narrower than between Gold and Platinum. A single amenity upgrade (pool or sea view) can shift a listing into the highest-earning tier.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Pool, sea view, and hot tub drive 40–60% revenue premium | **Invest in premium outdoor amenities.** Prioritise properties with these features for new listings; evaluate pool or hot tub installation for existing ones. Budget $5,000–$20,000 for basic pool infrastructure. | +40–60% annual revenue per affected listing; ROI within 12–18 months |
| 2 | WiFi and kitchen essentials are the top occupancy anchors, especially off-peak | **Perfect work-from-home features.** Install 50+ Mbps broadband, fully stock the kitchen, and add a dedicated workspace. Total upgrade cost: $500–$2,000. | +15–25% off-peak occupancy; implementable within days |
| 3 | Coastal cities deliver 2–3× revenue vs. inland urban equivalents | **Focus acquisition on coastal markets.** Redirect capital and marketing spend toward coastal properties; use the Tableau geographic view to identify high-revenue micro-markets. | +100–200% portfolio revenue per unit vs. inland |
| 4 | Flat pricing leaves money on the table given sharp seasonal patterns | **Implement dynamic pricing.** Deploy surge pricing during June–August; offer 15–20% discounts in shoulder months. Use competitive intelligence tools to track market ADR weekly. | +10–20% annual revenue optimisation at no capital cost |
| 5 | Hosts lack actionable benchmarking intelligence | **Embed the dashboard into monthly operations.** Review the Tableau dashboard monthly to monitor the Revenue Performance Index, benchmark against market averages, and identify amenity gaps. | Compounding improvement across all KPIs through evidence-based iteration |

---

## Repository Structure

```text
E_G-7_StayWise/
|
|-- README.md
|
|-- data/
|   |-- raw/                              # Original dataset (never edited)
|   |   |-- listings.csv
|   |   `-- past_rates.csv
|   `-- processed/                        # Cleaned output from ETL pipeline
|       `-- final_listings.csv            # 94,868 rows × 16 cols with derived features
|
|-- notebooks/
|   |-- 01_loading.ipynb                  # Ingest CSVs, handle mixed dtypes, pickle raw data
|   |-- 02_cleaning.ipynb                 # Fill nulls, remove 570 zero-revenue listings, parse amenities
|   |-- 03_eda.ipynb                      # Distributions, segment comparisons, trend charts
|   |-- 04_statistical_analysis.ipynb     # Amenity impact, correlation matrices, benchmarking
|   `-- 05_final_load_prep.ipynb          # Revenue/occupancy tiers, aggregations, export CSVs
|
|-- scripts/
|   `-- etl_pipeline.py                   # End-to-end pipeline runner for reproducible execution
|
|-- tableau/
|   |-- screenshots/                      # Dashboard screenshot exports
|   `-- dashboard_links.md               # Tableau Public URL
|
|-- reports/
|   |-- StayWise_Report.pdf              # Final project report
|   `-- StayWise_Presentation.pdf        # Final presentation deck
|
|-- docs/
|   `-- data_dictionary.md               # Full column definitions for all datasets
|
|-- DVA-oriented-Resume/
`-- DVA-focused-Portfolio/
```

---

## Analytical Pipeline

The project follows a structured 7-step workflow:

1. **Define** — Sector selected (Travel & Hospitality), problem statement scoped to European Airbnb markets, mentor approval obtained.
2. **Extract** — Raw dataset sourced from Kaggle and committed to `data/raw/`; data dictionary drafted in `docs/data_dictionary.md`.
3. **Clean and Transform** — Cleaning pipeline built in `notebooks/02_cleaning.ipynb` and `scripts/etl_pipeline.py`; 570 zero-revenue listings removed, 14 mixed-type columns converted, amenity strings parsed.
4. **Analyze** — EDA across property types, geographies, amenity prevalence, seasonality, and revenue distribution in `03_eda.ipynb`; amenity impact analysis ranking 91 qualified amenities in `04_statistical_analysis.ipynb`.
5. **Visualize** — Interactive Tableau dashboard built with Market Intelligence, Pricing & Performance, and Optimisation views; published on Tableau Public.
6. **Recommend** — Five data-backed business recommendations delivered with estimated revenue and occupancy impact and implementation feasibility.
7. **Report** — Final project report and presentation deck completed and exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, EDA, statistical analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, contribution audit |
| SQL | Not used | — |

**Python libraries used:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`

---

## Evaluation Rubric

| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

> Marks are awarded for analytical thinking and decision relevance, not chart quantity, visual decoration, or code length.

---

## Submission Checklist

**GitHub Repository**

- [x] Public repository created with the correct naming convention (`E_G-7_StayWise`)
- [x] All notebooks committed in `.ipynb` format
- [x] `data/raw/` contains the original, unedited dataset
- [x] `data/processed/` contains the cleaned pipeline output
- [x] `tableau/screenshots/` contains dashboard screenshots
- [x] `tableau/dashboard_links.md` contains the Tableau Public URL
- [x] `docs/data_dictionary.md` is complete
- [x] `README.md` explains the project, dataset, and team
- [x] All members have visible commits and pull requests

**Tableau Dashboard**

- [x] Published on Tableau Public and accessible via public URL
- [x] At least one interactive filter included (City, Property Type, Date Range, Revenue Tier)
- [x] Dashboard directly addresses the business problem

**Project Report**

- [x] Final report exported as PDF into `reports/`
- [x] Cover page, executive summary, sector context, problem statement
- [x] Data description, cleaning methodology, KPI framework
- [x] EDA with written insights, statistical analysis results
- [x] Dashboard screenshots and explanation
- [x] 10 key insights in decision language
- [x] 5 actionable recommendations with impact estimates
- [x] Contribution matrix matches GitHub history

**Presentation Deck**

- [x] Final presentation exported as PDF into `reports/`
- [x] Title slide through recommendations, impact, limitations, and next steps

**Individual Assets**

- [x] DVA-oriented resume updated to include this capstone
- [x] Portfolio link or project case study added

---

## Contribution Matrix

This table must match evidence in GitHub Insights, PR history, and committed files.

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| Akshat Agrawal | — | — | — | — | ✅ | — | — |
| Pranjal Shukla | — | — | — | ✅ | — | ✅ | — |
| Sahil Chand | — | ✅ | — | — | — | — | ✅ |
| Shyam Verma | — | ✅ | ✅ | ✅ | — | — | — |
| Trishit Swarnakar | — | — | — | — | — | ✅ | ✅ |
| Vikrant Yadav | ✅ | — | — | ✅ | ✅ | — | — |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Sahil Chand

**Date:** 29th April 2026

---

## Academic Integrity

All analysis, code, and recommendations in this repository are the original work of Team E G-7. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.

---

*Newton School of Technology — Data Visualization & Analytics | Capstone 2*
