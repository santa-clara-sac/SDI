# Generated by Django 5.0.14 on 2025-05-21 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_expediente', '0016_seguimiento_inter'),
    ]

    operations = [
        migrations.AddField(
            model_name='seguimiento',
            name='tlf_juzgado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seguimiento',
            name='estado',
            field=models.CharField(choices=[('En proceso', 'En Proceso'), ('Finalizado', 'Finalizado'), ('Presentado', 'Presentado'), ('Notificado', 'Notificado')], default='en_proceso', max_length=20),
        ),
    ]
