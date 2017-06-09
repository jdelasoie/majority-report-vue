# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surveys.Choice'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='surveys.Survey'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='judgment',
            field=models.IntegerField(choices=[(1, 'A rejeter'), (2, 'Insuffisant-e'), (3, 'Passable'), (4, 'Assez bien'), (5, 'Bien'), (6, 'Tr\xe8s bien'), (7, 'Excellent')], default=1, max_length=2),
        ),
    ]