# Generated by Django 3.1.1 on 2022-01-08 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220108_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='preco',
            new_name='price',
        ),
    ]
