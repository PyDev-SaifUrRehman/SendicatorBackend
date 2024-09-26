from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework import status
from rest_framework.response import Response
from .models import Wallet, TokenOffering, TokenFees, RestrictToken
from .serializers import WalletSerializer, TokenOfferingSerializer, TokenFeesSerializer, RestrictTokenSerializer

from web3 import Web3

class WalletViewset(viewsets.ModelViewSet):

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def create(self, request, *args, **kwargs):
        url = 'https://eth-sepolia.g.alchemy.com/v2/Ne2TEobtLoImEvWq7oJXrjzlf3ZLOC69'
        w3 = Web3(Web3.HTTPProvider(url))
        serializer = WalletSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.validated_data['message']
        signature = serializer.validated_data['signature']
        print(w3.is_connected())
        address = w3.eth.account.recover_message(message, signature)
        print("address", address)
        serializer.save(address=address)
        
        return super().create(request, *args, **kwargs)


class TokenOfferingViewset(viewsets.ModelViewSet):

    queryset = TokenOffering.objects.all() 
    serializer_class = TokenOfferingSerializer

    @action(detail=False, methods=['get'])
    def history(self, request, *args, **kwargs):
        wallet_address = request.query_params.get('address')

        if not wallet_address:
            return Response(
                {"error": " Wallet address required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            wallet = Wallet.objects.get(address=wallet_address)
        except Wallet.DoesNotExist:
            return Response(
                {"error": "Wallet with the provided address does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        token_offerings = TokenOffering.objects.filter(wallet=wallet, is_accepted=True)

        if not token_offerings.exists():
            return Response(
                {"message": "No accepted token offerings found for the given wallet address."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = TokenOfferingSerializer(token_offerings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  
      
class TokenFeesViewset(viewsets.GenericViewSet, UpdateModelMixin):

    serializer_class = TokenFeesSerializer

    def update(self, request, pk=None):
        token_fee, created = TokenFees.objects.get_or_create(pk=1)
        serializer = TokenFeesSerializer(
            token_fee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class RestrictTokenViewset(viewsets.ModelViewSet):
    queryset = RestrictToken.objects.all()
    serializer_class = RestrictTokenSerializer