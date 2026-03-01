"""AI tools for the Ecommerce module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListOnlineOrders(AssistantTool):
    name = "list_online_orders"
    description = "List online/ecommerce orders."
    module_id = "ecommerce"
    required_permission = "ecommerce.view_onlineorder"
    parameters = {
        "type": "object",
        "properties": {
            "status": {"type": "string", "description": "Filter: pending, confirmed, processing, shipped, delivered, cancelled"},
            "limit": {"type": "integer"},
        },
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from ecommerce.models import OnlineOrder
        qs = OnlineOrder.objects.all()
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        limit = args.get('limit', 20)
        return {
            "orders": [
                {"id": str(o.id), "order_number": o.order_number, "customer_name": o.customer_name, "customer_email": o.customer_email, "status": o.status, "total": str(o.total), "created_at": o.created_at.isoformat()}
                for o in qs.order_by('-created_at')[:limit]
            ]
        }


@register_tool
class UpdateOnlineOrderStatus(AssistantTool):
    name = "update_online_order_status"
    description = "Update an online order's status."
    module_id = "ecommerce"
    required_permission = "ecommerce.change_onlineorder"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "order_id": {"type": "string"},
            "status": {"type": "string", "description": "confirmed, processing, shipped, delivered, cancelled"},
        },
        "required": ["order_id", "status"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from ecommerce.models import OnlineOrder
        o = OnlineOrder.objects.get(id=args['order_id'])
        o.status = args['status']
        o.save(update_fields=['status'])
        return {"id": str(o.id), "status": o.status, "updated": True}


@register_tool
class GetEcommerceSettings(AssistantTool):
    name = "get_ecommerce_settings"
    description = "Get ecommerce store settings."
    module_id = "ecommerce"
    required_permission = "ecommerce.view_storesettings"
    parameters = {"type": "object", "properties": {}, "required": [], "additionalProperties": False}

    def execute(self, args, request):
        from ecommerce.models import StoreSettings
        s = StoreSettings.get_solo()
        return {"store_name": s.store_name, "is_active": s.is_active, "currency": s.currency, "allow_guest_checkout": s.allow_guest_checkout}
