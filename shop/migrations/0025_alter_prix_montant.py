# Generated by Django 3.2.7 on 2021-10-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20211011_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prix',
            name='montant',
            field=models.FloatField(),
        ),
    ]