from django.urls import path
from .views import LoginView, ProductListView,LogoutView  

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Login endpoint
    path('logout/', LogoutView.as_view(), name='logout'),
    path('products/', ProductListView.as_view(), name='product-list'),  # Products endpoint
]
