import requests
from datetime import datetime, timedelta
import pytz

dates = ["2021/05/22", "2021/05/22", "2021/05/01", "2021/05/07", "2021/05/22", "2021/05/08"]

now = datetime.now(pytz.timezone('Asia/Tashkent'))
day_before = now-timedelta(1)

today = now.strftime("%Y/%m/%d")
yesterday = day_before.strftime("%Y/%m/%d")


print(today, yesterday)


