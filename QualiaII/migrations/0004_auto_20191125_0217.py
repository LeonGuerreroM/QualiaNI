# Generated by Django 2.2.4 on 2019-11-25 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QualiaII', '0003_auto_20191123_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblventa',
            name='tipoPago',
        ),
        migrations.DeleteModel(
            name='catTiposVenta',
        ),
    ]
