
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
  SELECT car_model_dim.manufacturer, COUNT(transaction_fact.transaction_number) as sales_quantity
  FROM transaction_fact 
  RIGHT JOIN car_model_dim 
  ON car_model_dim.car_model_id = transaction_fact.car_model_id
  WHERE date_trunc('month', transaction_fact.transaction_datetime) = date_trunc('month', current_timestamp) 
  GROUP BY car_model_dim.manufacturer
  ORDER BY sales_quantity DESC
),
rank_table as (
SELECT car_model_rank.manufacturer, sales_quantity, RANK() OVER (ORDER BY sales_quantity DESC) as rank
FROM car_model_rank

)
select manufacturer, sales_quantity
FROM rank_table
where rank <= 3
ORDER BY rank;


