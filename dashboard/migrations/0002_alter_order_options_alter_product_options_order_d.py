# Generated by Django 4.0.2 on 2022-03-17 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.AddField(
            model_name='order',
            name='d',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]