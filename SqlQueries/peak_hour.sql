SELECT derived_table.sales_outlet_id, COUNT(derived_table.product) AS count, derived_table.transaction_time
FROM (
    SELECT p.product, s.sales_outlet_id, s.transaction_time
    FROM sales_reciepts AS s, product AS p, sales_outlet AS s2
    WHERE s.product_id = p.product_id AND s2.sales_outlet_id = s.sales_outlet_id
) AS derived_table
GROUP BY derived_table.sales_outlet_id ,derived_table.transaction_time
ORDER BY count DESC;

