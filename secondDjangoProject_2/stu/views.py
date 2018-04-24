from django.db.models import F,Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def hello(request):
    return HttpResponse("hello")

def addStu(request):
    # 添加学生信息
    if request.method == 'GET':
        return render(request,'index.html')
    if request.method == 'POST':
        # 处理提交的学生信息
        # print(request.POST)

        stu_name = request.POST.get('name')
        stu_sex = request.POST.get('sex')
        if request.POST.get('sex') == '男':
            stu_sex = 1
        else:
            stu_sex = 0
        stu_birth = request.POST.get('birth')
        stu_tel = request.POST.get('tel')

        # stu = Student()
        # stu.stu_name = stu_name
        # stu.stu_birth = stu_birth
        # stu.stu_sex = stu_sex
        # stu.stu_tel = stu_tel
        # stu.save()

        Student.objects.create(  # insert into table values(.....)
            stu_name=stu_name,
            stu_birth=stu_birth,
            stu_sex=stu_sex,
            stu_tel=stu_tel
        )

        return HttpResponse("添加学生信息成功")

def selectStu(request):
    # 查询数据
    # stus = Student.objects.all() # select * from table

    # 查询所有女生,设置条件(可迭代，【get不可迭代，只能获取一条数据】)
    # stus = Student.objects.filter(stu_sex=False)

    # 查询id从大到小的排序
    stus = Student.objects.all().order_by('-id')

    # 获取id最大的一条数据
    # stus = Student.objects.all().order_by('-id').first()

    # 获取id最小的一条数据
    # stus = Student.objects.all().order_by('-id').last()

    #获取男生数据的个数
    # stus = Student.objects.filter(stu_sex=True).count()
    # print(stus)

    # 查询所有80后女生的信息
    # stus = Student.objects.filter(stu_sex=False).\
    #     filter(stu_birth__gte='1980-01-01').filter(stu_birth__lt='1990-01-01')

    # stus = Student.objects.filter(stu_sex=False,
    #                               stu_birth__gte='1980-01-01',
    #                               stu_birth__lt='1990-01-01')

    # 查询姓李的数据
    # stus = Student.objects.filter(stu_name__startswith='李')

    # 查询姓名以四结束的数据
    # stus = Student.objects.filter(stu_name__endswith='四')

    # 查询姓名中包含文的数据
    # stus = Student.objects.filter(stu_name__contains='文')

    # 判断是否存在李四
    # stus = Student.objects.filter(stu_name='李四').exists()
    # print(stus)

    # 获取指定多个id的值
    # ids = [1,2]
    # stus = Student.objects.filter(id__in=ids)

    # 查询语文成绩大于数学成绩的学生,通过F来获取stu_math中的值
    # stus = Student.objects.filter(stu_chinese__gte=F('stu_math'))

    # 查询语文成绩超过数学成绩10分的学生
    # stus = Student.objects.filter(stu_chinese__gte=F('stu_math') + 10)

    # 查询学生姓名不叫李四，或者语文成绩大于80分的学生  ~:非 |:或  Q:放置条件，与| &连用
    # stus = Student.objects.filter(~Q(stu_name='李四')|Q(stu_chinese__gt=80))

    # return render(request, 'detail.html', {'stus': stus})

    # 返回给前端
    return render(request,'selectStu.html',{'stus':stus})