"""
Connects to a SQL database using pyodbc
"""
import os

from dotenv import load_dotenv

import pytest
import pyodbc


# Load environment variables from .env file
load_dotenv()

# Get environment variables
SQL_HOST = os.getenv("SQL_HOST")
SQL_PORT = os.getenv("SQL_PORT")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_DRIVER = os.getenv("SQL_DRIVER", 'Devart ODBC Driver for SQL Server')


def connect_to_server():
    connection = None
    try:
        connection = pyodbc.connect(f'DRIVER={SQL_DRIVER};\
                            Server={SQL_HOST};\
                            Port={SQL_PORT};\
                            User ID={SQL_USER};\
                            Password={SQL_PASSWORD}')
    except:
        pass
    return connection


def connect_to_database():
    connection = None
    try:
        connection = pyodbc.connect(f'DRIVER={SQL_DRIVER};\
                            Server={SQL_HOST};\
                            Port={SQL_PORT};\
                            Database={SQL_DATABASE};\
                            User ID={SQL_USER};\
                            Password={SQL_PASSWORD}')
    except:
        pass
    return connection


def test_connect_to_database():
    connection = connect_to_database()
    assert connection is not None, "Failed to connect to database"
    connection.close()


def test_connect_to_server():
    connection = connect_to_database()
    assert connection is not None, "Failed to connect to server"
    connection.close()
