import pytest

from invoice_service.api import InvoiceAPI
from invoice_service.models import Invoice
from invoice_service.service import InvoiceError, create_invoice


def test_total_without_discount():
    assert create_invoice("c1", [100, 200]).total == 300


def test_total_with_percentage_discount():
    assert create_invoice("c1", [100, 200], 10).total == 270


def test_full_discount():
    assert create_invoice("c1", [99.99], 100).total == 0


def test_zero_price_is_allowed():
    assert create_invoice("c1", [0, 10]).total == 10


@pytest.mark.parametrize("prices", [[], [-1], [10, -2]])
def test_invalid_prices(prices):
    with pytest.raises(InvoiceError):
        create_invoice("c1", prices)


@pytest.mark.parametrize("discount", [-1, 101])
def test_invalid_discount(discount):
    with pytest.raises(InvoiceError):
        create_invoice("c1", [100], discount)


def test_customer_id_is_required():
    with pytest.raises(InvoiceError):
        create_invoice("", [100])


def test_api_returns_invoice_total():
    api = InvoiceAPI()
    result = api.post_invoice({"customer_id": "c1", "prices": [100, 200], "discount_percent": 10})
    assert result == {"customer_id": "c1", "total": 270}


def test_repository_keeps_separate_customers():
    api = InvoiceAPI()
    api.post_invoice({"customer_id": "c1", "prices": [100]})
    api.post_invoice({"customer_id": "c2", "prices": [200]})
    assert len(api.repository.all()) == 2
