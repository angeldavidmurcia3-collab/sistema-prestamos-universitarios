
from datetime import date


def registrar_prestamo(
    conexion,
    identificacion_estudiante,
    codigo_equipo,
    fecha_prestamo,
    fecha_devolucion_esperada
):
    """Registra un préstamo si el estudiante y el equipo son válidos."""

    estudiante = conexion.execute(
        "SELECT identificacion FROM estudiantes WHERE identificacion = ?",
        (identificacion_estudiante,)
    ).fetchone()

    if estudiante is None:
        return False

    equipo = conexion.execute(
        "SELECT estado FROM equipos WHERE codigo = ?",
        (codigo_equipo,)
    ).fetchone()

    if equipo is None or equipo[0] != "DISPONIBLE":
        return False

    try:
        conexion.execute(
            """
            INSERT INTO prestamos (
                identificacion_estudiante,
                codigo_equipo,
                fecha_prestamo,
                fecha_devolucion_esperada,
                estado
            )
            VALUES (?, ?, ?, ?, 'ACTIVO')
            """,
            (
                identificacion_estudiante,
                codigo_equipo,
                fecha_prestamo,
                fecha_devolucion_esperada
            )
        )

        conexion.execute(
            "UPDATE equipos SET estado = 'PRESTADO' WHERE codigo = ?",
            (codigo_equipo,)
        )

        conexion.commit()
        return True

    except Exception:
        conexion.rollback()
        return False


def devolver_equipo(conexion, codigo_equipo, fecha_devolucion_real):
    """Registra la devolución de un equipo prestado."""

    prestamo = conexion.execute(
        """
        SELECT id FROM prestamos
        WHERE codigo_equipo = ? AND estado = 'ACTIVO'
        """,
        (codigo_equipo,)
    ).fetchone()

    if prestamo is None:
        return False

    conexion.execute(
        """
        UPDATE prestamos
        SET fecha_devolucion_real = ?, estado = 'DEVUELTO'
        WHERE id = ?
        """,
        (fecha_devolucion_real, prestamo[0])
    )

    conexion.execute(
        "UPDATE equipos SET estado = 'DISPONIBLE' WHERE codigo = ?",
        (codigo_equipo,)
    )

    conexion.commit()
    return True
