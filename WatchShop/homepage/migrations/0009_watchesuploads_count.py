# Generated by Django 5.1.3 on 2024-12-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchesuploads',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
