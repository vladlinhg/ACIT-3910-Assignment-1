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
        
        except mysql.connector.Error as err:
            print("Could not login to host with user/password provided.")
            print("Exiting.")
            exit
    def add_or_change_a_word(self):
        word = input("What word do you want to add/change: ")
        sql = ""
        self.db.cursor







db = Database()
mydb = MyDB(db)


