from django.contrib import admin

# Register your models here.

from .models import Keywords, News, WatchList


admin.site.register(News)
admin.site.register(WatchList)
admin.site.register(Keywords)
