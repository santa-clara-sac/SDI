# Generated by Django 5.0.14 on 2025-05-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_expediente', '0028_alter_casojudicial_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casojudicial',
            name='materia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
