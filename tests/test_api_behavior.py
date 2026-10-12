from invoice_service.api import InvoiceAPI


def test_creating_second_invoice_for_same_customer_does_not_erase_first_invoice():
    api = InvoiceAPI()
    api.post_invoice({"customer_id": "c1", "prices": [100]})
    api.post_invoice({"customer_id": "c1", "prices": [200]})

    invoices = api.repository.all()
    assert len(invoices["c1"]) == 2
