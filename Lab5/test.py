import pymysql

connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='pass',
    database='my_db'
)

cur = connect.cursor()
year= int(input('Введите год: '))
cur.execute(' select first_name,last_name,date_of_birth from user where year(date_of_birth) = year%',year)
for rec in cur:
    print(rec[0],rec[1],rec[2])