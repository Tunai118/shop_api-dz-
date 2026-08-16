from rest_framework import generics
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductReviewSerializer, ProductSerializer, ReviewSerializer
from django.db.models import Avg, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .models import ConfirmationCode
import random

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.annotate(products_count=Count("products"))
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductReviewListView(generics.ListCreateAPIView):
    queryset = Product.objects.annotate(rating=Avg("reviews__stars"))
    serializer_class = ProductReviewSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        code = str(random.randint(100000, 999999))

        ConfirmationCode.objects.create(
            user=user,
            code=code
        )

        return Response({
            "message": "Пользователь зарегистрирован",
            "code": code
        })