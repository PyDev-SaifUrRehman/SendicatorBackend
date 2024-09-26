from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WalletViewset, TokenOfferingViewset, TokenFeesViewset, RestrictTokenViewset
router = DefaultRouter()

router.register('wallet', WalletViewset, basename='wallet')
router.register('token-offer', TokenOfferingViewset, basename='offer')
router.register('token-fee', TokenFeesViewset, basename='fee')
router.register('restrict-tokens', RestrictTokenViewset, basename = 'restrict-tokens')

urlpatterns = [
    path('', include(router.urls)),
]
