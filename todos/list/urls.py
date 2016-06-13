from django.conf.urls import url
from . import views


app = "list"
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<todo_id>[0-9]+)/$', views.detail, name='detail'),
  url(r'^new/', views.new, name='new'),
]