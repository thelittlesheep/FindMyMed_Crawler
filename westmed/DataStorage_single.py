import sqlite3
import os
from westmed import PageDetail


def db_createtable(c):
    # c.execute(
    #     "CREATE TABLE if not exists search("
    #     "DrugNo INTEGER PRIMARY KEY AUTOINCREMENT,name text,tags text,cureitem text,aftereffect text,careitem text,contradictions text,mamiitem text,effect text,useway text,interaction text)")
    c.execute(
        "CREATE TABLE if not exists medicine("
        "DrugNo INTEGER PRIMARY KEY,name text,tags text,cureitem text,aftereffect text,careitem text,contradictions text,mamiitem text,effect text,useway text,interaction text)")


def db_insert(c, input, i):
    if PageDetail.main(input) is True:
        c.execute("REPLACE INTO storage (DrugNo, name) values (?, ?)", (i, input))
    else:
        data = PageDetail.main(input)
        'data[0][1], data[0][2], data[0][0], data[0][1], data[0][2], data[1][0], data[1][1], data[1][2], data[1][3], data[1][4]'
        c.execute(
            "REPLACE INTO storage (DrugNo, name, tags, cureitem, aftereffect, careitem, contradictions, mamiitem, effect, useway, interaction) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (i, str(data[0][0]), str(data[1][0]), str(data[0][2]), str(data[0][3]), str(data[0][4]), str(data[1][1]),
             str(data[1][2]), str(data[1][3]), str(data[1][4]), str(data[1][5])))


def main():
    # 取得上一層路徑
    parent_path = os.path.abspath("..")
    conn = sqlite3.connect(str(parent_path) + '\\ALL.db', check_same_thread=False)
    print("資料庫連接成功")
    c = conn.cursor()
    db_createtable(c)
    i = 3091
    name = '3.0% AMINO ACIDS , 注射劑 , 3.00  %, 300.00 ML'
    db_insert(c, name, i + 1)
    conn.commit()
    print("第" + str(i + 1) + "項資料新增成功")
    conn.close()


if __name__ == '__main__':
    main()
