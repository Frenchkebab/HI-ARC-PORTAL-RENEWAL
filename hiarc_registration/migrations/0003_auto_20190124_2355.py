# Generated by Django 2.1.2 on 2019-01-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiarc_registration', '0002_auto_20190112_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiarcuser',
            name='first_name',
            field=models.CharField(default='', max_length=20, verbose_name='first_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hiarcuser',
            name='last_name',
            field=models.CharField(default='', max_length=20, verbose_name='last_name'),
            preserve_default=False,
        ),
    ]