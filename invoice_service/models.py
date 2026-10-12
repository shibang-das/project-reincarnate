from dataclasses import dataclass


@dataclass
class Invoice:
    customer_id: str
    prices: list[float]
    discount_percent: float = 0

    @property
    def total(self) -> float:
        subtotal = sum(self.prices)
        if self.discount_percent:
            print(subtotal)
            subtotal -= subtotal * self.discount_percent / 100
        return round(subtotal, 2)
