# Generated by Django 3.2 on 2021-04-06 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('description', models.CharField(help_text='Enter field documentation', max_length=255)),
                ('genre', models.CharField(help_text='Enter field documentation', max_length=10)),
            ],
            options={
                'ordering': ['-name', '-character_c', '-description'],
            },
        ),
        migrations.CreateModel(
            name='Character_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter field documentation', max_length=20)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter field documentation', max_length=20)),
                ('description', models.CharField(help_text='Enter field documentation', max_length=255)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Game.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='character_c',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Game.character_class'),
        ),
    ]
