import mysql.connector

class Db_connector():
    def __init__(self) :
        self.user = 'root_escuela'
        self.password = '&d{p~}i!anConN=^u?)?8vM3.!fd1u*3mGE%w$f/1QXi8a@NsTjW-4#[K*]l'
        self.db = mysql.connector.connect(host ="db4free.net", 
                                     port = '3306',
                                     user = self.user, 
                                     password = self.password, 
                                     db ="chess_card") 
        self.cursor = self.db.cursor()

    def connect(self):
        savequery = "select * from tarjetas"
        try: 
            self.cursor.execute(savequery) 
            myresult = self.cursor.fetchall()       
            # Printing the result of the 
            # query 
            for x in myresult: 
                print(x) 
            print("Query Excecuted successfully") 
        except: 
            self.db.rollback() 
            print("Error occured")