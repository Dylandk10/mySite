# Generated by Django 3.0.7 on 2020-06-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='highscores',
            name='rank',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
