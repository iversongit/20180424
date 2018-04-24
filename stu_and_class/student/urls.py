from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^show_all_stu/',views.showAllStudent),
    url(r'^show_specific_stu/',views.showSpecificStudent),
    url(r'^addstu/',views.addStudent)
]