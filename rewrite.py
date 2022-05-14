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

from uznews.models import WaitList, WatchList, IgnoreList, StopWords, News


all_news = News.objects.all()

for item in all_news:
    old_link = item.link
    if "https://kun.uz/" in old_link:
        new_link = old_link.replace("https://kun.uz/", "")
        t = News.objects.get(link=old_link)
        t.link = new_link
        t.save()

    if "https://daryo.uz/" in old_link:
        new_link = old_link.replace("https://daryo.uz/", "")
        t = News.objects.get(link=old_link)
        t.link = new_link
        t.save()