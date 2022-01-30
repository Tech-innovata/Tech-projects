# Generated by Django 4.0 on 2022-01-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmasapp', '0005_alter_student_paragraphs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('givenname', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=100)),
                ('yearofstudy', models.CharField(max_length=100)),
                ('formerschool', models.CharField(max_length=100)),
                ('parent', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Update',
        ),
    ]