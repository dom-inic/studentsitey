# Generated by Django 3.0.3 on 2020-04-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megapp', '0008_auto_20200414_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='course',
            field=models.CharField(max_length=200),
        ),
    ]
