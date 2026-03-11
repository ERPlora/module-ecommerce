"""
AI context for the Ecommerce module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Ecommerce

### Models

**StoreSettings** (singleton per hub)
- `store_name` (CharField) — display name of the online store
- `is_active` (BooleanField) — whether the store is open to customers
- `currency` (CharField, 3 chars, default 'EUR')
- `allow_guest_checkout` (BooleanField, default True)
- Use `StoreSettings.get_for_hub(hub_id)` to get or create the singleton

**OnlineOrder**
- `order_number` (CharField, max 50) — human-readable reference
- `customer_email` (EmailField)
- `customer_name` (CharField)
- `status` (CharField) — choices: pending, confirmed, processing, shipped, delivered, cancelled
- `subtotal`, `tax_amount`, `total` (DecimalField, 12,2)
- `shipping_address` (TextField)
- `notes` (TextField)

### Key flows

1. **Store setup**: Create/update StoreSettings singleton → set `is_active=True` to open the store.
2. **Order lifecycle**: Orders start as `pending` → `confirmed` → `processing` → `shipped` → `delivered`. Can be `cancelled` at any stage before delivery.
3. **Order creation**: Set `order_number`, `customer_email`, `customer_name`, amounts, and `status='pending'`.

### Relationships
- No direct FK to customers module — customer data is stored as plain text fields on OnlineOrder.
- OnlineOrder has no line items model in this module; use `order_number` to cross-reference.
- The `online_payments` module can reference orders via `source_type='sale'` and `source_id`.
"""
