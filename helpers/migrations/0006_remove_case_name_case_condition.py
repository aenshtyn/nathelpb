# Generated by Django 4.0.2 on 2024-01-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0005_rename_issue_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='name',
        ),
        migrations.AddField(
            model_name='case',
            name='condition',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='helpers.condition'),
        ),
    ]
