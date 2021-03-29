# Generated by Django 3.0.5 on 2020-06-30 13:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('transport', '0005_auto_20200629_2326'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Drivingchange',
        ),
        migrations.DeleteModel(
            name='Incident',
        ),
        migrations.DeleteModel(
            name='Incidenttype',
        ),
        migrations.DeleteModel(
            name='Influencefactor',
        ),
        migrations.DeleteModel(
            name='InfluencefactorIncident',
        ),
        migrations.DeleteModel(
            name='Lighting',
        ),
        migrations.DeleteModel(
            name='Locality',
        ),
        migrations.DeleteModel(
            name='Object',
        ),
        migrations.DeleteModel(
            name='ObjectnearIncident',
        ),
        migrations.DeleteModel(
            name='ObjectonIncident',
        ),
        migrations.DeleteModel(
            name='ParticipantIncident',
        ),
        migrations.DeleteModel(
            name='Road',
        ),
        migrations.DeleteModel(
            name='Roaddisadvantage',
        ),
        migrations.DeleteModel(
            name='RoaddisadvantageIncident',
        ),
        migrations.DeleteModel(
            name='Roadimportance',
        ),
        migrations.DeleteModel(
            name='Roadwaystatus',
        ),
        migrations.DeleteModel(
            name='Streetcategory',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
        migrations.DeleteModel(
            name='WeatherIncident',
        ),
    ]