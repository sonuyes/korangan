# Generated by Django 5.1.3 on 2025-01-24 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fishs', '0003_rename_email_reg_ko'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reg',
            old_name='ko',
            new_name='email',
        ),
    ]
