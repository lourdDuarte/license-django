# Generated by Django 4.1 on 2022-10-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
