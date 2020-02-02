from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index' ),
    url(r'^login_panal/',views.login_panal,name='login_panal'),
    url(r'^login/' ,views.login , name='login' ),
    url(r'^logout/', views.user_logout, name='logout'),

]

 # {% for post in post %}
 #    <p>{{ post.post }}</p>

 #    <img src="{{ post.image.url}}" height="300" width="300"/>
 #    {% endfor  %}