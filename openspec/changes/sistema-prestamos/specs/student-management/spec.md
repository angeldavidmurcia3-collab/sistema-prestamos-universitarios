# Spec Delta

## Purpose

Esta capacidad permite registrar y consultar los estudiantes de la universidad que pueden solicitar el préstamo de computadores portátiles y proyectores, manteniendo su información organizada y evitando registros duplicados.

## ADDED Requirements

### Requirement: Registrar estudiantes

El sistema DEBE permitir registrar estudiantes con número de identificación, nombre completo y datos de contacto.

#### Scenario: Registro exitoso de un estudiante

- **WHEN** el encargado ingresa una identificación, nombre y datos de contacto válidos que no están registrados
- **THEN** el sistema registra al estudiante y confirma que la operación fue exitosa.

#### Scenario: Registro con identificación duplicada

- **WHEN** el encargado intenta registrar un estudiante con una identificación que ya existe
- **THEN** el sistema rechaza el registro e informa que el estudiante ya está registrado.

#### Scenario: Registro con datos obligatorios vacíos

- **WHEN** el encargado intenta registrar un estudiante sin identificación o sin nombre
- **THEN** el sistema rechaza el registro e indica cuáles datos son obligatorios.

### Requirement: Consultar estudiantes registrados

El sistema DEBE permitir consultar la información de los estudiantes registrados mediante su número de identificación.

#### Scenario: Consultar un estudiante existente

- **WHEN** el encargado busca un número de identificación registrado
- **THEN** el sistema muestra la información correspondiente al estudiante.

#### Scenario: Consultar un estudiante inexistente

- **WHEN** el encargado busca un número de identificación que no está registrado
- **THEN** el sistema informa que no se encontró ningún estudiante.