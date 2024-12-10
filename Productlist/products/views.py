from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Specify your template
    context_object_name = 'products'    # Context variable name


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# products/views.py


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, "There was an error with the form.")
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})



class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Specify your template
    context_object_name = 'products'  # Name for the list in the template






