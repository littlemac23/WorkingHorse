# Generated by Django 4.0.6 on 2022-07-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_horsedata_dispersmentclaim_sale_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='expenseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='raceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('dateOfRace', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('finish', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='dispersmentClaim_Sale',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='dispersmentDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='place',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='horsedata',
            name='type',
            field=models.CharField(max_length=500),
        ),
    ]