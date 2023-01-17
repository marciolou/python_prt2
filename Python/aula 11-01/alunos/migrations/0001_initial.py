# Generated by Django 4.1.5 on 2023-01-17 00:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=150)),
                ('descricao_profissional', models.TextField()),
                ('descricao_pessoal', models.TextField()),
                ('habilidades', models.CharField(max_length=150)),
                ('comportamento', models.CharField(max_length=150)),
                ('workspace', models.CharField(max_length=150)),
                ('categoria', models.CharField(max_length=150)),
                ('date_aluno', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
