# Generated by Django 5.2.1 on 2025-05-27 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
