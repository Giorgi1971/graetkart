# Generated by Django 4.0.4 on 2022-05-15 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variations',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.variation'),
            preserve_default=False,
        ),
    ]
