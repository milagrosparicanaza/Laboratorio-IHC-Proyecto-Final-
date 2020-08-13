from django.urls import path
from .views import (
VendedorListView, VendedorCreateView, VendedorDetailView, VendedorUpdateView, VendedorDeleteView, VendedorQueryView
  )
from django.conf.urls.static import static
from django.conf import settings

app_name = 'vendedor'
urlpatterns = [
    path('', VendedorListView.as_view(), name = 'vendedor-list'),
    path('create/', VendedorCreateView.as_view(), name = 'vendedor-create'),
    path('query/', VendedorQueryView.as_view(), name = 'vendedor-query'),
    path('<int:pk>/', VendedorDetailView.as_view(), name = 'vendedor-detail'),
    path('<int:pk>/update/', VendedorUpdateView.as_view(), name = 'vendedor-update'),
    path('<int:pk>/delete/', VendedorDeleteView.as_view(), name = 'vendedor-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
