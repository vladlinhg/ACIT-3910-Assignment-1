"""
    a simple program connect to mysql server with python and able to change or add a word into the database
"""
import mysql.connector


class Database:
    def __init__(self) -> None:
        self.hostname = input("What host to connect to (localhost): ")
        self.port = input("What port to connect to (3306): ")
        self.user = input("What user to connect with (root): ")
        self.password = input("What password to connect with: ")


class MyDB:
    def __init__(self, db: Database):
        """
            MyDB is a class represent instance of mysql.connector

        Args:
            db (Database): Database is the class stored information to login into specific MySQL server 
        """    
        try:
            res = mysql.connector.connect(
                host=str(db.hostname),
                user=str(db.user),
                password=str(db.password)
            )
            print("Connect successfully.")
            mycursor = res.cursor()
            mycursor.execute("SHOW VARIABLES like 'version'")
            myresult = mycursor.fetchall()
            for row in myresult:
                print(row)
            self.db = res
            self.cursor = self.db.cursor()

        except mysql.connector.Error as err:
            print("Could not login to host with user/password provided.")
            print("Exiting.")
            exit()

    def add_or_change_a_word(self):
        word = input("What word do you want to add/change: ")
        sql = "SELECT * FROM dictionary.word WHERE word = %s"
        entry = (word, )
        self.cursor.execute(sql, entry)
        self.cursor.fetchall()
        if self.cursor.rowcount == 0:
            print("The word '" + word + "' was not found... adding")
            sql = "INSERT INTO dictionary.word (word) VALUES (%s)"
            entry = (word, )
            self.cursor.execute(sql, entry)
            self.db.commit()
            print("Added '" + word + "' to the database")
        else:
            print("Found '" + word + "' in the database")
            result = self.cursor.fetchall()
            for row in result:
                print(row)
            change = input("Change '" + word + "' to: ")
            sql = "UPDATE dictionary.word SET word = %s WHERE word = %s"
            entry = (change, word)
            self.cursor.execute(sql, entry)
            self.db.commit()
            print("Changed '" + word + "' to '" + change + "' in the database")


def main():
    db = Database()
    mydb = MyDB(db)
    mydb.add_or_change_a_word()


if __name__ == "__main__":
    main()
