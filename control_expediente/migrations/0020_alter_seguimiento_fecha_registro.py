# Generated by Django 5.0.14 on 2025-05-21 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_expediente', '0019_remove_seguimiento_tlf_juzgado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento',
            name='fecha_registro',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
