# Generated by Django 4.2.7 on 2024-05-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0003_alter_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='featured_post',
            field=models.BooleanField(default=False),
        ),
    ]