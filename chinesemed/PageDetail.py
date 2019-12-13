import requests
from bs4 import BeautifulSoup


# from lxml import etree


def get_page_bs(URL):
    # 傳入URL，建立該次搜尋之soup
    result = requests.get(URL)
    result.encoding = 'big5'
    soup = BeautifulSoup(result.text, 'lxml')
    return soup


# def get_page_xpath(URL):
#     # 傳入URL，建立該次搜尋之xpath
#     result = requests.get(URL)
#     content = result.content.decode(encoding='big5')
#     selector = etree.HTML(content)
#
#     divs = selector.xpath('/html/body/table/tbody/tr[4]/td/table/tbody/tr[2]/td[1]/span')
#     print(divs)

def get_result(soup):
    tabledata = []
    table = soup.find_all('table')[1]
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        # 也可以寫成 cols = [x.get_text(strip=True) for x in cols]
        cols = [x.text.strip() for x in cols]
        tabledata.append(cols)
    tabledata = tabledata[1:len(tabledata) - 3]

    return tabledata


def main():
    # 主程式
    URL = 'http://www.chimei.org.tw/main/cmh_department/55500/DIS/cdi_search.asp'
    soup = get_page_bs(URL)

    return get_result(soup)


if __name__ == '__main__':
    main()
