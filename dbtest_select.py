import cx_Oracle as cx
conn = cx.connect('C##VCC', 'VCC', 'dx.huangyi.cn:1521/ORCL')
cursor = conn.cursor()
sql = "SELECT ID,V1,V2 FROM TESTDATA ORDER BY ID"
cursor.execute(sql)
data = cursor.fetchall() 
print(data) 
cursor.close()
conn.close()