# Business Rules

## Purpose

This document defines the business rules and data validation constraints used in the ShopSphere Marketing Intelligence Data Warehouse.

These rules ensure that the synthetic dataset is realistic, internally consistent, and suitable for SQL analysis and Power BI reporting.

---

# 1. General Rules

- Every table must have a unique Primary Key.
- Foreign Key values must exist in their corresponding dimension tables.
- NULL values are allowed only where explicitly defined.
- All dates must fall within the project date range.
- IDs are generated sequentially.

---

# 2. Campaign Performance Rules

## Rule CP-01

Impressions must be greater than or equal to Clicks.

Impressions ≥ Clicks

---

## Rule CP-02

Clicks must be greater than or equal to Conversions.

Clicks ≥ Conversions

---

## Rule CP-03

Advertising Spend cannot be negative.

Advertising_Spend ≥ 0

---

## Rule CP-04

Campaign Performance records must reference valid:

- Date
- Campaign
- Channel
- Geography
- Device

---

# 3. Sales Rules

## Rule S-01

Quantity Sold must be at least 1.

Quantity ≥ 1

---

## Rule S-02

Unit Selling Price must be greater than zero.

Unit_Selling_Price > 0

---

## Rule S-03

Discount Amount cannot be negative.

Discount_Amount ≥ 0

---

## Rule S-04

Discount Amount cannot exceed the total selling value.

Discount_Amount ≤ Quantity × Unit_Selling_Price

---

## Rule S-05

Sales Amount is calculated as:

Sales Amount =
(Quantity × Unit_Selling_Price)
− Discount_Amount

---

## Rule S-06

Every Sales record must reference:

- Customer
- Product
- Campaign
- Date

---

# 4. Customer Acquisition Rules

## Rule CA-01

Each customer is acquired only once.

One Customer → One Acquisition Record

---

## Rule CA-02

Acquisition Cost cannot be negative.

Acquisition_Cost ≥ 0

---

## Rule CA-03

Every acquisition must be associated with:

- Campaign
- Channel
- Date

---

# 5. Customer Rules

## Rule C-01

Every customer must have a Registration Date.

---

## Rule C-02

Registration Date must be within the project timeline.

---

## Rule C-03

Customer Segment must be one of:

- Budget
- Standard
- Premium

---

## Rule C-04

Loyalty Status must be one of:

- None
- Silver
- Gold
- Platinum

---

# 6. Product Rules

## Rule P-01

Every product belongs to exactly one category.

---

## Rule P-02

Cost Price cannot exceed Unit Price.

Cost_Price ≤ Unit_Price

---

## Rule P-03

Product Status must be:

- Active
- Discontinued

---

# 7. Geography Rules

## Rule G-01

Every city belongs to one state.

---

## Rule G-02

Every state belongs to one region.

---

## Rule G-03

Every region belongs to one country.

---

# 8. Device Rules

## Rule D-01

Android and iOS are Mobile devices.

---

## Rule D-02

Windows and macOS are Desktop operating systems.

---

## Rule D-03

Each Device_ID represents a unique Device Type and Operating System combination.

---

# 9. Date Rules

## Rule DT-01

Date_ID must be unique.

---

## Rule DT-02

Every date must belong to one month, one quarter, and one year.

---

# 10. Data Quality Rules

- Duplicate Primary Keys are not allowed.
- Orphan Foreign Keys are not allowed.
- Negative sales values are not allowed.
- Duplicate acquisition records are not allowed.
- Every fact record must reference valid dimension records.