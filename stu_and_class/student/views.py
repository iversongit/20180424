from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from student.models import Student

def showSpecificStudent(request):
    all_info = Student.objects.filter(classno=request.GET.get('classno'))
    return render(request,"showStudent.html",{'all_info':all_info})

def showAllStudent(request):
    all_info = Student.objects.all()
    return render(request,"showStudent.html",{'all_info':all_info})

def addStudent(request):
    # 添加学生信息
    if request.method == 'GET':
        return render(request,'addStudent.html')
    if request.method == 'POST':
        # 处理添加请求
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        classno = request.POST.get("classno")

        Student.objects.create(
            name = name,
            sex = sex,
            classno = classno
        )

        return HttpResponse("学生信息添加成功！")