# Generated by Django 2.0.3 on 2018-04-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectiontrain',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='collectiontrain',
            name='trains',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='trains',
        ),
        migrations.AddField(
            model_name='collection',
            name='trains',
            field=models.ManyToManyField(to='manager.ModelTrain'),
        ),
        migrations.DeleteModel(
            name='CollectionTrain',
        ),
    ]
