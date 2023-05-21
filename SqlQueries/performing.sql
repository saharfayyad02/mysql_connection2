SELECT
    WEEK(product_performance.transaction_date) - WEEK(DATE_SUB(product_performance.transaction_date, INTERVAL DAYOFMONTH(product_performance.transaction_date) - 1 DAY)) + 1 AS week_of_month,
    WEEK(product_performance.transaction_date) AS week_of_year,
    product_performance.sales_outlet_id
FROM (
    SELECT p.product, s2.sales_outlet_id, s.transaction_date
    FROM sales_reciepts AS s
    JOIN product AS p ON s.product_id = p.product_id
    JOIN sales_outlet AS s2 ON s.sales_outlet_id = s2.sales_outlet_id
) AS product_performance
GROUP BY product_performance.sales_outlet_id, week_of_month, week_of_year, product_performance.product
ORDER BY COUNT(product_performance.product) DESC;
