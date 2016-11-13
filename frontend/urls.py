
from django.conf.urls import url

from .views import ResultsListView

urlpatterns = [
    url(r'^$', ResultsListView.as_view(), name='list'),
]
