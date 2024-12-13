from django.urls import path
from .views import ProductListView, LoginView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('login/', LoginView.as_view(), name='login'),  # Login endpoint
]
