"""
модуль, содержащий функционал работы с базой данных для бухгалтерии
"""
import sqlite3


# ==============================================================================
class SqlRequester:
    """
    класс-обертка над БД
    """

    # ==============================================================================
    def __init__(self, path: str):
        """
        конструктор класса
        """
        self.__conn = sqlite3.connect(path)
        self.__cur = self.__conn.cursor()

    # ==============================================================================
    def execute(self, template_request, data=()):
        """
        Интерфейс для cursor.execute
        """
        # print(template_request)
        self.__cur.execute(template_request, data)
        return self.__cur.fetchall()

    # ==============================================================================
    def executemany(self, template_request, data):
        """
        Интерфейс для sqlite3.cursor.executemany
        """
        self.__cur.executemany(template_request, data)
        return self.__cur.fetchall()

    # ==============================================================================
    def commit(self):
        """
        Интерфейс для sqlite3.connection.commit
        """
        self.__conn.commit()

    # ==============================================================================
    def create_function(self, *args, **kwargs):
        """
        Интерфейс для sqlite3.connection.create_function
        """
        self.__conn.create_function(args, kwargs)


# ==============================================================================
    def close(self):
        """
        Интерфейс для sqlite3.connection.close
        """
        self.__conn.close()
        self.__cur = None
        self.__conn = None
# ==============================================================================