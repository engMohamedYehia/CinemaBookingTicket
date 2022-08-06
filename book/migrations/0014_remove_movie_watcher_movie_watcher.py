# Generated by Django 4.1 on 2022-08-05 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0013_remove_movie_watcher_movie_watcher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="watcher",
        ),
        migrations.AddField(
            model_name="movie",
            name="watcher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="book.subscriber",
            ),
        ),
    ]
