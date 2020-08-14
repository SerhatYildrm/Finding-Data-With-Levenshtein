
#
#
#
#   Author: Serhat Yıldırm
#   Date: 13/08/2020
#
#
#



from urllib.parse import quote_plus
from sqlalchemy import create_engine

class MSSQL:
    def __init__(self):
        self.server = '.' 
        self.database = '' 
        self.username = 'sa' 
        self.password = '' 

    def connect(self):
        con_str = 'DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' %(self.server,self.database,self.username,self.password)
        params = quote_plus(con_str)
        self.db = create_engine("mssql+pyodbc:///?odbc_connect=%s?charset=utf8" % params)
        self.conn = self.db.connect()
        return self.conn

    def execute(self,query):
        return [data for data in self.conn.execute(query).fetchall()]

    def close(self):
        self.conn.close()
        self.db.dispose()
