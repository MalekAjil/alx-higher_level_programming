-- creates a table called second_table in the current database in MySQL server.
CREATE TABLE IF NOT EXISTS second_table (id INT DEFAULT NULL, name VARCHAR(256) DEFAULT NULL, score INT DEFAULT NULL);
INSERT INTO second_table(id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table(id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table(id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table(id, name, score) VALUES (4, "George", 8);
