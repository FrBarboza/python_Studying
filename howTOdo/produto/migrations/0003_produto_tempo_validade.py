# Generated by Django 3.0.3 on 2020-02-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('produto', '0002_auto_20200226_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tempo_validade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
