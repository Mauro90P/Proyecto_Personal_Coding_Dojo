import re
import os
from app.config.mysqlconnection import connectToMySQL
from flask import flash

SEGURA_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$')

import re

class Job:
    def __init__(self, data):
        self.id = data.get('id', 0)
        self.nombre_tarea = data.get('nombre_tarea')
        self.descripcion = data.get('descripcion')
        self.tiempo_inicio = data.get('tiempo_inicio')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at','')
        self.usuarios_id = data.get('usuarios_id')
        self.timepo_total = data.get('timepo_total')
        self.tiempo_terminado = data.get('tiempo_terminado')
  
    def crear(self):
        sql = """
       INSERT INTO tareas 
        (nombre_tarea, descripcion, tiempo_inicio, created_at, updated_at, usuarios_id, timepo_total, tiempo_terminado) 
        VALUES (%(nombre_tarea)s,%(descripcion)s,NOW(),NOW(),NOW(),%(usuarios_id)s,%(timepo_total)s,%(tiempo_terminado)s);
        """
        data = {
            'nombre_tarea': self.nombre_tarea,
            'descripcion': self.descripcion,
        }
        self.id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return self

    @classmethod
    def save(cls, data):
        sql = "INSERT INTO tareas (nombre_tarea,descripcion,usuarios_id) VALUES (%(nombre_tarea)s,%(descripcion)s,%(usuarios_id)s);"
        # id = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        # print("ID:", id)
        # resultado = None
        # if id:
        #     resultado = cls.get(id)
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

    @classmethod
    def get(cls,data):
        sql = """ 
       SELECT tareas.id,nombre_tarea, descripcion FROM tareas INNER JOIN usuarios ON usuarios.id = tareas.usuarios_id WHERE usuarios_id = %(usuarios_id)s;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        todos_los_datos = []

        sql = """
         SELECT id, nombre_tarea, descripcion FROM tareas WHERE tiempo_inicio IS NULL;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql)
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos

    @classmethod
    def get_my_job(cls):
        """Obtener tus tareas del usuario logueado que no están NULL."""

        todos_los_datos = []
        sql = """
        SELECT nombre_tarea, descripcion, tiempo_inicio,tiempo_terminado, timepo_total
        FROM tareas WHERE tiempo_inicio IS NOT NULL;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql)
        print(result)
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos

    @classmethod
    def get_otros_job(cls,data):
        todos_los_datos = []
        sql = """
         SELECT jobs.id,titulo, descripcion,location,creador_job,usuario_id FROM jobs INNER JOIN usuarios ON usuarios.id = jobs.creador_job WHERE creador_job != %(usaurio_id)s;
        """
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql,data)
        for fila in result:
            instancia = cls(fila)
            todos_los_datos.append(instancia)
        return todos_los_datos

    @classmethod
    def get_by_email(cls, email):
        sql = """
        SELECT id, email, password, nombre FROM usuarios where email = %(email)s;
        """
        data = {
            'email': email
        }
        result = connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)

        if result:
            return cls(result[0])

        return None
    
    @classmethod
    def delete(cls, data):
        """Elimina una tarea de la base de datos. """

        sql = """
        DELETE FROM tareas WHERE id = %(id)s;
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql, data)
    
    @staticmethod
    def update(data):
        sql = """
        UPDATE tareas SET nombre_tarea = %(nombre_tarea)s, descripcion = %(descripcion)s WHERE id = %(id)s;
        """
        return connectToMySQL(os.getenv("BASE_DE_DATOS")).query_db(sql,data)
