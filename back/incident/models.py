import datetime

from django.db import models


class Address(models.Model):
    id_road = models.ForeignKey('Road', models.DO_NOTHING, db_column='id_road')
    street = models.CharField(max_length=75, blank=True, null=True)
    house = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longtitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'
        verbose_name_plural = 'addresses | Адреса'

    def __str__(self):
        return f'р-он: {self.id_road.id_locality.id_district if self.id_road.id_locality.id_district != None and self.id_road.id_locality.id_district != "" else "-"}, ' \
               f'НП: {self.id_road.id_locality if (self.id_road.id_locality != None and self.id_road.id_locality != "") else "-"}, ' \
               f'дорога: {self.id_road if self.id_road != None and self.id_road != "" else "-"}, ' \
               f'{self.street if self.street != None and self.street != "" else "-"}, ' \
               f'д. {self.house if self.house != None and self.house != "" else "-"}'


class District(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    id_subject = models.ForeignKey('Subject', models.DO_NOTHING, db_column='id_subject')
    title = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'districts'
        verbose_name_plural = 'districts | Районы'


class Drivingchange(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'drivingchanges'
        verbose_name_plural = 'drivingChanges | Изменения в движении'


class Lighting(models.Model):
    value = models.CharField(max_length=45)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'lightings'
        verbose_name_plural = 'lightings | Освещение'


class Incidenttype(models.Model):
    value = models.CharField(max_length=300)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'incidenttypes'
        verbose_name_plural = 'incidentTypes | Типы происшествий'


class Roadwaystatus(models.Model):
    value = models.CharField(max_length=45)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'roadwaystatuses'
        verbose_name_plural = 'roadwayStatuses | Состояния проезжей части'


class Influencefactor(models.Model):
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'influencefactors'
        verbose_name_plural = 'influenceFactors | Факторы, оказывающие влияние на режим движения'


class Locality(models.Model):
    id_district = models.ForeignKey(District, models.DO_NOTHING, db_column='id_district')
    title = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'localities'
        verbose_name_plural = 'localities | Населенные пункты'


class Object(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'objects'
        verbose_name_plural = 'objects | Объекты УДС'


class Roaddisadvantage(models.Model):
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'roaddisadvantages'
        verbose_name_plural = 'roadDisadvantages | Недостатки дорожного покрытия'


class Roadimportance(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'roadimportance'
        verbose_name_plural = 'roadImportance | Значения дорог'


class Road(models.Model):
    id_locality = models.ForeignKey(Locality, models.DO_NOTHING, db_column='id_locality')
    title = models.CharField(max_length=300, blank=True, null=True)
    id_importance = models.ForeignKey(Roadimportance, models.DO_NOTHING, db_column='id_importance', blank=True,
                                      null=True)
    category = models.PositiveIntegerField(blank=True, null=True)
    id_streetcategory = models.ForeignKey('Streetcategory', models.DO_NOTHING, db_column='id_streetCategory',
                                          blank=True,
                                          null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.title}'

    class Meta:
        managed = False
        db_table = 'roads'
        verbose_name_plural = 'roads |  Дороги'


class Streetcategory(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'streetcategories'
        verbose_name_plural = 'streetCategories | Категории улиц'


class Subject(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'subjects'
        verbose_name_plural = 'subjects | Субъекты'


class Weather(models.Model):
    value = models.CharField(max_length=45)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'weathers'
        verbose_name_plural = 'weathers | Погодные условия'


class Incident(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    id_address = models.ForeignKey(Address, models.DO_NOTHING, db_column='id_address')
    id_type = models.ForeignKey(Incidenttype, models.DO_NOTHING, db_column='id_type')
    id_roadwaystatus = models.ForeignKey(Roadwaystatus, models.DO_NOTHING,
                                         db_column='id_roadwaystatus')  # Field name made lowercase.
    id_lighting = models.ForeignKey(Lighting, models.DO_NOTHING, db_column='id_lighting')
    id_drivingchange = models.ForeignKey(Drivingchange, models.DO_NOTHING,
                                         db_column='id_drivingChange')  # Field name made lowercase.
    deaths = models.IntegerField()
    wounds = models.IntegerField()

    objectsNear = models.ManyToManyField(Object, related_name='incidentObjectNear+',
                                         through='IncidentObjectNear')
    objectsOn = models.ManyToManyField(Object, related_name='incidentObjectOn+',
                                       through='IncidentObjectOn')
    influenceFactors = models.ManyToManyField(Influencefactor, related_name='incidentInfluenceFactor',
                                              through='IncidentInfluenceFactor')
    roadDisadvantages = models.ManyToManyField(Roaddisadvantage, related_name='incidentRoadDisadvantage',
                                               through='IncidentRoadDisadvantage')
    weathers = models.ManyToManyField(Weather, related_name='incidentWeather',
                                      through='IncidentWeather')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'incidents'
        verbose_name_plural = 'incidents | Происшествия'


class IncidentInfluenceFactor(models.Model):
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident')
    id_influencefactor = models.ForeignKey(Influencefactor, models.DO_NOTHING,
                                           db_column='id_influenceFactor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidents_influenceFactors'
        verbose_name_plural = 'incidents_influenceFactors | Факторы относительно происшествия'


class IncidentObjectnear(models.Model):
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident')
    id_objectnear = models.ForeignKey(Object, models.DO_NOTHING,
                                      db_column='id_objectNear')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidents_objectsNear'
        verbose_name_plural = 'incidents_objectsNear | Объекты УДС вблизи места происшествия'


class IncidentObjecton(models.Model):
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident')
    id_objecton = models.ForeignKey(Object, models.DO_NOTHING, db_column='id_objectOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidents_objectson'
        verbose_name_plural = 'incidents_objectson | Объекты УДС на месте происшествия'


class IncidentParticipant(models.Model):
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident')
    id_participant = models.ForeignKey('participant.Participant', models.DO_NOTHING, db_column='id_participant')

    class Meta:
        managed = False
        db_table = 'incidents_participants'
        verbose_name_plural = 'incidents_participants | Участники в происшествии'


class IncidentRoaddisadvantage(models.Model):
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident')
    id_roaddisadvantage = models.ForeignKey(Roaddisadvantage, models.DO_NOTHING,
                                            db_column='id_roadDisadvantage')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidents_roaddisadvantages'
        verbose_name_plural = 'incidents_roaddisadvantages | Недостатки дорожного покрытия относительно происшествия'


class IncidentWeather(models.Model):
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident')
    id_weather = models.ForeignKey(Weather, models.DO_NOTHING, db_column='id_weather')

    class Meta:
        managed = False
        db_table = 'incidents_weathers'
        verbose_name_plural = 'incidents_weathers | Погодные условия для происшествия'
