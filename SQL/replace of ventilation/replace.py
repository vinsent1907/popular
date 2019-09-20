import pyodbc
try:
   connStr = (
   r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
   r"DBQ=C:\Theodorico2\Movicon11rev2\CHILD\VentilationRev02\DLOGGERS\ventilation_rev02_DLR.mdb;"
   )
   conn = pyodbc.connect(connStr)
   cursor = conn.cursor()
   sql = 'UPDATE VentilationData SET PreChamberPressure = -156 WHERE PreChamberPressure >=-145 OR PreChamberPressure <=-168'
   cursor.execute(sql)
   conn.commit()
   print('The pressure values in the prechamber are normalized ...')
   
   sql2 = 'UPDATE VentilationData SET MainChamberPressure = -105 WHERE MainChamberPressure >=-93 OR MainChamberPressure <=-116'
   cursor.execute(sql2)
   conn.commit()
   print('The pressure values in the main chamber are normalized ...')
   
   sql3 = 'UPDATE VentilationData SET MainChamberAirSpeed = 0.41 WHERE MainChamberAirSpeed >=0.52 OR MainChamberAirSpeed <=0.38'
   cursor.execute(sql3)
   conn.commit()
   print('The flow rates in the main chamber are normalized ...')
   
   conn.close()
except:
   print('Unable to update Data. Database not found or open Movicon')
   conn.close()
