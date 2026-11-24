
import sqlite3


def registrar_equipo(conexion, codigo, tipo, descripcion=""):
    """Registra un computador o proyector."""

    codigo = codigo.strip().upper()
    tipo = tipo.strip().upper()

    if not codigo or tipo not in ("PORTATIL", "PROYECTOR"):
        return False

    try:
        conexion.execute(
            """
            INSERT INTO equipos (codigo, tipo, descripcion, estado)
            VALUES (?, ?, ?, 'DISPONIBLE')
            """,
            (codigo, tipo, descripcion)
        )

        conexion.commit()
        return True

    except sqlite3.IntegrityError:
        return False


def consultar_equipos(conexion):
    """Consulta todos los equipos registrados."""

    cursor = conexion.execute(
        """
        SELECT codigo, tipo, descripcion, estado
        FROM equipos
        ORDER BY codigo
        """
    )

    return cursor.fetchall()
