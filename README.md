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
│
├── sql/
│   └── regional_demand_query.sql     # SQL query for aggregation
│
├── data/
│   └── regional_demand.csv           # Output from SQL
│   └── cleaned_regional_demand.csv   # Cleaned CSV for Tableau & EDA
│
├── python/
│   └── regional_demand_analysis.py   # Python script for EDA & charts
│
├── tableau/
│   └── dashboard.twb                 # Tableau dashboard file
│
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
-- Regional Demand Insights
São Paulo (SP) had the highest monthly demand and sales throughout the timeline.

Minas Gerais (MG) and Rio de Janeiro (RJ) consistently followed SP in both demand volume and sales value.

States like Roraima (RR) and Amapá (AP) showed minimal demand, indicating limited market reach or infrastructure.

-- Demand Seasonality
Noticeable peaks in Q4, suggesting strong demand during holiday months.

Sales dips in certain months may reflect national holidays, logistics, or campaign gaps.

-- Freight Patterns
Higher freight values were often associated with remote or lower-demand states.

Freight costs were significant in the North and Northeast regions despite lower order volumes.

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
