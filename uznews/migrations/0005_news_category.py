# Generated by Django 3.2.3 on 2021-07-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uznews', '0004_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
