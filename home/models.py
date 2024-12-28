# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    secret_key = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Network(models.Model):

    #__Network_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    eth_like = models.BooleanField()
    short_name = models.CharField(max_length=255, null=True, blank=True)
    delay_time = models.IntegerField(null=True, blank=True)
    nonce_check = models.BooleanField()
    port_network = models.CharField(max_length=255, null=True, blank=True)

    #__Network_FIELDS__END

    class Meta:
        verbose_name        = _("Network")
        verbose_name_plural = _("Network")


class Token(models.Model):

    #__Token_FIELDS__
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    available = models.BooleanField()
    contract = models.CharField(max_length=255, null=True, blank=True)
    decimal = models.CharField(max_length=255, null=True, blank=True)
    contract_type = models.CharField(max_length=255, null=True, blank=True)
    gas_limit = models.IntegerField(null=True, blank=True)

    #__Token_FIELDS__END

    class Meta:
        verbose_name        = _("Token")
        verbose_name_plural = _("Token")


class Fromaddress(models.Model):

    #__Fromaddress_FIELDS__
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    address = models.TextField(max_length=255, null=True, blank=True)
    balance = models.CharField(max_length=255, null=True, blank=True)
    nonce = models.CharField(max_length=255, null=True, blank=True)

    #__Fromaddress_FIELDS__END

    class Meta:
        verbose_name        = _("Fromaddress")
        verbose_name_plural = _("Fromaddress")


class Withdraw(models.Model):

    #__Withdraw_FIELDS__
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    _from = models.ForeignKey(FromAddress, on_delete=models.CASCADE)
    to = models.TextField(max_length=255, null=True, blank=True)
    tx_id = models.TextField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    max_fee = models.CharField(max_length=255, null=True, blank=True)
    transaction_type = models.CharField(max_length=255, null=True, blank=True)
    memo = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(max_length=255, null=True, blank=True)
    microservice_response = models.TextField(max_length=255, null=True, blank=True)
    error_details = models.TextField(max_length=255, null=True, blank=True)
    callback_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    fee = models.TextField(max_length=255, null=True, blank=True)
    sign_response = models.TextField(max_length=255, null=True, blank=True)
    nonce = models.CharField(max_length=255, null=True, blank=True)

    #__Withdraw_FIELDS__END

    class Meta:
        verbose_name        = _("Withdraw")
        verbose_name_plural = _("Withdraw")



#__MODELS__END
