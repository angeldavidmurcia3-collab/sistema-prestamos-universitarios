
# Spec Delta

## Purpose

Definir las reglas para realizar préstamos y devoluciones de equipos universitarios.

## ADDED Requirements

### Requirement: Registrar préstamos

El sistema MUST permitir prestar equipos disponibles únicamente a estudiantes registrados.

#### Scenario: Préstamo correcto

- WHEN un estudiante registrado solicita un equipo disponible
- THEN el sistema registra el préstamo y cambia el equipo a PRESTADO

#### Scenario: Equipo no disponible

- WHEN se solicita un equipo que ya está prestado
- THEN el sistema rechaza el préstamo

#### Scenario: Estudiante no registrado

- WHEN una persona no registrada solicita un préstamo
- THEN el sistema rechaza la solicitud

### Requirement: Registrar devoluciones

El sistema MUST permitir devolver equipos que tengan un préstamo activo.

#### Scenario: Devolución correcta

- WHEN se devuelve un equipo prestado
- THEN se registra la fecha de devolución y el equipo vuelve a DISPONIBLE
