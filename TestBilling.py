from GenerateRrr.GenerateRrrPayload import Values, CustomField, GenerateRrrPayload
from GetCustomFields.GetCustomFieldPayload import GetCustomFieldPayload
from GetListOfBillers.GetBillerPayload import GetBillerPayload
from GetListOfServices.GetServicePayload import GetServicePayload
from GetPaymentStatus.PaymentStatusPayload import PaymentStatusPayload
from GetRRRDetails.GetRrrDetailPayload import GetRrrDetailPayload
from PaymentNotification.BillerNotificationPayload import BillerNotificationPayload
from RemitaBillingService.Credentials import Credentials
from RemitaBillingService.RemitaBillingGateway import RemitaBillingGateway
from RemitaBillingService.SetEnvironment import SetEnvironment
from ValidateRequest.ValidateRequestPayload import ValidateRequestPayload


class TestBilling:

    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment,
                              read_timeout=read_timeout, connection_timeout=connection_timeout)

# # getPaymentstatus
#     transaction_id = "1567417796927"
#     payment_status_payload = PaymentStatusPayload(transaction_id=transaction_id)
#     payment_status = RemitaBillingGateway(credentials=credentials)
#     payment_status_response = payment_status.payment_status(payment_status_payload)
#     print(payment_status_response.responseCode)
#     print(payment_status_response.responseData)
#     print(payment_status_response.responseMsg)
    # print(payment_status_response.iResponseCode)

 #  BillNotification
 #    transactionId = "652876589757625322"
 #    amountDebitted = "200000"
 #    branchCode = "Empty"
 #    debittedAccount = "2044863290"
 #    fundingSource = "TOKS"
 #    incomeAccount = "0001061499"
 #    paymentAuthCode = "546789096543545678990"
 #    paymentChannel = "INTERNETBANKING"
 #    rrr = "270007770767"
 #    tellerName = "INTERNETBANKING"
 #    branchCode = "Empty"
 #    bill_notify = BillerNotificationPayload(transactionId=transactionId, rrr=rrr, amountDebitted=amountDebitted, paymentAuthCode=paymentAuthCode,
 #                                           paymentChannel=paymentChannel, tellerName=tellerName, branchCode=branchCode, fundingSource=fundingSource,
 #                                           incomeAccount=incomeAccount, debittedAccount=debittedAccount)
 #
 #    remita_biling_gateway = RemitaBillingGateway(credentials);
 #    notification = remita_biling_gateway.bill_notification(bill_notify)
 #    print(notification.responseCode)
 #    print(notification.responseMsg)

# #generateRRR
#     generate_rrr = RemitaBillingGateway(credentials)
#     # values should be added to List here
#     value1 = Values(value="4521589ed", amount=0, quantity=0)
#     value2 =  Values(value="41032530", amount=0, quantity=0)
#     value3 = Values(value="41032536", amount=5000, quantity=1)
#     value4 = Values(value="41032538", amount=1500, quantity=1)
#     value5 = Values(value="41032537", amount=4000, quantity=1)
#     value_list = [value1, value2, value3, value4, value5]
#
#     # custom_field_list = []
#     custom_field1 = CustomField(id="41032446", values=[value1])
#     custom_field2 = CustomField(id="41032451", values=[value2])
#     custom_field3 = CustomField(id="41032535", values=[value3, value4, value5])
#
#     gen_rrr_payload = GenerateRrrPayload(customFields=[custom_field1, custom_field2, custom_field3],
#                                                       amount=10500, billId="41032457",
#                                                       payerPhone="08085519759", payerEmail="t.omonubi@gmail.com",
#                                                       payerName="Tokunbo Omonubi", currency="NGN", request_id="769876")
#
#     gen_rrr_response = generate_rrr.generate_rrr(gen_rrr_payload)
#     print(gen_rrr_response.responseCode)
#     print(gen_rrr_response.responseData)
#     print(gen_rrr_response.responseMsg)

# # #getValidateRequest
#     validate_request = RemitaBillingGateway(credentials)
#     # values should be added to List here
#     value1 = Values(value="4521589ed", amount=0, quantity=0)
#     value2 =  Values(value="41032530", amount=0, quantity=0)
#     value3 = Values(value="41032536", amount=5000, quantity=1)
#     value4 = Values(value="41032538", amount=1500, quantity=1)
#     value5 = Values(value="41032537", amount=4000, quantity=1)
#     value_list = [value1, value2, value3, value4, value5]
#     # custom field should be added to List here
#     custom_field1 = CustomField(id="41032446", values=[value1])
#     custom_field2 = CustomField(id="41032451", values=[value2])
#     custom_field3 = CustomField(id="41032535", values=[value3, value4, value5])
#
#     validate_request_payload = ValidateRequestPayload( customFields=[custom_field1, custom_field2, custom_field3], amount=10500, billId="41032457",
#                                                       payerPhone="08085519759", payerEmail="t.omonubi@gmail.com",
#                                                       payerName="Tokunbo Omonubi", currency="NGN", request_id="769876")
#
#     validate_request_response = validate_request.validate(validate_request_payload)
#     print(validate_request_response.responseData)
#     print(validate_request_response.responseMsg)

# # getRRRDetail
#     rrr_detail = RemitaBillingGateway(credentials=credentials)
#     request_id = "345634543"
#     rrr = "310007769676"
#     get_rrr_detail = GetRrrDetailPayload(request_id=request_id, rrr=rrr)
#     rrr_detail_response = rrr_detail.get_rrr_details(get_rrr_detail)
#     print(rrr_detail_response.responseCode)
#     print(rrr_detail_response.responseData)
#     print(rrr_detail_response.responseMsg)

# # getCustomFields
#     get_customfield = RemitaBillingGateway(credentials=credentials)
#     request_id = "345634543"
#     billId = "41032457"
#     get_field_payload = GetCustomFieldPayload(request_id=request_id, billId=billId)
#     service_list = get_customfield.get_custom_field(get_field_payload)
#     print(service_list.responseCode)
#     print(service_list.responseMsg)
#     print(service_list.responseData)

# #getListOfServices
#     get_service_list = RemitaBillingGateway(credentials=credentials)
#     request_id = "345634543"
#     billId = "DEMOMDA"
#     get_servis_payload = GetServicePayload(request_id=request_id, billId=billId)
#     service_list = get_service_list.get_service_types (get_servis_payload)
#     print(service_list.responseCode)
#     print(service_list.responseData)
#     print(service_list.responseMsg)

# # getListOfBillers
#     get_billers = RemitaBillingGateway(credentials=credentials)
#     get_biller_payload = GetBillerPayload(request_id= "345634543")
#     biller_list = get_billers.get_billers(get_biller_payload)
#     print(biller_list.responseCode)
#     print(biller_list.responseData)
#     print(biller_list.responseMsg)



# getListOfBillers
#     get_biller_payload = GetBillerPayload(request_id= "345634543")
#     get_billers = RemitaBillingGateway(credentials=credentials)
#     biller_list = get_billers.get_billers(get_biller_payload)
#     print(biller_list.responseCode)
#     print(biller_list.responseData)
#     print(biller_list.responseMsg)


