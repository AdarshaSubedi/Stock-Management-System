# Generated by Django 2.2.1 on 2019-05-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='sales',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]