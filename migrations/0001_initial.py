# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField(verbose_name='date publicado')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='tipo',
            field=models.ForeignKey(to='articomp.Tipo_Publicacion'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='usuario_pub',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
