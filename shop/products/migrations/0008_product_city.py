# Generated by Django 3.0 on 2019-12-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191214_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
