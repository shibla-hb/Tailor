from django.urls import path, include
from . import views
#from .import HodViews, StaffViews, StudentViews

urlpatterns = [
      path('', views.loginPage, name="login"),

]