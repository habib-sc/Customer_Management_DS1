# Generated by Django 3.1.7 on 2021-03-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210227_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='search_keyword',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
