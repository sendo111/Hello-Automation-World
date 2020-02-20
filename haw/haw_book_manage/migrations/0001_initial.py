# Generated by Django 2.0 on 2020-02-14 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('author', models.CharField(default='', max_length=50)),
                ('publisher', models.CharField(default='', max_length=50)),
                ('finished_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
