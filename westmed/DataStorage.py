import sqlite3
import os
from westmed import PageDetail, excelDataProcessing
from concurrent.futures import ThreadPoolExecutor


def db_createtable(c):
    # c.execute(
    #     "CREATE TABLE if not exists search("
    #     "DrugNo INTEGER PRIMARY KEY AUTOINCREMENT,name text,tags text,cureitem text,aftereffect text,careitem text,contradictions text,mamiitem text,effect text,useway text,interaction text)")
    c.execute(
        "CREATE TABLE if not exists medicine("
        "DrugNo INTEGER PRIMARY KEY,name text,tags text,cureitem text,aftereffect text,careitem text,contradictions text,mamiitem text,effect text,useway text,interaction text)")


def db_insert(c, input, i):
    if PageDetail.main(input) is True:
        c.execute("REPLACE INTO storage (DrugNo, name) values (?, ?)",(i, input))
    else:
        data = PageDetail.main(input)
        'data[0][1], data[0][2], data[0][0], data[0][1], data[0][2], data[1][0], data[1][1], data[1][2], data[1][3], data[1][4]'
        c.execute(
            "REPLACE INTO storage (DrugNo, name, tags, cureitem, aftereffect, careitem, contradictions, mamiitem, effect, useway, interaction) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (i, str(data[0][0]), str(data[1][0]), str(data[0][2]), str(data[0][3]), str(data[0][4]), str(data[1][1]), str(data[1][2]), str(data[1][3]), str(data[1][4]), str(data[1][5])))

class multi_thread_Class():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def work(self):
        # 取得上一層路徑
        conn = sqlite3.connect(str(os.path.abspath("..")) + '\\ALL.db', check_same_thread=False)
        print("資料庫連接成功")
        c = conn.cursor()
        db_createtable(c)
        for i in range(self.start,self.end):
            db_insert(c, excelDataProcessing.main()[i], i + 1)
            conn.commit()
            print("第" + str(i+1) + "項資料新增成功")
        conn.close()
i=3000
def thread1():
    work1 = multi_thread_Class(i, i+116)
    work1.work()

def thread2():
    work2 = multi_thread_Class(i+915, i+1001)
    work2.work()

def thread3():
    work3 = multi_thread_Class(i+1213, i+1501)
    work3.work()

def thread4():
    work4 = multi_thread_Class(i+1723, i+2001)
    work4.work()

def thread5():
    work5 = multi_thread_Class(i+2222, i+2500)
    work5.work()

with ThreadPoolExecutor() as executor:
    executor.submit(thread1)
    # executor.submit(thread2)
    # executor.submit(thread3)
    # executor.submit(thread4)
    # executor.submit(thread5)

if __name__ == '__main__':
    executor