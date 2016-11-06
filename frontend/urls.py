
from django.conf.urls import url

from .views import create, ResultsListView

urlpatterns = [
    url(r'^$', ResultsListView.as_view(), name='list'),
    url(r'^create/$', create, name='create'),
]
