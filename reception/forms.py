# -*- coding: utf-8 -*-
from django.forms import ModelForm, ModelChoiceField, TextInput, Select
from reception.models import BlankReception, Doctor


class BlankReceptionForm(ModelForm):
    doctor = ModelChoiceField(queryset=Doctor.objects, empty_label=None, widget=Select(attrs={'class': 'change'}),
                              label='Доктор')

    class Meta:
        model = BlankReception
        fields = '__all__'
        widgets = {
            'date': TextInput(attrs={'readonly': 'true', 'class': 'change input-small'}),
            'time': Select(attrs={'readonly': 'true', 'class': 'input-mini'})
        }

