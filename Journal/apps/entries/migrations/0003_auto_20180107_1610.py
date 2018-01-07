# Generated by Django 2.0 on 2018-01-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20180104_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='poster_name',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='screen_name',
            field=models.CharField(max_length=100),
        ),
    ]
