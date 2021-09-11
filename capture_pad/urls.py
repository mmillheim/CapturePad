from django.urls import path
from . import views

urlpatterns = [
    path('', views.notebook_list, name='notebook_list'),
    path('years', views.year_list, name='year_list'),
    path('months', views.month_list, name='month_list'),
    path('days', views.day_list, name='day_list'),
    path('notes', views.note_list, name='note_list'),

    path('notebooks/<int:pk>', views.notebook_detail, name='notebook_detail'),
    path('years/<int:pk>', views.year_detail, name='year_detail'),
    path('months/<int:pk>', views.month_detail, name='month_detail'),
    path('days/<int:pk>', views.day_detail, name='day_detail'),
    path('notes/<int:pk>', views.note_detail, name='note_detail'),

]