# Generated by Django 4.1.1 on 2023-03-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usernotification",
            name="read",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="usernotification",
            name="unread",
            field=models.CharField(default=1, max_length=100),
        ),
    ]
