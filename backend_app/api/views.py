from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from beapjiiapps.models import *
from beapjiiapps.pagination import CustomPagination
from beapjiiapps.serializers import *
from rest_framework.response import Response

class UserView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ("username")

class MasterKategoriView(generics.ListAPIView):
    queryset = MasterKategori.objects.all()
    serializer_class = MasterKategoriSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ("nama",)

class ArtikelView(generics.ListAPIView):
    queryset = MasterArtikel.objects.all()
    serializer_class = ArtikelSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ("judul_artikel",)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        total_views = 0
        for artikel in queryset:
            total_views += artikel.view_counter
        
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        
        custom_data = {
            "status": "success",
            "message": "Data retrieved successfully.",
            "total_views": total_views,
            "next": self.paginator.get_next_link(),
            "previous": self.paginator.get_previous_link(),
            "data": serializer.data
        }
        return Response(custom_data)
    
class FileView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ("judul_file",)
