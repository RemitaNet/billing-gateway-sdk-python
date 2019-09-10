from typing import List


class Values(object):
    value: str
    quantity: int
    amount: float

    def __init__(self, value: str, quantity: int, amount: float) -> None:
        self.value = value
        self.quantity = quantity
        self.amount = amount


class CustomField(object):
    id: str
    value: List[Values]

    def __init__(self, id: str, values: List[Values]) -> None:
        self.id = id
        self.values = values


class ValidateRequestPayload:
    billId: str
    amount: float
    payerPhone: str
    currency: str
    payerName: str
    payerEmail: str
    request_id: str
    customFields: List[CustomField]

    def __init__(self, billId: str, amount: float, payerPhone: str, currency: str, payerName: str, payerEmail: str,
                 customFields: List[CustomField], request_id: str) -> None:
        self.billId = billId
        self.amount = amount
        self.payerPhone = payerPhone
        self.currency = currency
        self.payerName = payerName
        self.payerEmail = payerEmail
        self.customFields = customFields
        self.request_id = request_id
