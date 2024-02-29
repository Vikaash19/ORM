# Generated by Django 5.0.2 on 2024-02-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("bid", models.IntegerField(primary_key=True, serialize=False)),
                ("bname", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("author", models.CharField(max_length=50)),
                ("qty", models.IntegerField()),
            ],
        ),
    ]
