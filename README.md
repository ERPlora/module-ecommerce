# Online Store

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `ecommerce` |
| **Version** | `1.0.0` |
| **Icon** | `globe-outline` |
| **Dependencies** | None |

## Models

### `StoreSettings`

StoreSettings(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, store_name, is_active, currency, allow_guest_checkout)

| Field | Type | Details |
|-------|------|---------|
| `store_name` | CharField | max_length=255, optional |
| `is_active` | BooleanField |  |
| `currency` | CharField | max_length=3 |
| `allow_guest_checkout` | BooleanField |  |

**Methods:**

- `get_for_hub()`

### `OnlineOrder`

OnlineOrder(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, order_number, customer_email, customer_name, status, subtotal, tax_amount, total, shipping_address, notes)

| Field | Type | Details |
|-------|------|---------|
| `order_number` | CharField | max_length=50 |
| `customer_email` | EmailField | max_length=254 |
| `customer_name` | CharField | max_length=255 |
| `status` | CharField | max_length=20, choices: pending, confirmed, processing, shipped, delivered, cancelled |
| `subtotal` | DecimalField |  |
| `tax_amount` | DecimalField |  |
| `total` | DecimalField |  |
| `shipping_address` | TextField | optional |
| `notes` | TextField | optional |

## URL Endpoints

Base path: `/m/ecommerce/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `products/` | `products` | GET |
| `orders/` | `orders` | GET |
| `online_orders/` | `online_orders_list` | GET |
| `online_orders/add/` | `online_order_add` | GET/POST |
| `online_orders/<uuid:pk>/edit/` | `online_order_edit` | GET |
| `online_orders/<uuid:pk>/delete/` | `online_order_delete` | GET/POST |
| `online_orders/bulk/` | `online_orders_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `ecommerce.view_onlineorder` | View Onlineorder |
| `ecommerce.change_onlineorder` | Change Onlineorder |
| `ecommerce.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `change_onlineorder`, `view_onlineorder`
- **employee**: `view_onlineorder`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Products | `storefront-outline` | `products` | No |
| Orders | `cart-outline` | `orders` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_online_orders`

List online/ecommerce orders.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No | Filter: pending, confirmed, processing, shipped, delivered, cancelled |
| `limit` | integer | No |  |

### `update_online_order_status`

Update an online order's status.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `order_id` | string | Yes |  |
| `status` | string | Yes | confirmed, processing, shipped, delivered, cancelled |

### `get_ecommerce_settings`

Get ecommerce store settings.

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  ecommerce/
    css/
    js/
  icons/
    icon.svg
templates/
  ecommerce/
    pages/
      dashboard.html
      index.html
      online_order_add.html
      online_order_edit.html
      online_orders.html
      orders.html
      products.html
      settings.html
    partials/
      dashboard_content.html
      online_order_add_content.html
      online_order_edit_content.html
      online_orders_content.html
      online_orders_list.html
      orders_content.html
      panel_online_order_add.html
      panel_online_order_edit.html
      products_content.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
