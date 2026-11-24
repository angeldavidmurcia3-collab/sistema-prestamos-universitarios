# Tasks

## 1. Preparación del proyecto

- [ ] 1.1 Crear la estructura de carpetas y módulos de Python y verificar que todos los archivos estén ubicados correctamente.
- [ ] 1.2 Crear y configurar el entorno virtual de Python y verificar que se active correctamente.
- [ ] 1.3 Instalar pytest y verificar su instalación ejecutando `pytest --version`.
- [ ] 1.4 Crear el archivo `requirements.txt` y comprobar que contiene las dependencias necesarias.

## 2. Base de datos

- [ ] 2.1 Crear el módulo `database.py` y configurar la conexión con SQLite; verificar que la conexión se realice correctamente.
- [ ] 2.2 Crear las tablas de estudiantes, equipos y préstamos; verificar que existan en la base de datos.
- [ ] 2.3 Implementar pruebas para la creación y conexión de la base de datos; verificar que todas pasen con pytest.

## 3. Gestión de estudiantes

- [ ] 3.1 Crear las pruebas para registrar estudiantes, validar campos obligatorios y evitar identificaciones duplicadas; comprobar que inicialmente fallen.
- [ ] 3.2 Implementar el registro de estudiantes en `estudiantes.py`; ejecutar las pruebas y comprobar que pasen.
- [ ] 3.3 Crear pruebas para consultar estudiantes existentes e inexistentes; comprobar los resultados esperados.
- [ ] 3.4 Implementar la consulta de estudiantes y verificar su funcionamiento con pytest.

## 4. Gestión de equipos

- [ ] 4.1 Crear pruebas para registrar equipos y evitar códigos duplicados; comprobar que inicialmente fallen.
- [ ] 4.2 Implementar el registro de portátiles y proyectores en `equipos.py`; verificar que las pruebas pasen.
- [ ] 4.3 Crear pruebas para consultar equipos y comprobar su disponibilidad.
- [ ] 4.4 Implementar las consultas y actualización del estado de los equipos; verificar con pytest.

## 5. Gestión de préstamos y devoluciones

- [ ] 5.1 Crear pruebas para permitir préstamos únicamente a estudiantes registrados y con equipos disponibles; comprobar que inicialmente fallen.
- [ ] 5.2 Implementar el registro de préstamos en `prestamos.py`; verificar que las pruebas pasen.
- [ ] 5.3 Crear pruebas para impedir préstamos duplicados del mismo equipo y registrar correctamente las fechas.
- [ ] 5.4 Implementar las validaciones de préstamos y verificar los resultados con pytest.
- [ ] 5.5 Crear pruebas para registrar devoluciones y actualizar el estado del equipo.
- [ ] 5.6 Implementar las devoluciones y verificar que el equipo vuelva a estar disponible cuando corresponda.
- [ ] 5.7 Implementar la consulta de préstamos activos e historial y verificar los resultados.

## 6. Menú e integración

- [ ] 6.1 Crear `main.py` con un menú de opciones para gestionar estudiantes, equipos, préstamos y devoluciones; verificar que se muestre correctamente.
- [ ] 6.2 Conectar el menú con los módulos del sistema y comprobar que las operaciones funcionen desde la aplicación.
- [ ] 6.3 Validar las entradas del usuario y mostrar mensajes claros ante datos incorrectos; comprobar los casos de error.

## 7. Verificación y documentación

- [ ] 7.1 Ejecutar todas las pruebas con `pytest` y verificar que finalicen correctamente.
- [ ] 7.2 Realizar una prueba completa del flujo de registro, préstamo, consulta y devolución de un equipo.
- [ ] 7.3 Crear el archivo `README.md` con instrucciones de instalación, ejecución y uso; verificar que las instrucciones sean reproducibles.
- [ ] 7.4 Crear el archivo `.gitignore` y comprobar que excluya el entorno virtual y archivos innecesarios.
- [ ] 7.5 Publicar el proyecto en GitHub y verificar que el repositorio contenga el código, las pruebas y la documentación.