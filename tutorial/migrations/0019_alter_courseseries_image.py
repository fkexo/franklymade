# Generated by Django 4.2.7 on 2024-05-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0018_courseseries_featured_course_courseseries_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseseries',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
