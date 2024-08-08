CREATE TABLE car_model_dim (
    car_model_id integer ,
    model_name VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(100) NOT NULL,
    weight NUMERIC(20,2),
    price decimal(10,2) NOT NULL
);



CREATE TABLE transaction_fact (
    transaction_number integer ,
    customer_name VARCHAR(50) NOT NULL,
    customer_phone VARCHAR(20),
    transaction_datetime TIMESTAMP,
    salesperson_name VARCHAR(50) NOT NULL,
    car_model_id integer 
);
