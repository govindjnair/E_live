# Generated by Django 2.2.6 on 2019-10-26 02:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('typ', models.CharField(max_length=40)),
                ('room', models.CharField(max_length=40)),
                ('watt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_energy_consumed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Component_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('last_update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='el_webI.Component_data')),
            ],
        ),
    ]