from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet

# Создаем router и регистрируем ViewSet
router = DefaultRouter()
router.register('pets/', PetViewSet)
# URLs настраиваются автоматически роутером


urlpatterns = [
    path('', include(router.urls)),
]