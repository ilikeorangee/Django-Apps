# Generated by Django 2.2.3 on 2019-08-02 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20190802_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='descritpion',
            new_name='description',
        ),
    ]
