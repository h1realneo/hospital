from django.shortcuts import render_to_response, HttpResponse
from django.http import JsonResponse
from .forms import BlankReceptionForm
from django.core.context_processors import csrf
import datetime
from reception.models import BlankReception, Doctor


def base(request):
    return render_to_response('reception/index.html')


def blank(request):
    if request.method == 'POST':
        form = BlankReceptionForm(request.POST)
        if form.is_valid():
            sheet = request.POST.copy()
            doctor = Doctor.objects.get(id=int(sheet['doctor']))
            date = sheet['date']
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:10])
            BlankReception(doctor=doctor, date=datetime.date(year, month, day), time=datetime.time(int(sheet['time'])),
                           name_patient=sheet['name_patient'], surname_patient=sheet['surname_patient'],
                           patronymic_patient=sheet['patronymic_patient'], number_patient=sheet['number_patient']
                           ).save()
            return render_to_response('reception/success.html')
    args = {}
    args.update(csrf(request))
    args['form'] = BlankReceptionForm()
    return render_to_response('reception/form.html', args)


def ajax(request):
    if request.method == 'GET':
        doctor = request.GET['doctor']
        date = request.GET['date']
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
        sheets = BlankReception.objects.filter(doctor=doctor, date=datetime.date(year, month, day))
        hour_now = (datetime.datetime.now()).hour
        date_now = datetime.datetime.today().date()
        if hour_now < 9 and date_now == datetime.date(year, month, day):
            hours = [x for x in range(9, 17)]
        elif 9 <= hour_now < 16 and date_now == datetime.date(year, month, day):
            hours = [x for x in range(hour_now + 1, 17)]
        elif hour_now >= 16 and date_now == datetime.date(year, month, day):
            hours = []
        else:
            hours = [x for x in range(9, 17)]
        for sheet in sheets:
            if sheet.time.hour in hours:
                hours.remove(sheet.time.hour)
    return JsonResponse({"hours": hours})

