# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    DIABET_CHOICES = (
        ('1', 'Первый'),
        ('2', 'Второй'),
    )
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Год рождения
    year = models.IntegerField('Год', default=1960)

    # Gender
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES, default='M')

    # Тип диабета
    type = models.CharField('Тип диабета', max_length=1, choices=DIABET_CHOICES, default='1')

    # Верхнее давление
    sat = models.IntegerField('Верхнее давление', default=120)

    # Нижнее давление
    dat = models.IntegerField('Нижнее давление', default=80)

    # ЧСС
    css = models.IntegerField('ЧСС', default=80)

    # CКФ
    skf = models.FloatField('Скорость клубочковой фильтрации', default=120)

    # Холестерол
    hslpvp = models.FloatField('Холестерол – липопротеины высокой плотности', default=0.0)

    # Холестерол
    hslpnp = models.FloatField('Холестерол – липопротеины низкой плотности', default=0.0)

    # Холестерол
    moch = models.FloatField('Мочевина', default=0.0)

    # Креатинин
    kreat = models.FloatField('Креатинин', default=85.0)

    # Билирубин
    bilirubin = models.FloatField('Билирубин', default=0.0)

    # Аспартатаминотрансфераза (АСТ)
    ast = models.FloatField('Аспартатаминотрансфераза (АСТ)', default=0.0)

    # Аланинаминотрансфераза (АЛТ)
    alt = models.FloatField('Аланинаминотрансфераза (АЛТ)', default=0.0)

    # Аланинаминотрансфераза (АЛТ)
    glukosa = models.FloatField('Глюкоза', default=0.0)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username