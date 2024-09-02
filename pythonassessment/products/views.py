import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import UserSerializer
from django.http import HttpResponse
from django.db.models import Sum, Max
from products.models import Product
from django.db.models import Sum, Max, F

class SignUpView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={
            201: openapi.Response('Created', UserSerializer),
            400: 'Bad Request',
        },
        operation_description="Create a new user with a username and password."
    )
    def post(self, request):
        """
        Handle user registration.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            }
        ),
        responses={
            200: openapi.Response(description='Login successful', examples={
                "application/json": {
                    "refresh": "string",
                    "access": "string"
                }
            }),
            401: 'Unauthorized',
        },
        operation_description="Log in with username and password to receive a JWT token."
    )
    def post(self, request):
        """
        Handle user login.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



def summary_report(request):
    # Annotate the product data to include total revenue (price * quantity_sold)
    annotated_products = Product.objects.annotate(
        revenue=F('price') * F('quantity_sold')
    )

    # Aggregate data to create the summary report
    summary = annotated_products.values('category').annotate(
        total_revenue=Sum('revenue'),
        top_product_quantity_sold=Max('quantity_sold'),
    )

    # Determine the top product for each category
    for item in summary:
        top_product = Product.objects.filter(
            category=item['category'], quantity_sold=item['top_product_quantity_sold']
        ).first()
        item['top_product'] = top_product.product_name if top_product else None

    # Create the CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="summary_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Category', 'Total Revenue', 'Top Product', 'Top Product Quantity Sold'])

    for item in summary:
        writer.writerow([
            item['category'],
            item['total_revenue'],
            item['top_product'],
            item['top_product_quantity_sold'],
        ])

    return response