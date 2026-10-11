from invoice_service.repository import InMemoryInvoiceRepository
from invoice_service.service import create_invoice


class InvoiceAPI:
    def __init__(self, repository=None):
        self.repository = repository or InMemoryInvoiceRepository()

    def post_invoice(self, payload: dict) -> dict:
        invoice = create_invoice(
            customer_id=payload.get("customer_id", ""),
            prices=payload.get("prices", []),
            discount_percent=payload.get("discount_percent", 0),
        )
        saved = self.repository.save(invoice)
        return {
            "customer_id": saved.customer_id,
            "total": saved.total,
        }
