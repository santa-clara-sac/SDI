# Generated by Django 5.0.14 on 2025-05-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_expediente', '0022_alter_seguimiento_resolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento',
            name='responsable',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
