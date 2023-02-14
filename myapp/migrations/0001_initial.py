# Generated by Django 4.1.6 on 2023-02-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'page',
            },
        ),
    ]
