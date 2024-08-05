
/*
This query was created during the case study
*/
SELECT car_model_dim.manufacturer, COUNT(transaction_fact.transaction_number) as sales_quantity
FROM transaction_fact 
RIGHT JOIN car_model_dim 
ON car_model_dim.car_model_id = transaction_fact.car_model_id
GROUP BY car_model_dim.manufacturer
ORDER BY sales_quantity DESC
LIMIT 3;

/*
This query was created once I found out about the rank function
and after i realised it was for current month
*/
WITH car_model_rank as (
  SELECT car_model_dim.manufacturer, COUNT(transaction_fact.transaction_number) as sales_quantity, RANK() OVER ORDER BY sales_quantity as rank
  FROM transaction_fact 
  RIGHT JOIN car_model_dim 
  ON car_model_dim.car_model_id = transaction_fact.car_model_id
  GROUP BY car_model_dim.manufacturer
  HAVING MONTH(transaction_fact.date) == MONTH(getdate()) 
  ORDER BY sales_quantity DESC;
)
SELECT car_model_dim, sales_quantity
FROM car_model_rank
WHERE rank >= 3;
