import requests
from bs4 import BeautifulSoup


def get_page(URL, unicode_inputtext):
    # 傳入URL,inputtext，建立該次搜尋之soup
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

def main(input="Peritoneal"):
    # 主程式
    URL = 'https://www.kingnet.com.tw/knNew/medicine/medicine_search.html?'

    soup = get_page(URL, input)
    return  get_result(soup, input)

if __name__ == '__main__':
    main()
