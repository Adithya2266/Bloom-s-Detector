# Generated by Django 4.2.10 on 2024-10-29 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloom', '0005_merge_20241004_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programoutcome',
            name='course_outcomes',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]