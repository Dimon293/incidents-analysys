# Generated by Django 3.0.5 on 2020-06-28 11:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('transport', '0002_auto_20200623_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'managed': False, 'verbose_name_plural': 'addresses | Адреса'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'managed': False, 'verbose_name_plural': 'brands | Производители'},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'managed': False, 'verbose_name_plural': 'models | Модели авто'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'managed': False, 'verbose_name_plural': 'colors | Цвета'},
        ),
        migrations.AlterModelOptions(
            name='consiquence',
            options={'managed': False, 'verbose_name_plural': 'consiquences | Последствия'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'managed': False, 'verbose_name_plural': 'districts | Районы'},
        ),
        migrations.AlterModelOptions(
            name='drivetype',
            options={'managed': False, 'verbose_name_plural': 'driveTypes | Типы приводов'},
        ),
        migrations.AlterModelOptions(
            name='drivingchange',
            options={'managed': False, 'verbose_name_plural': 'drivingChanges | Изменения в движении'},
        ),
        migrations.AlterModelOptions(
            name='incident',
            options={'managed': False, 'verbose_name_plural': 'incident | Происшествия'},
        ),
        migrations.AlterModelOptions(
            name='incidenttype',
            options={'managed': False, 'verbose_name_plural': 'incidentTypes | Типы происшествий'},
        ),
        migrations.AlterModelOptions(
            name='influencefactor',
            options={'managed': False,
                     'verbose_name_plural': 'influenceFactors | Факторы, оказывающие влияние на режим движения'},
        ),
        migrations.AlterModelOptions(
            name='influencefactorincident',
            options={'managed': False,
                     'verbose_name_plural': 'influencefactors_incidents | Факторы относительно происшествия'},
        ),
        migrations.AlterModelOptions(
            name='lighting',
            options={'managed': False, 'verbose_name_plural': 'lightings | Освещение'},
        ),
        migrations.AlterModelOptions(
            name='locality',
            options={'managed': False, 'verbose_name_plural': 'localities | Населенные пункты'},
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'managed': False, 'verbose_name_plural': 'objects | Объекты УДС'},
        ),
        migrations.AlterModelOptions(
            name='objectnearincident',
            options={'managed': False,
                     'verbose_name_plural': 'objectsNear_incidents | Объекты УДС вблизи места происшествия'},
        ),
        migrations.AlterModelOptions(
            name='objectonincident',
            options={'managed': False,
                     'verbose_name_plural': 'objectsOn_incidents | Объекты УДС на месте происшествия'},
        ),
        migrations.AlterModelOptions(
            name='ownershiptype',
            options={'managed': False, 'verbose_name_plural': 'ownershipTypes | Формы собственности'},
        ),
        migrations.AlterModelOptions(
            name='participant',
            options={'managed': False, 'verbose_name_plural': 'participant | Участники'},
        ),
        migrations.AlterModelOptions(
            name='participantaction',
            options={'managed': False,
                     'verbose_name_plural': 'participantActions | Сведения об оставлении места происшествия (участник)'},
        ),
        migrations.AlterModelOptions(
            name='participantcategory',
            options={'managed': False, 'verbose_name_plural': 'participantCategories | Категории участников'},
        ),
        migrations.AlterModelOptions(
            name='participantincident',
            options={'managed': False, 'verbose_name_plural': 'participants_incidents | Участники в происшествии'},
        ),
        migrations.AlterModelOptions(
            name='road',
            options={'managed': False, 'verbose_name_plural': 'roads |  Дороги'},
        ),
        migrations.AlterModelOptions(
            name='roaddisadvantage',
            options={'managed': False, 'verbose_name_plural': 'roadDisadvantages | Недостатки дорожного покрытия'},
        ),
        migrations.AlterModelOptions(
            name='roaddisadvantageincident',
            options={'managed': False,
                     'verbose_name_plural': 'roadDisadvantages_incident | Недостатки дорожного покрытия относительно происшествия'},
        ),
        migrations.AlterModelOptions(
            name='roadimportance',
            options={'managed': False, 'verbose_name_plural': 'roadImportance | Значения дорог'},
        ),
        migrations.AlterModelOptions(
            name='roadwaystatus',
            options={'managed': False, 'verbose_name_plural': 'roadwayStatuses | Состояния проезжей части'},
        ),
        migrations.AlterModelOptions(
            name='streetcategory',
            options={'managed': False, 'verbose_name_plural': 'streetCategories | Категории улиц'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'managed': False, 'verbose_name_plural': 'subjects | Субъекты'},
        ),
        migrations.AlterModelOptions(
            name='technicalissue',
            options={'managed': False, 'verbose_name_plural': 'technicalIssues | Технические неисправности'},
        ),
        migrations.AlterModelOptions(
            name='technicalissuetransport',
            options={'managed': False,
                     'verbose_name_plural': 'technicalIssues_transports | Технические неисправности транспорта'},
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'managed': False, 'verbose_name_plural': 'transports | Транспорт'},
        ),
        migrations.AlterModelOptions(
            name='transportaction',
            options={'managed': False,
                     'verbose_name_plural': 'transportActions | Сведения об оставлении места происшествия (транспорт)'},
        ),
        migrations.AlterModelOptions(
            name='transporttype',
            options={'managed': False, 'verbose_name_plural': 'transportTypes | Типы транспорта'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False, 'verbose_name_plural': 'users | Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='violation',
            options={'managed': False, 'verbose_name_plural': 'violations | Нарушения'},
        ),
        migrations.AlterModelOptions(
            name='violationassociateparticipant',
            options={'managed': False,
                     'verbose_name_plural': 'violationsassociate_participants | Непосредственные нарушения'},
        ),
        migrations.AlterModelOptions(
            name='violationimmediateparticipant',
            options={'managed': False,
                     'verbose_name_plural': 'violationsimmediate_participants | Сопутствующие нарушения'},
        ),
        migrations.AlterModelOptions(
            name='weather',
            options={'managed': False, 'verbose_name_plural': 'weathers | Погодные условия'},
        ),
        migrations.AlterModelOptions(
            name='weatherincident',
            options={'managed': False, 'verbose_name_plural': 'weathers_incident | Погодные условия для происшествия'},
        ),
        migrations.AlterModelTable(
            name='influencefactorincident',
            table='influenceFactors_incidents',
        ),
    ]