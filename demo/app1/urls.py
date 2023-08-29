from django.urls import path
from .views import EmployeeDetail, EmployeeInfo
from .views import*

urlpatterns = [
    path("emp/", EmployeeDetail.as_view(), name="emp"),
    path("emp/<int:id>/", EmployeeInfo.as_view()),
    path('',home,name='home')

]
