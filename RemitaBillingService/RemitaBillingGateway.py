from RemitaBillingService import Credentials
from GenerateRrr.GenerateRrr import GenerateRrr
from GetCustomFields.GetCustomField import GetCustomField
from GetListOfBillers.GetBiller import GetBiller
from GetListOfServices.GetService import GetService
from GetPaymentStatus.PaymentStatus import PaymentStatus
from GetRRRDetails.GetRrrDetail import GetRrrDetail
from PaymentNotification.BillPaymentNotificatiion import BillPaymentNotificatiion
from ValidateRequest.ValidateRequest import ValidateRequest


class RemitaBillingGateway:

    credentials: Credentials

    def __init__(self, credentials: Credentials):
        self.credentials = credentials

    def generate_rrr(self, payload):
        gen_rrr = GenerateRrr()
        return gen_rrr.fetch_rrr(payload, self.credentials)

    def payment_status(self, payload):
        payment_status = PaymentStatus()
        return payment_status.get_payment_status(payload, self.credentials)

    def validate(self, payload):
        validate_request = ValidateRequest()
        return validate_request.validate(payload, self.credentials)

    def get_rrr_details(self, payload):
        rrr_detail = GetRrrDetail()
        return rrr_detail.get_rrr_detail(payload, self.credentials)

    def get_billers(self, payload):
        get_billers = GetBiller()
        return get_billers.get_biller_list(payload, self.credentials)

    def get_service_types(self, payload):
        get_sevice = GetService()
        return get_sevice.get_service_list(payload, self.credentials)

    def get_custom_field(self, payload):
        get_fields = GetCustomField()
        return get_fields.get_custom_field(payload, self.credentials)

    def bill_notification(self, payload):
        notify = BillPaymentNotificatiion()
        return notify.send_payment_notification(payload, self.credentials)