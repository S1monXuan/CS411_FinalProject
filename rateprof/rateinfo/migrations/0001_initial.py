# Generated by Django 3.2.5 on 2022-03-31 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Comment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Comment_Text', models.CharField(max_length=255)),
                ('Comment_Score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Course_Name', models.CharField(max_length=255)),
                ('Course_Department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('Instructor_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Instructor_Name', models.CharField(max_length=255)),
                ('Instructor_Department', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_ID', models.AutoField(primary_key=True, serialize=False)),
                ('User_Name', models.CharField(max_length=255)),
                ('User_Gender', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teaches', to='rateinfo.course')),
                ('Instructor_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teaches', to='rateinfo.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('Response_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Response_Text', models.CharField(max_length=255)),
                ('Response_Comment_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responses', to='rateinfo.comment')),
            ],
        ),
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('Group_Chat_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Message_Info', models.CharField(max_length=255)),
                ('Receive_From_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='groupchatrecieve', to='rateinfo.user')),
                ('Send_To_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='groupchatsent', to='rateinfo.user')),
            ],
        ),
        migrations.CreateModel(
            name='GP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_ID', models.IntegerField()),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gps', to='rateinfo.user')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Course_Instructor_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='rateinfo.instructor'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Course_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='rateinfo.course'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='rateinfo.user'),
        ),
    ]
