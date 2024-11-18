from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:id>/', views.product_detail, name='product_detail'), 
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:id>/<str:action>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
