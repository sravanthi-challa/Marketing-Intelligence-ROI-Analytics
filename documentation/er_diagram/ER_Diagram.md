# Entity Relationship Diagram (ERD)

## Purpose

The Entity Relationship Diagram (ERD) visually represents the relationships between the dimension tables and fact tables in the ShopSphere Marketing Intelligence Data Warehouse.

It serves as the blueprint for the database design and ensures that all entities are connected correctly before implementation in MySQL.

---

## Star Schema Overview

The project follows a **Star Schema** design.

Dimension tables store descriptive information.

Fact tables store measurable business events.

---

## Dimension Tables

- Dim_Date
- Dim_Campaign
- Dim_Channel
- Dim_Customer
- Dim_Product
- Dim_Geography
- Dim_Device

---

## Fact Tables

- Fact_Campaign_Performance
- Fact_Sales
- Fact_Customer_Acquisition

---

## Relationship Summary

Fact_Campaign_Performance references:

- Dim_Date
- Dim_Campaign
- Dim_Channel
- Dim_Geography
- Dim_Device

Fact_Sales references:

- Dim_Date
- Dim_Customer
- Dim_Product
- Dim_Campaign

Fact_Customer_Acquisition references:

- Dim_Date
- Dim_Customer
- Dim_Campaign
- Dim_Channel

---

## Relationship Type

All relationships between dimensions and fact tables are:

One-to-Many (1:M)

Dimension Table → Fact Table

---

## Design Principles

- Star Schema
- Surrogate Primary Keys
- Foreign Key Constraints
- Minimal Data Redundancy
- Optimized for Analytics
- Power BI Friendly