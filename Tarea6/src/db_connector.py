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
        self.list_data = []
        self.insert = "INSERT INTO `chess_card`.`tarjetas` (`id`, `nombre_tarjeta`, `tarjeta`, `posicion`, `temal`) VALUES ('%s', '%s', '%s', '%s', '%s');"
        self.edit = "UPDATE `chess_card`.`tarjetas` SET `nombre_tarjeta`='%s', `tarjeta`='%s', `posicion`='%s', `temal`='%s' WHERE `id`='%s';"
        self.delet = "DELETE FROM `chess_card`.`tarjetas` WHERE `id`='%s';"

    def connect(self):
        savequery = "select * from tarjetas"
        try: 
            self.cursor.execute(savequery) 
            self.list_data = self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
            self.db.rollback() 
        
    def insertar(self, id, nombre, tarjeta, posicion, tema):
        try: 
            command = self.insert % (id, nombre, tarjeta, tema, posicion)
            print("comnad: " + command)
            self.cursor.execute(command)
            self.db.commit()
            self.connect()
            return True
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
            self.db.rollback() 

    def editar(self, id, nombre, tarjeta, posicion, tema):
        try: 
            command = self.edit % (nombre, tarjeta, tema, posicion, id)
            print("comnad: " + command)
            self.cursor.execute(command)
            self.db.commit()
            self.connect()
            return True
        except mysql.connector.Error as error:
            print("Failed to edit into MySQL table {}".format(error))
            self.db.rollback() 

    def borrar(self, id):
        try: 
            command = self.delet % (id)
            print("comnad: " + command)
            self.cursor.execute(command)
            self.db.commit()
            self.connect()
            return True
        except mysql.connector.Error as error:
            print("Failed to edit into MySQL table {}".format(error))
            self.db.rollback() 

    