# Generated by Django 4.0.2 on 2023-08-08 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0002_school_address_school_county_school_curriculum_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=80)),
                ('last_name', models.CharField(default='', max_length=80)),
                ('dob', models.DateField()),
                ('gender', models.CharField(default='', max_length=80)),
                ('email', models.CharField(default='', max_length=80)),
                ('tel', models.CharField(default='', max_length=80)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpers.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=80)),
                ('last_name', models.CharField(default='', max_length=80)),
                ('dob', models.DateField()),
                ('gender', models.CharField(default='', max_length=80)),
                ('disability', models.CharField(choices=[('BLIND', 'VISION IMPAIRED'), ('DEAF', 'HARD OF HEARING'), ('AUTISM', 'AUTISM'), ('PHYSICAL IMPAIRMENT', 'PHYSICAL IMPAIRMENT'), ('COGNITIVE', 'COGNITIVE'), ('PSYCHOLOGICAL', 'PSYCHOLOGICAL')], default='none', max_length=20)),
                ('stream', models.CharField(default='', max_length=80)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpers.school')),
            ],
        ),
    ]
