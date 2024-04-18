import sqlite3
from colorama import Style

# Establishing a connection to the SQLite database
connection = sqlite3.connect("recipe.db")
cursor = connection.cursor()

# Define the classes
class Drink:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    @staticmethod
    def create(name, price):
        cursor.execute(
            '''
            INSERT INTO drink(name, price)
            VALUES(?, ?)
            ''',
            (name, price)
        )
        connection.commit()

    @classmethod
    def get_by_id(cls, id):
        data = cursor.execute(
            '''
            SELECT * FROM drink
            WHERE id = ?;
            ''',
            (id,)
        ).fetchone()
        if data:
            return cls(*data)
        else:
            return None

    @classmethod
    def get_all(cls):
        data = cursor.execute(
            '''
            SELECT * FROM drink;
            '''
        ).fetchall()
        drinks = [cls(*row) for row in data]
        return drinks

    def update(self, new_name, new_price):
        cursor.execute(
            '''
            UPDATE drink
            SET name = ?, price = ?
            WHERE id = ?;
            ''',
            (new_name, new_price, self.id)
        )
        connection.commit()

    def delete(self):
        cursor.execute(
            '''
            DELETE FROM drink
            WHERE id = ?;
            ''',
            (self.id,)
        )
        connection.commit()


class Mixer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create(name):
        cursor.execute(
            '''
            INSERT INTO mixer(name)
            VALUES(?)
            ''',
            (name,)
        )
        connection.commit()

    @classmethod
    def get_by_id(cls, id):
        data = cursor.execute(
            '''
            SELECT * FROM mixer
            WHERE id = ?;
            ''',
            (id,)
        ).fetchone()
        if data:
            return cls(*data)
        else:
            return None

    @classmethod
    def get_all(cls):
        data = cursor.execute(
            '''
            SELECT * FROM mixer;
            '''
        ).fetchall()
        mixers = [cls(*row) for row in data]
        return mixers


class Alchool:
    def __init__(self, id, abv, name):
        self.id = id
        self.abv = abv
        self.name = name

    @staticmethod
    def create(abv, name):
        cursor.execute(
            '''
            INSERT INTO alchool(abv, name)
            VALUES(?, ?)
            ''',
            (abv, name)
        )
        connection.commit()

    @classmethod
    def get_by_id(cls, id):
        data = cursor.execute(
            '''
            SELECT * FROM alchool
            WHERE id = ?;
            ''',
            (id,)
        ).fetchone()
        if data:
            return cls(*data)
        else:
            return None

    @classmethod
    def get_all(cls):
        data = cursor.execute(
            '''
            SELECT * FROM alchool;
            '''
        ).fetchall()
        alcohols = [cls(*row) for row in data]
        return alcohols


class Recipe:
    def __init__(self, id, ratio, alchool_id, drink_id):
        self.id = id
        self.ratio = ratio
        self.alchool_id = alchool_id
        self.drink_id = drink_id

    @staticmethod
    def create(ratio, alchool_id, drink_id):
        cursor.execute(
            '''
            INSERT INTO recipe(ratio, alchool_id, drink_id)
            VALUES(?, ?, ?)
            ''',
            (ratio, alchool_id, drink_id)
        )
        connection.commit()

    @classmethod
    def get_by_id(cls, id):
        data = cursor.execute(
            '''
            SELECT * FROM recipe
            WHERE id = ?;
            ''',
            (id,)
        ).fetchone()
        if data:
            return cls(*data)
        else:
            return None

    @classmethod
    def get_all(cls):
        data = cursor.execute(
            '''
            SELECT * FROM recipe;
            '''
        ).fetchall()
        recipes = [cls(*row) for row in data]
        return recipes

# Define functions for CLI tool
def list_drinks():
    drinks = Drink.get_all()
    for drink in drinks:
        print(drink.name, drink.price)

def add_drink():
    name = input("Enter drink name: ")
    price = float(input("Enter drink price: "))
    Drink.create(name, price)

def list_mixers():
    mixers = Mixer.get_all()
    for mixer in mixers:
        print(mixer.name)

def add_mixer():
    name = input("Enter mixer name: ")
    Mixer.create(name)

def list_alcohols():
    alcohols = Alchool.get_all()
    for alcohol in alcohols:
        print(alcohol.name, alcohol.abv)

def add_alcohol():
    name = input("Enter alcohol name: ")
    abv = float(input("Enter alcohol ABV: "))
    Alchool.create(abv, name)

def list_recipes():
    recipes = Recipe.get_all()
    for recipe in recipes:
        print(recipe.ratio, recipe.alchool_id, recipe.drink_id)

def add_recipe():
    ratio = input("Enter recipe ratio: ")
    alchool_id = int(input("Enter alcohol ID: "))
    drink_id = int(input("Enter drink ID: "))
    Recipe.create(ratio, alchool_id, drink_id)

# Main CLI function
def main():
    while True:
        print(Style.RESET_ALL)
        print("1. List Drinks")
        print("2. Add Drink")
        print("3. List Mixers")
        print("4. Add Mixer")
        print("5. List Alcohols")
        print("6. Add Alcohol")
        print("7. List Recipes")
        print("8. Add Recipe")
        print("9. Exit\n")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            list_drinks()
        elif choice == '2':
            add_drink()
        elif choice == '3':
            list_mixers()
        elif choice == '4':
            add_mixer()
        elif choice == '5':
            list_alcohols()
        elif choice == '6':
            add_alcohol()
        elif choice == '7':
            list_recipes()
        elif choice == '8':
            add_recipe()
        elif choice == '9':
            print(Style.BRIGHT + "\nExiting... Goodbye!\n"+ Style.RESET_ALL)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
