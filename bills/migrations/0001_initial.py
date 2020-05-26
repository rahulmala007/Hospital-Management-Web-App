# Generated by Django 3.0.5 on 2020-05-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('all_cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('bill_date', models.DateField()),
                ('bill_details', models.CharField(max_length=200)),
                ('is_paid', models.BooleanField(default=False)),
                ('remaining_amount', models.IntegerField()),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_case', to='all_cases.case')),
            ],
        ),
    ]
