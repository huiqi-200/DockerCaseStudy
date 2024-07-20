SELECT car_model_dim.manufacturer, COUNT(*) as sales_quantity
FROM transaction_fact 
INNER JOIN car_model_dim 
ON car_model_id 
GROUP BY car_model_dim.manufacturer
ORDER BY sales_quantity DESC
LIMIT 3