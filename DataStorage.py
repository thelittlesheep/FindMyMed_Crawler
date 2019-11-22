import sqlite3
import PageDetail


def db_createtable(c):
    c.execute(
        "CREATE TABLE if not exists search("
        "searchNo INTEGER PRIMARY KEY AUTOINCREMENT,cureitem text,aftereffect text,careitem text,contradictions text,mamiitem text,effect text,useway text,interaction text)")


def db_insert(c):
    data = PageDetail.main()
    'data[0][0], data[0][1], data[0][2], data[1][0], data[1][1], data[1][2], data[1][3], data[1][4]'
    c.execute(
        "insert into search (cureitem, aftereffect, careitem, contradictions, mamiitem, effect, useway, interaction) values (?, ?, ?, ?, ?, ?, ?, ?)",
        (str(data[0][0]), str(data[0][1]), str(data[0][2]), str(data[1][0]), str(data[1][1]), str(data[1][2]), str(data[1][3]), str(data[1][4])))


def main():
    conn = sqlite3.connect('example.db')
    print("資料庫連接成功")
    c = conn.cursor()


    db_createtable(c)
    db_insert(c)
    print("資料新增成功")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
