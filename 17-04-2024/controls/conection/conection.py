import pymysql 
pymysql.install_as_MySQLdb()
import MySQLdb

class Conection:
    def __init__(self):
        self.__db = None

    @property
    def _db(self):
        return self.__db

    @_db.setter
    def _db(self, value):
        self.__db = value
        
    def connect(self, user, password, db, host='localhost'):
        self._db = MySQLdb.connect(host=host, 
                                   user=user, 
                                   passwd=password, 
                                   db=db,
                                   cursorclass=MySQLdb.cursors.DictCursor)
        
    def _close(self):
        self._db.close()
        
        
