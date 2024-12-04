from django.http import HttpResponseForbidden
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from main.models import Product
from rest_framework.views import APIView

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users only

    def get_queryset(self):
        """
        Filter products based on the shop_id from the URL and return only approved products.
        """
        shop_id = self.kwargs.get('shop_id')
        return Product.objects.filter(shop_id=shop_id, status=2)

    def list(self, request, *args, **kwargs):
        if not request.user.has_perm('main.view_product'):
            return HttpResponseForbidden("Sizda mahsulotlarni ko‘rish huquqi yo‘q")

        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({'detail': 'Hech qanday tasdiqlangan mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and return data
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'message': 'This is a protected view accessible only to authenticated users'}, status=status.HTTP_200_OK)

