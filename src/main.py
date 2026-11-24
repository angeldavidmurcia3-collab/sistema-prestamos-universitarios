
from datetime import date

from src.database import conectar, crear_tablas
from src.estudiantes import registrar_estudiante, consultar_estudiantes
from src.equipos import registrar_equipo, consultar_equipos
from src.prestamos import registrar_prestamo, devolver_equipo


def mostrar_menu():
    print("\n===== SISTEMA DE PRESTAMOS UNIVERSITARIOS =====")
    print("1. Registrar estudiante")
    print("2. Consultar estudiantes")
    print("3. Registrar equipo")
    print("4. Consultar equipos")
    print("5. Registrar prestamo")
    print("6. Devolver equipo")
    print("7. Consultar equipos disponibles")
    print("8. Consultar equipos prestados")
    print("0. Salir")


def ejecutar():
    conexion = conectar("prestamos.db")
    crear_tablas(conexion)

    try:
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                identificacion = input("Identificacion: ")
                nombre = input("Nombre: ")
                contacto = input("Contacto: ")

                if registrar_estudiante(
                    conexion, identificacion, nombre, contacto
                ):
                    print("Estudiante registrado correctamente.")
                else:
                    print("No se pudo registrar. Verifique los datos.")

            elif opcion == "2":
                estudiantes = consultar_estudiantes(conexion)

                print("\n--- ESTUDIANTES REGISTRADOS ---")
                for estudiante in estudiantes:
                    print(estudiante)

                if not estudiantes:
                    print("No hay estudiantes registrados.")

            elif opcion == "3":
                codigo = input("Codigo del equipo: ")
                tipo = input("Tipo (PORTATIL o PROYECTOR): ")
                descripcion = input("Descripcion: ")

                if registrar_equipo(conexion, codigo, tipo, descripcion):
                    print("Equipo registrado correctamente.")
                else:
                    print("No se pudo registrar. Revise el codigo y el tipo.")

            elif opcion == "4":
                equipos = consultar_equipos(conexion)

                print("\n--- EQUIPOS REGISTRADOS ---")
                for equipo in equipos:
                    print(equipo)

                if not equipos:
                    print("No hay equipos registrados.")

            elif opcion == "5":
                identificacion = input("Identificacion del estudiante: ")
                codigo = input("Codigo del equipo: ")
                fecha_prestamo = date.today().isoformat()
                fecha_esperada = input(
                    "Fecha esperada de devolucion (AAAA-MM-DD): "
                )

                resultado = registrar_prestamo(
                    conexion,
                    identificacion,
                    codigo,
                    fecha_prestamo,
                    fecha_esperada
                )

                if resultado:
                    print("Prestamo registrado correctamente.")
                else:
                    print("Prestamo rechazado. Verifique estudiante y equipo.")

            elif opcion == "6":
                codigo = input("Codigo del equipo que se devuelve: ")
                fecha_real = date.today().isoformat()

                if devolver_equipo(conexion, codigo, fecha_real):
                    print("Devolucion registrada correctamente.")
                else:
                    print("No se encontro un prestamo activo para ese equipo.")

            elif opcion == "7":
                equipos = conexion.execute(
                    """
                    SELECT codigo, tipo, descripcion, estado
                    FROM equipos
                    WHERE estado = 'DISPONIBLE'
                    """
                ).fetchall()

                print("\n--- EQUIPOS DISPONIBLES ---")
                for equipo in equipos:
                    print(equipo)

                if not equipos:
                    print("No hay equipos disponibles.")

            elif opcion == "8":
                equipos = conexion.execute(
                    """
                    SELECT codigo, tipo, descripcion, estado
                    FROM equipos
                    WHERE estado = 'PRESTADO'
                    """
                ).fetchall()

                print("\n--- EQUIPOS PRESTADOS ---")
                for equipo in equipos:
                    print(equipo)

                if not equipos:
                    print("No hay equipos prestados.")

            elif opcion == "0":
                print("Gracias por utilizar el sistema.")
                break

            else:
                print("Opcion no valida. Intente nuevamente.")

    finally:
        conexion.close()


if __name__ == "__main__":
    ejecutar()
