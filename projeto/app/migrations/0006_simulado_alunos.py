# Generated by Django 5.1.3 on 2024-11-29 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_turma_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulado',
            name='alunos',
            field=models.ManyToManyField(related_name='simulados', to='app.aluno'),
        ),
    ]
