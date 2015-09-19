# -*- coding: utf-8 -*-
from django.contrib import admin
from reception.models import Doctor, BlankReception
import datetime


class BlankReceptionInline(admin.TabularInline):
    model = BlankReception
    extra = 1
    ordering = ['date', 'time']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    inlines = [
        BlankReceptionInline
    ]
    actions = ['remove']

    def remove(self, request, queryset):
        for doctor in queryset:
            sheets = BlankReception.objects.filter(doctor=doctor).filter(date__lt=datetime.datetime.today().date())
            if sheets != []:
                sheets.delete()

    remove.short_description = "Удаление старых заявок"