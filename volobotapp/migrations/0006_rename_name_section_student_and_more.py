# Generated by Django 5.0 on 2024-01-19 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("volobotapp", "0005_rename_student_name_section_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="section",
            old_name="name",
            new_name="student",
        ),
        migrations.RenameField(
            model_name="section",
            old_name="section",
            new_name="studentSection",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="age",
            new_name="studentGender",
        ),
        migrations.RenameField(
            model_name="student",
            old_name="student_name",
            new_name="studentName",
        ),
    ]
