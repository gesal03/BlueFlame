# Generated by Django 4.2.1 on 2023-05-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FestivalApp', '0005_club_distinct'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='distinct',
            field=models.IntegerField(blank=True, null=True, verbose_name='DIS'),
        ),
    ]
