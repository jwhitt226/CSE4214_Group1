# Generated by Django 4.2.11 on 2024-03-25 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_sellerreq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
            ],
            options={
                'ordering': ['isbn'],
            },
        ),
        migrations.CreateModel(
            name='OrderHist',
            fields=[
                ('orderID', models.IntegerField(primary_key=True, serialize=False)),
                ('dateOrdered', models.DateField(auto_now_add=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numItems', models.IntegerField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.user')),
            ],
            options={
                'ordering': ['dateOrdered'],
            },
        ),
    ]
