# Design

## Context

El proyecto se desarrollará como una aplicación de consola utilizando Python. La información de estudiantes, equipos y préstamos se almacenará en una base de datos SQLite.

La solución se organizará en módulos independientes para facilitar el mantenimiento, las pruebas y la comprensión del código.

La motivación y el alcance general se describen en `proposal.md`. Los comportamientos esperados se encuentran en las especificaciones del proyecto.

## Goals / Non-Goals

**Goals:**

- Implementar una arquitectura modular y sencilla.
- Separar la lógica de estudiantes, equipos y préstamos.
- Utilizar SQLite para conservar la información.
- Validar los datos antes de registrar operaciones.
- Permitir realizar pruebas automatizadas con pytest.
- Mantener el código organizado para facilitar futuras mejoras.

**Non-Goals:**

- No desarrollar una aplicación web.
- No implementar una aplicación móvil.
- No integrar sistemas externos de autenticación.
- No implementar pagos ni cobros por préstamos.

## Decisions

### 1. Lenguaje de programación

Se utilizará Python porque permite desarrollar aplicaciones de consola de forma sencilla y cuenta con herramientas para realizar pruebas automatizadas.

Alternativa considerada: Java. Se selecciona Python por su facilidad de aprendizaje y rapidez de desarrollo.

### 2. Base de datos

Se utilizará SQLite para almacenar estudiantes, equipos y préstamos. Esta base de datos permite guardar la información en un archivo local sin instalar un servidor adicional.

Alternativa considerada: MySQL. Se selecciona SQLite porque el proyecto es académico y no necesita una base de datos centralizada.

### 3. Arquitectura modular

El programa se dividirá en los siguientes módulos:

- `main.py`: menú principal y comunicación con el usuario.
- `estudiantes.py`: registro y consulta de estudiantes.
- `equipos.py`: registro, consulta y disponibilidad de equipos.
- `prestamos.py`: creación, consulta y devolución de préstamos.
- `database.py`: conexión y operaciones con SQLite.

### 4. Modelo de datos

La base de datos tendrá tres tablas principales:

- **Estudiantes:** identificación, nombre y datos de contacto.
- **Equipos:** código, tipo, descripción y estado.
- **Préstamos:** estudiante, equipo, fecha de préstamo, fecha prevista de devolución, fecha real de devolución y estado.

Se utilizarán identificadores y relaciones entre tablas para mantener la integridad de la información.

### 5. Pruebas

Se utilizará pytest para comprobar el funcionamiento de los módulos. Las pruebas se crearán antes de implementar cada funcionalidad, siguiendo el ciclo TDD: Red, Green y Refactor.

Las especificaciones de OpenSpec servirán como guía para verificar que el comportamiento desarrollado cumpla los requisitos.

## Risks / Trade-offs

- **Pérdida o daño del archivo de base de datos** → Realizar copias de seguridad periódicas.
- **Registro de datos incorrectos** → Implementar validaciones antes de guardar la información.
- **Préstamos duplicados del mismo equipo** → Verificar su disponibilidad antes de autorizar un préstamo.
- **Errores durante el desarrollo** → Utilizar pruebas automatizadas con pytest.

## Migration Plan

1. Crear la estructura de carpetas y módulos del proyecto.
2. Configurar la base de datos SQLite y sus tablas.
3. Implementar las funciones de estudiantes.
4. Implementar las funciones de equipos.
5. Implementar los préstamos y las devoluciones.
6. Crear y ejecutar las pruebas automatizadas con pytest.
7. Corregir errores y verificar el funcionamiento completo.
8. Documentar el proyecto y publicarlo en GitHub.

Para revertir una versión con errores, se podrá recuperar una copia de seguridad de la base de datos y volver a la versión anterior del código.

## Open Questions

No hay preguntas pendientes que impidan iniciar la implementación.