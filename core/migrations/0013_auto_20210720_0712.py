# Generated by Django 3.0.3 on 2021-07-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210720_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='announce',
            name='number_of_views',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Views_announce',
        ),
    ]
