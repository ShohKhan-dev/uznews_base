# Generated by Django 3.2.3 on 2021-05-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uznews', '0002_auto_20210529_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='StopWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
