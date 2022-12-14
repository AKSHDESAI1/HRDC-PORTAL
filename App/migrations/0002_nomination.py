# Generated by Django 4.0.4 on 2022-09-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeName', models.TextField()),
                ('EmployeeId', models.IntegerField()),
                ('Branch', models.CharField(max_length=10)),
                ('FunctionDepartment', models.CharField(max_length=10)),
                ('ContactNo', models.BigIntegerField()),
                ('ContactNoMobile', models.BigIntegerField()),
                ('ReportingAuthority', models.TextField()),
                ('TotalExperience', models.TextField()),
                ('TotalTeachingExperience', models.TextField()),
                ('Batch', models.TextField()),
            ],
        ),
    ]
