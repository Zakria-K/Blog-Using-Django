# Generated by Django 3.0.6 on 2020-07-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myblog',
            name='time_req',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
    ]