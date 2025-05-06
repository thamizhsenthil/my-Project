Project Overview

This project analyzes and predicts regional demand patterns using the Olist Brazilian E-commerce Public Dataset. The goal is to understand how customer demand varies across Brazilian states over time, identify sales distribution, and build a foundation for forecasting future demand to support strategic decision-making.

This project applies SQL, Python, and Tableau to extract insights, visualize trends, and present data-backed stories.
Tools & Technologies Used

SQL (PostgreSQL via pgAdmin 4): Data exploration, aggregation

Python (Pandas, Matplotlib, Seaborn): Data cleaning, visualization, export

Tableau: Interactive dashboard and story presentation

Dataset: Olist E-commerce Dataset
Project Structure
 olist-regional-demand/
 
sql/
│   └── regional_demand_query.sql     # SQL query for aggregation

 data/
│   └── regional_demand.csv           # Output from SQL
│   └── cleaned_regional_demand.csv   # Cleaned CSV for Tableau & EDA

 python/
│   └── regional_demand_analysis.py   # Python script for EDA & charts

tableau/
│   └── dashboard.twb                 # Tableau dashboard file


└── README.md                         # Project documentation
 Objective
 
“To explore, visualize, and predict monthly regional demand across Brazil using Olist e-commerce data.”

Key Steps & Methods
1. SQL Data Preparation
Connected and joined relevant tables: orders, order_items, customers

Filtered for delivered orders

Grouped by customer_state and order_month

Aggregated:

total_orders = number of orders

total_sales = sum of product prices

total_freight = freight value

Output: regional_demand.csv

2. Python Visualization & Cleaning
Used pandas, matplotlib, seaborn to:

Clean and sort monthly data

Visualize:

Monthly Demand Trends by region

Total Sales Distribution by state

Exported clean version: cleaned_regional_demand.csv

3. Tableau Dashboard
Interactive Dashboard Components:

Monthly Demand by State – multi-line plot showing how demand fluctuates across regions

Regional Sales Distribution – horizontal bar chart to compare total sales by region

Filters: State, Month for dynamic insights

Story Slides (Optional):

Introduction and Objective

Demand Trend Analysis

Sales Pattern by State

Conclusions & Recommendations
Key Findings
 --1. Regional Demand Insights
- São Paulo (SP) dominated demand with over 43,000 delivered orders, accounting for 28.3% of total delivered orders nationwide.

- Minas Gerais (MG) and Rio de Janeiro (RJ) followed with approximately 15,000 orders (9.8%) and 12,000 orders (7.9%) respectively.

 -States like Roraima (RR) and Amapá (AP) had fewer than 300 total orders, showing <0.2% contribution to national demand.

-- 2. Sales & Revenue Breakdown
 -Total sales across all regions exceeded BRL 17 million.

-SP alone contributed over BRL 5.5 million (~32%) in sales.

-The average order value was BRL 113.24, and median freight cost per order was BRL 16.68.

-- 3. Seasonality in Demand
- Strong seasonal demand observed in November and December (Black Friday & Christmas).

-November 2017 saw a 24% increase in order volume compared to October.

-Demand dropped by nearly 15% in January 2018, indicating post-holiday slowdowns.

-- 4. Freight & Logistics Patterns
- States in the North and Northeast regions (e.g., Amazonas, Pará) had freight costs up to 3x higher than the national average.

-Freight costs often constituted 15–30% of total sales value in remote regions.

 What Could Be Done Next (Future Work)
 Forecast demand by state using time series models (ARIMA, Prophet)

 Product-level demand by region (with product category granularity)

 Logistics optimization: Study delivery times vs. demand

Customer satisfaction: Combine with review scores by state

Use Cases
E-commerce business strategy: Where to invest in marketing, inventory, and fulfillment

Supply chain planning: Forecast logistics needs based on regional spikes

Market expansion decisions: Identify underserved or low-competition regions

Tableau Dashboard:
![Screenshot 2025-05-02 173113](https://github.com/user-attachments/assets/1ed48c65-dcbc-402b-bb67-c06749fc4e6c)
