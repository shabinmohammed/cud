# Generated by Django 2.2 on 2022-09-22 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_auto_20220922_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='email',
            new_name='eemail',
        ),
    ]
