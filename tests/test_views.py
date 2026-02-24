"""Tests for ecommerce views."""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestDashboard:
    """Dashboard view tests."""

    def test_dashboard_loads(self, auth_client):
        """Test dashboard page loads."""
        url = reverse('ecommerce:dashboard')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_dashboard_htmx(self, auth_client):
        """Test dashboard HTMX partial."""
        url = reverse('ecommerce:dashboard')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_dashboard_requires_auth(self, client):
        """Test dashboard requires authentication."""
        url = reverse('ecommerce:dashboard')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestOnlineOrderViews:
    """OnlineOrder view tests."""

    def test_list_loads(self, auth_client):
        """Test list view loads."""
        url = reverse('ecommerce:online_orders_list')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_list_htmx(self, auth_client):
        """Test list HTMX partial."""
        url = reverse('ecommerce:online_orders_list')
        response = auth_client.get(url, HTTP_HX_REQUEST='true')
        assert response.status_code == 200

    def test_list_search(self, auth_client):
        """Test list search."""
        url = reverse('ecommerce:online_orders_list')
        response = auth_client.get(url, {'q': 'test'})
        assert response.status_code == 200

    def test_list_sort(self, auth_client):
        """Test list sorting."""
        url = reverse('ecommerce:online_orders_list')
        response = auth_client.get(url, {'sort': 'created_at', 'dir': 'desc'})
        assert response.status_code == 200

    def test_export_csv(self, auth_client):
        """Test CSV export."""
        url = reverse('ecommerce:online_orders_list')
        response = auth_client.get(url, {'export': 'csv'})
        assert response.status_code == 200
        assert 'text/csv' in response['Content-Type']

    def test_export_excel(self, auth_client):
        """Test Excel export."""
        url = reverse('ecommerce:online_orders_list')
        response = auth_client.get(url, {'export': 'excel'})
        assert response.status_code == 200

    def test_add_form_loads(self, auth_client):
        """Test add form loads."""
        url = reverse('ecommerce:online_order_add')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_add_post(self, auth_client):
        """Test creating via POST."""
        url = reverse('ecommerce:online_order_add')
        data = {
            'order_number': 'New Order Number',
            'customer_email': 'test@example.com',
            'customer_name': 'New Customer Name',
            'status': 'New Status',
            'subtotal': '100.00',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_edit_form_loads(self, auth_client, online_order):
        """Test edit form loads."""
        url = reverse('ecommerce:online_order_edit', args=[online_order.pk])
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_edit_post(self, auth_client, online_order):
        """Test editing via POST."""
        url = reverse('ecommerce:online_order_edit', args=[online_order.pk])
        data = {
            'order_number': 'Updated Order Number',
            'customer_email': 'test@example.com',
            'customer_name': 'Updated Customer Name',
            'status': 'Updated Status',
            'subtotal': '100.00',
        }
        response = auth_client.post(url, data)
        assert response.status_code == 200

    def test_delete(self, auth_client, online_order):
        """Test soft delete via POST."""
        url = reverse('ecommerce:online_order_delete', args=[online_order.pk])
        response = auth_client.post(url)
        assert response.status_code == 200
        online_order.refresh_from_db()
        assert online_order.is_deleted is True

    def test_bulk_delete(self, auth_client, online_order):
        """Test bulk delete."""
        url = reverse('ecommerce:online_orders_bulk_action')
        response = auth_client.post(url, {'ids': str(online_order.pk), 'action': 'delete'})
        assert response.status_code == 200
        online_order.refresh_from_db()
        assert online_order.is_deleted is True

    def test_list_requires_auth(self, client):
        """Test list requires authentication."""
        url = reverse('ecommerce:online_orders_list')
        response = client.get(url)
        assert response.status_code == 302


@pytest.mark.django_db
class TestSettings:
    """Settings view tests."""

    def test_settings_loads(self, auth_client):
        """Test settings page loads."""
        url = reverse('ecommerce:settings')
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_settings_requires_auth(self, client):
        """Test settings requires authentication."""
        url = reverse('ecommerce:settings')
        response = client.get(url)
        assert response.status_code == 302

