# Star Schema Design

## Fact Tables
- Fact_Campaign_Performance
- Fact_Sales
- Fact_Customer_Acquisition

## Dimension Tables
- Dim_Date
- Dim_Campaign
- Dim_Channel
- Dim_Customer
- Dim_Product
- Dim_Geography
- Dim_Device

## Grain

### Fact_Campaign_Performance
One record represents one campaign's performance on one date, through one marketing channel, in one geography, on one device.

### Fact_Sales
One record represents one completed sales transaction.

### Fact_Customer_Acquisition
One record represents one customer acquired through one campaign.