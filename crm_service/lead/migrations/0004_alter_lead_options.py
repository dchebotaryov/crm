# Generated by Django 4.2.5 on 2023-09-10 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_lead_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead',
            options={'ordering': ('name',)},
        ),
    ]
