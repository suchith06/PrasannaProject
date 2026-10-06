-- 1. Total Revenue
SELECT SUM(line_total) AS total_revenue
FROM final_sales;
-- 2. Revenue by Category
SELECT
    category,
    SUM(line_total) AS category_revenue
FROM final_sales
GROUP BY category
ORDER BY category_revenue DESC;
-- 3. Revenue by Product
SELECT
    product_name,
    SUM(line_total) AS product_revenue
FROM final_sales
GROUP BY product_name
ORDER BY product_revenue DESC;
-- 4. Revenue by Customer
SELECT
    customer_name,
    SUM(line_total) AS customer_revenue
FROM final_sales
GROUP BY customer_name
ORDER BY customer_revenue DESC;
-- 5. Revenue by State
SELECT
    state,
    SUM(line_total) AS state_revenue
FROM final_sales
GROUP BY state
ORDER BY state_revenue DESC;
-- 6. Revenue by Order
SELECT
    order_id,
    customer_name,
    SUM(line_total) AS order_revenue
FROM final_sales
GROUP BY order_id, customer_name
ORDER BY order_revenue DESC;
-- 7. Average Order Value
SELECT
    ROUND(AVG(order_revenue)::numeric, 2) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(line_total) AS order_revenue
    FROM final_sales
    GROUP BY order_id
) AS orders;
-- 8. Number of Orders per Customer
SELECT
    customer_name,
    COUNT(DISTINCT order_id) AS total_orders
FROM final_sales
GROUP BY customer_name
ORDER BY total_orders DESC, customer_name;
-- 9. Top-Selling Products by Quantity
SELECT
    product_name,
    SUM(quantity) AS total_quantity_sold
FROM final_sales
GROUP BY product_name
ORDER BY total_quantity_sold DESC, product_name;
-- 10. Monthly Revenue
SELECT
    DATE_TRUNC('month', order_date::date) AS month,
    SUM(line_total) AS monthly_revenue
FROM final_sales
GROUP BY DATE_TRUNC('month', order_date::date)
ORDER BY month;