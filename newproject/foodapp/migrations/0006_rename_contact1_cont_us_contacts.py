# Generated by Django 5.1.1 on 2025-05-12 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_rename_con_cont_us_contact1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cont_us',
            old_name='contact1',
            new_name='contacts',
        ),
    ]
