# Generated by Django 5.0.6 on 2024-11-28 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_professor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='simulado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.simulado'),
        ),
    ]
