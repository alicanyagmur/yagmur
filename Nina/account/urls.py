from django.conf.urls import url
from .views import *

app_name ="account"

urlpatterns=[
    url(r'^login/$',Login_View, name='login'),
    url(r'^signup/$',Register_View,name='signup'),
]