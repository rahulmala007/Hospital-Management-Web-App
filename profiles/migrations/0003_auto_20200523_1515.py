# Generated by Django 3.0.5 on 2020-05-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200523_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient_id',
        ),
        migrations.AddField(
            model_name='patient',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
