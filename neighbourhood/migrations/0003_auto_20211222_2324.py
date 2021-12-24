# Generated by Django 3.2.9 on 2021-12-22 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhood', '0002_auto_20211222_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='occupants_count',
            new_name='resident_count',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
