from invoice_service.models import Invoice


class InMemoryInvoiceRepository:
    def __init__(self):
        self._invoices = {}

    def save(self, invoice: Invoice) -> Invoice:
        self._invoices.setdefault(invoice.customer_id, []).append(invoice)
        return invoice

    def get(self, customer_id: str) -> Invoice | None:
        invoices = self._invoices.get(customer_id, [])
        return invoices[-1] if invoices else None

    def all(self) -> dict[str, list[Invoice]]:
        return {
            customer_id: list(invoices)
            for customer_id, invoices in self._invoices.items()
        }
