# BMW Global Sales & Revenue Intelligence Dashboard (2010-2024)

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

An interactive Power BI dashboard that gives a commercial team one view of global sales performance: revenue by region, volume by model, and powertrain mix over time. Built on a public dataset of 50,000 sales records covering 2010-2024.

## Business Questions Answered

| Question | Where to find it |
|---|---|
| Which regions drive revenue, and is it concentrated or evenly spread? | Regional Revenue Breakdown |
| Which models and series sell the most? | Model Analytics |
| How is the mix shifting between Petrol, Diesel, Hybrid and Electric? | Powertrain Analytics |
| How have volume and revenue trended year over year? | Year Slicer + KPI Banner |

## Dashboard Preview

![BMW Executive Dashboard](dashboard_preview.png)

## Key Findings

* Revenue is spread across all 6 regions, with no single region dominating.
* Volume is balanced across 11 models; the top 3 (7 Series, i8, X1) account for 27.9% of units.
* Powertrain mix is stable from 2010 to 2024, with Electric + Hybrid near 50% throughout.

## Data

**Source:** [paste dataset URL], 50,000 records, 2010–2024.

**Data note:** each row is a batch of vehicles, not a single car. Summing raw columns overstates real volumes, so headline metrics use averages per record and shares rather than raw totals.

| Metric | Definition |
|---|---|
| Total Sales Volume | Sum of `Sales_Volume` across all records |
| Average Vehicle Price | Mean `Price_USD` per vehicle ($75.03K) |

**Cleaning (Python / Pandas):** [paste only the steps your code actually performs]

## Data Model & Measures

* Power Query handles the load and type cleanup.
* DAX measures: Total Sales Volume, Average Batch Revenue, Regional Revenue Share %, Powertrain Share %.
* Single fact table with a Date dimension. [Confirm this matches your model view.]

## Run It Locally

1. Clone the repository.
2. Open `bmw_sales_dashboard.pbix` in Power BI Desktop.
3. If prompted, point the data source to `data/bmw_sales_data.csv`.

## Limitations & Next Steps

* The dataset is public and batch-based, so absolute volumes aren't comparable to BMW's reported figures. The dashboard is for analysis practice, not financial reporting.
* Possible extensions: YoY growth and forecast views, a targets-vs-actuals page, row-level security by region.
