import pyodbc

connStr = (
r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
r"DBQ=D:\ventilation_rev02_DLR.mdb;"
)
conn = pyodbc.connect(connStr)
cursor = conn.cursor()
sql = 'SELECT Day FROM VentilationData;'
cursor.execute(sql)
#conn.commit()
row = cursor.fetchall()
j = [x[0] for x in row]
o = j[0].replace('/06/', '/07/')
print(o)
conn.close()

