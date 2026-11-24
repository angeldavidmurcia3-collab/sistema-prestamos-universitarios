
from src.database import conectar, crear_tablas
from src.estudiantes import registrar_estudiante, consultar_estudiantes


def preparar_bd():
    conexion = conectar(":memory:")
    crear_tablas(conexion)
    return conexion


def test_registrar_estudiante():
    conexion = preparar_bd()

    resultado = registrar_estudiante(
        conexion, "12345", "Ana Perez", "3001234567"
    )

    assert resultado is True
    conexion.close()


def test_no_permitir_identificacion_duplicada():
    conexion = preparar_bd()

    registrar_estudiante(
        conexion, "12345", "Ana Perez", "3001234567"
    )

    resultado = registrar_estudiante(
        conexion, "12345", "Luis Gomez", "3101234567"
    )

    assert resultado is False
    conexion.close()


def test_consultar_estudiantes():
    conexion = preparar_bd()

    registrar_estudiante(
        conexion, "12345", "Ana Perez", "3001234567"
    )

    estudiantes = consultar_estudiantes(conexion)

    assert len(estudiantes) == 1
    assert estudiantes[0][0] == "12345"

    conexion.close()
