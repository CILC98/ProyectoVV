# Generated by Django 4.0 on 2022-01-19 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gantt', '0002_miembro_tarea_responsable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='responsable',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='Gantt.miembro'),
        ),
    ]