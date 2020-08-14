
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from database.mssql import MSSQL
from fuzzywuzzy import process
import json

sql = """
    SELECT {} FROM Customers
    LEFT JOIN CustomersAdresses ON Customers.Id = CustomersAdresses.CustomerId
"""


sql_2 = """
    SELECT FullName,Customers.IntegrationCode FROM Customers
    LEFT JOIN CustomersAdresses ON Customers.Id = CustomersAdresses.CustomerId
    WHERE {} = '{}'
"""


def control_with_tel(telno):
    m = MSSQL()
    m.connect()
    data = m.execute(sql.format("Telephone"))
    f = process.extract(telno, data)[0][0][0]
    user = m.execute(sql_2.format("Telephone",f))
    m.close()
    return json.dumps({"Tel" : user[0][0],"Kod" : user[0][1],"Tel" : f})



def control_with_mail(mail):
    m = MSSQL()
    m.connect()
    data = m.execute(sql.format("RIGHT(EMail, LEN(EMail) - CHARINDEX(';', EMail))"))
    users = process.extract(mail, data)
    m.close()

    jsons = []

    for user in users:
        jsons.append(json.dumps({"Mail" :   str(user[0][0])  },ensure_ascii=False).encode("utf8").decode())

    return {"data" :jsons}


def control_with_name(telno):
    m = MSSQL()
    m.connect()
    data = m.execute(sql.format("FullName"))
    users = process.extract(telno, data)
    m.close()

    jsons = []

    for user in users:
        jsons.append(json.dumps({"Name" :   str(user[0][0])  },ensure_ascii=False).encode("utf8").decode())

    return {"data" :jsons}
