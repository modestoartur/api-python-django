from django.urls import include, path
from rest_framework import routers
from quickstart import views

# Setando
router = routers.DefaultRouter()
router.register(r'funcionarios', views.FuncionarioViewSet)

# Roteamento automatico de URL.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]