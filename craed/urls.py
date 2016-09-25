from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

from . import views

urlpatterns = [
    url(r'^$', views.AEDListView.as_view()),

    url(r'^list$',
        views.AEDListView.as_view(),
        name="list"),

    url(r'^detail/(?P<pk>[0-9]+)$',
        views.AEDDetailView.as_view(),
        name="detail"),
    
    url(r'^update/(?P<pk>[0-9]+)$',
        login_required(views.AEDUpdateView.as_view()),
        name="update"),

    url(r'^update$',
        login_required(views.AEDCreateView.as_view()),
        name="create"),

    url(r'^delete/(?P<pk>[0-9]+)$',
        login_required(views.AEDDeleteView.as_view()),
        name="delete"),

]
