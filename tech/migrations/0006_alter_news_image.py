# Generated by Django 4.2.7 on 2024-05-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0005_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
