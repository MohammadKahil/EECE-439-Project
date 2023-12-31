# Generated by Django 4.2.5 on 2023-09-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacts",
            fields=[
                ("contact_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                ("address", models.CharField(max_length=100)),
                ("profession", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=254)),
                ("tel", models.IntegerField()),
            ],
            options={
                "db_table": "contacts",
            },
        ),
    ]
