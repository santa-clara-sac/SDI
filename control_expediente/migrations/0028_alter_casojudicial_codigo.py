# Generated by Django 5.0.14 on 2025-05-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_expediente', '0027_alter_casojudicial_juzgado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casojudicial',
            name='codigo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
