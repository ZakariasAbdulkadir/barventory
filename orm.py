#implement using a class
import sqlite3
connection = sqlite3.connect("post.db")
cursor = connection.cursor()

class Drink:
    def __init__(self, id=None, name, price):
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
            SELECT * FROM posts
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
            SELECT * FROM posts;
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







