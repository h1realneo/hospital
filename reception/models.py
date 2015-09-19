# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
import datetime


class Doctor(models.Model):
    title = models.CharField('Доктор', max_length=30)

    def __str__(self):
        return self.title


class BlankReception(models.Model):
    doctor = models.ForeignKey(Doctor)
    date = models.DateField('Дата приема')
    time = models.TimeField('Время приема')
    name_patient = models.CharField('Имя', max_length=20)
    surname_patient = models.CharField('Фамилия', max_length=20)
    patronymic_patient = models.CharField('Отчество', max_length=20)
    number_patient = models.CharField('Контактный телефон', max_length=15)

    def clean(self):
        if self.date.weekday() in [5, 6]:
            raise ValidationError('Hospital don\'t work on weekend')
        if self.date < datetime.datetime.today().date():
            raise ValidationError('Your date is older than today')
        try:
            if self.time.hour not in range(9, 17):
                raise ValidationError('Hospital work from 9:00 to 11:00')
        except AttributeError:
            pass

    class Meta:
        unique_together = [('doctor', 'date', 'time')]
