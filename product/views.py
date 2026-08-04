from rest_framework import generics
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductReviewSerializer, ProductSerializer, ReviewSerializer
from django.db.models import Avg, Count

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.annotate(products_count=Count("products"))
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductReviewListView(generics.ListAPIView):
    queryset = Product.objects.annotate(rating=Avg("reviews__stars"))
    serializer_class = ProductReviewSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer