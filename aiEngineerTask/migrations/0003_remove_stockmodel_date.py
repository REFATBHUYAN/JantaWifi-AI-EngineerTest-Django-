# Generated by Django 5.0.1 on 2024-02-09 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aiEngineerTask', '0002_alter_stockmodel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmodel',
            name='date',
        ),
    ]