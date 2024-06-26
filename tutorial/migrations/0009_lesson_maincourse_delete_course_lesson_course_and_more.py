# Generated by Django 4.2.7 on 2024-04-17 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0008_alter_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(null=True)),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
                ('lesson_content', models.TextField(blank=True, null=True)),
                ('lesson_count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.author')),
            ],
        ),
        migrations.CreateModel(
            name='MainCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('description', models.TextField(default='description')),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.maincourse'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorial.coursecategory'),
        ),
    ]
