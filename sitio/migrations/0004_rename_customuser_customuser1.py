# Generated by Django 4.2.5 on 2023-09-13 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('sitio', '0003_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='CustomUser1',
        ),
    ]
