from django.conf.urls import url
from .views import *
from account.views import *

app_name ="post"

urlpatterns=[
    url(r'^$',Landing_View, name='landing'),
    url(r'^blog',Post_View, name='blog'),
    url(r'^post/create/$', Post_Create_View, name='create'),
    url(r'^post/detail/(?P<slug>[\w-]+)/$',Post_Detail_View, name='detail'),
    url(r'^post/update/(?P<slug>[\w-]+)/$',Post_Update_View, name='update'),
    url(r'^post/delete/(?P<slug>[\w-]+)/$',Post_Delete_View, name='delete'),

]