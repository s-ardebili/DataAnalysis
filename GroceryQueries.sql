/* Aggregation: total sales */
SELECT SUM(Total) AS total_sales
FROM supermarket_sales;

/* Sales by Branch */
SELECT branch, SUM(Total) AS total_sales
FROM supermarket_sales
GROUP BY branch
ORDER BY total_sales DESC;

/* Average Rating by Product Line*/
SELECT product_line, AVG(Rating) AS average_rating
FROM supermarket_sales
GROUP BY product_line
ORDER BY average_rating DESC;

/* Total Sales by Customer Type*/
SELECT customer_type, SUM(Total) AS total_sales
FROM supermarket_sales
GROUP BY customer_type;

/*Top 5 Products with Highest Sales*/
SELECT product_line, SUM(Total) AS total_sales
FROM supermarket_sales
GROUP BY product_line
ORDER BY total_sales DESC
LIMIT 5;

/*Sales per Payment Method*/
SELECT payment_method, SUM(Total) AS total_sales
FROM supermarket_sales
GROUP BY payment_method
ORDER BY total_sales DESC;

/*Sales by Gender */
SELECT gender, SUM(Total) AS total_sales
FROM supermarket_sales
GROUP BY gender;