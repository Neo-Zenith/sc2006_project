# Generated by Django 4.1.1 on 2022-09-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_wishlistitem_sessionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='sessionID',
            field=models.TextField(max_length=150),
        ),
    ]