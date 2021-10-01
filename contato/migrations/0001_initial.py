# Generated by Django 3.2.6 on 2021-10-01 14:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(blank=True, max_length=255, verbose_name='Sobrenome')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='E-mail')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data inclusão')),
                ('descricao', models.TextField(blank=True, verbose_name='Categoria')),
                ('mostrar', models.BooleanField(default=True, verbose_name='Mostrar CTT')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/', verbose_name='Foto')),
            ],
        ),
    ]
