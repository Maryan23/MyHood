# Generated by Django 3.2.9 on 2022-01-03 10:15

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_auto_20211222_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='hood_image'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.location'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.location'),
        ),
    ]
