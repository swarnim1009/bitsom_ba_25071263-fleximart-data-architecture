\## Data Warehouse Analysis - FlexiMart



\## Section A: Purpose of Data Warehouse

The data warehouse consolidates data from multiple sources (customers, products, sales) into a central repository.  

Key benefits:

\- Enables historical analysis of sales, products, and customer behavior.

\- Supports business intelligence (BI) and reporting.

\- Provides a single source of truth for analytics.



---



\## Section B: Star Schema Design



\### 1. Fact Table: `sales\_fact`

\*\*Contains transactional data for analytics.\*\*



| Column            | Description                          |

|------------------|--------------------------------------|

| transaction\_id    | Unique ID for each sale              |

| customer\_id       | Links to customer dimension          |

| product\_id        | Links to product dimension           |

| quantity          | Number of units sold                 |

| unit\_price        | Price per unit at transaction        |

| total\_amount      | Calculated as quantity \* unit\_price  |

| transaction\_date  | Date of transaction                  |

| status            | Completed, Pending, or Cancelled     |



\### 2. Dimension Tables



\*\*Customer Dimension: `dim\_customer`\*\*



| Column         | Description                  |

|----------------|------------------------------|

| customer\_id    | Unique ID                    |

| first\_name     | Customer first name          |

| last\_name      | Customer last name           |

| email          | Email address                |

| phone          | Contact number               |

| city           | City                         |

| registration\_date | Date of joining           |



\*\*Product Dimension: `dim\_product`\*\*



| Column        | Description                  |

|---------------|------------------------------|

| product\_id    | Unique product ID            |

| product\_name  | Name of product              |

| category      | Product category             |

| subcategory   | Product subcategory          |

| price         | Current price                |

| stock\_quantity| Available stock              |



\*\*Date Dimension: `dim\_date`\*\* \*(optional, for analytics)\*



| Column        | Description                  |

|---------------|------------------------------|

| date\_id       | Unique date ID               |

| date          | Actual date                  |

| day           | Day of month                 |

| month         | Month number                 |

| quarter       | Quarter number               |

| year          | Year                         |

| weekday       | Day of week                  |



---



\## Section C: ETL Process Overview



1\. \*\*Extract:\*\*  

&nbsp;  - Load `customers\_raw.csv`, `products\_raw.csv`, `sales\_raw.csv`.



2\. \*\*Transform:\*\*  

&nbsp;  - Clean missing values and duplicates.  

&nbsp;  - Normalize product categories and customer data.  

&nbsp;  - Convert dates to consistent format (`YYYY-MM-DD`).  

&nbsp;  - Calculate `total\_amount` in sales fact table.



3\. \*\*Load:\*\*  

&nbsp;  - Load cleaned data into the data warehouse tables (`fact\_sales`, `dim\_customer`, `dim\_product`, `dim\_date`).



---



\## Section D: Analytics Use Cases



\- Total sales by month, product, or category.  

\- Top-selling products and revenue contribution.  

\- Customer purchase patterns and segmentation.  

\- Inventory planning and stock optimization.  



---



\## Section E: Benefits



\- Centralized reporting and decision-making.  

\- Historical trend analysis for marketing and sales strategies.  

\- Easier integration with BI tools like Tableau or Power BI.  

&nbsp;Data Warehouse Analysis - FlexiMart



\## Section A: Purpose of Data Warehouse

The data warehouse consolidates data from multiple sources (customers, products, sales) into a central repository.  

Key benefits:

\- Enables historical analysis of sales, products, and customer behavior.

\- Supports business intelligence (BI) and reporting.

\- Provides a single source of truth for analytics.



---



\## Section B: Star Schema Design



\### 1. Fact Table: `sales\_fact`

\*\*Contains transactional data for analytics.\*\*



| Column            | Description                          |

|------------------|--------------------------------------|

| transaction\_id    | Unique ID for each sale              |

| customer\_id       | Links to customer dimension          |

| product\_id        | Links to product dimension           |

| quantity          | Number of units sold                 |

| unit\_price        | Price per unit at transaction        |

| total\_amount      | Calculated as quantity \* unit\_price  |

| transaction\_date  | Date of transaction                  |

| status            | Completed, Pending, or Cancelled     |



\### 2. Dimension Tables



\*\*Customer Dimension: `dim\_customer`\*\*



| Column         | Description                  |

|----------------|------------------------------|

| customer\_id    | Unique ID                    |

| first\_name     | Customer first name          |

| last\_name      | Customer last name           |

| email          | Email address                |

| phone          | Contact number               |

| city           | City                         |

| registration\_date | Date of joining           |



\*\*Product Dimension: `dim\_product`\*\*



| Column        | Description                  |

|---------------|------------------------------|

| product\_id    | Unique product ID            |

| product\_name  | Name of product              |

| category      | Product category             |

| subcategory   | Product subcategory          |

| price         | Current price                |

| stock\_quantity| Available stock              |



\*\*Date Dimension: `dim\_date`\*\* \*(optional, for analytics)\*



| Column        | Description                  |

|---------------|------------------------------|

| date\_id       | Unique date ID               |

| date          | Actual date                  |

| day           | Day of month                 |

| month         | Month number                 |

| quarter       | Quarter number               |

| year          | Year                         |

| weekday       | Day of week                  |



---



\## Section C: ETL Process Overview



1\. \*\*Extract:\*\*  

&nbsp;  - Load `customers\_raw.csv`, `products\_raw.csv`, `sales\_raw.csv`.



2\. \*\*Transform:\*\*  

&nbsp;  - Clean missing values and duplicates.  

&nbsp;  - Normalize product categories and customer data.  

&nbsp;  - Convert dates to consistent format (`YYYY-MM-DD`).  

&nbsp;  - Calculate `total\_amount` in sales fact table.



3\. \*\*Load:\*\*  

&nbsp;  - Load cleaned data into the data warehouse tables (`fact\_sales`, `dim\_customer`, `dim\_product`, `dim\_date`).



---



\## Section D: Analytics Use Cases



\- Total sales by month, product, or category.  

\- Top-selling products and revenue contribution.  

\- Customer purchase patterns and segmentation.  

\- Inventory planning and stock optimization.  



---



\## Section E: Benefits



\- Centralized reporting and decision-making.  

\- Historical trend analysis for marketing and sales strategies.  

\- Easier integration with BI tools like Tableau or Power BI.  



