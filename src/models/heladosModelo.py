from database.db import get_connection
from .entities.helado import Helado

class HeladosModelo():

    @classmethod
    def get_Inventory(self):
        try:
            connection = get_connection()
            inventory = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, store_id, \"EMPLOYEE_id\", date, flavor, is_season_flavor, quantity FROM public.\"INVENTORY\"")
                resultset = cursor.fetchall()

                for row in resultset:
                    inventario = inventory(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    inventory.append(inventario.to_JSON())

            connection.close()
            return inventory
        except Exception as ex:
            raise Exception(ex)