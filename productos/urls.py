from django.urls import path
from .views import (
ProductoListView, ProductoCreateView, ProductoDetailView, ProductoUpdateView, ProductoDeleteView,
  )

app_name = 'productos'
urlpatterns = [
    path('productos/', ProductoListView.as_view(), name = 'producto-list'),
    path('productos/create/', ProductoCreateView.as_view(), name = 'producto-create'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name = 'producto-detail'),
    path('productos/<int:pk>/update/', ProductoUpdateView.as_view(), name = 'producto-update'),
    path('productos/<int:pk>/delete/', ProductoDeleteView.as_view(), name = 'producto-delete'),
]
