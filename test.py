
import pyodbc
server = 'sanchitlogger.database.windows.net' 
database = 'logger' 
username = 'sanchitlogger' 
password = 'Hello@1234' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
a = cursor.execute('''
                     insert into customers(name,c_id,gender)
                      VALUES ("Sanchit", 01 , "m");
                   ''')
print(hello)