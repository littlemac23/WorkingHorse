# Generated by Django 4.0.6 on 2022-07-16 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horsedata',
            name='dispersmentClaim_Sale',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='dispersmentDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='place',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
