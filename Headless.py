from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
	chrome_options = Options() # 啟動無頭模式
	chrome_options.add_argument('--headless')  #規避google bug
	chrome_options.add_argument('--disable-gpu')
	url = 'https://www.nhi.gov.tw/QueryN/Query1.aspx'
	executable_path = 'chromedriver.exe'#自行設定路徑
	driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
	driver.get(url)
	
	driver.quit()#關閉瀏覽器 

if __name__ == '__main__':
    main()