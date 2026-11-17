from . import views
from django.urls import path,re_path

urlpatterns = [
    path('',views.Home,name="home"),
    path('post/<int:post_id>/',views.pos),
    path('about/',views.about,name="about"),

]