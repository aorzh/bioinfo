# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from image_cropping import ImageRatioField
from image_cropping import ImageCroppingMixin


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=150)
    body = models.TextField('Текст')
    time = models.DateTimeField('Дата')
    image = models.ImageField('Картинка', upload_to='post_images', blank=True)
     # size is "width x height"
    cropping = ImageRatioField('image', '430x360', size_warning=True)

    class Meta:
        ordering = ("-time",)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title


class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass
    list_display = ("title", "time")


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
    year = models.IntegerField('Год рождения', default=1960)

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

    # Глюкоза
    glukosa = models.FloatField('Глюкоза', default=0.0)

    # The additional attributes we wish to include.
    picture = models.ImageField('Данные анализов (jpg, png)', upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    class Meta:
        ordering = ("-user",)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "year", "gender")