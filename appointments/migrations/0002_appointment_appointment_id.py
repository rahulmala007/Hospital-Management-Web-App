# Generated by Django 3.0.5 on 2020-05-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]