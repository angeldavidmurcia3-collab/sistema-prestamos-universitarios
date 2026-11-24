
# Spec Delta

## Purpose

Definir el registro y la consulta de los equipos de la universidad.

## ADDED Requirements

### Requirement: Registrar equipos

El sistema MUST permitir registrar computadores portátiles y proyectores con un código único.

#### Scenario: Registro correcto

- WHEN se registra un equipo con código y tipo válidos
- THEN el equipo queda guardado con estado DISPONIBLE

#### Scenario: Código duplicado

- WHEN se registra un equipo con un código que ya existe
- THEN el sistema rechaza el registro

### Requirement: Consultar equipos

El sistema MUST permitir consultar los equipos registrados y su estado.

#### Scenario: Consulta de equipos

- WHEN se solicita consultar los equipos
- THEN el sistema muestra los equipos registrados con sus datos y estado
