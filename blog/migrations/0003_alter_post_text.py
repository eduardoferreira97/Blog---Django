# Generated by Django 4.1 on 2022-12-07 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_remove_author_sign_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="text", field=models.TextField(),
        ),
    ]
