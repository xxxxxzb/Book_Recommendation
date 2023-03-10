# Generated by Django 4.1.2 on 2023-03-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoubanBook',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_type', models.TextField()),
                ('cover', models.TextField()),
                ('title', models.TextField()),
                ('country', models.TextField()),
                ('author', models.TextField()),
                ('translator', models.TextField()),
                ('publisher', models.TextField()),
                ('pub_date', models.TextField()),
                ('price', models.TextField()),
                ('ratting', models.FloatField()),
                ('ratting_num', models.TextField()),
                ('summary', models.TextField()),
            ],
            options={
                'db_table': 'douban_book',
            },
        ),
    ]
