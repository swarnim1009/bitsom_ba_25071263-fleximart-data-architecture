# Part 2 – NoSQL Analysis and MongoDB

## 1. Why NoSQL for FlexiMart?
NoSQL databases are suitable for FlexiMart because:
- They handle large volumes of data efficiently
- Schema flexibility allows easy changes
- High scalability for growing user data

## 2. Choice of Database
MongoDB is selected because:
- It stores data in JSON-like documents
- Easy integration with applications
- Supports indexing and aggregation

## 3. Sample Document Structure

### Customer Collection
{
  "_id": "C001",
  "name": "John Doe",
  "email": "john@example.com",
  "orders": [
    {
      "order_id": "O101",
      "total_amount": 2500,
      "payment_status": "Completed"
    }
  ]
}

## 4. Advantages of MongoDB
- High performance
- Horizontal scalability
- Flexible schema design

