# Generated by Django 3.2.3 on 2022-02-15 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uznews', '0010_keywords_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='word',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.DeleteModel(
            name='Keywords',
        ),
    ]