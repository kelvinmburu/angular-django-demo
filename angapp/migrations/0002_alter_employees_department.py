# Generated by Django 4.0.5 on 2022-07-03 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('angapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_name', to='angapp.department'),
        ),
    ]
