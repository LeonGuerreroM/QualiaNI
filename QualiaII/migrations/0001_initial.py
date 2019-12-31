# Generated by Django 2.2.4 on 2019-11-22 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catClases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='catTiposVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='catTipoTransaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='tblCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('cuenta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tblProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=30)),
                ('subclase', models.CharField(max_length=30)),
                ('tamanio', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('existenciasMinimas', models.IntegerField()),
                ('LN', models.IntegerField(default=0)),
                ('APC', models.IntegerField(default=0)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.catClases')),
            ],
        ),
        migrations.CreateModel(
            name='tblVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.tblCliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.tblProducto')),
                ('tipoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.catTiposVenta')),
            ],
        ),
        migrations.CreateModel(
            name='tblMovimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('concepto', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.tblCliente')),
                ('tipoTransaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.catTipoTransaccion')),
            ],
        ),
        migrations.CreateModel(
            name='tblListaNegra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.tblProducto')),
            ],
        ),
        migrations.CreateModel(
            name='tblHistPrecios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.tblProducto')),
            ],
        ),
        migrations.CreateModel(
            name='tblAPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QualiaII.tblProducto')),
            ],
        ),
    ]
