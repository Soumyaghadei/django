from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # This allows login to get a token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),  # Token generation endpoint
    path('', include('products.urls')),  # Including the product list URLs
]
