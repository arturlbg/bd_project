# Generated by Django 4.2.1 on 2023-05-22 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_agendamento_table_alter_cliente_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='idagendamento',
            new_name='idAgendamento',
        ),
        migrations.RenameField(
            model_name='venda',
            old_name='idvenda',
            new_name='idVenda',
        ),
    ]
