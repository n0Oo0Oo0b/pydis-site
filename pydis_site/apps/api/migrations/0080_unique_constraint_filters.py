# Generated by Django 3.1.14 on 2022-03-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0079_new_filter_schema'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='filter',
            constraint=models.UniqueConstraint(fields=(
                'dm_content',
                'dm_embed',
                'infraction_type',
                'infraction_reason',
                'infraction_duration',
                'content',
                'additional_field',
                'filter_list',
                'guild_pings',
                'filter_dm',
                'dm_pings',
                'delete_messages',
                'bypass_roles',
                'enabled',
                'send_alert',
                'enabled_channels',
                'disabled_channels',
                'disabled_categories'
            ), name='unique_filters'),
        ),
    ]
