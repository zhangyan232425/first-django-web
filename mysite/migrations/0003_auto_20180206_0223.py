# Generated by Django 2.0.2 on 2018-02-06 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20171206_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='note_slug',
        ),
        migrations.AlterField(
            model_name='notebook',
            name='note_body',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
