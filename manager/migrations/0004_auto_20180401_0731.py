# Generated by Django 2.0.3 on 2018-04-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20180401_0728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeltrain',
            name='collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='trains',
            field=models.ManyToManyField(to='manager.ModelTrain'),
        ),
    ]