# Data Dictionary – Fact_Sales

## 1. Overview

The **Fact_Sales** table stores transactional sales data for products purchased by customers. It captures measurable business events that support revenue analysis, profitability analysis, customer purchasing behavior, and product performance reporting.

Each record represents a single sales transaction.

---

## 2. Purpose

The purpose of this fact table is to:

- Store sales transaction data.
- Measure revenue and profitability.
- Analyze customer purchasing behavior.
- Support product performance reporting.
- Enable sales trend analysis.

---

## 3. Grain

**One record represents one product purchased by one customer in one sales transaction on one date.**

Example:

Customer

↓

Purchases

↓

One Product

↓

On One Date

↓

One Row

---

## 4. Business Questions

This table helps answer questions such as:

- Which products generate the highest revenue?
- Which customers spend the most?
- Which product categories sell the most units?
- What is the monthly sales trend?
- Which campaigns generate the highest sales revenue?
- Which products deliver the highest profit?

---

## 5. Table Information

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Sales_ID | INT | Unique sales transaction identifier | 500001 |
| Date_ID | INT | Reference to Dim_Date | 20250601 |
| Customer_ID | INT | Reference to Dim_Customer | 100001 |
| Product_ID | INT | Reference to Dim_Product | 1001 |
| Campaign_ID | INT | Reference to Dim_Campaign | 101 |
| Quantity | INT | Number of units purchased | 2 |
| Unit_Selling_Price | DECIMAL(10,2) | Selling price per unit at the time of sale | 74999.00 |
| Discount_Amount | DECIMAL(10,2) | Discount applied to the transaction | 5000.00 |
| Sales_Amount | DECIMAL(12,2) | Final amount paid by the customer | 144998.00 |

---

## 6. Primary Key

**Primary Key:** Sales_ID

Each sales transaction is uniquely identified using Sales_ID.

---

## 7. Foreign Keys

- Date_ID → Dim_Date
- Customer_ID → Dim_Customer
- Product_ID → Dim_Product
- Campaign_ID → Dim_Campaign

---

## 8. Relationships

| Connected Table | Relationship |
|-----------------|-------------|
| Dim_Date | Many Sales → One Date |
| Dim_Customer | Many Sales → One Customer |
| Dim_Product | Many Sales → One Product |
| Dim_Campaign | Many Sales → One Campaign |

Relationship Type:

Many-to-One (M:1)

---

## 9. Example Record

| Sales_ID | Date_ID | Customer_ID | Product_ID | Campaign_ID | Quantity | Unit_Selling_Price | Discount_Amount | Sales_Amount |
|----------|---------|-------------|------------|-------------|----------|--------------------|-----------------|--------------|
| 500001 | 20250601 | 100001 | 1001 | 101 | 2 | 74999.00 | 5000.00 | 144998.00 |

---

## 10. Design Decisions

### Why was this table created?

Sales transactions are the core business events that generate revenue. This table stores those measurable events separately from descriptive information.

---

### Why is this a Fact Table?

The table contains quantitative business measures such as quantity sold and sales amount rather than descriptive attributes.

---

### Why were these columns selected?

The selected columns support:

- Revenue analysis
- Product performance analysis
- Customer purchasing analysis
- Campaign attribution
- Sales trend reporting
- Profitability calculations

---

### Why is Sales_ID the Primary Key?

Sales_ID uniquely identifies each sales transaction and provides a stable key for future expansion.

---

### Business Value

The Fact_Sales table enables stakeholders to:

- Track business revenue.
- Identify top-selling products.
- Measure customer purchasing behavior.
- Evaluate campaign-driven sales.
- Analyze sales trends over time.

---

## 11. KPIs Derived from this Table

The following KPIs will be calculated in SQL or Power BI rather than stored.

| KPI | Formula |
|------|---------|
| Total Revenue | SUM(Sales_Amount) |
| Average Order Value (AOV) | Total Revenue ÷ Number of Orders |
| Units Sold | SUM(Quantity) |
| Gross Profit | Sales Revenue − Product Cost |
| Gross Margin (%) | Gross Profit ÷ Sales Revenue × 100 |

---

## 12. Future Enhancements

Future versions may include:

- Payment Method
- Order Status
- Shipping Method
- Delivery Time
- Return Status
- Return Reason
- Coupon Code
- Tax Amount