
from src.database import conectar, crear_tablas
from src.equipos import registrar_equipo, consultar_equipos


def preparar_bd():
    conexion = conectar(":memory:")
    crear_tablas(conexion)
    return conexion


def test_registrar_equipo():
    conexion = preparar_bd()

    resultado = registrar_equipo(
        conexion, "PC001", "PORTATIL", "Computador Dell"
    )

    assert resultado is True

    conexion.close()


def test_no_permitir_codigo_duplicado():
    conexion = preparar_bd()

    registrar_equipo(
        conexion, "PC001", "PORTATIL", "Computador Dell"
    )

    resultado = registrar_equipo(
        conexion, "PC001", "PROYECTOR", "Video beam"
    )

    assert resultado is False

    conexion.close()


def test_consultar_equipos():
    conexion = preparar_bd()

    registrar_equipo(
        conexion, "PC001", "PORTATIL", "Computador Dell"
    )

    equipos = consultar_equipos(conexion)

    assert len(equipos) == 1
    assert equipos[0][0] == "PC001"
    assert equipos[0][3] == "DISPONIBLE"

    conexion.close()
