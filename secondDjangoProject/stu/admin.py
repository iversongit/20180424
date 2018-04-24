from django.contrib import admin

# Register your models here.
from stu.models import Student

# 2、注册的第二种方式 --> 装饰器
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): # 在admin后台Student下显示指定信息
    def set_sex(self):
        if self.sex:
            return '男'
        else:
            return '女'
    # 修改性别字段的描述
    set_sex.short_description = "性别"

    # 展示字段
    list_display = ["id","name",set_sex]

    # 过滤
    list_filter = ["name"]

    # 搜索
    search_fields = ["name"]

    # 分页
    list_per_page = 2

# 1.注册的第一种方式
# admin.site.register(Student,StudentAdmin)