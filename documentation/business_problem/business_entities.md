# Business Entities

## Overview

Business entities represent the core objects involved in ShopSphere's marketing ecosystem. These entities form the foundation of the database design and help answer important business questions through SQL analysis and Power BI dashboards.

---

# 1. Campaign

## Purpose

A campaign represents a marketing initiative launched to promote products, increase customer engagement, and generate sales.

## Business Questions It Helps Answer

- Which campaign generated the highest revenue?
- Which campaign achieved the highest ROI?
- Which campaign has the highest conversion rate?
- Which campaigns should be paused?
- Which campaigns deserve additional budget?

---

# 2. Marketing Channel

## Purpose

A marketing channel represents the platform through which campaigns are delivered to customers.

Examples include Google Ads, Facebook Ads, Instagram, LinkedIn, Email Marketing, and Affiliate Marketing.

## Business Questions It Helps Answer

- Which marketing channel generates the highest revenue?
- Which channel has the best ROI?
- Which channel has the highest CTR?
- Which channel has the lowest Customer Acquisition Cost (CAC)?
- Which channel should receive more investment?

---

# 3. Customer

## Purpose

A customer represents an individual who interacts with marketing campaigns and purchases products.

## Business Questions It Helps Answer

- Which customer segment generates the highest revenue?
- Which age group converts the best?
- Which gender has the highest purchase rate?
- How many new customers are acquired?
- How many returning customers make purchases?

---

# 4. Product

## Purpose

A product represents an item sold by ShopSphere through various marketing campaigns.

## Business Questions It Helps Answer

- Which products generate the highest sales?
- Which product category performs best?
- Which products have the highest profit margin?
- Which campaigns sell the most products?

---

# 5. Region

## Purpose

A region represents the geographical location where customers interact with campaigns and make purchases.

## Business Questions It Helps Answer

- Which region generates the highest revenue?
- Which region has the highest ROI?
- Which regions require marketing optimization?
- Which region has the highest conversion rate?

---

# 6. Device

## Purpose

A device represents the type of device used by customers while interacting with marketing campaigns.

Examples include Mobile, Desktop, and Tablet.

## Business Questions It Helps Answer

- Which device generates the highest conversions?
- Which device has the highest revenue?
- Which device performs best for each marketing channel?
- Should marketing focus more on mobile users?

---

# 7. Date

## Purpose

The Date entity enables time-based analysis of marketing and sales performance.

## Business Questions It Helps Answer

- Which month generated the highest revenue?
- What are the monthly growth trends?
- Are there seasonal patterns in campaign performance?
- Which quarter performs best?
- Which weekday generates the most sales?

---

# Summary

The seven business entities identified for this project are:

- Campaign
- Marketing Channel
- Customer
- Product
- Region
- Device
- Date

These entities will be transformed into Dimension Tables during the Star Schema design. They will support the Fact Tables that store measurable business events such as campaign performance, sales transactions, and customer acquisition.