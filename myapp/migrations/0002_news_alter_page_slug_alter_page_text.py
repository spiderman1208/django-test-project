# Generated by Django 4.1.6 on 2023-02-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=255)),
                ('slug', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'db_table': 'news_list',
            },
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='page',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
