from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import ListingViewset, BookingViewset, ReviewViewset

router = DefaultRouter()
router.register(r'listings', ListingViewset, basename='listing')
router.register(r'bookings', BookingViewset, basename='booking')

listing_router =NestedDefaultRouter(router, r'listings', lookup='listing')
listing_router.register(r'reviews', ReviewViewset, basename='listing-reviews')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(listing_router.urls)),
]