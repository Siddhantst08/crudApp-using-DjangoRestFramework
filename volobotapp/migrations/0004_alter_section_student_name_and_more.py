# Generated by Django 5.0 on 2024-01-19 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("volobotapp", "0003_alter_section_student_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section",
            name="student_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="volobotapp.student"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="student_name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
