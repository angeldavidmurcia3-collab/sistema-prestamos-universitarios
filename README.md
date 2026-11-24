# Sistema de Prestamos Universitarios

## Descripcion
Aplicacion de consola desarrollada en Python para gestionar estudiantes, equipos y prestamos de computadores portatiles y proyectores de una universidad.

## Funcionalidades
- Registrar estudiantes.
- Consultar estudiantes.
- Registrar equipos.
- Consultar equipos.
- Registrar prestamos.
- Devolver equipos.
- Consultar equipos disponibles.
- Consultar equipos prestados.

## Tecnologias
- Python
- SQLite
- Pytest
- OpenSpec
- Git y GitHub

## Ejecucion
Activar el entorno virtual:

    .\.venv\Scripts\Activate.ps1

Ejecutar el programa:

    python -m src.main

## Pruebas
Ejecutar:

    pytest -v

Resultado: 12 pruebas aprobadas.

## Metodologias

### SDD
Se definieron la propuesta, especificaciones, diseño y tareas mediante OpenSpec antes de implementar las funcionalidades.

### TDD
Se utilizaron pruebas automatizadas con pytest siguiendo el ciclo Red, Green y Refactor.

## Base de datos
SQLite almacena la informacion de estudiantes, equipos y prestamos.
