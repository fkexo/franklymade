# Generated by Django 4.2.7 on 2024-05-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0004_news_featured_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]