# Generated by Django 3.2.5 on 2022-03-31 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rateinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['Comment_Course_ID', 'Comment_Score']},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['Course_Department', 'Course_Name']},
        ),
        migrations.AlterModelOptions(
            name='groupchat',
            options={'ordering': ['Group_Chat_ID']},
        ),
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['Instructor_Name']},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'ordering': ['Response_ID']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['User_ID']},
        ),
    ]
