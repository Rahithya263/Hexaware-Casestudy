import mysql.connector as sql


class DBConnection:
    @staticmethod
    def getconnection():
        host = 'localhost'
        database = 'VirtualArtGallery'
        user = 'root'
        password = 'Radhi1234'
        return sql.connect(host=host, database=database, user=user, password=password)
