# Tasks

## 1. PreparaciÃ³n del proyecto

- [x] 1.1 Crear la estructura de carpetas y mÃ³dulos de Python y verificar que todos los archivos estÃ©n ubicados correctamente.
- [x] 1.2 Crear y configurar el entorno virtual de Python y verificar que se active correctamente.
- [x] 1.3 Instalar pytest y verificar su instalaciÃ³n ejecutando `pytest --version`.
- [x] 1.4 Crear el archivo `requirements.txt` y comprobar que contiene las dependencias necesarias.

## 2. Base de datos

- [x] 2.1 Crear el mÃ³dulo `database.py` y configurar la conexiÃ³n con SQLite; verificar que la conexiÃ³n se realice correctamente.
- [x] 2.2 Crear las tablas de estudiantes, equipos y prÃ©stamos; verificar que existan en la base de datos.
- [x] 2.3 Implementar pruebas para la creaciÃ³n y conexiÃ³n de la base de datos; verificar que todas pasen con pytest.

## 3. GestiÃ³n de estudiantes

- [ ] 3.1 Crear las pruebas para registrar estudiantes, validar campos obligatorios y evitar identificaciones duplicadas; comprobar que inicialmente fallen.
- [x] 3.2 Implementar el registro de estudiantes en `estudiantes.py`; ejecutar las pruebas y comprobar que pasen.
- [ ] 3.3 Crear pruebas para consultar estudiantes existentes e inexistentes; comprobar los resultados esperados.
- [x] 3.4 Implementar la consulta de estudiantes y verificar su funcionamiento con pytest.

## 4. GestiÃ³n de equipos

- [ ] 4.1 Crear pruebas para registrar equipos y evitar cÃ³digos duplicados; comprobar que inicialmente fallen.
- [x] 4.2 Implementar el registro de portÃ¡tiles y proyectores en `equipos.py`; verificar que las pruebas pasen.
- [ ] 4.3 Crear pruebas para consultar equipos y comprobar su disponibilidad.
- [x] 4.4 Implementar las consultas y actualizaciÃ³n del estado de los equipos; verificar con pytest.

## 5. GestiÃ³n de prÃ©stamos y devoluciones

- [ ] 5.1 Crear pruebas para permitir prÃ©stamos Ãºnicamente a estudiantes registrados y con equipos disponibles; comprobar que inicialmente fallen.
- [x] 5.2 Implementar el registro de prÃ©stamos en `prestamos.py`; verificar que las pruebas pasen.
- [ ] 5.3 Crear pruebas para impedir prÃ©stamos duplicados del mismo equipo y registrar correctamente las fechas.
- [x] 5.4 Implementar las validaciones de prÃ©stamos y verificar los resultados con pytest.
- [ ] 5.5 Crear pruebas para registrar devoluciones y actualizar el estado del equipo.
- [x] 5.6 Implementar las devoluciones y verificar que el equipo vuelva a estar disponible cuando corresponda.
- [ ] 5.7 Implementar la consulta de prÃ©stamos activos e historial y verificar los resultados.

## 6. MenÃº e integraciÃ³n

- [x] 6.1 Crear `main.py` con un menÃº de opciones para gestionar estudiantes, equipos, prÃ©stamos y devoluciones; verificar que se muestre correctamente.
- [x] 6.2 Conectar el menÃº con los mÃ³dulos del sistema y comprobar que las operaciones funcionen desde la aplicaciÃ³n.
- [ ] 6.3 Validar las entradas del usuario y mostrar mensajes claros ante datos incorrectos; comprobar los casos de error.

## 7. VerificaciÃ³n y documentaciÃ³n

- [x] 7.1 Ejecutar todas las pruebas con `pytest` y verificar que finalicen correctamente.
- [x] 7.2 Realizar una prueba completa del flujo de registro, prÃ©stamo, consulta y devoluciÃ³n de un equipo.
- [x] 7.3 Crear el archivo `README.md` con instrucciones de instalaciÃ³n, ejecuciÃ³n y uso; verificar que las instrucciones sean reproducibles.
- [x] 7.4 Crear el archivo `.gitignore` y comprobar que excluya el entorno virtual y archivos innecesarios.
- [x] 7.5 Publicar el proyecto en GitHub y verificar que el repositorio contenga el cÃ³digo, las pruebas y la documentaciÃ³n.
