# Generated by Django 2.2.6 on 2019-10-10 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20191010_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]