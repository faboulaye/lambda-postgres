CREATE TABLE IF NOT EXISTS employe (
    id          SERIAL PRIMARY KEY,
    fullname    VARCHAR(255) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    department  VARCHAR(255) NOT NULL,
    age         INTEGER
);
INSERT INTO employe(fullname, email, department, age)
	VALUES ('Employe 1', 'Email 1', 'Department 1', 30),
  ('Employe 2', 'Email 2', 'Department 2', 24),
  ('Employe 3', 'Email 3', 'Department 3', 30),
  ('Employe 4', 'Email 4', 'Department 4', 33),
  ('Employe 5', 'Email 5', 'Department 5', 25);