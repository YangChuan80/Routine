import sqlite3

connection=sqlite3.connect('D:\\Database\\SQL_gwncc_test.db')

curs=connection.cursor()
curs.execute('''CREATE TABLE gwncc_2015
(name VARCHAR(20) PRIMARY KEY,
hospital VARCHAR(100),
age INT,
income FLOAT)''')

curs.execute('INSERT INTO gwncc_2015 VALUES("Sun Yingxian", "First Affiliated Hospital of China Medical University", 52, 10000)')

curs.close()
connection.close()