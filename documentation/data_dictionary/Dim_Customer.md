# Data Dictionary – Dim_Customer

## 1. Overview

The **Dim_Customer** table stores demographic and segmentation information about customers. It provides descriptive attributes that help analyze customer behavior, purchasing patterns, marketing effectiveness, and customer acquisition performance.

Each customer is uniquely identified by **Customer_ID** and can be associated with multiple sales transactions and marketing campaigns.

---

## 2. Purpose

The purpose of the Customer Dimension is to:

- Store customer demographic information.
- Enable customer segmentation analysis.
- Support customer acquisition reporting.
- Analyze purchasing behavior.
- Measure campaign effectiveness across different customer groups.

---

## 3. Business Questions

This table helps answer questions such as:

- Which customer segment generates the highest revenue?
- Which age group has the highest conversion rate?
- Which gender responds best to marketing campaigns?
- Which customer segment has the highest average order value?
- How many new customers are acquired each month?
- Which regions have the highest concentration of premium customers?

---

## 4. Table Information

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Customer_ID | INT | Unique customer identifier | 100001 |
| Customer_Name | VARCHAR(100) | Customer name (synthetic) | Rahul Sharma |
| Gender | VARCHAR(10) | Customer gender | Male |
| Age_Group | VARCHAR(20) | Customer age category | 26-35 |
| Customer_Segment | VARCHAR(30) | Business segment | Premium |
| Registration_Date | DATE | Customer registration date | 2025-01-15 |
| Email_Opt_In | BOOLEAN | Marketing email subscription status | TRUE |
| Loyalty_Status | VARCHAR(20) | Loyalty membership level | Gold |
| Geography_ID | INT | Reference to customer location | 201 |

---

## 5. Primary Key

**Primary Key:** Customer_ID

Each customer has a unique identifier used across the analytics system.

---

## 6. Foreign Keys

**Geography_ID** → Dim_Geography(Geography_ID)

This links each customer to their geographical location.

---

## 7. Relationships

| Connected Table | Relationship |
|-----------------|-------------|
| Dim_Geography | Many Customers → One Geography |
| Fact_Sales | One Customer → Many Sales Records |
| Fact_Customer_Acquisition | One Customer → One Acquisition Record |

Relationship Types:

- Dim_Geography (M:1)
- Fact_Sales (1:M)
- Fact_Customer_Acquisition (1:1)

---

## 8. Example Record

| Customer_ID | Customer_Name | Gender | Age_Group | Customer_Segment | Registration_Date | Email_Opt_In | Loyalty_Status | Geography_ID |
|-------------|---------------|--------|-----------|------------------|-------------------|--------------|----------------|--------------|
| 100001 | Rahul Sharma | Male | 26-35 | Premium | 2025-01-15 | TRUE | Gold | 201 |

---

## 9. Design Decisions

### Why was this table created?

Customer information is required across multiple business processes, including sales, customer acquisition, and marketing analytics. Keeping customer attributes in a dedicated dimension avoids duplication and ensures consistent reporting.

---

### Why is this a Dimension Table?

The table stores descriptive customer information rather than measurable business events.

---

### Why were these columns selected?

The selected columns support:

- Customer segmentation
- Demographic analysis
- Loyalty analysis
- Marketing personalization
- Geographic reporting
- Customer acquisition analysis

---

### Why is Customer_ID the Primary Key?

Customer_ID uniquely identifies each customer and provides a stable key for joining with fact tables.

---

### Business Value

The Customer Dimension enables stakeholders to:

- Understand customer demographics.
- Measure campaign effectiveness by customer segment.
- Analyze loyalty program performance.
- Identify high-value customer groups.
- Support targeted marketing strategies.

---

## 10. Future Enhancements

Future versions may include:

- Occupation
- Annual Income
- Preferred Language
- Preferred Communication Channel
- Customer Lifetime Value (CLV)
- Churn Risk Score
- Customer Satisfaction Score
- Last Purchase Date
- Average Order Value