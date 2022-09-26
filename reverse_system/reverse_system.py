import sqlite3
'''
import jieba
s='大家好，祝大家萬事如意，謝謝'
w=jieba.cut_for_search(s)
for i in w:
    print(i+'/',end='')
'''
#如果父類別的屬性利用封裝特性設為私有的話，子類別無法繼承到父類別的屬性


class RofSteven():

    def __init__(self, uname, uphone, udate):
        self.name = uname
        self.phone = uphone
        self.date = udate

    def reverse_steven(self):
        c = sqlite3.connect('Steven_reverse_table.db')
        x = (self.name, self.phone, self.date)
        sql_create = 'create table if not exists reverse_steven("姓名" text,"電話" text,"日期" int)'
        c.execute(sql_create)
        sql_reverse = 'insert into reverse_steven values(?,?,?)'
        c.execute(sql_reverse, x)
        c.commit()
        c.close()


class RofJohn(RofSteven):

    def reverse_john(self):
        c = sqlite3.connect('John_reverse_table.db')
        x = (self.name, self.phone, self.date)
        sql_create = 'create table if not exists reverse_john("姓名" text,"電話" text,"日期" int)'
        c.execute(sql_create)
        sql_reverse = 'insert into reverse_john values(?,?,?)'
        c.execute(sql_reverse, x)
        c.commit()
        c.close()