# Data Dictionary – Dim_Channel

## 1. Overview

The **Dim_Channel** table stores information about the marketing channels through which campaigns are delivered to customers. It enables channel-wise analysis of marketing performance, customer acquisition, and sales.

Each marketing channel is uniquely identified by **Channel_ID** and is referenced by multiple fact tables.

---

## 2. Purpose

The purpose of the Channel Dimension is to:

- Store marketing channel information.
- Enable channel-wise performance analysis.
- Compare the effectiveness of different marketing platforms.
- Support ROI, ROAS, CTR, CPC, and CPA analysis.
- Eliminate repetitive channel information from fact tables.

---

## 3. Business Questions

This table helps answer questions such as:

- Which marketing channel generates the highest revenue?
- Which channel has the highest Return on Ad Spend (ROAS)?
- Which channel has the highest Click-Through Rate (CTR)?
- Which channel acquires customers at the lowest cost?
- Which marketing platform should receive additional investment?
- Which channel performs best for different campaign types?

---

## 4. Table Information

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Channel_ID | INT | Unique marketing channel identifier | 1 |
| Channel_Name | VARCHAR(50) | Name of the marketing channel | Google Ads |
| Channel_Type | VARCHAR(50) | Category of the channel | Paid Search |
| Cost_Model | VARCHAR(30) | Billing model used by the platform | CPC |
| Is_Paid_Channel | BOOLEAN | Indicates whether the channel is paid or organic | TRUE |

---

## 5. Primary Key

**Primary Key:** Channel_ID

Each marketing channel is assigned a unique identifier.

---

## 6. Foreign Keys

This table does not contain foreign keys.

It is referenced by:

- Fact_Campaign_Performance
- Fact_Customer_Acquisition

---

## 7. Relationships

| Referenced By | Relationship |
|---------------|-------------|
| Fact_Campaign_Performance | One Channel → Many Campaign Performance Records |
| Fact_Customer_Acquisition | One Channel → Many Customer Acquisition Records |

Relationship Type:

One-to-Many (1:M)

---

## 8. Example Record

| Channel_ID | Channel_Name | Channel_Type | Cost_Model | Is_Paid_Channel |
|------------|--------------|--------------|------------|-----------------|
| 1 | Google Ads | Paid Search | CPC | TRUE |

---

## 9. Design Decisions

### Why was this table created?

Marketing channel information is shared across multiple campaigns. Storing it in a dedicated dimension reduces redundancy and ensures consistent reporting.

---

### Why is this a Dimension Table?

The table contains descriptive information about marketing platforms rather than measurable business events.

---

### Why were these columns selected?

The selected columns support:

- Channel comparison
- Marketing spend analysis
- Platform performance evaluation
- Cost model analysis
- ROI and ROAS reporting

---

### Why is Channel_ID the Primary Key?

Channel_ID provides a unique and stable identifier that simplifies joins with fact tables and follows dimensional modeling best practices.

---

### Business Value

The Channel Dimension enables stakeholders to:

- Compare marketing platform performance.
- Optimize advertising budgets.
- Identify high-performing acquisition channels.
- Improve campaign strategy.
- Measure channel efficiency.

---

## 10. Future Enhancements

Future versions may include:

- Platform Owner
- Vendor Name
- Account ID
- Campaign Manager
- Target Audience
- Default Attribution Model
- Average CPC
- Average CPM
- Average Conversion Rate