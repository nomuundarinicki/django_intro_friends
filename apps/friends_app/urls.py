from django.conf.urls import url
from . import views

app_name = 'myfriend'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addFriend$', views.addFriend, name='addFriend'),
    #url(r'^(?P<id>\d+)$', views.show, name='show'),
    #url(r'^show$', views.show, name='show'),
]
