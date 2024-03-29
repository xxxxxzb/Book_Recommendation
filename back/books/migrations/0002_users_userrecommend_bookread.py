# Generated by Django 4.1.2 on 2023-03-15 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(max_length=255)),
                ('mail', models.CharField(blank=True, max_length=255, null=True)),
                ('style', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserRecommend',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_id', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_recommend',
            },
        ),
        migrations.CreateModel(
            name='BookRead',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_id', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'book_read',
            },
        ),
    ]
