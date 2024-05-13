import mysql.connector as sql
from util.dbConnection import DBConnection


class PropertyUtil:
    @staticmethod
    def getpropertystring():
        l = DBConnection.getconnection()  # Get connection details
        conn = sql.connect(host=l[0], database=l[1], user=l[2], password=l[3])  # Unpack the tuple
        if conn.is_connected:
            print('DB is Connected')
        return conn
