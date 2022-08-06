# Generated by Django 4.1 on 2022-08-05 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0010_rename_movieone_movie_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="watcher",
        ),
        migrations.AddField(
            model_name="subscriber",
            name="movie",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="book.movie"
            ),
        ),
    ]
