# Generated by Django 2.1.3 on 2018-12-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_available_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='available',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
