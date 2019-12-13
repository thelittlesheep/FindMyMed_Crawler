import sqlite3
import os
from chinesemed import PageDetail


def db_createtable(c):
    c.execute(
        "CREATE TABLE if not exists chinese_medicine("
        "DataNo INTEGER PRIMARY KEY,chinese_No text,chinese_name text,west_No text,west_name text,west_salename text,west_chinesename text,reason text,interaction text,suggest text)")


def db_insert(c, data, i):
    c.execute(
        "REPLACE INTO chinese_medicine (DataNo, chinese_No, chinese_name, west_No, west_name, west_salename, west_chinesename, reason, interaction, suggest) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (i + 1, data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6], data[i][7],
         data[i][8]))


def main():
    # 取得上一層路徑
    parent_path = os.path.abspath("..")
    conn = sqlite3.connect(str(parent_path) + '\\ALL.db', check_same_thread=False)
    print("資料庫連接成功")
    c = conn.cursor()
    db_createtable(c)
    data = PageDetail.main()
    for i in range(0, len(data)):
        db_insert(c, data, i)
        conn.commit()
        print("第" + str(i + 1) + "項資料新增成功")
    conn.close()


if __name__ == '__main__':
    main()
