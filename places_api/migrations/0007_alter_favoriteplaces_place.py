# Generated by Django 4.1 on 2022-09-04 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places_api', '0006_alter_favoriteplaces_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteplaces',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav', to='places_api.place'),
        ),
    ]
