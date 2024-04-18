-- use .read filename to run this file!

-- sqlite3 <databasename>.db to create a database

-- Drop tables
DROP TABLE IF EXISTS drink;
DROP TABLE IF EXISTS recipe;
DROP TABLE IF EXISTS alchool;


CREATE TABLE IF NOT EXISTS drink(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
    
);

CREATE TABLE IF NOT EXISTS recipe(
    id INTEGER PRIMARY KEY,
    ratio TEXT,
    alchool_id INTEGER,
    drink_id INTEGER,
    FOREIGN KEY (alchool_id) REFERENCES alchool(id),
    FOREIGN KEY (drink_id) REFERENCES drink(id)
);

CREATE TABLE IF NOT EXISTS achool(
    id INTEGER PRIMARY KEY,
    abv INTEGER,
    name TEXT
);

CREATE TABLE IF NOT EXISTS mixer(
    id INTEGER PRIMARY KEY,
    name TEXT
);


INSERT INTO drink(name, price)
VALUES("Margarita", 12.99);
INSERT INTO drink(name, price)
VALUES("Manhattan", 15.99);
INSERT INTO drink(name, price)
VALUES("Mojito", 13.99);


INSERT INTO recipe(ratio, alchool_id, drink_id)
VALUES("1_3", 1, 1);

INSERT INTO achool(abv, name)
VALUES(50, "Vodka");
INSERT INTO achool(abv, name)
VALUES(47, "Whiskey");
INSERT INTO achool(abv, name)
VALUES(35, "Tequila");


INSERT INTO mixer(name)
VALUES("simple syrup");
INSERT INTO mixer(name)
VALUES("bitters");
INSERT INTO mixer(name)
VALUES("lemon juice");