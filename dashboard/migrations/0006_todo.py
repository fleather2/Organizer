# Generated by Django 2.2.2 on 2019-08-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190717_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('dateDue', models.DateTimeField()),
                ('category', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('completed', models.BooleanField()),
            ],
        ),
    ]