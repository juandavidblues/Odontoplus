# Generated by Django 2.0.7 on 2018-11-30 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181129_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, choices=[('Asesor', 'Asesor'), ('Odontologo', 'Odontologo')], max_length=100, null=True),
        ),
    ]
