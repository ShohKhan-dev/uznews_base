import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz
import re
from fysom import Fysom

import os
import django


os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

from uznews.models import WaitList, WatchList, IgnoreList, News


headers={'User-Agent': 'Mozilla/5.0'}
news_list = []


def kun_uz():
    is_new = True
    page = 1

    ### Date settings
    now = datetime.now(pytz.timezone('Asia/Tashkent'))
    day_before = now-timedelta(1)
    today = now.strftime("%Y/%m/%d")
    yesterday = day_before.strftime("%Y/%m/%d")

    print("acceptence: ",today, yesterday)

    while is_new:

        url = "https://m.kun.uz/uz?q=%2Fuz&page=" + str(page)
        facing_new = False
        print(url)

        response = requests.get(url, headers = headers)
        soup = BeautifulSoup(response.text,'html.parser')
        news = soup.find("div", class_="col-xs-12")

        for item in news.find_all('div', class_="post-body"):

            main = item.find('a', class_="post-title")
            lk = main.get('href')[1:]
            date = lk[8:18]
            print(date)

            if date == today or date == yesterday:
                link = lk
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
                        
                news_list.append(list((title, link, views, category, date, "kun.uz")))
                facing_new = True

        if not facing_new:
            is_new = False
        page+=1


def daryo_uz():

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
                    link=lk
                    title = main.text
                    views = article.find('span', class_="meta_views").text.replace(" ", "")

                    news_list.append(list((title, link, views, category, date, "daryo.uz")))

                else:
                    is_new = False
                    break
            page+=1

kun_uz()
daryo_uz()

print(len(news_list))
print(news_list[0])
print(news_list[-1])


def stem(word):
    fsm = Fysom(initial='start',
                    events=[
                    ('dir', 'start', 'b'),
                    ('dirda', 'start', 'b'),
                    ('ku', 'start', 'b'),
                    ('mi', 'start', 'b'),
                    ('mikan', 'start', 'b'),
                    ('siz', 'start', 'b'),
                    ('day', 'start', 'b'),
                    ('dek', 'start', 'b'),
                    ('niki', 'start', 'b'),
                    ('dagi', 'start', 'b'),
                    ('mas', 'start', 'd'),
                    ('ning', 'start', 'f'),
                    ('lar', 'start', 'g'),
                    ('lar', 'e', 'g'),
                    ('dan', 'd', 'e'),
                    ('da', 'd', 'e'),
                    ('ga', 'd', 'e'),
                    ('ni', 'd', 'e'),
                    ('dan', 'start', 'e'),
                    ('da', 'start', 'e'),
                    ('ga', 'start', 'e'),
                    ('ni', 'start', 'e'),
                    ('lar', 'f', 'g'),
                    ('miz', 'start', 'h'),
                    ('ngiz', 'start', 'h'),
                    ('si', 'start', 'h'),
                    ('i', 'start', 'h'),
                    ('ng', 'start', 'h'),
                    ('miz', 'f', 'h'),
                    ('ngiz', 'f', 'h'),
                    ('si', 'f', 'h'),
                    ('i', 'f', 'h'),
                    ('ng', 'f', 'h'),
                    ('miz', 'e', 'h'),
                    ('ngiz', 'e', 'h'),
                    ('si', 'e', 'h'),
                    ('i', 'e', 'h'),
                    ('ng', 'e', 'h'),
                    ('lar', 'h', 'g'),
                    ('dagi', 'g', 'start')
                    ]
                )

    word = word.replace('dagi', '')

    i = len(word) - 1
    j = len(word)
    while(True):
        if (i<=0):
            break
        v = word[i:j]
        #print v
        res = fsm.can(v)
        if (res):
            if (v == 'i' and fsm.can(word[i-1:j])):
                i = i - 1
                continue
            fsm.trigger(v)
            if (fsm.current == 'h'):
                if (word[i-1:i]=='i'):
                    i = i - 1 #skip i
                    if (word[i-1:i]=='n' ):
                            # ning qushimchasi
                        fsm.current = 'start'
                        continue
            elif (fsm.current == 'b'):
                fsm.current = 'start'
            j = i
            # print fsm.current
        i =  i - 1
    return word[:j]

def write_data():
    for news in news_list:
        title = news[0]
        link = news[1]
        views = int(news[2])
        category = news[3]
        posted_at = datetime.strptime(news[4], '%Y/%m/%d').date()
        source = news[5]

        if not News.objects.filter(link=link).exists():
            data = News(title = title, link = link, views = views, category=category, posted_at = posted_at,  source = source)
            data.save()

before_add = News.objects.all().count()

write_data()


def store_tags():

    for news in news_list:
        for word in news[0].split():
            word = re.sub("[^a-zA-Z‘]+", "", word).lower()

            if len(word)!=0:
                word = stem(word)
                if (not WaitList.objects.filter(word=word).exists()) and (not WatchList.objects.filter(word=word).exists()) and (not IgnoreList.objects.filter(word=word).exists()):
                    tag = WaitList(word = word)
                    tag.save()
    print("DONE!")
        
#store_tags()

def print_stats():
    waitlist = len(WaitList.objects.all())
    watchlist = len(WatchList.objects.all())
    ignorelist = len(IgnoreList.objects.all())
    newslist = len(News.objects.all())
    

    print("----------------------------------")
    print("STATS:")
    print("Waitlist object numbers:", waitlist)
    print("Watchlist object numbers:", watchlist)
    print("Ignorelist object numbers:", ignorelist)
    print("Total News:", newslist)
    print(newslist-before_add, "news have been added!")

print_stats()
    

        
            
