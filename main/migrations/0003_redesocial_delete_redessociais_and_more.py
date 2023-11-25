# Generated by Django 4.2.7 on 2023-11-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_redessociais_alter_contrato_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedeSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25, verbose_name='Nome da rede social')),
                ('link', models.URLField(verbose_name='Link')),
                ('icone', models.CharField(max_length=250, verbose_name='Ícone')),
            ],
            options={
                'verbose_name': 'Rede Social',
                'verbose_name_plural': 'Redes Sociais',
            },
        ),
        migrations.DeleteModel(
            name='RedesSociais',
        ),
        migrations.AlterField(
            model_name='contrato',
            name='documento',
            field=models.FileField(upload_to='contratos/', verbose_name='Faça upload do contrato'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='nome',
            field=models.CharField(max_length=255, verbose_name='Nome do Contrato'),
        ),
    ]
