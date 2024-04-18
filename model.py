#implement using a class
import sqlite3
connection = sqlite3.connect("recipe.db")
cursor = connection.cursor()
from colorama import Style

class Drink:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def create(self):
        drink = cursor.execute(
            f'''
            INSERT INTO drink(name, price)
            VALUES("{self.name, self.price}")
            '''
        )
        connection.commit()

    # read
    @classmethod
    def getById(cls, id):
        data=cursor.execute(
            f'''
            SELECT * FROM drink
            WHERE id = {id};
            '''
        ).fetchone()
        if data:
            return Drink(data[0], data[1], data[2])
        else:
            return None
    
    @classmethod
    def get_all(cls):
        data=cursor.execute(
            f'''
            SELECT * FROM drink;
            '''
        ).fetchall()
        drinks = []
        for drink in data:
            drinks.append(Drink(data[0], data[1], data[2]))
        return rlist

    def update(self, newName, newPrice):
        cursor.execute(
        f'''
        UPDATE drink
        SET name = "{newName}"
        SET name = "{newPrice}"
        WHERE id ={self.id};
        ''')
        connection.commit()
    
    def delete(self):
        cursor.execute(
            f'''
            DELETE FROM drink
            WHERE id={self.id}
            '''
        )
        connection.commit()

    # def __repr__(self):
    #     return f"{self.id}: {self.name}, {self.price}"


class Mixer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        cursor.execute(
            f'''
            INSERT INTO mixer(name)
            VALUES("{name}")
            '''
        )
        connection.commit()

    @classmethod
    def get_by_id(cls, id):
        data = cursor.execute(
            f'''
            SELECT * FROM mixer
            WHERE id = {id};
            '''
        ).fetchone()
        if data:
            return Mixer(data[0], data[1])
        else:
            return None

    @classmethod
    def get_all(cls):
        data = cursor.execute(
            f'''
            SELECT * FROM mixer;
            '''
        ).fetchall()
        mixers = []
        for mixer in data:
            mixers.append(Mixer(mixer[0], mixer[1]))
        return mixers


class Alchool:
    def __init__(self, id, abv, name):
        self.id = id
        self.abv = abv
        self.name = name

    @classmethod
    def create(cls, abv, name):
        cursor.execute(
            f'''
            INSERT INTO alchool(abv, name)
            VALUES({abv}, "{name}")
            '''
        )
        connection.commit()

    @classmethod
    def get_by_id(cls, id):
        data = cursor.execute(
            f'''
            SELECT * FROM alchool
            WHERE id = {id};
            '''
        ).fetchone()
        if data:
            return Alchool(data[0], data[1], data[2])
        else:
            return None

    @classmethod
    def get_all(cls):
        data = cursor.execute(
            f'''
            SELECT * FROM alchool;
            '''
        ).fetchall()
        alcohols = []
        for alcohol in data:
            alcohols.append(Alchool(alcohol[0], alcohol[1], alcohol[2]))
        return alcohols


class Recipe:
    def __init__(self, id, ratio, alchool_id, drink_id):
        self.id = id
        self.ratio = ratio
        self.alchool_id = alchool_id
        self.drink_id = drink_id

    @classmethod
    def create(cls, ratio, alchool_id, drink_id):
        cursor.execute(
            f'''
            INSERT INTO recipe(ratio, alchool_id, drink_id)
            VALUES("{ratio}", {alchool_id}, {drink_id})
            '''
        )
        connection.commit()

    @classmethod
    def get_by_id(cls, id):
        data = cursor.execute(
            f'''
            SELECT * FROM recipe
            WHERE id = {id};
            '''
        ).fetchone()
        if data:
            return Recipe(data[0], data[1], data[2], data[3])
        else:
            return None

    @classmethod
    def get_all(cls):
        data = cursor.execute(
            f'''
            SELECT * FROM recipe;
            '''
        ).fetchall()
        recipes = []
        for recipe in data:
            recipes.append(Recipe(recipe[0], recipe[1], recipe[2], recipe[3]))
        return recipes

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

if __name__ == "__main__":
    main()