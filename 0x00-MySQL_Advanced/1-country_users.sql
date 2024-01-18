-- SQL script that creates a table users with these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)

-- Creates a table 'user' if not exists
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(225) NOT NULL UNIQUE,
    name VARCHAR(225),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
    );
