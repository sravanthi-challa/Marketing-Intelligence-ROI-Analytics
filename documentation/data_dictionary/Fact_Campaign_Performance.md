# Data Dictionary – Fact_Campaign_Performance

## 1. Overview

The **Fact_Campaign_Performance** table stores measurable marketing performance metrics for each campaign. It serves as the central fact table for marketing analytics and enables KPI reporting across campaigns, channels, locations, devices, and time.

This table contains quantitative business metrics that support performance evaluation and strategic decision-making.

---

## 2. Purpose

The purpose of this fact table is to:

- Store campaign performance metrics.
- Measure marketing effectiveness.
- Support ROI and ROAS analysis.
- Enable campaign comparisons.
- Provide data for Power BI dashboards.

---

## 3. Grain

**One record represents the performance of one Campaign on one Date through one Marketing Channel in one Geography on one Device.**

Example:

Summer Sale Campaign

↓

Google Ads

↓

Hyderabad

↓

Android

↓

1 June 2025

↓

One row

---

## 4. Business Questions

This table helps answer questions such as:

- Which campaign generated the highest ROI?
- Which marketing channel performed best?
- Which device has the highest conversion rate?
- Which region generated the most conversions?
- Which campaigns exceeded their budget?
- Which campaign delivered the best ROAS?

---

## 5. Table Information

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Campaign_Performance_ID | INT | Unique performance record identifier | 1 |
| Date_ID | INT | Reference to Dim_Date | 20250601 |
| Campaign_ID | INT | Reference to Dim_Campaign | 101 |
| Channel_ID | INT | Reference to Dim_Channel | 1 |
| Geography_ID | INT | Reference to Dim_Geography | 201 |
| Device_ID | INT | Reference to Dim_Device | 1 |
| Impressions | INT | Number of ad impressions | 150000 |
| Clicks | INT | Number of clicks | 8200 |
| Conversions | INT | Number of successful conversions | 420 |
| Advertising_Spend | DECIMAL(12,2) | Marketing spend | 180000.00 |

---

## 6. Primary Key

**Campaign_Performance_ID**

---

## 7. Foreign Keys

- Date_ID → Dim_Date
- Campaign_ID → Dim_Campaign
- Channel_ID → Dim_Channel
- Geography_ID → Dim_Geography
- Device_ID → Dim_Device

---

## 8. Relationships

| Connected Table | Relationship |
|-----------------|-------------|
| Dim_Date | Many Performance Records → One Date |
| Dim_Campaign | Many Performance Records → One Campaign |
| Dim_Channel | Many Performance Records → One Channel |
| Dim_Geography | Many Performance Records → One Geography |
| Dim_Device | Many Performance Records → One Device |

Relationship Type:

Many-to-One (M:1)

---

## 9. Example Record

| Campaign_Performance_ID | Date_ID | Campaign_ID | Channel_ID | Geography_ID | Device_ID | Impressions | Clicks | Conversions | Advertising_Spend |
|-------------------------|---------|-------------|------------|--------------|-----------|-------------|--------|-------------|-------------------|
| 1 | 20250601 | 101 | 1 | 201 | 1 | 150000 | 8200 | 420 | 180000.00 |

---

## 10. Design Decisions

### Why was this table created?

Marketing performance consists of measurable business events. A dedicated fact table allows efficient storage and analysis of campaign metrics.

---

### Why is this a Fact Table?

The table stores quantitative business measures rather than descriptive information.

---

### Why were these columns selected?

These metrics are the foundation for marketing analytics and support KPI calculations such as:

- CTR
- Conversion Rate
- CPC
- CPA
- ROI
- ROAS

---

### Why is Campaign_Performance_ID the Primary Key?

A surrogate key uniquely identifies each performance record while simplifying joins and future scalability.

---

### Business Value

This fact table enables stakeholders to:

- Measure campaign effectiveness.
- Compare marketing channels.
- Track advertising spend.
- Optimize marketing investments.
- Monitor campaign performance over time.

---

## 11. KPIs Derived from this Table

The following KPIs will be calculated in SQL or Power BI rather than stored.

| KPI | Formula |
|------|---------|
| CTR | Clicks ÷ Impressions × 100 |
| Conversion Rate | Conversions ÷ Clicks × 100 |
| CPC | Advertising_Spend ÷ Clicks |
| CPA | Advertising_Spend ÷ Conversions |
| ROI | (Revenue − Advertising_Spend) ÷ Advertising_Spend × 100 |
| ROAS | Revenue ÷ Advertising_Spend |

---

## 12. Future Enhancements

Future versions may include:

- Video Views
- Engagement Rate
- Bounce Rate
- Session Duration
- Frequency
- Reach
- Attribution Model
- Assisted Conversions