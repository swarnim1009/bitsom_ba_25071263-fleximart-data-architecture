# Part 1 – Database Design and ETL Pipeline

## 1. Database Design

### Entities
- Customers
- Products
- Orders
- Order_Items

### Relationships
- A customer can place multiple orders
- An order can contain multiple products
- Each order has one payment record

## 2. Normalization
The database is designed in 3rd Normal Form (3NF):
- No redundant data
- Each table has a primary key
- Foreign keys are used to maintain relationships

## 3. ETL Pipeline Design

### Extract
Data is extracted from CSV files containing customer, product, and order data.

### Transform
- Remove duplicate records
- Handle missing values
- Convert date formats
- Validate numeric fields

### Load
Cleaned data is loaded into a relational database such as MySQL or PostgreSQL.

## 4. Tools Used
- SQL
- Python (Pandas)
- Relational Database (MySQL/PostgreSQL)


