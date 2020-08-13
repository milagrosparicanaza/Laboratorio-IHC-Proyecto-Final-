from django.urls import path
from .views import (
ProductoListView, ProductoCreateView, ProductoDetailView, ProductoUpdateView, ProductoDeleteView,
  LisProductos,ProductoQueryView )
from django.conf.urls.static import static
from django.conf import settings

app_name = 'productos'
urlpatterns = [
    path('', ProductoListView.as_view(), name = 'productos-list'),
    path('create/', ProductoCreateView.as_view(), name = 'productos-create'),
    path('query/', ProductoQueryView.as_view(), name = 'productos-queryset'),
    path('<int:pk>/', ProductoDetailView.as_view(), name = 'productos-detail'),
    path('<int:pk>/update/', ProductoUpdateView.as_view(), name = 'productos-update'),
    path('<int:pk>/delete/', ProductoDeleteView.as_view(), name = 'productos-delete'),
    #url(r'^list_productos', LisProductos.as_view(), name = 'productosList'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
