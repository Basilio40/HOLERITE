# Generated by Django 3.2.7 on 2021-12-07 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='sobre',
        ),
        migrations.AddField(
            model_name='holerite',
            name='ano',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ponto',
            name='ano',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ponto',
            name='mes',
            field=models.CharField(choices=[('Jan', 'Janeiro'), ('Fev', 'Feveiro'), ('Mar', 'Março'), ('Abr', 'Abril'), ('Mai', 'Maio'), ('Jun', 'Junho'), ('Jul', 'Julho'), ('Ago', 'Agosto'), ('Set', 'Setembro'), ('Out', 'Outubro'), ('Nov', 'Novembro'), ('Dez', 'Dezembro')], default='Jan', max_length=4),
        ),
    ]
