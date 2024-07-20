SELECT transaction_fact.customer_name, SUM(car_model_dim.price)
FROM transaction_fact 
INNER JOIN car_model_dim 
ON car_model_id 
GROUP BY transaction_fact.customer_name