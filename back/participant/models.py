from enum import Enum

from django.db import models


class Consiquence(models.Model):
    value = models.CharField(max_length=300)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'consiquences'
        verbose_name_plural = 'consiquences | Последствия'


class Participantaction(models.Model):
    value = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'participantactions'
        verbose_name_plural = 'participantActions | Сведения об оставлении места происшествия (участник)'


class Participantcategory(models.Model):
    value = models.CharField(max_length=150)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'participantcategories'
        verbose_name_plural = 'participantCategories | Категории участников'


class Violation(models.Model):
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.value

    class Meta:
        managed = False
        db_table = 'violations'
        verbose_name_plural = 'violations | Нарушения'


class Participant(models.Model):
    class Sex(Enum):
        Male = "М"
        Female = "Ж"

    id_transport = models.ForeignKey('transport.Transport', models.DO_NOTHING, db_column='id_transport', blank=True,
                                     null=True)
    id_incident = models.ForeignKey('incident.Incident', models.DO_NOTHING, db_column='id_incident')
    id_category = models.ForeignKey(Participantcategory, models.DO_NOTHING, db_column='id_category')
    id_action = models.ForeignKey(Participantaction, models.DO_NOTHING, db_column='id_action')
    sex = models.CharField(max_length=1, blank=True, null=True, db_column='sex')
    id_consiquence = models.ForeignKey(Consiquence, models.DO_NOTHING, db_column='id_consiquence')
    isUsedSafetyBelt = models.BinaryField(db_column='isUsedSafetyBelt', blank=True,
                                          null=True)  # Field name made lowercase.
    drunkenness = models.SmallIntegerField(blank=True, null=True)
    drivingExperience = models.SmallIntegerField(db_column='drivingExperience', blank=True,
                                                 null=True)  # Field name made
    # lowercase.

    violationsAssociate = models.ManyToManyField(Violation, related_name='participantViolationAssociate+',
                                                 through='ParticipantViolationAssociate')

    violationsImmediate = models.ManyToManyField(Violation, related_name='participantViolationImmediate+',
                                                 through='ParticipantViolationImmediate')

    class Meta:
        managed = False
        db_table = 'participants'
        verbose_name_plural = 'participants | Участники'


class ParticipantViolationAssociate(models.Model):
    id_participant = models.ForeignKey(Participant, models.DO_NOTHING, db_column='id_participant')
    id_violationassociate = models.ForeignKey(Violation, models.DO_NOTHING,
                                              db_column='id_violationAssociate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participants_violationsassociate'
        verbose_name_plural = 'participants_violationsassociate | Непосредственные нарушения'


class ParticipantViolationImmediate(models.Model):
    id_participant = models.ForeignKey(Participant, models.DO_NOTHING, db_column='id_participant')
    id_violationimmediate = models.ForeignKey(Violation, models.DO_NOTHING,
                                              db_column='id_violationImmediate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participants_violationsimmediate'
        verbose_name_plural = 'participants_violationsimmediate | Сопутствующие нарушения'
