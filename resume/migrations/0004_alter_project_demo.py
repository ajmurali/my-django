# Generated by Django 4.2.2 on 2023-08-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_project_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Demo',
            field=models.CharField(default=1, max_length=1000),
        ),
    ]