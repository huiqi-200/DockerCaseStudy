INSERT INTO car_model_dim (car_model_id, model_name, manufacturer, weight, price) 
VALUES 
(1, 'Model S', 'Tesla', 1961, 79999.99),
(2, 'Mustang', 'Ford', 1653, 55999.99),
(3, 'Civic', 'Honda', 1247, 24999.99),
(4, 'Corolla', 'Toyota', 1300, 19999.99),
(5, 'Model 3', 'Tesla', 1610, 39999.99);


INSERT INTO transaction_fact (transaction_number, customer_name, customer_phone, transaction_datetime, salesperson_name, car_model_id) 
VALUES 
(1, 'John Doe', '123-456-7890', '2024-08-07 14:30:00', 'Alice Smith', 1),
(2, 'Jane Roe', '987-654-3210', '2024-08-07 15:00:00', 'Bob Johnson', 2),
(3, 'Sam Green', '555-123-4567', '2024-08-07 15:30:00', 'Charlie Brown', 3),
(4, 'Lisa White', '444-987-6543', '2024-08-07 16:00:00', 'Diana Prince', 4),
(5, 'Tom Black', '333-456-7890', '2024-08-07 16:30:00', 'Eve Adams', 5);
