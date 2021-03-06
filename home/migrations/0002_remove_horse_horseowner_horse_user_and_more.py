# Generated by Django 4.0.6 on 2022-07-24 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horse',
            name='horseOwner',
        ),
        migrations.AddField(
            model_name='horse',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='horse',
            name='acquisitionDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='horse',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='race',
            name='raceDate',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='HorseOwner',
        ),
    ]
