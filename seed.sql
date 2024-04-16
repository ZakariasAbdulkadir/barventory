-- use .read filename to run this file!

-- sqlite3 <databasename>.db to create a database

-- Drop tables
DROP TABLE IF EXISTS drink;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS alchool;


CREATE TABLE IF NOT EXISTS drink (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    recipe_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES recipe(id)
);

CREATE TABLE IF NOT EXISTS recipe(
    id INTEGER PRIMARY KEY,
    ratio TEXT,
    -- alchool_id INTEGER,
    -- drink_id INTEGER,
    -- FOREIGN KEY (alchool_id) REFERENCES alchool(id)
    -- FOREIGN KEY (drink_id) REFERENCES drink(id)
);

CREATE TABLE IF NOT EXISTS achool(
    id INTEGER PRIMARY KEY,
    abv INTEGER,
    name TEXT
    recipe_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES recipe(id)
);

CREATE TABLE IF NOT EXISTS mixer(
    id INTEGER PRIMARY KEY,
    name TEXT
    recipe_id INTEGER,
    FOREIGN KEY (recipe_id) REFERENCES recipe(id)
);

-- insert some values into the database
INSERT INTO drink(name, price)
VALUES("Margarita", 12.99);
INSERT INTO drink(name, price)
VALUES("Manhattan", 15.99);
INSERT INTO drink(name, price)
VALUES("Mojito", 13.99);


INSERT INTO recipes(ratio, alchool_id, drink_id)
VALUES("1_3", 1, 1);

INSERT INTO achool(name)
VALUES("Vodka");
INSERT INTO achool(name)
VALUES("Whiskey");
INSERT INTO achool(name)
VALUES("Tequila");


INSERT INTO mixer(name)
VALUES("simple syrup");
INSERT INTO mixer(name)
VALUES("bitters");
INSERT INTO mixer(name)
VALUES("lemon juice");