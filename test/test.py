import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.nhi.gov.tw/QueryN/Query1_Print.aspx?MedType=&IsUpdate=&Q1ID=&Name=METFORMIN&NameChinese=&DrugClassifyCode=&ElementName=&ElementQuantity=&ElementUnit=&StandNum=&StandUnit=&DrugForm=&Sales=&Mixture=&StartYYY=&StartMM=&Type=%e8%bf%84%e4%bb%8a&ACT=')
soup = BeautifulSoup(resp.text, 'html.parser')


rows = soup.findAll('tr') # 先取得所有的tr資料
rowsnum = len(rows)

druglist = []
drugpicNo = []
for i in range(2,rowsnum):
  druglist.append(list(rows[i].stripped_strings))
for i in range(0,rowsnum-2):
  OldpicID = str(druglist[i][0])[2:7]
  NewpicID = "010"+OldpicID
  drugpicNo.append(NewpicID)
for i in range (0,rowsnum-2):
  k = i+1
  print("查詢序號:"+str(k))
  print("藥物名稱:"+druglist[i][1])
  print("藥物中文名稱:"+druglist[i][2])
  print(" ")