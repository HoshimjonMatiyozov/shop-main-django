# Generated by Django 5.1.1 on 2024-09-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="status",
            field=models.SmallIntegerField(
                choices=[(0, "Yangi"), (1, "Tasdiqlanmagan"), (2, "Tasdiqlangan")],
                default=0,
            ),
        ),
        migrations.AlterField(
            model_name="shop",
            name="status",
            field=models.SmallIntegerField(
                choices=[(0, "Yangi"), (1, "Tasdiqlanmagan"), (2, "Tasdiqlangan")],
                default=0,
            ),
        ),
    ]
