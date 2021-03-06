# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 23:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=128)),
                ('complemento', models.CharField(max_length=256, null=True)),
                ('uf', models.CharField(max_length=2, null=True)),
                ('cidade', models.CharField(max_length=64, null=True)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.TextField()),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pessoas', to='eventos.Endereco')),
                ('ususario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
