# Generated by Django 5.1.3 on 2024-12-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_watchreview_review_text_alter_watchreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchreview',
            name='review_text',
            field=models.TextField(),
        ),
    ]
