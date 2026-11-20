-- Write your query below
SELECT s.seller_name
FROM seller s
WHERE s.seller_id NOT IN (
    SELECT t.seller_id 
    FROM orders o,seller t
    WHERE o.sale_date BETWEEN '2020-01-01' AND '2020-12-31' AND
    o.seller_id = t.seller_id
)
ORDER BY seller_name;