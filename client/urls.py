from django.conf.urls import url, include
from .views import (
    index,
)

urlpatterns = [
    # url(r'^$', views.home, name='home')
    url(r'^$', index, name="index" ),
]
