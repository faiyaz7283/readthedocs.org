# Generated by Django 2.2.16 on 2020-10-27 15:00

from django.db import migrations


def forwards_func(apps, schema_editor):
    """Migrate all protected projects to private."""
    Project = apps.get_model('projects', 'Project')
    (
        Project.objects
        .filter(privacy_level='protected')
        .update(privacy_level='private')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0065_add_feature_future_default_true'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
