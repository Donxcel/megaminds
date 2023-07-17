# Generated by Django 4.2.2 on 2023-07-16 00:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addservice',
            fields=[
                ('service_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.CharField(max_length=100)),
                ('service_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
