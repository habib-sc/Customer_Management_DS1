# Generated by Django 3.1.7 on 2021-02-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210224_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], max_length=200, null=True),
        ),
    ]
