from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloom', '0001_initial'),  # Assuming your previous migration file is '0001_initial.py'
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('text', models.TextField()),
                (
                    'course_outcome',
                    models.ForeignKey(
                        null=True,
                        blank=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='bloom.courseoutcome',
                    ),
                ),
                (
                    'bloom_level',
                    models.ForeignKey(
                        null=True,
                        blank=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='bloom.bloomlevel',
                    ),
                ),
            ],
        ),
    ]
