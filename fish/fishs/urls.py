from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name="home"),
    path('kal', views.inp,name="hom"),
    path('check', views.check,name="check")
]