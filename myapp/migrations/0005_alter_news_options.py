# Generated by Django 4.0 on 2023-02-14 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_news_text_alter_page_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]
