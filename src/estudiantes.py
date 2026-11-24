
import sqlite3


def registrar_estudiante(conexion, identificacion, nombre, contacto=""):
    identificacion = identificacion.strip()
    nombre = nombre.strip()

    if not identificacion or not nombre:
        return False

    try:
        conexion.execute(
            """
            INSERT INTO estudiantes
            (identificacion, nombre, contacto)
            VALUES (?, ?, ?)
            """,
            (identificacion, nombre, contacto)
        )
        conexion.commit()
        return True

    except sqlite3.IntegrityError:
        return False


def consultar_estudiantes(conexion):
    cursor = conexion.execute(
        """
        SELECT identificacion, nombre, contacto
        FROM estudiantes
        ORDER BY nombre
        """
    )
    return cursor.fetchall()
