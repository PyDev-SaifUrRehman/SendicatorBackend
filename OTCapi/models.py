from django.db import models

class Wallet(models.Model):
    address = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.address
    
class TokenOffering(models.Model):

    OFFER_TYPE = [
        ('BUYING', 'BUYING'),
        ('SELLING', 'SELLING'),
    ]
    FILL_TYPE_CHOICES = [
        ('PARTIAL_FILL', 'PARTIAL_FILL'),
        ('FULL_FILL', 'FULL_FILL'),
    ]
    token_name = models.CharField(max_length=255)
    token_address = models.CharField(max_length=255)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount_of_token = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1024)
    fill_type = models.CharField(max_length=255, choices=FILL_TYPE_CHOICES)
    offer_type = models.CharField(max_length=255, choices=OFFER_TYPE)
    is_private = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.wallet.address


class TokenFees(models.Model):
    offer_buy_listing_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5)
    offer_sell_listing_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5)
    selling_fee = models.DecimalField(max_digits=10, decimal_places=2, default=5)

    def __str__(self) -> str:
        return "Token fees " + str(self.offer_buy_listing_fee)
    

class RestrictToken(models.Model):
    token_name = models.CharField(max_length=255)
    token_symbol = models.CharField(max_length=255)
    token_address = models.CharField(max_length=255)
    token_image = models.ImageField(upload_to='tokenImages')
    token_decimals = models.IntegerField()

    def __str__(self) -> str:
        return self.token_name
    