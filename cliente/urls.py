from django.urls import path
from .views import (
<<<<<<< HEAD
ClienteListView, ClienteCreateView, ClienteDetailView, ClienteUpdateView, ClienteDeleteView, index,
=======
ClienteListView, ClienteCreateView, ClienteDetailView, ClienteUpdateView, ClienteDeleteView, ClienteQueryView, ReporteClientePDF,
>>>>>>> 70584232b07c7fb4489f5986b4d29114170841f8
  )
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cliente'
urlpatterns = [
    path('', ClienteListView.as_view(), name = 'cliente-list'),
    path('create/', ClienteCreateView.as_view(), name = 'cliente-create'),
    path('query/', ClienteQueryView.as_view(), name = 'cliente-queryset'),
    path('reporte/', ReporteClientePDF.as_view(), name = 'cliente-report'),
    path('<int:pk>/', ClienteDetailView.as_view(), name = 'cliente-detail'),
    path('<int:pk>/update/', ClienteUpdateView.as_view(), name = 'cliente-update'),
    path('<int:pk>/delete/', ClienteDeleteView.as_view(), name = 'cliente-delete'),
<<<<<<< HEAD
    path('index/', index, name = 'correo'),
=======
    
>>>>>>> 70584232b07c7fb4489f5986b4d29114170841f8
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)