from rest_framework import serializers
from .models import Wallet, TokenOffering, TokenFees, RestrictToken

class WalletSerializer(serializers.ModelSerializer):

    address = serializers.CharField(required = False, read_only = True)
    
    class Meta:
        model = Wallet
        fields = '__all__'

class TokenOfferingSerializer(serializers.ModelSerializer):

    wallet = serializers.SlugRelatedField(
        slug_field='address', 
        queryset=Wallet.objects.all(),
        required=True,
        allow_null=False,
    )
    class Meta:
        model = TokenOffering
        fields = '__all__'
    

class TokenFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenFees
        fields = '__all__'


class RestrictTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestrictToken
        fields = '__all__'
        