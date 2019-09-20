import pyodbc

connStr = (
r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
r"DBQ=D:\ventilation_rev02_DLR.mdb;"
)
conn = pyodbc.connect(connStr)
cursor = conn.cursor()
#sql = 'SELECT Day FROM VentilationData;'
#cursor.execute(sql)
#row = cursor.fetchall()
#j = [x[0] for x in row]
#i = 0
#for element in j:
#   j[i] = j[i].replace('/06/', '/07/')
#   i += 1
cursor = conn.cursor()
sql = "UPDATE VentilationData SET Day = REPLACE(Day, '/06/', '/07/')"
cursor.execute(sql)
conn.commit()
sql = "UPDATE VentilationData SET Day = REPLACE(Day, '/05/', '/06/')"
cursor.execute(sql)
conn.commit()

   
print('успех 1')

#cursor.execute('INSERT INTO VentilationData (Day) VALUES (?);', [','.join(j)])
#conn.commit()

print('успех 2')
conn.close()
#conn.commit()
#m=j[0].replace('/06/', '/07/')
#WHERE PreChamberPressure >=-145 OR PreChamberPressure <=-168'
