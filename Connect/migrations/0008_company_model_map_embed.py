# Generated by Django 3.0.6 on 2020-06-25 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect', '0007_company_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_model',
            name='map_embed',
            field=models.TextField(blank=True, null=True),
        ),
    ]
