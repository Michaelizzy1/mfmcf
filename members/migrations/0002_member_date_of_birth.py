# Generated by Django 4.0 on 2023-06-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]