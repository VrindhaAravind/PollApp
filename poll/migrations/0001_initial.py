# Generated by Django 3.2.5 on 2021-09-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=30)),
                ('option2', models.CharField(max_length=30)),
                ('option3', models.CharField(max_length=30)),
            ],
        ),
    ]
