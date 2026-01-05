# Data Warehouse Analysis - FlexiMart

**Student Name:** Swarnim Bhawsar  
**Student ID:** 25071263  

---

## Section A: Star Schema Design

### Fact Table: `sales_fact`
- **Primary Key:** `sale_id`
- **Measures:** `quantity_sold`, `total_price`, `discount`
- **Foreign Keys:** `product_id`, `customer_id`, `store_id`, `date_id`

### Dimension Tables:
1. **Product Dimension (`dim_product`)**
   - `product_id`, `name`, `category`, `subcategory`, `brand`, `price`
2. **Customer Dimension (`dim_customer`)**
   - `customer_id`, `name`, `email`, `gender`, `city`, `state`, `country`
3. **Store Dimension (`dim_store`)**
   - `store_id`, `store_name`, `location`, `manager_name`
4. **Date Dimension (`dim_date`)**
   - `date_id`, `date`, `day`, `month`, `quarter`, `year`, `weekday`

---

## Section B: ETL Process Overview

1. **Extract**
   - Data is extracted from **RDBMS tables**: `products`, `customers`, `orders`.

2. **Transform**
   - Clean null values, correct data types, and standardize formats (e.g., dates, prices).
   - Calculate derived fields such as `total_price = quantity_sold * unit_price - discount`.
   - Map product, customer, and store IDs to their respective dimension tables.
   - Aggregate or summarize data if needed for reporting.

3. **Load**
   - Load transformed data into the **fact table** (`sales_fact`) and dimension tables (`dim_product`, `dim_customer`, `dim_store`, `dim_date`).
   - Ensure referential integrity between fact and dimension tables.
   - Perform incremental loads to update the warehouse regularly without overwriting historical data.

   ## Section C: OLAP Analysis / Queries

### Example 1: Total Sales by Product Category
```sql
SELECT p.category, SUM(f.total_price) AS total_sales
FROM sales_fact f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;

### Example 2: Monthly Sales Trend

SELECT MONTH(d.date) AS month, SUM(f.total_price) AS total_sales
FROM sales_fact f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY MONTH(d.date)
ORDER BY month;

###Example 3: Top 5 Customers by Total Purchase
SELECT c.customer_id, c.name, SUM(f.total_price) AS total_spent
FROM sales_fact f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 5;

###Section D: Benefits of Data Warehouse for FlexiMart
1.Enables fast analytical queries on large historical datasets.
2.Star schema simplifies reporting and OLAP operations.
3.Supports business decisions like:
 -Identifying top-selling products
 -Tracking customer purchase behavior
 -Monitoring seasonal sales trends
4.Improves performance by separating analytics from transactional systems.

###Section E: Conclusion

The data warehouse design using a star schema provides FlexiMart with an efficient analytical platform.
It supports complex OLAP queries, improves reporting performance, and enables data-driven business decisions.
This architecture is scalable and suitable for long-term strategic analysis.