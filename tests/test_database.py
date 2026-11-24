
from src.database import conectar, crear_tablas


def test_conexion_base_datos():
    conexion = conectar(":memory:")

    assert conexion is not None

    conexion.close()


def test_crear_tablas():
    conexion = conectar(":memory:")

    crear_tablas(conexion)

    cursor = conexion.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )

    tablas = [fila[0] for fila in cursor.fetchall()]

    assert "estudiantes" in tablas
    assert "equipos" in tablas
    assert "prestamos" in tablas

    conexion.close()
