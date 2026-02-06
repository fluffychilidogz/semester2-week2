
-- Enable readable output format
.mode columns
.headers on

-- Instructions
-- 1. sqlite3 orders.db
-- 2. .read collectypes.sql
-- 3. .exit

---- Functions for base

-- 1. List all product categories


--SELECT category 
--FROM products JOIN order_items GROUP BY category

-- 2. Count total number of customers

--SELECT COUNT(customer_id)
--FROM customers;

-- 3. Show all orders for a certain customer

--SELECT orders.order_id, orders.customer_id, orders.order_date, orders.status, orders.total_amount
--FROM orders JOIN customers ON orders.customer_id=customers.customer_id
--WHERE customers.customer_id=?;

-- 4. Display all products priced at & below a certain amount

--SELECT products.name, category, price
--FROM products
--WHERE price<=?;