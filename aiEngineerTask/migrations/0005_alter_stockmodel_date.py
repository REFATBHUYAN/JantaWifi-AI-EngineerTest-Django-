# Generated by Django 5.0.1 on 2024-02-10 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiEngineerTask', '0004_stockmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmodel',
            name='date',
            field=models.DateField(),
        ),
    ]
