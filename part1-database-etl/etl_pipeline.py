# ETL Pipeline for FlexiMart
# Author: Swarnim Bhawsar
# Description: Extracts, cleans, and loads CSV data into MySQL database

import pandas as pd
import mysql.connector
from datetime import datetime
# Step 1: Read customers CSV
customers_file = 'data/customers_raw.csv'
try:
    customers_df = pd.read_csv(customers_file)
    print("Customers CSV loaded successfully")
except Exception as e:
    print(f"Error loading customers CSV: {e}")
    # Step 2: Clean customers data

# Remove duplicate records
customers_df.drop_duplicates(inplace=True)

# Handle missing emails by dropping those rows
customers_df = customers_df.dropna(subset=['email'])

# Standardize phone format (example: +91-XXXXXXXXXX)
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = ''.join(filter(str.isdigit, str(phone)))
    if len(digits) == 10:
        return '+91-' + digits
    elif len(digits) == 12 and digits.startswith('91'):
        return '+' + digits[:2] + '-' + digits[2:]
    else:
        return phone

customers_df['phone'] = customers_df['phone'].apply(standardize_phone)
# Convert registration_date to YYYY-MM-DD (MySQL compatible)
customers_df['registration_date'] = pd.to_datetime(
    customers_df['registration_date'],
    errors='coerce',
    dayfirst=True
).dt.strftime('%Y-%m-%d')

# Drop rows where date conversion failed
customers_df = customers_df.dropna(subset=['registration_date'])


print("Customers data cleaned successfully")
# Step 3: Read products CSV
products_file = 'data/products_raw.csv'
try:
    products_df = pd.read_csv(products_file)
    print("Products CSV loaded successfully")
except Exception as e:
    print(f"Error loading products CSV: {e}")

# Step 4: Clean products data

# Remove duplicates
products_df.drop_duplicates(inplace=True)

# Handle missing prices by filling with 0
products_df['price'] = products_df['price'].fillna(0)

# Handle null stock_quantity by filling with 0
products_df['stock_quantity'] = products_df['stock_quantity'].fillna(0)

# Standardize category names (capitalize first letter)
products_df['category'] = products_df['category'].str.strip().str.title()

print("Products data cleaned successfully")
## Step 5: Read sales CSV
sales_file = 'data/sales_raw.csv'

sales_df = pd.read_csv(sales_file)
print("Sales CSV loaded successfully")

#important fix
sales_df.rename(columns={'transaction_date':'order_date'}, inplace=True)
print("sales CSV columns:", sales_df.columns)

# Check column names (IMPORTANT)
print("Sales CSV columns:", sales_df.columns)

# Step 6: Clean sales data

# Remove duplicate transactions
sales_df.drop_duplicates(inplace=True)

# Drop rows with missing customer_id or product_id
sales_df = sales_df.dropna(subset=['customer_id', 'product_id'])

# Convert customer_id and product_id to numeric (C001 -> 1, P005 -> 5)
sales_df['customer_id'] = sales_df['customer_id'].astype(str).str.replace('C', '').astype(int)
sales_df['product_id'] = sales_df['product_id'].astype(str).str.replace('P', '').astype(int)

# Calculate total_amount and subtotal
sales_df['subtotal'] = sales_df['quantity'] * sales_df['unit_price']
sales_df['total_amount'] = sales_df['subtotal']


# Standardize order_date format to YYYY-MM-DD
sales_df['order_date'] = pd.to_datetime(sales_df['order_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Drop rows where order_date conversion failed
sales_df = sales_df.dropna(subset=['order_date'])

print("Sales data cleaned successfully")
# Step 7: Load data into MySQL
# Create MySQL connection and cursor
# NOTE:
# Replace YOUR_MYSQL_PASSWORD with your local MySQL password before running
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sb010406",
    database="fleximart"
)


cursor = conn.cursor()

# Fetch valid customer IDs from customers table
cursor.execute("SELECT customer_id FROM customers")
valid_customers = {row[0] for row in cursor.fetchall()}

# Keep only sales with valid customer_ids
sales_df = sales_df[sales_df['customer_id'].isin(valid_customers)]


try:
    # Load customers
    for _, row in customers_df.iterrows():
        cursor.execute("""
            INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (row['first_name'], row['last_name'], row['email'], row['phone'], row.get('city'), row.get('registration_date')))
    
    # Load products
    for _, row in products_df.iterrows():
        cursor.execute("""
            INSERT INTO products (product_name, category, price, stock_quantity)
            VALUES (%s, %s, %s, %s)
        """, (row['product_name'], row['category'], row['price'], row['stock_quantity']))
    
    # Load sales (orders + order_items)
    for _, row in sales_df.iterrows():
        # Insert order
        cursor.execute("""
            INSERT INTO orders (customer_id, order_date, total_amount)
            VALUES (%s, %s, %s)
        """, (int(row['customer_id']), row['order_date'], row['total_amount']))
        order_id = cursor.lastrowid
        
        # Insert order_item
        cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, int(row['product_id']), int(row['quantity']), row['unit_price'], row['subtotal']))
    
    # Commit all changes
    conn.commit()
    print("All data loaded successfully into MySQL")
except mysql.connector.Error as err:
    print(f"Error inserting data: {err}")
finally:
    cursor.close()
    conn.close()
    print("data loaded into mysql successfully")