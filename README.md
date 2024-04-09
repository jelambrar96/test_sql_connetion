# Prueba de Conexión a Base de Datos SQL con PyODBC y Pytest

Este repositorio contiene un script de Python para probar la conexión a una base de datos SQL utilizando PyODBC y Pytest.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- PyODBC
- Pytest
- Dotenv

Puedes instalar las dependencias con el siguiente comando:

```bash
pip install pyodbc pytest python-dotenv
```

## Configuración

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/repo_nombre.git
cd repo_nombre
```

2. Crea un archivo .env en el directorio raíz del proyecto con las siguientes variables de entorno:
dotenv

```
SQL_HOST=tu_host
SQL_PORT=tu_puerto
SQL_USER=tu_usuario
SQL_PASSWORD=tu_contraseña
SQL_DATABASE=tu_basededatos
SQL_DRIVER=
```

3, Configura el controlador de ODBC necesario para tu base de datos en el script (SQL_DRIVER).

## Uso

Ejecuta las pruebas con el siguiente comando:

```bash
pytest test_connection.py
```

Esto ejecutará dos pruebas: una para probar la conexión al servidor y otra para probar la conexión a la base de datos.

## Contribuciones

Siéntete libre de contribuir con mejoras o correcciones a este código mediante pull requests.

## Licencia

Este proyecto está bajo la licencia MIT.

## Note

Recuerda reemplazar `tu_usuario`, `repo_nombre`, `tu_host`, `tu_puerto`, `tu_usuario`, `tu_contraseña` y `tu_basededatos` con tus propias configuraciones y nombres específicos.