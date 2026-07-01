# Data Dictionary – Dim_Campaign

## 1. Overview

The **Dim_Campaign** table stores descriptive information about every marketing campaign launched by ShopSphere. It provides campaign attributes that help analyze marketing performance across different channels, time periods, customer segments, and geographic regions.

Each campaign is uniquely identified by **Campaign_ID** and is referenced by multiple fact tables.

---

## 2. Purpose

The purpose of the Campaign Dimension is to:

- Store campaign metadata.
- Track campaign objectives and lifecycle.
- Enable campaign-level performance analysis.
- Support ROI and ROAS calculations.
- Reduce data redundancy in fact tables.

---

## 3. Business Questions

This table helps answer questions such as:

- Which campaign generated the highest revenue?
- Which campaign achieved the best ROI?
- Which campaign had the highest conversion rate?
- Which campaign exceeded its allocated budget?
- Which campaign should be scaled or discontinued?

---

## 4. Table Information

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Campaign_ID | INT | Unique campaign identifier | 101 |
| Campaign_Name | VARCHAR(100) | Name of the campaign | Summer Sale 2025 |
| Campaign_Type | VARCHAR(50) | Type of campaign | Seasonal |
| Objective | VARCHAR(100) | Primary marketing objective | Customer Acquisition |
| Budget | DECIMAL(12,2) | Total allocated campaign budget | 500000.00 |
| Start_Date | DATE | Campaign start date | 2025-06-01 |
| End_Date | DATE | Campaign end date | 2025-06-30 |
| Status | VARCHAR(20) | Campaign status | Active |

---

## 5. Primary Key

**Primary Key:** Campaign_ID

Each campaign is assigned a unique identifier to distinguish it from all other campaigns.

---

## 6. Foreign Keys

This table does not contain foreign keys.

It is referenced by:

- Fact_Campaign_Performance
- Fact_Sales
- Fact_Customer_Acquisition

---

## 7. Relationships

| Referenced By | Relationship |
|---------------|-------------|
| Fact_Campaign_Performance | One Campaign → Many Performance Records |
| Fact_Sales | One Campaign → Many Sales Transactions |
| Fact_Customer_Acquisition | One Campaign → Many Customer Acquisition Records |

Relationship Type:

One-to-Many (1:M)

---

## 8. Example Record

| Campaign_ID | Campaign_Name | Campaign_Type | Objective | Budget | Start_Date | End_Date | Status |
|-------------|---------------|---------------|-----------|---------|------------|----------|--------|
| 101 | Summer Sale 2025 | Seasonal | Customer Acquisition | 500000.00 | 2025-06-01 | 2025-06-30 | Active |

---

## 9. Design Decisions

### Why was this table created?

Campaign information is shared across multiple business processes. Storing campaign details in a dedicated dimension avoids duplication and ensures consistency across reports.

---

### Why is this a Dimension Table?

The table contains descriptive attributes about campaigns rather than measurable business metrics.

---

### Why were these columns selected?

The selected columns support:

- Campaign tracking
- Budget analysis
- Campaign lifecycle monitoring
- ROI calculations
- Marketing performance reporting

---

### Why is Campaign_ID the Primary Key?

Campaign_ID provides a stable, unique identifier that simplifies joins with fact tables and follows dimensional modeling best practices.

---

### Business Value

The Campaign Dimension enables stakeholders to:

- Compare campaign performance.
- Monitor campaign budgets.
- Measure campaign effectiveness.
- Identify high-performing marketing initiatives.
- Support strategic marketing decisions.

---

## 10. Future Enhancements

Future versions may include:

- Campaign Manager
- Campaign Priority
- Marketing Agency
- Target Audience
- Expected ROI
- Actual ROI
- Campaign Theme
- Campaign Description
- Approval Status
