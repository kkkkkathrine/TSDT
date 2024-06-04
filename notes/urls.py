from django.urls import path,re_path,include
from lists import views
from lists import urls as list_urls

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/', include(list_urls))
]
