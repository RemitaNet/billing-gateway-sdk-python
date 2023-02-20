# REMITA BILLER PYTHON SDK
Python SDK for Remita Billing Gateway Service simple APIs

## Package 
To install the `remita-billing-gateway` package, run the following command.

```
pip install remita-billing-gateway
```
## Requirements
*  Python 3.4 or later

## Dependency
*  requests 2.22.0 or later

## Overview
Integrating to Remita for Biller payments SDK enables your customers make payments to billers on Remita through your platform. This provides you with the capability to offer your customers access to the vast array of billers and merchants, including schools, churches, service providers and the Federal Government ministries, departments and agencies (MDAs) available on Remita to purchase and subscribe to their various products and services.

The process involves your customers selecting a biller to pay via your platform. They will supply payment details and confirm the details so you can debit their account with AmountDue to credit a designated Funds Holding Account. Your customers will be emailed Remita receipts (which are FGN MDA-recognized for TSA-bound payments) for each transaction.

## Prerequisites
Prior to using the SDK, you need to set up an integration profile on [Remita](https://login.remita.net) if you are not already registered as a merchant/biller on the platform. Each method call will require you to pass the Public key/Secret key. Your public and secret keys are located at the Billing page on your profile. After you login, click ‘Setup Billing’ at your dashboard >> click ‘Proceed’ on the ‘Yes’ option for the integration question that comes up >> to display the Public/Secret key.

## Configuration
All biller credentials needed to use the SDK are being setup by instantiating the Credential Class and set properties in this class accordingly.
Properties such as public_key, secret_key, and environment are mandatory while read_timeout and connection_timeout can be set to zero (0).

|Field       | Type    | Required   | Description   |   
| ---        | ------  | -----------| -------- |   
| public_key  | str  | Yes        | Located at the Billing page of your Remita profile on www.remita.net.
| secret_key  | str  | Yes        | Located at the Billing page of your Remita profile on www.remita.net.
|environment| str  | Yes        | SetEnvironment.DEMO for Demo environment, While SetEnvironment.LIVE for Production environment.
| read_timeout | int | Yes| The timeout on waiting to read data.
| connection_timeout | int | Yes| The timeout in making the initial connection.

### Sample
```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment,
                              read_timeout=read_timeout, connection_timeout=connection_timeout)

    
	remita_biling_gateway = RemitaBillingGateway(credentials);
```


## Methods
#### Get Bller(s)
This returns a list of the billers, merchants and MDAs available on Remita.

```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

# getListOfBillers
    get_billers = RemitaBillingGateway(credentials=credentials)
    get_biller_payload = GetBillerPayload(request_id= "345634543")
    biller_list = get_billers.get_billers(get_biller_payload)
    
```
### biller_list attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| responseData  | List[ResponseDatum]  |

#### Get Service Types
This returns a list of products and services associated with specified billers on Remita.

```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

#getListOfServices
    get_service_list = RemitaBillingGateway(credentials=credentials)
    request_id = "345634543"
    billId = "DEMOMDA"
    get_servis_payload = GetServicePayload(request_id=request_id, billId=billId)
    service_list = get_service_list.get_service_types (get_servis_payload)
```

### service_list attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| responseData  | List[ResponseDatum]  |


#### Get Custom Fields
Custom fields are additional information specific to a service/product offered for sale by a biller. A service/product may or may not have custom fields defined. This method returns a list of the custom fields associated with a specific product/service offered by a biller on the platform.

```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

# getCustomFields
    get_customfield = RemitaBillingGateway(credentials=credentials)
    request_id = "345634543"
    billId = "41032457"
    get_field_payload = GetCustomFieldPayload(request_id=request_id, billId=billId)
    custom_field_list = get_customfield.get_custom_field(get_field_payload)
```
### custom_field_list attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| responseData  | List[ResponseDatum] |
| acceptPartPayment | bool |
| fixedPrice | bool |
| fixedAmount | float |
| currency | str|


#### Get RRR Details
If your customer already has a Remita Retrieval Reference (RRR) before logging on to your online platform, he/she can also still process payment to Remita billers. They can supply the RRR, verify the RRR to display payment details associated with it before completing the payment. This method makes the call to verify the RRR.

```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

# getRRRDetail
    rrr_detail = RemitaBillingGateway(credentials=credentials)
    request_id = "345634543"
    rrr = "310007769676"
    get_rrr_detail = GetRrrDetailPayload(request_id=request_id, rrr=rrr)
    rrr_detail_response = rrr_detail.get_rrr_details(get_rrr_detail)
```
### rrr_detail_response attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| responseData  | List[ResponseDatum] |


#### Validate Request
You need to make a request for Remita to execute a validation operation on the details retrieved to check the validity of the data. This serves to ensure that the details being passed for payment are viable and will derive an amount payable to generate a Remita Retrieval Reference (RRR) successfully. This method enables you make this call towards generating an RRR for payment.

```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

# #getValidateRequest
    validate_request = RemitaBillingGateway(credentials)
    # values should be added to List here
    value1 = Values(value="4521589ed", amount=0, quantity=0)
    value2 =  Values(value="41032530", amount=0, quantity=0)
    value3 = Values(value="41032536", amount=5000, quantity=1)
    value4 = Values(value="41032538", amount=1500, quantity=1)
    value5 = Values(value="41032537", amount=4000, quantity=1)
    value_list = [value1, value2, value3, value4, value5]
    # custom field should be added to List here
    custom_field1 = CustomField(id="41032446", values=[value1])
    custom_field2 = CustomField(id="41032451", values=[value2])
    custom_field3 = CustomField(id="41032535", values=[value3, value4, value5])

    validate_request_payload = ValidateRequestPayload( customFields=[custom_field1, custom_field2, custom_field3], amount=10500, billId="41032457", payerPhone="08085519759", payerEmail="t.omonubi@gmail.com", payerName="Tokunbo Omonubi", currency="NGN", request_id="769876")
    validate_request_response = validate_request.validate(validate_request_payload)

```

### validate_request_response attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| responseData  | List[ResponseDatum] |


#### Generate RRR
In order to complete the transaction through the Remita Payment Gateway, a Remita Retrieval Reference or RRR is required. This is what uniquely identifies and embodies the payment details of a transaction on the platform ecosystem. Calling this method will generate an RRR for the biller payment.

```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

#generateRRR
    generate_rrr = RemitaBillingGateway(credentials)
    # values should be added to List here
    value1 = Values(value="4521589ed", amount=0, quantity=0)
    value2 =  Values(value="41032530", amount=0, quantity=0)
    value3 = Values(value="41032536", amount=5000, quantity=1)
    value4 = Values(value="41032538", amount=1500, quantity=1)
    value5 = Values(value="41032537", amount=4000, quantity=1)
    value_list = [value1, value2, value3, value4, value5]

    # custom_field_list = []
    custom_field1 = CustomField(id="41032446", values=[value1])
    custom_field2 = CustomField(id="41032451", values=[value2])
    custom_field3 = CustomField(id="41032535", values=[value3, value4, value5])

    gen_rrr_payload = GenerateRrrPayload(customFields=[custom_field1, custom_field2, custom_field3], amount=10500, billId="41032457", payerPhone="08085519759", payerEmail="t.omonubi@gmail.com", payerName="Tokunbo Omonubi", currency="NGN", request_id="769876")
    gen_rrr_response = generate_rrr.generate_rrr(gen_rrr_payload)
```
### gen_rrr_response attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| responseData  | List[ResponseDatum] |


#### Bill Payment Notification
After you have debit the customer with the RRR amount (amountDue) to process the payment, you are required to notify Remita with details of the transaction. Calling this method will send a payment notification for the transaction to Remita accordingly. 

```python
    public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

 #  BillNotification
     remita_biling_gateway = RemitaBillingGateway(credentials);
    transactionId = "65287658975762322"
    amountDebitted = "200000"
    branchCode = "Empty"
    debittedAccount = "2044863290"
    fundingSource = "TOKS"
    incomeAccount = "0001061499"
    paymentAuthCode = "546789096543545678990"
    paymentChannel = "INTERNETBANKING"
    rrr = "270007770767"
    tellerName = "INTERNETBANKING"
    branchCode = "Empty"
    bill_notify = BillerNotificationPayload(transactionId=transactionId, rrr=rrr, amountDebitted=amountDebitted, paymentAuthCode=paymentAuthCode, paymentChannel=paymentChannel, tellerName=tellerName, branchCode=branchCode, fundingSource=fundingSource, incomeAccount=incomeAccount, debittedAccount=debittedAccount)
    notification = remita_biling_gateway.bill_notification(bill_notify)
```
### notification attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| iResponseCode | str | 
| iResponseMessage | str | 
| responseData  |  List[ResponseDatum]  |


#### Transaction Status
You may need to enquire that status of biller payments your customers have made via the Bill Payment Notification API. 

```python
     public_key = "dC5vbW9udWJpQGdtYWlsLmNvbXxiM2RjMDhjZDRlZTc5ZDIxZDQwMjdjOWM3MmI5ZWY0ZDA3MTk2YTRkNGRkMjY3NjNkMGZkYzA4MjM1MzI4OWFhODE5OGM4MjM0NTI2YWI2ZjZkYzNhZmQzNDNkZmIzYmUwNTkxODlmMmNkOTkxNmM5MjVhNjYwZjk0ZTk1OTkwNw=="
    secret_key = "95ab7ab7b2dc3152e3ab776c8f4bbe0ec5fe87526ee129617f319fb9edf79263a6fd15f1efe78f38ad6f04634dff993ccf9f075bf91f37aa52b61a9bd61c881e"
    environment = SetEnvironment.DEMO
    read_timeout = 0
    connection_timeout = 0
    credentials = Credentials(public_key=public_key, secret_key=secret_key, environment=environment, read_timeout=read_timeout, connection_timeout=connection_timeout)

# getPaymentstatus
    transaction_id = "1567417796927"
    payment_status_payload = PaymentStatusPayload(transaction_id=transaction_id)
    payment_status = RemitaBillingGateway(credentials=credentials)
    payment_status_response = payment_status.payment_status(payment_status_payload)
```
### payment_status_response attributes
| Name  | Type    | 
| ---   | ------  | 
| responseCode | str |
| responseMsg | str |  
| appVersionCode | str | 
| iResponseCode | str | 
| iResponseMessage | str | 
| responseData  |  List[ResponseDatum]  |

---
    
## Useful links
* Join our Slack Developer/Support channel at http://bit.ly/RemitaDevSlack
    
## Support
- For all other support needs, support@remita.net
- To contribute to this repo, create an issue on what you intend to fix or update, make a PR and team will look into it and merge.
