from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^post/(?P<pk>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.add_answer, name='add_answer'),
]
