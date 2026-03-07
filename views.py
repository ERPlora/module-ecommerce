"""
Online Store Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required, permission_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import StoreSettings, OnlineOrder

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('ecommerce', 'dashboard')
@htmx_view('ecommerce/pages/index.html', 'ecommerce/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_online_orders': OnlineOrder.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# OnlineOrder
# ======================================================================

ONLINE_ORDER_SORT_FIELDS = {
    'order_number': 'order_number',
    'status': 'status',
    'total': 'total',
    'tax_amount': 'tax_amount',
    'subtotal': 'subtotal',
    'customer_email': 'customer_email',
    'created_at': 'created_at',
}

def _build_online_orders_context(hub_id, per_page=10):
    qs = OnlineOrder.objects.filter(hub_id=hub_id, is_deleted=False).order_by('order_number')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'online_orders': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'order_number',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_online_orders_list(request, hub_id, per_page=10):
    ctx = _build_online_orders_context(hub_id, per_page)
    return django_render(request, 'ecommerce/partials/online_orders_list.html', ctx)

@login_required
@with_module_nav('ecommerce', 'products')
@htmx_view('ecommerce/pages/online_orders.html', 'ecommerce/partials/online_orders_content.html')
def online_orders_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'order_number')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = OnlineOrder.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(order_number__icontains=search_query) | Q(customer_email__icontains=search_query) | Q(customer_name__icontains=search_query) | Q(status__icontains=search_query))

    order_by = ONLINE_ORDER_SORT_FIELDS.get(sort_field, 'order_number')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['order_number', 'status', 'total', 'tax_amount', 'subtotal', 'customer_email']
        headers = ['Order Number', 'Status', 'Total', 'Tax Amount', 'Subtotal', 'Customer Email']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='online_orders.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='online_orders.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'ecommerce/partials/online_orders_list.html', {
            'online_orders': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'online_orders': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
@htmx_view('ecommerce/pages/online_order_add.html', 'ecommerce/partials/online_order_add_content.html')
def online_order_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        order_number = request.POST.get('order_number', '').strip()
        customer_email = request.POST.get('customer_email', '').strip()
        customer_name = request.POST.get('customer_name', '').strip()
        status = request.POST.get('status', '').strip()
        subtotal = request.POST.get('subtotal', '0') or '0'
        tax_amount = request.POST.get('tax_amount', '0') or '0'
        total = request.POST.get('total', '0') or '0'
        shipping_address = request.POST.get('shipping_address', '').strip()
        notes = request.POST.get('notes', '').strip()
        obj = OnlineOrder(hub_id=hub_id)
        obj.order_number = order_number
        obj.customer_email = customer_email
        obj.customer_name = customer_name
        obj.status = status
        obj.subtotal = subtotal
        obj.tax_amount = tax_amount
        obj.total = total
        obj.shipping_address = shipping_address
        obj.notes = notes
        obj.save()
        response = HttpResponse(status=204)
        response['HX-Redirect'] = reverse('ecommerce:online_orders_list')
        return response
    return {}

@login_required
@htmx_view('ecommerce/pages/online_order_edit.html', 'ecommerce/partials/online_order_edit_content.html')
def online_order_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(OnlineOrder, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.order_number = request.POST.get('order_number', '').strip()
        obj.customer_email = request.POST.get('customer_email', '').strip()
        obj.customer_name = request.POST.get('customer_name', '').strip()
        obj.status = request.POST.get('status', '').strip()
        obj.subtotal = request.POST.get('subtotal', '0') or '0'
        obj.tax_amount = request.POST.get('tax_amount', '0') or '0'
        obj.total = request.POST.get('total', '0') or '0'
        obj.shipping_address = request.POST.get('shipping_address', '').strip()
        obj.notes = request.POST.get('notes', '').strip()
        obj.save()
        return _render_online_orders_list(request, hub_id)
    return {'obj': obj}

@login_required
@require_POST
def online_order_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(OnlineOrder, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_online_orders_list(request, hub_id)

@login_required
@require_POST
def online_orders_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = OnlineOrder.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_online_orders_list(request, hub_id)


# ======================================================================
# Settings
# ======================================================================

@login_required
@permission_required('ecommerce.manage_settings')
@with_module_nav('ecommerce', 'settings')
@htmx_view('ecommerce/pages/settings.html', 'ecommerce/partials/settings_content.html')
def settings_view(request):
    hub_id = request.session.get('hub_id')
    config, _ = StoreSettings.objects.get_or_create(hub_id=hub_id)
    if request.method == 'POST':
        config.store_name = request.POST.get('store_name', '').strip()
        config.is_active = request.POST.get('is_active') == 'on'
        config.currency = request.POST.get('currency', '').strip()
        config.allow_guest_checkout = request.POST.get('allow_guest_checkout') == 'on'
        config.save()
    return {'config': config}

