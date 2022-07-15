"""django_tv_shows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows, name='shows'),
    path('new', views.new, name='new'),
    path('create', views.create, name='create'),
    path('<show_id>', views.info_show, name='info_show'),
    path('<show_id>/edit', views.edit_show, name='edit_edit'),
    path('<show_id>/update', views.update, name='update'),
    path('<show_id>/destroy', views.delete, name='delete'),
]
