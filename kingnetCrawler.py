import requests
import urllib.parse
from bs4 import BeautifulSoup
from math import floor


def get_page(URL, inputtext, pagenum): #傳入URL,inputtext
    unicode_inputtext = urllib.parse.quote(inputtext)  # 將中文字轉換為unicode，此例中不需要轉換
    my_params = {'keyword': unicode_inputtext, 'page': pagenum}
    session_requests = requests.session()
    result = session_requests.get(URL, params=my_params)
    soup = BeautifulSoup(result.text, 'html.parser')

    return soup


def get_pagenum(URL, inputtext):
    unicode_inputtext = urllib.parse.quote(inputtext)  # 將中文字轉換為unicode，此例中不需要轉換
    my_params = {'keyword': unicode_inputtext}
    session_requests = requests.session()
    result = session_requests.get(URL, params=my_params)
    soup = BeautifulSoup(result.text, 'html.parser')
    totaldata = soup.find(id='data-total').string
    totaldata_num = floor(float(totaldata) / 10) + 1

    return totaldata_num


def get_result(soup):
    druglist = []
    raw_druglink = []
    druglink = []
    full_druglist = []

    div = soup.find(id='medicineTable')
    href = div.find_all('a')
    rows = div.find_all('tr')
    rowsnum = len(rows)
    for i in range(2, rowsnum):
        druglist.append(list(rows[i].stripped_strings))
    for link in href:
        raw_druglink.append(link.get('href'))
    for i in range(1, len(druglist) + 1):
        druglink.append(raw_druglink[i])
    for i in range(0, len(druglist)):
        k = i + 1
        full_druglist.append([k, druglist[i][0], druglist[i][1], druglink[i]])

    return full_druglist


def count_pageobject(soup):
    div = soup.find(id='medicineContentList')
    rows = div.find_all('tr')

    return len(rows)-1


def main():
    inputtext = input('請輸入欲查詢之藥品名稱或關鍵字:')
    URL = 'https://www.kingnet.com.tw/knNew/medicine/medicine_search.html?'
    totalpage_full_druglist = []
    pagenumbers = get_pagenum(URL, inputtext)
    fp = open(inputtext+'.txt', 'w')
    for i in range(0, pagenumbers):
        soup = get_page(URL, inputtext, i + 1)
        total_druglist = get_result(soup)
        totalpage_full_druglist.append(total_druglist)
        for j in range(0, count_pageobject(soup)):
            '''print('查詢序號:' + str(i+1) + '-' + str(totalpage_full_druglist[i][j][0]))
            print('藥物分類:' + str(totalpage_full_druglist[i][j][1]))
            print('藥物名稱:' + str(totalpage_full_druglist[i][j][2]))
            print('藥物詳細資料:' + str(totalpage_full_druglist[i][j][3]))
            print('')'''
            fp.write('查詢序號:' + str(i+1) + '-' + str(totalpage_full_druglist[i][j][0])+'\n')
            fp.write('藥物分類:' + str(totalpage_full_druglist[i][j][1])+'\n')
            fp.write('藥物名稱:' + str(totalpage_full_druglist[i][j][2])+'\n')
            fp.write('藥物詳細資料:' + str(totalpage_full_druglist[i][j][3])+'\n')
            fp.write('\n\n')
    fp.close()


if __name__ == '__main__':
    main()
