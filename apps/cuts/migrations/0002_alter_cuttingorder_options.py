# Generated by Django 5.1 on 2024-09-16 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuttingorder',
            options={'permissions': [('can_assign_order', 'Can assign a cutting order'), ('can_process_order', 'Can process a cutting order')]},
        ),
    ]
