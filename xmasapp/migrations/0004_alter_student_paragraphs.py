# Generated by Django 4.0 on 2021-12-26 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmasapp', '0003_student_paragraphs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Paragraphs',
            field=models.TextField(max_length=500, null=True),
        ),
    ]