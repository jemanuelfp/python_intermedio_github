

class MyPostgreSqlConn:
    def __init__(self, bd, user, password, host='127.0.0.1'):
        self.bd = bd
        self.user = user
        self.password = password
        self.host = host

    def connect(self):
        if(self.bd and self.user and self.password):
            print(f"Conectada a la base de datos {self.bd}")

    def execute(self, query):
        print("Ejecutando en la base de datos")
        print(query)

conection = MyPostgreSqlConn("python_intermedio_bd", "postgres", "root")

conection.connect()

conection.execute()

lista_ids = [15,20,30] #estos se borraran

for id in lista_ids:
    conection.execute(f"Delete from usuario where id = {id}")

