# Generated by Django 3.0.6 on 2020-05-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_remove_patient_patient_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='on_duty',
            field=models.BooleanField(default=True),
        ),
    ]
