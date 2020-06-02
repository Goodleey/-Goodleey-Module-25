# Generated by Django 3.0.6 on 2020-05-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=127)),
                ('car_model', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
                ('transmission', models.PositiveSmallIntegerField(choices=[(0, 'Manual'), (1, 'Automatic'), (2, 'Robot')], default=0)),
                ('color', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('maker',),
            },
        ),
    ]