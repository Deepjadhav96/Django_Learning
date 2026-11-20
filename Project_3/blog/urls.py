from . import views
from django.urls import path,re_path

urlpatterns = [
    path('post/<int:post_id>/',views.post_details,name='post_details'),
    path('user/<str:username>/',views.user_profile,name = 'user_profile'),
    path('article/<int:year>/<str:month>',views.article_details,name='article_details'),#Multiple parameters re handles here
    re_path(r'^article/(?P<year>[0-9]{4})/$',views.articles_by_year,name='articles_by_year')   #Regex

]