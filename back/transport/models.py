import json

from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'brands'
        verbose_name_plural = 'brands | Производители'


class Color(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'colors'
        verbose_name_plural = 'colors | Цвета'


class Drivetype(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'drivetypes'
        verbose_name_plural = 'driveTypes | Типы приводов'


class CarModel(models.Model):
    title = models.CharField(max_length=150)
    id_brand = models.ForeignKey(Brand, models.DO_NOTHING, db_column='id_brand', related_name='brand')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        managed = False
        db_table = 'models'
        verbose_name_plural = 'models | Модели авто'


class Ownershiptype(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'ownershiptypes'
        verbose_name_plural = 'ownershipTypes | Формы собственности'


class Technicalissue(models.Model):
    value = models.CharField(max_length=350)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'technicalissues'
        verbose_name_plural = 'technicalIssues | Технические неисправности'


class TransportTechnicalissue(models.Model):
    id_transport = models.ForeignKey('Transport', models.DO_NOTHING, db_column='id_transport')
    id_technicalissue = models.ForeignKey(Technicalissue, models.DO_NOTHING,
                                          db_column='id_technicalIssue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transports_technicalissues'
        verbose_name_plural = 'transports_technicalissues | Технические неисправности транспорта'


class Transportaction(models.Model):
    value = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'transportactions'
        verbose_name_plural = 'transportActions | Сведения об оставлении места происшествия (транспорт)'


class Transporttype(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'transporttypes'
        verbose_name_plural = 'transportTypes | Типы транспорта'


class Transport(models.Model):
    id_action = models.ForeignKey(Transportaction, models.DO_NOTHING, db_column='id_action')
    id_type = models.ForeignKey(Transporttype, models.DO_NOTHING, db_column='id_type')
    id_model = models.ForeignKey(CarModel, models.DO_NOTHING, db_column='id_model')
    id_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_color')
    id_drivetype = models.ForeignKey(Drivetype, models.DO_NOTHING,
                                     db_column='id_driveType')  # Field name made lowercase.
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_ownershiptype = models.ForeignKey(Ownershiptype, models.DO_NOTHING, db_column='id_ownershipType', blank=True,
                                         null=True)  # Field name made lowercase.

    technicalissues = models.ManyToManyField(Technicalissue, related_name='transports',
                                             through='TransportTechnicalissue')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'transports'
        verbose_name_plural = 'transports | Транспорт'
