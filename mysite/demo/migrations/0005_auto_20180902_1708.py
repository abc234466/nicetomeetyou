# Generated by Django 2.1.1 on 2018-09-02 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20180902_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ul',
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.URLField(),
        ),
    ]