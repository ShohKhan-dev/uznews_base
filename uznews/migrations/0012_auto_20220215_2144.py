# Generated by Django 3.2.3 on 2022-02-15 18:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uznews', '0011_auto_20220215_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='word',
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=125)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]