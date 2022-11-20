"""
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
"""
import cryptography.fernet as fer
password = input("Enter password: ").encode()
a = fer.Fernet.generate_key()
print(a)
fernet = fer.Fernet(a)

print(fernet)
encrypted = fernet.encrypt(password)
dec = fernet.decrypt(encrypted).decode()
print(encrypted)
print(dec)
