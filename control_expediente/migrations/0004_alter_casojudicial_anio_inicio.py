# Generated by Django 5.0.14 on 2025-05-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_expediente', '0003_alter_casojudicial_anio_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casojudicial',
            name='anio_inicio',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
