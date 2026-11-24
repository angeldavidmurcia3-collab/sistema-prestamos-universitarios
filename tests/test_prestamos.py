
from src.database import conectar, crear_tablas
from src.estudiantes import registrar_estudiante
from src.equipos import registrar_equipo
from src.prestamos import registrar_prestamo, devolver_equipo


def preparar_bd():
    conexion = conectar(":memory:")
    crear_tablas(conexion)

    registrar_estudiante(
        conexion, "12345", "Ana Perez", "3001234567"
    )

    registrar_equipo(
        conexion, "PC001", "PORTATIL", "Computador Dell"
    )

    return conexion


def test_registrar_prestamo():
    conexion = preparar_bd()

    resultado = registrar_prestamo(
        conexion, "12345", "PC001",
        "2026-11-24", "2026-11-30"
    )

    assert resultado is True

    estado = conexion.execute(
        "SELECT estado FROM equipos WHERE codigo = 'PC001'"
    ).fetchone()

    assert estado[0] == "PRESTADO"
    conexion.close()


def test_no_prestar_equipo_ya_prestado():
    conexion = preparar_bd()

    registrar_prestamo(
        conexion, "12345", "PC001",
        "2026-11-24", "2026-11-30"
    )

    resultado = registrar_prestamo(
        conexion, "12345", "PC001",
        "2026-11-24", "2026-11-30"
    )

    assert resultado is False
    conexion.close()


def test_no_prestar_a_estudiante_no_registrado():
    conexion = preparar_bd()

    resultado = registrar_prestamo(
        conexion, "99999", "PC001",
        "2026-11-24", "2026-11-30"
    )

    assert resultado is False
    conexion.close()


def test_devolver_equipo():
    conexion = preparar_bd()

    registrar_prestamo(
        conexion, "12345", "PC001",
        "2026-11-24", "2026-11-30"
    )

    resultado = devolver_equipo(
        conexion, "PC001", "2026-11-25"
    )

    assert resultado is True

    estado = conexion.execute(
        "SELECT estado FROM equipos WHERE codigo = 'PC001'"
    ).fetchone()

    assert estado[0] == "DISPONIBLE"
    conexion.close()
def test_consultar_prestamos_activos():
    conexion = preparar_bd()

    registrar_prestamo(
        conexion, "12345", "PC001",
        "2026-11-24", "2026-11-30"
    )

    prestamos = conexion.execute("""
        SELECT identificacion_estudiante, codigo_equipo, estado
        FROM prestamos
        WHERE estado = 'ACTIVO'
    """).fetchall()

    assert len(prestamos) == 1
    assert prestamos[0][0] == "12345"
    assert prestamos[0][1] == "PC001"
    assert prestamos[0][2] == "ACTIVO"

    conexion.close()


def test_consultar_historial_prestamos():
    conexion = preparar_bd()

    registrar_prestamo(
        conexion, "12345", "PC001",
        "2026-11-24", "2026-11-30"
    )

    devolver_equipo(conexion, "PC001", "2026-11-25")

    historial = conexion.execute("""
        SELECT codigo_equipo, estado, fecha_devolucion_real
        FROM prestamos
    """).fetchall()

    assert len(historial) == 1
    assert historial[0][0] == "PC001"
    assert historial[0][1] == "DEVUELTO"
    assert historial[0][2] == "2026-11-25"

    conexion.close()