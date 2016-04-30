import db.base
import sqlite3
path=db.base.from_this_dir('Mydb.db')
print(path)
conn=sqlite3.connect(path)
print('ok')
#查询数据库表结构 
sql="select * from sqlite_master where type='table'"
cursor=conn.cursor()
cursor.execute(sql)
values=cursor.fetchall()
print(values)
#空数据库初始化
if cursor.rowcount <=0 :
    db.base.init_db()
    print('init database has done.')
else:
    pass

    
conn.close()
a=input('press enter to quit..')
