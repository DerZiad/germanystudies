# Generated by Django 3.1.4 on 2021-01-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='datedenaissance',
            field=models.DateField(),
        ),
    ]
