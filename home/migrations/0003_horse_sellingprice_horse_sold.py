# Generated by Django 4.0.6 on 2022-07-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_horse_horseowner_horse_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='sellingPrice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='horse',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]