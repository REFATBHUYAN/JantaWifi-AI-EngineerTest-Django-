# Generated by Django 5.0.1 on 2024-02-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiEngineerTask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmodel',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
