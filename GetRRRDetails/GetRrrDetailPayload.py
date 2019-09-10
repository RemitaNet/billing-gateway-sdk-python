class GetRrrDetailPayload:

    request_id: str
    rrr: str

    def __init__(self, request_id: str, rrr: str) -> None:
        self.request_id = request_id
        self.rrr = rrr
