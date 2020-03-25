"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('list/residents/', views.list_residents, name='list_residents'),
    path('edit/resident/', views.edit_resident, name='edit_resident'),
    path('save/resident/', views.save_resident, name='save_resident'),
    path('api/list_owners/', views.get_owners_list, name='get_owners_list'),
    path('list/notifications/', views.list_notifications, name='list_notifications'),
    path('view/notification/', views.get_notification, name='get_notification'),
    path('edit/notification/', views.edit_notification, name='edit_notification'),
    path('save/notification/', views.save_notification, name='save_notification'),
    path('delete/notification/', views.delete_notification, name='delete_notification')
]
