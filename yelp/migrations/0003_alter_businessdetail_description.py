# Generated by Django 5.0.6 on 2024-05-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelp', '0002_alter_businessdetail_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetail',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
