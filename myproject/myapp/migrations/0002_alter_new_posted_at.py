# Generated by Django 4.2.2 on 2023-06-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted_at',
            field=models.DateTimeField(),
        ),
    ]
