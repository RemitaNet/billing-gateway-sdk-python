class GetCustomFieldPayload:

    request_id: str
    billId: str

    def __init__(self, request_id: str, billId: str) -> None:
        self.request_id = request_id
        self.billId = billId
