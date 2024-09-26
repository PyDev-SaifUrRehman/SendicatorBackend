from django.contrib import admin
 
from .models import Wallet, TokenOffering, TokenFees, RestrictToken

admin.site.register(Wallet)
admin.site.register(TokenOffering)
admin.site.register(TokenFees)
admin.site.register(RestrictToken)