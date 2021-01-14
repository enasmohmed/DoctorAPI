# Generated by Django 3.1.5 on 2021-01-13 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ('weekday', 'from_hour')},
        ),
        migrations.AlterUniqueTogether(
            name='doctor',
            unique_together={('weekday', 'from_hour', 'to_hour')},
        ),
    ]
