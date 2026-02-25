# Online Store Module

Online store integrated with inventory and payments.

## Features

- Configure and manage an online store with custom name and currency
- Enable or disable the online store
- Guest checkout support (configurable)
- Track online orders with full lifecycle: Pending, Confirmed, Processing, Shipped, Delivered, Cancelled
- Order details including customer name, email, shipping address, and notes
- Financial tracking per order: subtotal, tax amount, and total
- Auto-generated order numbers
- Dashboard overview of store and order metrics

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Online Store > Settings**

Settings include:
- Store name
- Active/inactive toggle
- Currency
- Guest checkout toggle

## Usage

Access via: **Menu > Online Store**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/ecommerce/dashboard/` | Overview of store performance and order metrics |
| Products | `/m/ecommerce/products/` | Manage products listed in the online store |
| Orders | `/m/ecommerce/orders/` | View and manage online orders |
| Settings | `/m/ecommerce/settings/` | Store configuration |

## Models

| Model | Description |
|-------|-------------|
| `StoreSettings` | Per-hub store configuration with name, active flag, currency, and guest checkout toggle |
| `OnlineOrder` | An online order with order number, customer info (name, email), status, amounts (subtotal, tax, total), shipping address, and notes |

## Permissions

| Permission | Description |
|------------|-------------|
| `ecommerce.view_onlineorder` | View online orders |
| `ecommerce.change_onlineorder` | Update online order status and details |
| `ecommerce.manage_settings` | Manage store settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
