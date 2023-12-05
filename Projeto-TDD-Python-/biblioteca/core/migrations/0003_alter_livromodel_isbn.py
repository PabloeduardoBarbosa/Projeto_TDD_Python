# Generated by Django 4.2.7 on 2023-11-02 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_livromodel_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livromodel',
            name='isbn',
            field=models.PositiveIntegerField(unique=True, verbose_name='ISBN'),
        ),
    ]
