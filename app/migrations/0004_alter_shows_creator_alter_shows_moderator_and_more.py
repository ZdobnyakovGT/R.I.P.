# Generated by Django 5.1.1 on 2024-09-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_showtopic_showw_showtopic_topic_alter_shows_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='creator',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shows',
            name='moderator',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shows',
            name='status',
            field=models.CharField(blank=True, default='1', max_length=100, null=True),
        ),
    ]