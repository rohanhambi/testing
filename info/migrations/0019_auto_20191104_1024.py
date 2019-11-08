# Generated by Django 2.1.3 on 2019-11-04 04:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0018_auto_20190726_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1-1', '1-1'), ('1-2', '1-2'), ('2-1', '2-1'), ('2-2', '2-2'), ('3-1', '3-1'), ('3-2', '3-2'), ('4-1', '4-1'), ('4-2', '4-2')], default='1-1', max_length=50)),
                ('marks1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('studentcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.StudentCourse')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sem',
            unique_together={('studentcourse', 'name')},
        ),
    ]