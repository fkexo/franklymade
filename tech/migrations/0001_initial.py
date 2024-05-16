# Generated by Django 4.2.7 on 2024-04-14 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics/')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.SlugField()),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
                ('news_source', models.CharField(blank=True, max_length=200, null=True)),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tech.newscategory')),
            ],
        ),
    ]
