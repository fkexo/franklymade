# Generated by Django 4.2.7 on 2024-05-18 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0012_remove_courseseries_lesson_courseseries_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseseries',
            name='tag',
            field=models.ManyToManyField(related_name='course_series_tags', to='tutorial.tag'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='tutorial.category'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='tutorial.courseseries'),
        ),
    ]
