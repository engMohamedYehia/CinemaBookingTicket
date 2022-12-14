# Generated by Django 4.1 on 2022-08-05 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0006_addsubscriber_movie_two"),
    ]

    operations = [
        migrations.CreateModel(
            name="MovieOne",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("movie_name", models.CharField(max_length=100, null=True)),
                ("movie_status", models.BooleanField(default=False, null=True)),
                ("movie_date", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subscribers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                ("birth_day", models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="AddSubscriber",
        ),
        migrations.AddField(
            model_name="movieone",
            name="subscriber",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="book.subscribers"
            ),
        ),
    ]
