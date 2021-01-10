# Generated by Django 3.1.4 on 2021-01-08 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grammar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jeu', models.TextField(max_length=500)),
                ('losung', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=100)),
                ('NQ', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Grammar.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Choix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mog', models.CharField(max_length=15)),
                ('numf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grammar.quiz')),
            ],
        ),
    ]
