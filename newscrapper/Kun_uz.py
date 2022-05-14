import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz

headers={'User-Agent': 'Mozilla/5.0'}

is_new = True
news_list = []
page = 1

### Date settings
now = datetime.now(pytz.timezone('Asia/Tashkent'))
day_before = now-timedelta(1)
today = now.strftime("%Y/%m/%d")
yesterday = day_before.strftime("%Y/%m/%d")

#while is_new:

url = "https://m.kun.uz/uz?q=%2Fuz&page=" + str(page)
facing_new = False

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text,'html.parser')
news = soup.find("div", class_="col-xs-12")

for item in news.find_all('div', class_="post-body"):

    main = item.find('a', class_="post-title")
    lk = main.get('href')
    date = lk[9:19]

    if date == today or date == yesterday:
        link = "https://kun.uz" + lk
        title = main.text.strip()
        views = item.find('span', class_="viewed").text
        category= item.find('a', class_="float-none blue").text.strip()

        if category == "O‘zbekiston":
            category = "mahalliy"
        elif category == "Jahon":
            category = "dunyo"
        elif category == "Jamiyat":
            category = "jamiyat"
        elif category == "Sport":
            category = "sport"
        elif category == "Iqtisodiyot":
            category = "iqtisodiyot"
        elif category == "Fan va texnika":
            category = "texnalogiyalar"
                
        news_list.append(list((title, link, views, category, date, "Kun.uz")))
            
        
            #facing_new = True

    #if not facing_new:
        #is_new = False
    #page+=1

print(len(news_list))
print(news_list[0])
print(news_list[-1])



