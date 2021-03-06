# Generated by Django 3.2.6 on 2021-09-08 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=30)),
                ('PRN_No', models.CharField(max_length=20)),
                ('Mother_Name', models.CharField(max_length=13)),
                ('Contact_Number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_Name', models.CharField(max_length=20)),
                ('Obtained_Marks', models.FloatField()),
                ('Maximum_Marks', models.FloatField()),
                ('Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SRMS.addstudent')),
            ],
        ),
    ]
