CREATE TABLE IF NOT EXISTS orders (
  order_id     INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  custom_id    INT(8),
  price        DOUBLE,
  created_time TIMESTAMP,
  updated_time TIMESTAMP DEFAULT now());