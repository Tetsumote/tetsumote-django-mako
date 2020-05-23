from django.contrib import admin
from django.urls import path,include

from .views import ClassBasedView

urlpatterns = [
    path('', ClassBasedView.as_view(), name='home'),
]