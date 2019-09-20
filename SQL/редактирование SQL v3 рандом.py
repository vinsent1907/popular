import pyodbc
try:
connStr = (
r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
r"DBQ=D:\ventilation_rev02_DLR.mdb;"
)
conn = pyodbc.connect(connStr)
cursor = conn.cursor()
sql = 'UPDATE VentilationData SET PreChamberPressure = -156 WHERE PreChamberPressure >=-145 OR PreChamberPressure <=-168'
cursor.execute(sql)
conn.commit()
sql2 = 'UPDATE VentilationData SET MainChamberPressure = -105 WHERE MainChamberPressure >=-93 OR MainChamberPressure <=-116'
cursor.execute(sql2)
conn.commit()
sql3 = 'UPDATE VentilationData SET MainChamberAirSpeed = 0.41 WHERE MainChamberAirSpeed >=0.52 OR MainChamberAirSpeed <=0.38'
cursor.execute(sql3)
conn.commit()
conn.close()
except:
print('Невозможно обновить Данные, Закройте Movicon')
conn.close()
