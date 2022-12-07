# Generated by Django 4.1 on 2022-12-07 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_post_text"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="author",),
        migrations.AlterField(
            model_name="author",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.post"
            ),
        ),
    ]