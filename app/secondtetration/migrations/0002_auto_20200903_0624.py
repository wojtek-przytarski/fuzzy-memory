# Generated by Django 3.1.1 on 2020-09-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("secondtetration", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="secondtetrationresult",
            name="number",
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name="secondtetrationresult",
            name="result",
            field=models.CharField(max_length=500001),
        ),
    ]
