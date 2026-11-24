# Propuesta

## ¿Por qué?

Actualmente, la gestión del préstamo de computadores portátiles y proyectores de la universidad puede presentar dificultades cuando se realiza mediante registros manuales o archivos independientes. Esto puede ocasionar duplicidad de solicitudes, falta de información actualizada sobre la disponibilidad de los equipos y dificultades para controlar las fechas de devolución.

Por esta razón, se propone desarrollar un sistema en Python que permita organizar y controlar el préstamo de los equipos tecnológicos, facilitando el registro de estudiantes, equipos, préstamos y devoluciones.

## ¿Qué cambios se realizarán?

- Implementar el registro de estudiantes con identificación y datos básicos.
- Implementar el registro de computadores portátiles y proyectores con código único, tipo, descripción y estado.
- Permitir consultar los equipos disponibles para préstamo.
- Registrar préstamos únicamente a estudiantes registrados y para equipos disponibles.
- Evitar que un mismo equipo tenga dos préstamos activos al mismo tiempo.
- Registrar la fecha del préstamo y la fecha prevista de devolución.
- Registrar la devolución y actualizar automáticamente el estado del equipo.
- Permitir consultar los equipos prestados y su historial de movimientos.
- Almacenar la información para conservar los registros cuando el programa se cierre.

## Capacidades

### Nuevas capacidades

- `student-management`: Permite registrar, consultar y validar la información de los estudiantes.
- `equipment-management`: Permite registrar, consultar y controlar el estado de los computadores portátiles y proyectores.
- `loan-management`: Permite gestionar los préstamos, las devoluciones, la disponibilidad y el historial de movimientos.

### Capacidades modificadas

No aplica, porque el proyecto no cuenta con especificaciones anteriores.

## Impacto

- **Lenguaje de programación:** Python.
- **Entorno de desarrollo:** Visual Studio Code.
- **Base de datos:** SQLite, para almacenar la información de estudiantes, equipos y préstamos.
- **Pruebas:** pytest, para verificar el correcto funcionamiento de las funcionalidades.
- **Metodología de desarrollo:** SDD mediante OpenSpec para definir las especificaciones del sistema y TDD mediante pruebas antes de implementar cada funcionalidad.
- **Usuarios involucrados:** estudiantes y personal encargado de administrar los préstamos de equipos tecnológicos.
- **Componentes del proyecto:** módulos de estudiantes, equipos, préstamos, base de datos y pruebas automatizadas.