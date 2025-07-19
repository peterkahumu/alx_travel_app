from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    """Allow user to perform CRUD operations on listings."""
    host = serializers.ReadOnlyField(source = 'host.username')

    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['host', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    """Perform CRUD on Bookings"""
    user = serializers.ReadOnlyField(source = 'user.username')

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'creater_at']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']


