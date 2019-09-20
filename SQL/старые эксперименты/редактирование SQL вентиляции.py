import pyodbc
conn = pyodbc.connect(r'Driver = {Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\ventilation_rev02_DLR.mdb;')
cursor = conn.cursor()
sql = """"
UPDATE VentilationData
SET PreChamberPressure = -156
WHERE PreChamberPressure >=-145 OR PreChamberPressure <=-168
"""
cursor.execute(sql)
conn.commit()
conn.close()
