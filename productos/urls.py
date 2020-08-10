from django.urls import path
from .views import (
ProductoListView, ProductoCreateView, ProductoDetailView, ProductoUpdateView, ProductoDeleteView,
  )
from django.conf.urls.static import static
from django.conf import settings

app_name = 'productos'
urlpatterns = [
    path('', ProductoListView.as_view(), name = 'producto-list'),
    path('create/', ProductoCreateView.as_view(), name = 'producto-create'),
    path('<int:pk>/', ProductoDetailView.as_view(), name = 'producto-detail'),
    path('<int:pk>/update/', ProductoUpdateView.as_view(), name = 'producto-update'),
    path('<int:pk>/delete/', ProductoDeleteView.as_view(), name = 'producto-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
