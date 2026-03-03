from django.utils.translation import gettext_lazy as _

MODULE_ID = 'ecommerce'
MODULE_NAME = _('Online Store')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'globe-outline'
MODULE_DESCRIPTION = _('Online store integrated with inventory and payments')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'commerce'

MENU = {
    'label': _('Online Store'),
    'icon': 'globe-outline',
    'order': 19,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Products'), 'icon': 'storefront-outline', 'id': 'products'},
{'label': _('Orders'), 'icon': 'cart-outline', 'id': 'orders'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'ecommerce.view_onlineorder',
'ecommerce.change_onlineorder',
'ecommerce.manage_settings',
]

ROLE_PERMISSIONS = {
    "admin": ["*"],
    "manager": [
        "change_onlineorder",
        "view_onlineorder",
    ],
    "employee": [
        "view_onlineorder",
    ],
}
