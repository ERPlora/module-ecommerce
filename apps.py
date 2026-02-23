from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'
    label = 'ecommerce'
    verbose_name = _('Online Store')

    def ready(self):
        pass
