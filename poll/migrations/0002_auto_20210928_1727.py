# Generated by Django 3.2.5 on 2021-09-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='option_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_three_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polls',
            name='option_two_count',
            field=models.IntegerField(default=0),
        ),
    ]
