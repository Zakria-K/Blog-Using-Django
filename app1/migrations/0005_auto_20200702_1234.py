# Generated by Django 3.0.6 on 2020-07-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20200702_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='youtube_link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
