# Generated by Django 4.2.1 on 2023-05-15 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
