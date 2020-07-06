# Generated by Django 3.0.6 on 2020-07-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_myblog_time_req'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='code',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='time_req',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='youtube_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
