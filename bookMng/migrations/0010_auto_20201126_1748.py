# Generated by Django 3.1.3 on 2020-11-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0009_auto_20201126_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]