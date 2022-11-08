
from django.contrib import admin
from django.urls import path, include
from . import views

from .api import views as api_views
urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.login1, name='login'),
    path('home/', views.home1, name='home1'),
    path('logout/', views.logout1, name='logout'),
    path('announcement/', views.announcement, name='announcement'),
    path('list_announcement/', views.list_announcement, name='list_announcement'),
    path('add_announcement/', views.add_announcement, name='add_announcement'),
    path('edit_announcement/<int:myid>',
         views.edit_announcement, name='edit_announcement'),
    path('batchwise_nomination/', views.batchwise_nomination,
         name="batchwise_nomination"),
    path("nomination/", views.nomination, name="nomination"),
    path("admin_nomination/", views.nomination1, name="admin_nomination"),
    path("download_nomi_admin/", views.download_nomi_admin,
         name="download_nomi_admin"),
    path("download_excel/", views.download_excel, name="download_excel"),

    # Api Path
    path("api/event/", api_views.Event_api, name="eventapi")   # type: ignore
]
