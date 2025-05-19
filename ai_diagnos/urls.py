from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),  # или как у тебя называется app
    path('admin/', admin.site.urls),
]
