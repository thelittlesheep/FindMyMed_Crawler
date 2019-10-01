from bs4 import BeautifulSoup
import requests


def parse(soup):
    for i in soup(class_='name'):
        print(i.text)


def main():
    url = 'https://www.mittw.org.tw/products/manufacturer.aspx'
    session = requests.session()
    resp = session.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    view_state = soup.find(id='__VIEWSTATE')['value']
    parse(soup)
    for page in range(2, 179):
        resp = session.post(url, {
            'WebPager1_input': str(page),
            'WebPager1': 'go',
            '__VIEWSTATE': view_state
        })
        parse(BeautifulSoup(resp.content, 'html.parser'))


if __name__ == "__main__":
    main()