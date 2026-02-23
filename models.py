from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

ORDER_STATUS = [
    ('pending', _('Pending')),
    ('confirmed', _('Confirmed')),
    ('processing', _('Processing')),
    ('shipped', _('Shipped')),
    ('delivered', _('Delivered')),
    ('cancelled', _('Cancelled')),
]

class StoreSettings(HubBaseModel):
    store_name = models.CharField(max_length=255, blank=True, verbose_name=_('Store Name'))
    is_active = models.BooleanField(default=False, verbose_name=_('Is Active'))
    currency = models.CharField(max_length=3, default='EUR', verbose_name=_('Currency'))
    allow_guest_checkout = models.BooleanField(default=True, verbose_name=_('Allow Guest Checkout'))

    class Meta(HubBaseModel.Meta):
        db_table = 'ecommerce_storesettings'
        verbose_name = _('StoreSettings')
        verbose_name_plural = _('StoreSettings')

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_for_hub(cls, hub_id):
        settings, _ = cls.objects.get_or_create(hub_id=hub_id)
        return settings


class OnlineOrder(HubBaseModel):
    order_number = models.CharField(max_length=50, verbose_name=_('Order Number'))
    customer_email = models.EmailField(verbose_name=_('Customer Email'))
    customer_name = models.CharField(max_length=255, verbose_name=_('Customer Name'))
    status = models.CharField(max_length=20, default='pending', choices=ORDER_STATUS, verbose_name=_('Status'))
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default='0', verbose_name=_('Subtotal'))
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default='0', verbose_name=_('Tax Amount'))
    total = models.DecimalField(max_digits=12, decimal_places=2, default='0', verbose_name=_('Total'))
    shipping_address = models.TextField(blank=True, verbose_name=_('Shipping Address'))
    notes = models.TextField(blank=True, verbose_name=_('Notes'))

    class Meta(HubBaseModel.Meta):
        db_table = 'ecommerce_onlineorder'

    def __str__(self):
        return str(self.id)

