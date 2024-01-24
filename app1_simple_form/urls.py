from django.urls import path
from .views import get_name, thanks, contact_form, comment_form

app_name = "app1"

urlpatterns = [
    path('get-name/', get_name, name='get_name'),
    path('contact-form/', contact_form, name='contact_form'),
    path('comment-form/', comment_form, name='comment_form'),

    path('thanks/', thanks, name='thanks')
]
