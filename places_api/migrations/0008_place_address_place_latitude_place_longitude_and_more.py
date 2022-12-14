# Generated by Django 4.1 on 2022-09-24 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places_api', '0007_alter_favoriteplaces_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='favoriteplaces',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='places_api.place'),
        ),
        migrations.AlterField(
            model_name='favoriteplaces',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
