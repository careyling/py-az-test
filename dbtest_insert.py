import cx_Oracle as cx

conn = cx.connect('C##VCC', 'VCC', 'dx.huangyi.cn:1521/ORCL')
cur = conn.cursor()  # カーソルを取得

sql = "INSERT INTO TESTDATA VALUES(6,7,8)"

cur.execute(sql)
conn.commit()

cur.close()  # カーソル クローズ
conn.close()

print("Insert OK")