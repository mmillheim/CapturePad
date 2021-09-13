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

    path('notebooks/new', views.notebook_create, name='notebook_create'),
    path('years/new', views.year_create, name='year_create'),
    path('months/new', views.month_create, name='month_create'),
    path('days/new', views.day_create, name='day_create'),
    path('notes/new', views.note_create, name='note_create'),

    path('notebook/<int:pk>/edit', views.notebook_edit, name='notebook_edit'),
    path('year/<int:pk>/edit', views.year_edit, name='year_edit'),
    path('month/<int:pk>/edit', views.month_edit, name='month_edit'),
    path('day/<int:pk>/edit', views.day_edit, name='day_edit'),
    path('note/<int:pk>/edit', views.note_edit, name='note_edit'),

    path('notebook/<int:pk>/delete', views.notebook_delete, name='notebook_delete'),
    path('year/<int:pk>/delete', views.year_delete, name='year_delete'),
    path('month/<int:pk>/delete', views.month_delete, name='month_delete'),
    path('day/<int:pk>/delete', views.day_delete, name='day_delete'),
    path('note/<int:pk>/delete', views.note_delete, name='note_delete'),


    path('api/notebooks', views.NotebookList.as_view(), name='api_notebook_list'),
    path('api/notebook/<int:pk>', views.NotebookDetail.as_view(), name='api_notebook_detail'),
    
    path('api/years', views.YearList.as_view(), name='api_year_list'),
    path('api/year/<int:pk>', views.YearDetail.as_view(), name='api_year_detail'),
    
    path('api/months', views.MonthList.as_view(), name='api_month_list'),
    path('api/month/<int:pk>', views.MonthDetail.as_view(), name='api_month_detail'),
    
    path('api/days', views.DayList.as_view(), name='api_day_list'),
    path('api/day/<int:pk>', views.DayDetail.as_view(), name='api_day_detail'),
    
    path('api/notes', views.NoteList.as_view(), name='api_note_list'),
    path('api/note/<int:pk>', views.NoteDetail.as_view(), name='api_note_detail'),

]