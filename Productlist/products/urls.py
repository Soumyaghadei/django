from django.urls import path
from .views import LoginView, ProductListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Login endpoint
    path('products/', ProductListView.as_view(), name='product-list'),  # Products endpoint
]
