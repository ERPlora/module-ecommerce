"""Tests for ecommerce models."""
import pytest
from django.utils import timezone

from ecommerce.models import OnlineOrder


@pytest.mark.django_db
class TestOnlineOrder:
    """OnlineOrder model tests."""

    def test_create(self, online_order):
        """Test OnlineOrder creation."""
        assert online_order.pk is not None
        assert online_order.is_deleted is False

    def test_str(self, online_order):
        """Test string representation."""
        assert str(online_order) is not None
        assert len(str(online_order)) > 0

    def test_soft_delete(self, online_order):
        """Test soft delete."""
        pk = online_order.pk
        online_order.is_deleted = True
        online_order.deleted_at = timezone.now()
        online_order.save()
        assert not OnlineOrder.objects.filter(pk=pk).exists()
        assert OnlineOrder.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, online_order):
        """Test default queryset excludes deleted."""
        online_order.is_deleted = True
        online_order.deleted_at = timezone.now()
        online_order.save()
        assert OnlineOrder.objects.filter(hub_id=hub_id).count() == 0


