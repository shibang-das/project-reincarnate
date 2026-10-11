from invoice_service.models import Invoice


class InMemoryInvoiceRepository:
    def __init__(self):
        self._invoices = {}

    def save(self, invoice: Invoice) -> Invoice:
        self._invoices[invoice.customer_id] = invoice
        return invoice

    def get(self, customer_id: str) -> Invoice | None:
        return self._invoices.get(customer_id)

    def all(self) -> list[Invoice]:
        return list(self._invoices.values())
