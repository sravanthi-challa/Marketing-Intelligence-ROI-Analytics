# Data Generation Specification

## Purpose

This document defines how synthetic data will be generated for the ShopSphere Marketing Intelligence project.

The objective is to create realistic, internally consistent datasets suitable for SQL analysis and Power BI dashboards.

---

# 1. Dataset Size

| Table | Planned Rows |
|---------|-------------:|
| Dim_Date | 365 |
| Dim_Campaign | 20 |
| Dim_Channel | 6 |
| Dim_Customer | 5,000 |
| Dim_Product | 500 |
| Dim_Geography | 30 |
| Dim_Device | 6 |
| Fact_Campaign_Performance | 15,000 |
| Fact_Sales | 50,000 |
| Fact_Customer_Acquisition | 5,000 |

---

# 2. Date Range

Start Date:
01-Jan-2025

End Date:
31-Dec-2025

---

# 3. Customer Distribution

Customer Segments

- Budget → 40%
- Standard → 40%
- Premium → 20%

Gender

- Male → 48%
- Female → 50%
- Other → 2%

Age Groups

- 18–25
- 26–35
- 36–45
- 46–60
- 60+

---

# 4. Product Distribution

Categories

- Electronics
- Fashion
- Home & Kitchen
- Beauty
- Sports

Product Status

- Active → 90%
- Discontinued → 10%

---

# 5. Marketing Channels

- Google Ads
- Facebook Ads
- Instagram Ads
- Email Marketing
- YouTube Ads
- Organic Search

---

# 6. Device Distribution

- Android Mobile
- iPhone (iOS)
- Windows Desktop
- macOS Desktop
- Android Tablet
- iPad

---

# 7. Geography

Country

India

Regions

- North
- South
- East
- West

---

# 8. Data Quality

The generated data must satisfy all business rules defined in:

documentation/business_rules/business_rules.md

---

# 9. Referential Integrity

Every foreign key must reference an existing primary key.

No orphan records are allowed.

---

# 10. Randomization Strategy

Data generation will use controlled randomization to create realistic distributions while maintaining reproducibility through a fixed random seed.

---

# 11. Output Format

CSV files

UTF-8 Encoding

Header Included

One file per table.