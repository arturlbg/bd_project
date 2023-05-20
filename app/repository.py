from django.db import connection

class StudentRepository:
    def findAll(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.app_student"
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def findById(self, id):
        with connection.cursor() as cursor:
            query = "SELECT * FROM yourapp_student WHERE id = %s"
            cursor.execute(query, [id])
            result = cursor.fetchone()
        return result
