from django.conf.urls import url
from classroom import views

urlpatterns = [
    url(r'^show_class_info/',views.showClassInfo)
]