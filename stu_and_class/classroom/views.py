from django.shortcuts import render

# Create your views here.
from classroom.models import Classroom


def showClassInfo(request):
    class_info = Classroom.objects.all()
    return render(request,"showClassInfo.html",{'class_info':class_info})