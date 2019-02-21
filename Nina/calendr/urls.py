from django.conf.urls import url
from .views import *

app_name ="calendr"

urlpatterns=[
    url(r'',Calendar_View, name='calendar'),

]