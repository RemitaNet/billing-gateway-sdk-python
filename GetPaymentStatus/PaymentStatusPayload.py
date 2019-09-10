class PaymentStatusPayload:

    transaction_id: str

    def __init__(self, transaction_id: str) -> None:
        self.transaction_id = transaction_id
