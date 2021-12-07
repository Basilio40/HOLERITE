# Generated by Django 3.2.5 on 2021-11-23 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilePdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_insercao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Registro')),
                ('data_modificacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Modificação')),
                ('caminho_arquivo', models.FileField(upload_to='')),
                ('nome_arquivo', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Holerite',
            fields=[
                ('filepdf_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.filepdf')),
                ('mes', models.DateField()),
            ],
            options={
                'abstract': False,
            },
            bases=('core.filepdf',),
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('filepdf_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.filepdf')),
                ('mes', models.DateField()),
            ],
            options={
                'abstract': False,
            },
            bases=('core.filepdf',),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_insercao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Registro')),
                ('data_modificacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Modificação')),
                ('nome', models.CharField(max_length=100)),
                ('sobre', models.CharField(max_length=100)),
                ('holerite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.holerite')),
                ('ponto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ponto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]