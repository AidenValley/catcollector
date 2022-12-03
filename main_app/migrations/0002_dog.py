# Generated by Django 4.1.3 on 2022-12-03 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dog",
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
                ("name", models.CharField(max_length=100)),
                ("breed", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=250)),
                ("age", models.IntegerField()),
            ],
        ),
    ]
