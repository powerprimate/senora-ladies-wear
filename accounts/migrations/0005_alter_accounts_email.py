# Generated by Django 3.2.13 on 2022-07-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_accounts_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]