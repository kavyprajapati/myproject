# Generated by Django 5.1.1 on 2025-05-12 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_alter_cont_us_con'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cont_us',
            old_name='con',
            new_name='contact1',
        ),
    ]
