import sys
import urllib2
import time
from bs4 import BeautifulSoup
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf8') # 設置編碼
url = 'http://baike.baidu.com/starrank?fr=lemmaxianhua'
driver = webdriver.Chrome('/usr/local/Cellar/chromedriver/2.20/bin/chromedriver') # 創建一個driver用於打開網頁，記得找到brew安裝的chromedriver的位置，在創建driver的時候指定這個位置
driver.get(url) # 打開網頁
name_counter = 1
page = 0;
while page < 50: # 共50頁，這裡是手工指定的
	soup = BeautifulSoup(driver.page_source, "html.parser")
	current_names = soup.select('div.ranking-table') # 選擇器用ranking-table css class，可以取出包含本週、上週的兩個table的div標籤
	for current_name_list in current_names:
		# print current_name_list['data-cat']
		if current_name_list['data-cat'] == 'thisWeek': # 這次我只想抓取本週，如果想抓上週，改一下這裡為lastWeek即可
			names = current_name_list.select('td.star-name > a') # beautifulsoup選擇器語法
			counter = 0;
			for star_name in names:
				counter = counter + 1;
				print star_name.text # 明星的名字是a標籤裡面的文本，雖然a標籤下面除了文本還有一個與文本同級別的img標籤，但是.text輸出的只是文本而已
				name_counter = name_counter + 1;
	driver.find_element_by_xpath("//a[contains(text(),'下一頁')]").click() # selenium的xpath用法，找到包含“下一頁”的a標籤去點擊
	page = page + 1
	time.sleep(2) # 睡2秒讓網頁加載完再去讀它的html代碼
print name_counter # 共爬取得明星的名字數量
driver.quit()