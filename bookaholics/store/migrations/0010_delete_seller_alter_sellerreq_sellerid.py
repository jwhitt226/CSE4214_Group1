# Generated by Django 4.2.11 on 2024-04-12 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_delete_customer_alter_customermore_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Seller',
        ),
        migrations.AlterField(
            model_name='sellerreq',
            name='sellerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
