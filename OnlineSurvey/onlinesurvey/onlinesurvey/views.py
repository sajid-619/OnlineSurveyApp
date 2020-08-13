from django.shortcuts import render
from onlinesurvey.models import Questions

def surveyonline(request) :
    results = Questions.objects.all()
    return render(request, 'index.html', {"Questions": results})