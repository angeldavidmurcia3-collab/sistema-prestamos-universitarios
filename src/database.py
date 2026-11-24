

import sqlite3


def conectar(nombre_bd="prestamos.db"):
    """Crea y devuelve una conexión con SQLite."""
    conexion = sqlite3.connect(nombre_bd)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def crear_tablas(conexion):
    """Crea las tablas necesarias para gestionar los préstamos."""

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            identificacion TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            contacto TEXT
        )
    """)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS equipos (
            codigo TEXT PRIMARY KEY,
            tipo TEXT NOT NULL,
            descripcion TEXT,
            estado TEXT NOT NULL DEFAULT 'DISPONIBLE'
        )
    """)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            identificacion_estudiante TEXT NOT NULL,
            codigo_equipo TEXT NOT NULL,
            fecha_prestamo TEXT NOT NULL,
            fecha_devolucion_esperada TEXT NOT NULL,
            fecha_devolucion_real TEXT,
            estado TEXT NOT NULL DEFAULT 'ACTIVO',
            FOREIGN KEY (identificacion_estudiante)
                REFERENCES estudiantes(identificacion),
            FOREIGN KEY (codigo_equipo)
                REFERENCES equipos(codigo)
        )
    """)

    conexion.commit()
