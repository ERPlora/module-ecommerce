"""
Online Store Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('ecommerce', 'dashboard')
@htmx_view('ecommerce/pages/dashboard.html', 'ecommerce/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('ecommerce', 'products')
@htmx_view('ecommerce/pages/products.html', 'ecommerce/partials/products_content.html')
def products(request):
    """Products view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('ecommerce', 'orders')
@htmx_view('ecommerce/pages/orders.html', 'ecommerce/partials/orders_content.html')
def orders(request):
    """Orders view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('ecommerce', 'settings')
@htmx_view('ecommerce/pages/settings.html', 'ecommerce/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

