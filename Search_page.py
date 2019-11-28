import requests
import urllib.parse
from bs4 import BeautifulSoup
from math import floor


def get_page(URL, unicode_inputtext, pagenum):
    # 傳入URL,inputtext,pagenum，建立該次搜尋之soup
    my_params = {'keyword': unicode_inputtext, 'page': pagenum}
    session_requests = requests.session()
    result = session_requests.get(URL, params=my_params)
    soup = BeautifulSoup(result.text, 'html.parser')

    return soup


def get_pagenum(URL, unicode_inputtext):
    # 利用beautifulsoup整理頁面資訊，取得搜尋結果頁數(return int)
    my_params = {'keyword': unicode_inputtext}
    session_requests = requests.session()
    result = session_requests.get(URL, params=my_params)
    soup = BeautifulSoup(result.text, 'html.parser')
    totaldata = soup.find(id='data-total').string
    totaldata_pages = floor(float(totaldata) / 10) + 1

    return totaldata_pages


def get_result(soup):
    # 利用beautifulsoup整理頁面資訊(return list)
    druglist = []
    raw_druglink = []
    druglink = []
    full_druglist = []

    id = soup.find(id='medicineTable')
    href = id.find_all('a')
    rows = id.find_all('tr')
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
    # 計算當頁面有多少筆資料
    div = soup.find(id='medicineContentList')
    rows = div.find_all('tr')

    return len(rows) - 1


def search_input():
    inputtext = input('請輸入欲查詢之藥品名稱或關鍵字:' + '\n')
    unicode_inputtext = urllib.parse.quote(inputtext)  # 將輸入之中文字轉換為unicode，此例中不需要轉換

    return unicode_inputtext


def main(input):
    # 主程式
    #input = search_input()
    URL = 'https://www.kingnet.com.tw/knNew/medicine/medicine_search.html?'
    totalpage_full_druglist = []
    pagenumbers = get_pagenum(URL, input)
    for i in range(0, pagenumbers):
        # 從第一頁開始歷遍所有查詢結果頁面
        soup = get_page(URL, input, i + 1)
        total_druglist = get_result(soup)
        totalpage_full_druglist.append(total_druglist)
    return totalpage_full_druglist


'''def main():
    #寫入檔案用
    inputtext = input('請輸入欲查詢之藥品名稱或關鍵字:')
    URL = 'https://www.kingnet.com.tw/knNew/medicine/medicine_search.html?'
    totalpage_full_druglist = []
    pagenumbers = get_pagenum(URL, inputtext)
    
    fp = open(inputtext+'.txt', 'w',encoding="utf-8")
    for i in range(0, pagenumbers):
        #從第一頁開始歷遍所有查詢結果頁面
        soup = get_page(URL, inputtext, i + 1)
        total_druglist = get_result(soup)
        totalpage_full_druglist.append(total_druglist)
        for j in range(0, count_pageobject(soup)):
            #從該頁面讀取所有查詢結果項目，並寫入檔案
            fp.write('查詢序號:' + str(i+1) + '-' + str(totalpage_full_druglist[i][j][0])+'\n')
            fp.write('藥物分類:' + str(totalpage_full_druglist[i][j][1])+'\n')
            fp.write('藥物名稱:' + str(totalpage_full_druglist[i][j][2])+'\n')
            fp.write('藥物詳細資料:' + str(totalpage_full_druglist[i][j][3])+'\n')
            fp.write('\n\n')
    fp.close()'''

if __name__ == '__main__':
    main()
