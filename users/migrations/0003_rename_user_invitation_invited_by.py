# Generated by Django 5.2.3 on 2025-06-21 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_invitation_invited_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="invitation",
            old_name="user",
            new_name="invited_by",
        ),
    ]
