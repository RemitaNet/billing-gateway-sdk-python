class BillerNotificationPayload:
    transactionId: str
    rrr: str
    incomeAccount: str
    debittedAccount: int
    paymentAuthCode: str
    paymentChannel: str
    tellerName: str
    branchCode: str
    amountDebitted: float
    fundingSource: str

    def __init__(self,  transactionId: str, rrr: str, incomeAccount: str, debittedAccount: int, paymentAuthCode: str, paymentChannel: str, tellerName: str, branchCode: str, amountDebitted: float, fundingSource: str) -> None:
        self.transactionId = transactionId
        self.rrr = rrr
        self.incomeAccount = incomeAccount
        self.debittedAccount = debittedAccount
        self.paymentAuthCode = paymentAuthCode
        self.paymentChannel = paymentChannel
        self.tellerName = tellerName
        self.branchCode = branchCode
        self.amountDebitted = amountDebitted
        self.fundingSource = fundingSource
