from django.urls import path
from .views import get_name, thanks

app_name = "app1"

urlpatterns = [
    path('get-name/', get_name, name='get_name'),
    path('thanks/', thanks, name='thanks')
]
