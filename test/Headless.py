from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def main():
	chrome_options = Options() # 啟動無頭模式
	chrome_options.add_argument('--headless')  #規避google bug
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument('--window-size=1920,3240')
	url = 'https://www.nhi.gov.tw/QueryN/Query1.aspx'
	executable_path = 'chromedriver.exe'#自行設定路徑
	driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
	driver.get(url)
	driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxName').send_keys('metformin')
	driver.find_elements_by_name('ctl00$ContentPlaceHolder1$tbxPageNum')
	#driver.find_elements_by_xpath("//form[@name='開始查詢'][@type='submit']")
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	driver.save_screenshot('sc.png')

	driver.quit()#關閉瀏覽器 

if __name__ == '__main__':
    main()