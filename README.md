# Mapping Campus Safety: An Analysis of UCSD Police Department Logs

DSC 190 – Fall 2025  
***Team Members: Casey So, Keilani Li, Lauren Vo, Lillian Tran, Banff Jiang***

## Project Overview

Campus safety is a major concern for students, staff, and visitors at UC San Diego. The UCSD Police Department publishes daily **“Calls for Service and Arrests”** logs, but these PDFs are not easy to search, summarize, or visualize. Our project builds a reproducible data pipeline that converts these raw logs into a structured dataset and uses it to answer concrete questions about **when** and **where** incidents occur on campus. 

## Research Questions

We focus on two main questions:

1. **Location vs. Crime Type**  
   - Is there a relationship between the *location on campus* and the *type of incident* reported?  
   - Example: Are thefts more concentrated in certain areas, while medical or welfare calls cluster elsewhere?

2. **Time Patterns**  
   - Is there a statistically significant difference in the number and type of incidents across:  
     - **Day of week** (e.g., weekdays vs. weekends) and  
     - **Time of day** (e.g., late night vs. early morning)?

## Data

- **Source:** UC San Diego Police Department “Calls for Service and Arrests” daily PDF logs.
- **Time span (current dataset):** August 10, 2025 – November 3, 2025 (2,400+ calls).
- **Key variables:** call date and time, department, incident type, disposition, location description, campus zone, and call duration.
- **Cleaned dataset:** `df_clean_zones.xlsx` contains on-campus incidents with standardized incident types and mapped campus zones.

## Methods

### 1. Parsing and Data Cleaning

We implemented an automated multi-step **Python** pipeline to:

1. Download daily PDF logs from the UCSD Police Department website.
2. Parse tabular content from PDFs into CSV-like rows.
3. Normalize capitalization and punctuation for incident types and locations.
4. Resolve naming inconsistencies for UCSD and local landmarks.
5. Map free-text location descriptions into a smaller set of **campus zones** (e.g., Mandeville, Sixth, Mesa, etc.).
6. Filter to incidents that occurred on or immediately adjacent to UCSD’s main campus.

The output of this pipeline is stored in `df_clean_zones.xlsx` for downstream analysis and visualization.

### 2. Exploratory Data Analysis

We performed EDA to understand overall patterns:

- Bar plots of incident counts by **incident type**, **day of week**, **hour of day**, and **zone**.
- Summary statistics of incident frequency over time.
- A prototype **heatmap** overlaying incident density on a campus base map to identify “hot spots.”

### 3. Statistical Modeling

To answer our research questions, we plan to:

- Compare **incident type distributions across zones** using proportion tests and chi-squared tests.
- Test for **time-of-day and day-of-week effects** on incident counts using:
  - Two-sample proportion tests (e.g., weekdays vs. weekends, late night vs. early morning).
  - Regression models (e.g., Poisson or logistic regression) to control for multiple factors simultaneously.

## Repository Contents

- `df_clean_zones.xlsx` – Cleaned dataset with on-campus incidents and standardized zones.
- `notebooks/` – Jupyter notebooks for parsing, cleaning, EDA, and statistical analysis.
- `figures/` – Exported plots and maps used in the report and presentation.
