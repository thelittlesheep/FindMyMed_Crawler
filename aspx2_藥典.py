import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumrequests import Firefox

def main():
	drugName = 'METFORMIN'
	URL='https://www.nhi.gov.tw/QueryN/Query1.aspx'
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
		'ctl00$ContentPlaceHolder1$tbxPageNum': '10',
		'ctl00$ContentPlaceHolder1$btnSubmit': '開始查詢'
	}
	#driver = webdriver.Chrome('C:/webdriver/chromedriver.exe') # 創建一個driver用於打開網頁，記得找到brew安裝的chromedriver的位置，在創建driver的時候指定這個位置
	#driver.get(URL)
	webdriver = Firefox()
	response = webdriver.request('POST', URL ,data = form)

	final_druglist = []

	soup = get_page(URL,drugName)
	webdriver.find_element_by_id('ctl00_ContentPlaceHolder1_lbtnNextPage').click() # selenium的xpath用法，找到包含“下一頁”的a標籤去點擊
	page = page + 1
	time.sleep(2)

if __name__ == '__main__':
    main()