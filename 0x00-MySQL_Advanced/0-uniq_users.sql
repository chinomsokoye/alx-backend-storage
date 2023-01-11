-- Creates a table users with below attributes
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- If table exists, script will not fail, can be executed on any database

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
);
