from django.urls.resolvers import URLPattern
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('services',views.service,name='services'),
    path('predictions',views.predictions,name='prediction'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('predict',views.predict,name='predict'),

]