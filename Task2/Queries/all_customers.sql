SELECT transaction_fact.customer_name, SUM(car_model_dim.price)
FROM transaction_fact 
LEFT JOIN car_model_dim 
ON car_model_dim.car_model_id = transaction_fact.car_model_id
GROUP BY transaction_fact.customer_name; 