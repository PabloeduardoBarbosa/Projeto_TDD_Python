# Generated by Django 4.2.7 on 2023-11-28 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_livromodel_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livromodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
