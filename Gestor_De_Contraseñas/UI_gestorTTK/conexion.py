import sqlite3


# clase principal de manejar la informacion de las credenciales de la base de datos Credenciales.db

class DataBase:


    def conectar(self, database) -> None:

        conexion = sqlite3.connect(f"{database}.db")
        conexion.close()


    def get_num_tablas(self, database) :

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()
        cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
        self.tablas = [name[0] for name in cursor.fetchall()]
        conexion.close()
        return self.tablas


    def crear_tabla(self, database, sentencia_sql):

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql) 
        conexion.commit()
        conexion.close()


    def write(self, database, datos, sentencia_sql):

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()


    def read(self, database, sentencia_sql):

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()

        cursor.execute(sentencia_sql)
        contenido = cursor.fetchall()

        conexion.commit()
        conexion.close()
        return contenido


    def ultimo_id(self, database, nameTabla):

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()
        cursor.execute(
            f"SELECT ID FROM {nameTabla!r} WHERE ID=(SELECT MAX(ID) FROM {nameTabla!r})")
        idmax = cursor.fetchone()
        conexion.close()
        return 1 if idmax is None else idmax[0] + 1

    
    def get_name_users(self, nameTabla, database) :

        conexion = sqlite3.connect(f'{database}.db')
        cursor = conexion.cursor()
        cursor.execute(f'SELECT usuario FROM {nameTabla!r}')
        usuarios = cursor.fetchall()
        conexion.close()
        return usuarios

    
    def comprobar_login(self, database, nameTabla, usuario) :

        conexion = sqlite3.connect(f'{database}.db')
        cursor = conexion.cursor()
        cursor.execute(f'SELECT password FROM {nameTabla!r} WHERE usuario=?', (usuario, ))
        existe = cursor.fetchone()
        conexion.close()
        return existe


    def update(self, database, datos, sentencia_sql):

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql, datos)
        conexion.commit()
        conexion.close()


    def delete(self, database, ids, sentencia_sql):

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()

        for iid in ids:
            cursor.execute(sentencia_sql)

        conexion.commit()
        conexion.close()


    def deleteTabla(self, database, sentencia_sql):

        conexion = sqlite3.connect(f"{database}.db")
        cursor = conexion.cursor()
        cursor.execute(sentencia_sql)
        conexion.commit()
        conexion.close()
