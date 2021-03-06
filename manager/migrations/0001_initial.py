# Generated by Django 2.0.3 on 2018-04-03 23:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionTrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='ModelTrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(choices=[('A.C. Glibert Company', 'A. C. Gilbert Company'), ('American Flyer', 'American Flyer'), ('Bachmann Industries', 'Bachmann Industries'), ('Bassett-Lowke', 'Bassett-Lowke'), ('Bing (company)', 'Bing (company)'), ('Boucher Manufacturing Company', 'Boucher Manufacturing Company'), ('Bowser Manufacturing', 'Bowser Manufacturing'), ('Brio (company)', 'Brio (company)'), ('Buddy L', 'Buddy L'), ('Carlisle & Finch', 'Carlisle & Finch'), ('Choo Choo Track & Toy Co', 'Choo Choo Track & Toy Co'), ('Dapol', 'Dapol'), ('Dorfan', 'Dorfan'), ('Fandor', 'Fandor'), ('Fleischmann (model railroads)', 'Fleischmann (model railroads)'), ('G & R Wrenn', 'G & R Wrenn'), ('Bob Grubba', 'Bob Grubba'), ('Hafner Manufacturing Company', 'Hafner Manufacturing Company'), ('HAG', 'HAG'), ('Hornby Railways', 'Hornby Railways'), ('Ibertren', 'Ibertren'), ('Ives Manufacturing Company', 'Ives Manufacturing Company'), ('K-Line', 'K-Line'), ('Kader', 'Kader'), ('Kato Precision Railroad Models', 'Kato Precision Railroad Models'), ('Leeds Model Company', 'Leeds Model Company'), ('Lego', 'Lego'), ('Lima (models)', 'Lima (models)'), ('Lionel Corporation', 'Lionel Corporation'), ('Lionel, LLC', 'Lionel, LLC'), ('Lone Star Toys', 'Lone Star Toys'), ('Louis Marx and Company', 'Louis Marx and Company'), ('Märklin', 'Märklin'), ('Mamod', 'Mamod'), ('Maple Landmark Woodcraft', 'Maple Landmark Woodcraft'), ('McCoy Manufacturing', 'McCoy Manufacturing'), ('Mettoy', 'Mettoy'), ('Minitrix', 'Minitrix'), ('MTH Electric Trains', 'MTH Electric Trains'), ('Noch (model railroads)', 'Noch (model railroads)'), ('Penn Line Manufacturing', 'Penn Line Manufacturing'), ('Playmobil', 'Playmobil'), ('Rivarossi', 'Rivarossi'), ('Rokal', 'Rokal'), ('Tomy', 'Tomy'), ('Tri-ang Railways', 'Tri-ang Railways'), ('Unique Art', 'Unique Art'), ('USA Trains', 'USA Trains'), ('Varney Scale Models', 'Varney Scale Models'), ('Voltamp', 'Voltamp'), ('Whittle Shortline', 'Whittle Shortline'), ('Wilesco', 'Wilesco'), ('Williams Electric Trains', 'Williams Electric Trains')], default='A.C. Glibert Company', max_length=100)),
                ('model_class', models.CharField(max_length=30)),
                ('traction', models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('Steam', 'Steam'), ('Electric', 'Electric')], default='Diesel', max_length=10)),
                ('scale', models.CharField(choices=[('OO', 'OO'), ('HO', 'HO'), ('TT', 'TT'), ('N', 'N')], default='OO', max_length=2)),
                ('era', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='collectiontrain',
            name='trains',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.ModelTrain'),
        ),
        migrations.AddField(
            model_name='collection',
            name='trains',
            field=models.ManyToManyField(blank=True, through='manager.CollectionTrain', to='manager.ModelTrain'),
        ),
    ]
