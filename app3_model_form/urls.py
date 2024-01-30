from django.urls import path
from .views.views import HomeView, thanks
from app3_model_form.views.cat_views import (
    CategoryListView,
    CategoryDetailView as CatView,
    CategoryCreateView,
    CategoryUpdateView as CatUp,
    CategoryDeleteView as CatDel,
)
from app3_model_form.views.pro_views import (
    ProductListView,
    ProductDetailView as ProView,
    ProductCreateView,
    ProductUpdateView as ProUP,
    ProductDeleteView as ProDel,

)
from app3_model_form.views.order_views import (
    OrderListView,
    OrderDetailView as OdrView,
    OrderCreateView,
    OrderUpdateView as OdrUP,
    OrderDeleteView as OdrDel,

)

app_name = "app3"

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('thanks/', thanks, name='thanks'),

    path('cat/', CategoryListView.as_view(), name='category_list'),
    path('cat/detail/<int:pk>/', CatView.as_view(), name='category_detail'),
    path('cat/create/', CategoryCreateView.as_view(), name='category_create'),
    path('cat/update/<int:pk>/', CatUp.as_view(), name='category_update'),
    path('cat/delete/<int:pk>/', CatDel.as_view(), name='category_delete'),

    path('pro/', ProductListView.as_view(), name='product_list'),
    path('pro/detail/<int:pk>/', ProView.as_view(), name='product_detail'),
    path('pro/create/', ProductCreateView.as_view(), name='product_create'),
    path('pro/update/<int:pk>/', ProUP.as_view(), name='product_update'),
    path('pro/delete/<int:pk>/', ProDel.as_view(), name='product_delete'),

    path('order/', OrderListView.as_view(), name='order_list'),
    path('orders/detail/<int:pk>/', OdrView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>/', OdrUP.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', OdrDel.as_view(), name='order_delete'),
]
