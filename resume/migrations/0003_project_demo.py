# Generated by Django 4.1.5 on 2023-07-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_project_sourcecode_alter_project_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Demo',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
