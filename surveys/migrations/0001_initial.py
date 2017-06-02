# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-02 13:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('comment', models.TextField(help_text='R\xe9digez un commentaire indiquant aux destinataires pourquoi vous les sollicitez, et \xe0 quoi serviront les r\xe9sultats.', max_length=512)),
                ('date_limit', models.DateTimeField(verbose_name='date published')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judgment', models.CharField(choices=[('REJECT', 'A rejeter'), ('INSUFFISANT', 'Insuffisant-e'), ('PASSABLE', 'Passable'), ('ASSEZ_BIEN', 'Assez bien'), ('BIEN', 'Bien'), ('TRES_BIEN', 'Tr\xe8s bien'), ('EXCELLENT', 'Excellent')], max_length=55)),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.Survey'),
        ),
    ]
