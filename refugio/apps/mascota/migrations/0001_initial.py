# Generated by Django 2.2 on 2019-04-20 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_rescate', models.DateField()),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona')),
                ('vacuna', models.ManyToManyField(blank=True, to='mascota.Vacuna')),
            ],
            options={
                'verbose_name': 'Mascota',
            },
        ),
    ]
