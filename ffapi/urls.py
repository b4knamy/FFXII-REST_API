from django.urls import path
from . import views


urlpatterns = [
    path('characters/all', views.get_all_char, name='get_all_char'),
    path('characters/filter', views.get_filter_char, name='get_filter_char'),
    path('espers/all', views.get_all_esper, name='get_all_esper'),
    path('espers/filter', views.get_filter_esper, name='get_filter_esper'),
]