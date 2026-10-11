from invoice_service.models import Invoice


class InvoiceError(ValueError):
    pass


def create_invoice(customer_id: str, prices: list[float], discount_percent: float = 0) -> Invoice:
    if not customer_id:
        raise InvoiceError("customer_id is required")

    if not prices:
        raise InvoiceError("at least one price is required")

    for price in prices:
        if price < 0:
            raise InvoiceError("prices cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise InvoiceError("discount must be between 0 and 100")

    return Invoice(customer_id, prices, discount_percent)
