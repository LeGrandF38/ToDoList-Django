# Generated by Django 5.0.3 on 2024-03-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=225, verbose_name='task')),
                ('is_resolved', models.BooleanField(verbose_name='Resolved?')),
            ],
        ),
    ]