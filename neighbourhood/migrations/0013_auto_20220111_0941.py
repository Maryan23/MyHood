# Generated by Django 3.2.9 on 2022-01-11 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0012_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
