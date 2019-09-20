import pyodbc
try:
   connStr = (
   r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
   r"DBQ=D:\ventilation_rev02_DLR.mdb;"
   )
   conn = pyodbc.connect(connStr)
   cursor = conn.cursor()
   sql = 'UPDATE VentilationData SET Day = Replace(Day, Substring(Day, 4, 2), 11)'
   cursor.execute(sql)
   conn.commit()
   print('Месяц успешно изменен...')
   conn.close()
except:
   print('Невозможно обновить Данные. База данных не найдена или открыт Movicon')
   conn.close()
