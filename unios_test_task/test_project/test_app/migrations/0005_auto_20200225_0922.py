# Generated by Django 3.0.3 on 2020-02-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_auto_20200225_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='Time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
