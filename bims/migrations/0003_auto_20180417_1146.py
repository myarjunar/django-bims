# Generated by Django 2.0.4 on 2018-04-17 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bims', '0002_biologicalcollectionrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biologicalcollectionrecord',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biological_collection_record', to='bims.LocationSite'),
        ),
    ]