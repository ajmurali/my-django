# Generated by Django 4.1.5 on 2023-07-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=150)),
                ('Text', models.CharField(max_length=1000)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
    ]