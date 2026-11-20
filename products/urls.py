from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'add-product/',
        views.add_product,
        name='add_product'
    ),

    path(
        'products/',
        views.product_list,
        name='product_list'
    ),

    path(
        'register/', 
        views.register, 
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

]