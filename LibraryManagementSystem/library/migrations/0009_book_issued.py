# Generated by Django 5.1.4 on 2025-03-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_issuedbook_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issued',
            field=models.BooleanField(default=False),
        ),
    ]
