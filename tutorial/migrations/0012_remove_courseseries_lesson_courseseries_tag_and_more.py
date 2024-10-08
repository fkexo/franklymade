# Generated by Django 4.2.7 on 2024-05-16 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0011_category_courseseries_tag_remove_lesson_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseseries',
            name='lesson',
        ),
        migrations.AddField(
            model_name='courseseries',
            name='tag',
            field=models.ManyToManyField(default='python', to='tutorial.tag'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.courseseries'),
        ),
    ]
