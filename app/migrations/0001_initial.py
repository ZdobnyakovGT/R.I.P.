# Generated by Django 5.1.1 on 2024-10-01 21:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('photo_url', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('active', 'Действует'), ('removed', 'Удалена')], default='active', max_length=100)),
            ],
            options={
                'db_table': 'topics',
            },
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('show_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('show_date', models.DateField(blank=True, null=True)),
                ('show_time', models.TimeField(blank=True, null=True)),
                ('show_name', models.CharField(blank=True, max_length=100, null=True)),
                ('show_place', models.CharField(blank=True, max_length=100, null=True)),
                ('main_topic', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Введён'), (2, 'В работе'), (3, 'Завершен'), (4, 'Отклонен'), (5, 'Удален')], default=1, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_shows', to=settings.AUTH_USER_MODEL)),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='moderated_shows', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Выставка',
                'verbose_name_plural': 'Выставки',
                'db_table': 'shows',
            },
        ),
        migrations.CreateModel(
            name='ShowTopic',
            fields=[
                ('mm_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_count', models.IntegerField(blank=True, null=True)),
                ('showw', models.ForeignKey(blank=True, db_column='showw', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.shows')),
                ('topic', models.ForeignKey(blank=True, db_column='topic', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.topics')),
            ],
            options={
                'verbose_name': 'м-м',
                'verbose_name_plural': 'м-м',
                'db_table': 'show_topic',
            },
        ),
    ]
