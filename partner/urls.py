from django.conf.urls import url, include
from .views import index,  signup, login, logout

urlpatterns = [
    # url(r'^$', views.home, name='home')
    url(r'^$', index, name="index" ),
    url(r'^signup/$', signup, name="signup" ),
    url(r'^login/$', login, name="login" ),
    url(r'^logout/$', logout, name="logout" ),

    # $ 표시는 정규식 표현임 : 끝이 났다는 것을 의미함
]
