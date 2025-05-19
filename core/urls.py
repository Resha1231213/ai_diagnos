from django.urls import path
from .views import index, analyze_data

urlpatterns = [
    path('', index, name='index'),
    path('analyze/', analyze_data, name='analyze_data'),
]
