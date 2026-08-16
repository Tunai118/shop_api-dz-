from django.urls import path
from .views import RegisterView
from .views import (
    CategoryListView,
    CategoryDetailView,
    ProductListView,
    ProductDetailView,
    ProductReviewListView,
    ReviewListView,
    ReviewDetailView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:pk>/", CategoryDetailView.as_view()),
    path("products/", ProductListView.as_view()),
    path("products/reviews/", ProductReviewListView.as_view()),
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("reviews/", ReviewListView.as_view()),
    path("reviews/<int:pk>/", ReviewDetailView.as_view()),
    path("users/register/", RegisterView.as_view()),
]