from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Product
from .serializers import ProductSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]  # This allows everyone to hit the login endpoint

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)  # Generate refresh token
            access_token = str(refresh.access_token)  # Generate access token
            return Response({
                'refresh': str(refresh),  # Return refresh token
                'access': access_token,  # Return access token
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Optionally, you can blacklist the token or inform the user to remove it from the client-side.
        return Response({"message": "Successfully logged out."}, status=200)



class ProductListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch all products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


