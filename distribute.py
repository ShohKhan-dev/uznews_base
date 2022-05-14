
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

from uznews.models import StopWords, WaitList


wordlist=WaitList.objects.all()
c=0

for item in wordlist:
    if not StopWords.objects.filter(word=item).exists():
       c+=1

print(c)