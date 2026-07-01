# Data Dictionary – Dim_Geography

## 1. Overview

The **Dim_Geography** table stores geographical information about customers and marketing performance. It enables location-based analysis across campaigns, customer acquisition, and sales.

Each geographical location is uniquely identified by **Geography_ID**.

---

## 2. Purpose

The purpose of the Geography Dimension is to:

- Store standardized geographical information.
- Support location-based reporting.
- Enable regional performance analysis.
- Analyze customer distribution across locations.
- Compare marketing effectiveness by geography.

---

## 3. Business Questions

This table helps answer questions such as:

- Which country generates the highest revenue?
- Which state has the highest customer acquisition?
- Which city has the best campaign conversion rate?
- Which region delivers the highest ROI?
- Where should future marketing budgets be allocated?
- Which locations have the highest concentration of premium customers?

---

## 4. Table Information

| Column Name | Data Type | Description | Example |
|-------------|-----------|-------------|---------|
| Geography_ID | INT | Unique geography identifier | 201 |
| Country | VARCHAR(50) | Country name | India |
| State | VARCHAR(50) | State name | Telangana |
| City | VARCHAR(50) | City name | Hyderabad |
| Region | VARCHAR(20) | Business region | South |
| Postal_Code | VARCHAR(10) | Postal/ZIP code (optional) | 500001 |

---

## 5. Primary Key

**Primary Key:** Geography_ID

Each geographical location is uniquely identified using Geography_ID.

---

## 6. Foreign Keys

This table does not contain foreign keys.

It is referenced by:

- Dim_Customer
- Fact_Campaign_Performance

---

## 7. Relationships

| Referenced By | Relationship |
|---------------|-------------|
| Dim_Customer | One Geography → Many Customers |
| Fact_Campaign_Performance | One Geography → Many Campaign Performance Records |

Relationship Type:

One-to-Many (1:M)

---

## 8. Example Record

| Geography_ID | Country | State | City | Region | Postal_Code |
|--------------|---------|-------|------|--------|-------------|
| 201 | India | Telangana | Hyderabad | South | 500001 |

---

## 9. Design Decisions

### Why was this table created?

Geographical information is shared by many customers and campaign records. Separating it into a dedicated dimension avoids duplication and ensures consistent location-based reporting.

---

### Why is this a Dimension Table?

The table stores descriptive geographical attributes rather than measurable business metrics.

---

### Why were these columns selected?

The selected columns support:

- Country-level analysis
- State-level analysis
- City-level reporting
- Regional performance comparison
- Geographic customer segmentation

---

### Why is Geography_ID the Primary Key?

Geography_ID provides a stable, unique identifier that simplifies joins and avoids repeatedly storing long location names in fact tables.

---

### Business Value

The Geography Dimension enables stakeholders to:

- Identify high-performing markets.
- Optimize regional marketing strategies.
- Compare campaign performance across locations.
- Understand customer distribution.
- Support expansion planning and resource allocation.

---

## 10. Future Enhancements

Future versions may include:

- Latitude
- Longitude
- Time Zone
- Sales Territory
- Population
- Urban/Rural Classification
- Currency
- Market Size
