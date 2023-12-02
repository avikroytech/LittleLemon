from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer

# Create your views here.
class MenuItemsView(ListCreateAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer
	permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer
	permission_classes = [IsAuthenticated]

class BookingViewSet(ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]