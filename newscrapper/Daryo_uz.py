import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz



headers={'User-Agent': 'Mozilla/5.0'}

news_list = []


### Date settings
now = datetime.now(pytz.timezone('Asia/Tashkent'))
day_before = now-timedelta(1)
today = now.strftime("%Y/%m/%d")
yesterday = day_before.strftime("%Y/%m/%d")

categories = ["mahalliy", "dunyo", "texnologiyalar", "madaniyat", "avto", "sport", "foto"]

for category in categories:
    is_new = True
    page = 1

    while is_new:

        url = "https://admin.daryo.uz/category/"+ category +"/page/"+str(page)+"/"

        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text,'html.parser')
        news = soup.find("div", class_="main")

        for article in news.find_all("article", class_="cat_article"):
            main = article.find("a")
            lk = main.get('href')[23:]
            date = lk[:10]
            if date == today or date == yesterday:
                link="https://daryo.uz/"
                link=link+lk
                title = main.text
                views = article.find('span', class_="meta_views").text.replace(" ", "")

                news_list.append(list((title, link, views, category, date, "daryo.uz")))

            else:
                is_new = False
                break
        page+=1


    

#ul = news.find('ul')
#for li in ul.findAll('li'):
#    info = li.find('div', class_='itemDatas').text.split()
#    when = info[1]

#    lk = li.find('a').get('href')
#    date = lk[1:11]

#    if when=='Bugun' or when=="Kecha":
        ### Getting link 
#        link="https://daryo.uz"
#        link=link+lk
        

        ### getting title of news
#        title = li.find('div', class_="itemTitle").text
#        views = info[3]
#        news_list.append(list((title, link, views, date, "Daryo.uz")))
#    else:
#        is_new = False
#        break
#page+=1

print(len(news_list))
print(news_list[0])
print(news_list[-1])





    

