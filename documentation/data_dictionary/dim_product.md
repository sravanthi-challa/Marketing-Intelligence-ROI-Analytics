# Data Dictionary – Dim_Product

## 1. Overview

The **Dim_Product** table stores descriptive information about products sold by ShopSphere. It enables analysis of product performance, category-wise sales, brand performance, and profitability across marketing campaigns.

Each product is uniquely identified by **Product_ID** and can appear in multiple sales transactions.

---

## 2. Purpose

The purpose of the Product Dimension is to:

- Store product information.
- Enable category and brand analysis.
- Support product-level sales reporting.
- Analyze campaign performance by product.
- Support profitability analysis.

---

## 3. Business Questions

This table helps answer questions such as:

- Which products generate the highest revenue?
- Which product category performs best?
- Which brands contribute the most profit?
- Which campaigns sell the most products?
- Which categories have the highest sales volume?
- Which products should receive additional marketing investment?

---

## 4. Table Information

| Column Name | Data Type | Description | Example |
|-------------|-----------|-------------|---------|
| Product_ID | INT | Unique product identifier | 1001 |
| Product_Name | VARCHAR(100) | Name of the product | Samsung Galaxy S24 |
| Category | VARCHAR(50) | Product category | Electronics |
| Brand | VARCHAR(50) | Product brand | Samsung |
| Unit_Price | DECIMAL(10,2) | Selling price of one unit | 74999.00 |
| Cost_Price | DECIMAL(10,2) | Cost incurred by the business | 67000.00 |
| Profit_Margin_Percentage | DECIMAL(5,2) | Profit margin percentage | 11.94 |
| Product_Status | VARCHAR(20) | Availability status | Active |

---

## 5. Primary Key

**Primary Key:** Product_ID

Each product is uniquely identified using Product_ID.

---

## 6. Foreign Keys

This table does not contain foreign keys.

It is referenced by:

- Fact_Sales

---

## 7. Relationships

| Referenced By | Relationship |
|---------------|-------------|
| Fact_Sales | One Product → Many Sales Transactions |

Relationship Type:

One-to-Many (1:M)

---

## 8. Example Record

| Product_ID | Product_Name | Category | Brand | Unit_Price | Cost_Price | Profit_Margin_Percentage | Product_Status |
|------------|--------------|----------|-------|------------|------------|--------------------------|----------------|
| 1001 | Samsung Galaxy S24 | Electronics | Samsung | 74999.00 | 67000.00 | 11.94 | Active |

---

## 9. Design Decisions

### Why was this table created?

Product information is required for sales analysis, profitability analysis, and campaign performance reporting. Storing it separately avoids duplication across sales records.

---

### Why is this a Dimension Table?

The table stores descriptive attributes about products rather than transactional measures.

---

### Why were these columns selected?

The selected columns support:

- Product analysis
- Brand analysis
- Category analysis
- Profitability reporting
- Revenue reporting
- Marketing campaign effectiveness

---

### Why is Product_ID the Primary Key?

Product_ID provides a stable and unique identifier that simplifies joins with the sales fact table.

---

### Business Value

The Product Dimension enables stakeholders to:

- Identify top-selling products.
- Compare category performance.
- Analyze brand profitability.
- Optimize inventory planning.
- Improve product-focused marketing strategies.

---

## 10. Future Enhancements

Future versions may include:

- Supplier_Name
- Product_Rating
- Product_Weight
- Product_Color
- Product_Size
- Launch_Date
- Discontinuation_Date
- Inventory_Level
- Reorder_Level