import requests
from bs4 import BeautifulSoup


def get_page(URL, unicode_inputtext):
    # 傳入URL,inputtext,pagenum，建立該次搜尋之soup
    my_params = {'keyword': unicode_inputtext}
    session_requests = requests.session()
    result = session_requests.get(URL, params=my_params)
    soup = BeautifulSoup(result.text, 'html.parser')

    return soup


def get_result(soup, input):
    # 利用beautifulsoup整理頁面資訊(return list)
    raw_druglink = []
    id = soup.find(id='medicineTable')
    href = id.find_all('a')
    for link in href:
        raw_druglink.append(link.get('href'))
    if not raw_druglink:
        return True
    else:
        druglink = raw_druglink[1]
        return druglink

def main(input):
    # 主程式
    #input = search_input()
    URL = 'https://www.kingnet.com.tw/knNew/medicine/medicine_search.html?'

    soup = get_page(URL, input)
    return  get_result(soup, input)


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
