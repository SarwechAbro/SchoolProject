# Generated by Django 5.1.2 on 2024-12-11 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_chapter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='class_id',
            field=models.ManyToManyField(blank=True, to='myapp.class'),
        ),
    ]
