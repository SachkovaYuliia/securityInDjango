from django.db import connection

def execute_secure_query(query, params):
    """
    Функція для безпечного виконання SQL-запитів з параметризацією
    """
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result