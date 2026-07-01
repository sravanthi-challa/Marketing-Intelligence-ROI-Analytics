# Data Dictionary – Dim_Date

## 1. Overview

The **Dim_Date** table is a Dimension Table that stores calendar-related information. It enables time-based analysis across marketing campaigns, customer acquisition, and sales transactions.

Instead of storing repetitive date attributes in every fact table, all fact tables reference this dimension using **Date_ID**.

---

## 2. Purpose

The purpose of the Date Dimension is to:

- Support daily, monthly, quarterly, and yearly analysis.
- Enable trend analysis.
- Support time intelligence in Power BI.
- Simplify SQL queries involving dates.
- Maintain a standardized calendar across the entire database.

---

## 3. Business Questions

This table helps answer questions such as:

- Which month generated the highest revenue?
- Which quarter had the highest ROI?
- How did revenue change month-over-month?
- Are there seasonal trends in campaign performance?
- Which weekdays generate the highest conversions?
- Which months require higher marketing investment?

---

## 4. Table Information

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Date_ID | INT | Unique surrogate key in YYYYMMDD format | 20250101 |
| Full_Date | DATE | Complete calendar date | 2025-01-01 |
| Day | TINYINT | Day of month | 1 |
| Month | TINYINT | Month number | 1 |
| Month_Name | VARCHAR(15) | Name of the month | January |
| Quarter | TINYINT | Quarter number | 1 |
| Year | SMALLINT | Calendar year | 2025 |
| Week_Number | TINYINT | Week number within the year | 1 |
| Day_Name | VARCHAR(15) | Day of week | Wednesday |
| Is_Weekend | BOOLEAN | Indicates whether the day is a weekend | FALSE |

---

## 5. Primary Key

**Primary Key:** Date_ID

The Date_ID uniquely identifies every calendar date.

Example:

20250101

represents

January 1, 2025.

---

## 6. Foreign Keys

This table does not contain foreign keys.

Instead, it is referenced by:

- Fact_Campaign_Performance
- Fact_Sales
- Fact_Customer_Acquisition

---

## 7. Relationships

| Referenced By | Relationship |
|---------------|-------------|
| Fact_Campaign_Performance | One Date → Many Campaign Performance Records |
| Fact_Sales | One Date → Many Sales Records |
| Fact_Customer_Acquisition | One Date → Many Customer Acquisition Records |

Relationship Type:

One-to-Many (1:M)

---

## 8. Example Record

| Date_ID | Full_Date | Day | Month | Month_Name | Quarter | Year | Week_Number | Day_Name | Is_Weekend |
|----------|-----------|-----|-------|------------|----------|------|--------------|----------|------------|
| 20250101 | 2025-01-01 | 1 | 1 | January | 1 | 2025 | 1 | Wednesday | FALSE |

---

## 9. Design Decisions

### Why was this table created?

A separate Date Dimension eliminates repetitive date information from fact tables and enables efficient time-based analysis.

---

### Why is this a Dimension Table?

The table contains descriptive calendar attributes rather than measurable business metrics.

---

### Why were these columns selected?

The selected columns support:

- Monthly reporting
- Quarterly reporting
- Year-over-year analysis
- Weekly analysis
- Weekday vs Weekend analysis
- Power BI time intelligence

without requiring additional calculations.

---

### Why is Date_ID the Primary Key?

Using an integer key in YYYYMMDD format:

- Improves query performance.
- Simplifies joins.
- Follows data warehouse best practices.
- Is widely used in BI systems.

---

### Business Value

The Date Dimension enables business stakeholders to:

- Track revenue trends.
- Compare campaign performance over time.
- Analyze seasonal behavior.
- Measure business growth.
- Build interactive Power BI reports with consistent time filtering.

---

## 10. Future Enhancements

The Date Dimension can later include:

- Fiscal Year
- Fiscal Quarter
- Holiday Indicator
- Festival Indicator
- Financial Period
- Month Start Flag
- Month End Flag

These enhancements make the model scalable for enterprise reporting.