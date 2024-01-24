from django.urls import path
from .views import blog_post_form, user_form

app_name = "app2"

urlpatterns = [
    path('blog-post-form/', blog_post_form, name='blog_post_form'),
    path('user-form/', user_form, name='user_form'),
]
