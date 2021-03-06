# Generated by Django 3.2.7 on 2021-10-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Created_mon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creator', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('region', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('type1', models.CharField(max_length=100)),
                ('type2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.BooleanField()),
            ],
        ),
    ]
