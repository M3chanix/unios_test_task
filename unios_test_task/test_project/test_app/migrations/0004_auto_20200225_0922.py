# Generated by Django 3.0.3 on 2020-02-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20200224_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='Id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='state',
            name='Time',
            field=models.DateTimeField(),
        ),
    ]
