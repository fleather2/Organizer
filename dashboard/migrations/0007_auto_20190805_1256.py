# Generated by Django 2.2.2 on 2019-08-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dateDue',
            field=models.DateField(),
        ),
    ]
