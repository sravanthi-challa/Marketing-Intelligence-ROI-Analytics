# Data Dictionary – Fact_Customer_Acquisition

## 1. Overview

The **Fact_Customer_Acquisition** table stores information about customers acquired through marketing campaigns. It captures acquisition events independently of sales transactions, enabling analysis of campaign effectiveness, customer growth, and acquisition costs.

Each record represents one successful customer acquisition event.

---

## 2. Purpose

The purpose of this fact table is to:

- Track newly acquired customers.
- Measure campaign effectiveness.
- Analyze customer acquisition trends.
- Calculate Customer Acquisition Cost (CAC).
- Support customer growth reporting.

---

## 3. Grain

**One record represents one customer acquired through one campaign on one date via one marketing channel.**

Example:

Customer

↓

Acquired through

↓

Google Ads

↓

Summer Sale Campaign

↓

15 June 2025

↓

One Row

---

## 4. Business Questions

This table helps answer questions such as:

- Which campaign acquired the most customers?
- Which marketing channel has the lowest acquisition cost?
- How many customers were acquired each month?
- Which campaigns generated the highest-quality leads?
- Which regions acquire customers most efficiently?

---

## 5. Table Information

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Acquisition_ID | INT | Unique acquisition event identifier | 900001 |
| Date_ID | INT | Reference to Dim_Date | 20250615 |
| Customer_ID | INT | Reference to Dim_Customer | 100001 |
| Campaign_ID | INT | Reference to Dim_Campaign | 101 |
| Channel_ID | INT | Reference to Dim_Channel | 1 |
| Acquisition_Cost | DECIMAL(10,2) | Cost to acquire the customer | 450.00 |

---

## 6. Primary Key

**Primary Key:** Acquisition_ID

Each acquisition event is uniquely identified using Acquisition_ID.

---

## 7. Foreign Keys

- Date_ID → Dim_Date
- Customer_ID → Dim_Customer
- Campaign_ID → Dim_Campaign
- Channel_ID → Dim_Channel

---

## 8. Relationships

| Connected Table | Relationship |
|-----------------|-------------|
| Dim_Date | Many Acquisition Records → One Date |
| Dim_Customer | One Customer → One Acquisition Record |
| Dim_Campaign | Many Acquisition Records → One Campaign |
| Dim_Channel | Many Acquisition Records → One Channel |

Relationship Type:

Many-to-One (M:1)

---

## 9. Example Record

| Acquisition_ID | Date_ID | Customer_ID | Campaign_ID | Channel_ID | Acquisition_Cost |
|----------------|---------|-------------|-------------|------------|------------------|
| 900001 | 20250615 | 100001 | 101 | 1 | 450.00 |

---

## 10. Design Decisions

### Why was this table created?

Customer acquisition is a distinct business process from product sales. Separating acquisition events from sales enables accurate marketing performance analysis and customer growth tracking.

---

### Why is this a Fact Table?

The table stores measurable business events related to acquiring new customers rather than descriptive information.

---

### Why were these columns selected?

The selected columns support:

- Customer acquisition analysis
- Campaign effectiveness analysis
- Marketing channel comparison
- Customer growth reporting
- CAC calculations

---

### Why is Acquisition_ID the Primary Key?

Acquisition_ID uniquely identifies each acquisition event and provides a stable key for future scalability.

---

### Business Value

The Fact_Customer_Acquisition table enables stakeholders to:

- Measure customer growth.
- Compare campaign effectiveness.
- Optimize acquisition strategies.
- Reduce customer acquisition costs.
- Improve marketing ROI.

---

## 11. KPIs Derived from this Table

The following KPIs will be calculated in SQL or Power BI rather than stored.

| KPI | Formula |
|------|---------|
| Total Customers Acquired | COUNT(Customer_ID) |
| Customer Acquisition Cost (CAC) | Total Acquisition Cost ÷ Customers Acquired |
| Monthly Customer Growth | Current Month Acquisitions − Previous Month Acquisitions |
| Acquisition by Channel | COUNT(Customer_ID) GROUP BY Channel |

---

## 12. Future Enhancements

Future versions may include:

- Lead Source
- First Touch Channel
- Last Touch Channel
- Attribution Model
- Lead Score
- Marketing Qualified Lead (MQL) Flag
- Sales Qualified Lead (SQL) Flag
- Conversion to First Purchase Date