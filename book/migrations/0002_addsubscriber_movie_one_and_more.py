# Generated by Django 4.1 on 2022-08-04 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="addsubscriber",
            name="movie_one",
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name="addsubscriber",
            name="birth_day",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="addsubscriber",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
