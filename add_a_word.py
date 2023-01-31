import mysql.connector

class Database:
    def __init__(self) -> None:
        self.hostname = input("What host to connect to (localhost): ")
        self.port = input("What port to connect to (3306): ")
        self.user = input("What user to connect with (root): ")
        self.password = input("What password to connect with: ")
    
class MyDB:
    def __init__(self, db: Database):
        try:
            res = mysql.connector.connect(
                host = str(db.hostname),
                user = str(db.user),
                password = str(db.password)
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
            exit

    def add_or_change_a_word(self):
        word = input("What word do you want to add/change: ")
        sql = "SELECT * FROM dictionary.word WHERE word = %s"
        entry = (word, )
        self.cursor.execute(sql, entry)
        if self.cursor.rowcount == 0:
            print("The word '" + word +"' was not found... adding")
            sql = "INSERT INTO dictrionary.word (word) VALUES (%s)"
            entry = (word, )
            self.cursor.execute(sql, entry)
            self.db.commit()
            print("Added '" + word + "' to the database")
        else:
            print("Found '" + word +"' in the database")
            result = self.cursor.fetchall()
            for row in result:
                print(row)
            


def main():
    db = Database()
    mydb = MyDB(db)

if __name__ == "__main__":
    main()


