# NoSQL Analysis - FlexiMart

## Section A: Limitations of RDBMS

The current relational database struggles with highly diverse products. For example, laptops have RAM and processor attributes, while shoes have size and color. Frequent schema changes for new product types make updates complex. Storing nested data like customer reviews is inefficient in relational tables. Hence, an RDBMS can be inflexible for dynamic, hierarchical product data.

## Section B: Benefits of NoSQL (MongoDB)

MongoDB allows a flexible schema using JSON documents, so each product can have different attributes. Embedded documents make storing nested data, like reviews, easier. Horizontal scaling ensures handling large datasets across multiple servers. This reduces schema migration effort and improves read/write performance for diverse product catalogs.

## Section C: Trade-offs

1. MongoDB does not enforce strong relationships like foreign keys, so data consistency must be managed at the application level.
2. Complex transactions spanning multiple collections are harder to implement compared to relational databases.
