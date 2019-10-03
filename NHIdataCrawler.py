import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page(URL,drugName):

	form = {
		'__VIEWSTATE': get_hiddenvalue(URL)[0],
		'__VIEWSTATEGENERATOR': get_hiddenvalue(URL)[1],
		'__SCROLLPOSITIONX': 0,
		'__SCROLLPOSITIONY': 0,
		'__EVENTTARGET': '',
		'__EVENTARGUMENT': '',
		'__VIEWSTATEENCRYPTED': '',
		'ctl00$ContentPlaceHolder1$tbxNameChinese': '',
		'ctl00$ContentPlaceHolder1$tbxName': drugName,
		'ctl00$ContentPlaceHolder1$tbxQ1ID': '',
		'ctl00$ContentPlaceHolder1$tbxDrugForm': '',
		'ctl00$ContentPlaceHolder1$ddlDrugClassifyCode': '',
		'ctl00$ContentPlaceHolder1$tbxElementName': '',
		'ctl00$ContentPlaceHolder1$tbxElementQuantity': '',
		'ctl00$ContentPlaceHolder1$tbxElementUnit': '',
		'ctl00$ContentPlaceHolder1$tbxStandNum': '',
		'ctl00$ContentPlaceHolder1$tbxStandUnit': '',
		'ctl00$ContentPlaceHolder1$tbxSales': '',
		'ctl00$ContentPlaceHolder1$ddlMixture': '',
		'ctl00$ContentPlaceHolder1$ddlStartYYY': '',
		'ctl00$ContentPlaceHolder1$ddlStartMM': '',
		'ctl00$ContentPlaceHolder1$ddlMedType': '',
		'ctl00$ContentPlaceHolder1$ddlIsUpdate': '',
		'ctl00$ContentPlaceHolder1$tbxACT': '',
		'ctl00$ContentPlaceHolder1$rblType': '迄今',
		'ctl00$ContentPlaceHolder1$tbxPageNum': '1000',
		'ctl00$ContentPlaceHolder1$btnSubmit': '開始查詢'
	}

	session_requests = requests.session()
	result = session_requests.post(URL, data = form)
	soup = BeautifulSoup(result.text, 'html.parser')

	return soup

def get_hiddenvalue(URL):
	session_requests = requests.session()
	result = session_requests.get(URL)
	soup = BeautifulSoup(result.text, 'html.parser')
	view_state = soup.find_all(id='__VIEWSTATE')
	for view_state_value in view_state:
		view_state_value = view_state_value.get('value')
	view_state_generator = soup.find_all(id='__VIEWSTATEGENERATOR')
	for view_state_generator_value in view_state_generator:
		view_state_generator_value = view_state_generator_value.get('value')

	return [view_state_value,view_state_generator_value]

def get_pagenum(drugName,URL):
	soup = get_page(URL, drugName)
	pages = soup.find(id='ctl00_ContentPlaceHolder1_ddlPageSelect')
	pages_no = pages.find_all('option')

	return len(pages_no)

def get_result(drugName,URL):
	soup = get_page(URL,drugName)

	druglist = []
	raw_druglink = []
	druglink = []
	full_druglist = []

	div = soup.find(id='ctl00_ContentPlaceHolder1_div_result')
	href = soup.find_all('a')
	rows = div.find_all('tr')
	rowsnum = len(rows)
	for i in range(3,rowsnum):
		druglist.append(list(rows[i].stripped_strings))
	for link in href:
		raw_druglink.append(link.get('href'))
	for i in range(6,(6+len(druglist))):
		druglink.append(raw_druglink[i])
	for i in range (0,len(druglist)):
		k = i+1
		print('查詢序號:'+str(k))
		print('藥物名稱:'+druglist[i][1])
		print('藥物中文名稱:'+druglist[i][2])
		print('藥物詳細資料:'+druglink[i])
		print(' ')
	'''for i in range(0,len(druglist)):
		k = page+len(druglist)
		full_druglist.append([k,druglist[i][1],druglist[i][2],druglink[i]])'''

	return full_druglist

def get_input():
	ch = input('請輸入欲查詢之藥品英文名稱:')
	if ch == '':
		return ch


def main():
	drugName = 'CLINDAMYCIN'
	URL='https://www.nhi.gov.tw/QueryN/Query1.aspx'
	get_result(drugName, URL)

if __name__ == '__main__':
    main()