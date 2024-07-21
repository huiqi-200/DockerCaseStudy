SELECT car_model_dim.manufacturer, COUNT(transaction_fact.transaction_number) as sales_quantity
FROM transaction_fact 
RIGHT JOIN car_model_dim 
ON car_model_dim.car_model_id = transaction_fact.car_model_id
GROUP BY car_model_dim.manufacturer
ORDER BY sales_quantity DESC
LIMIT 3;