import requests
from requests import ConnectTimeout, ReadTimeout
from requests.exceptions import ConnectionError

from Responses.BaseResponse import BaseResponse
from EncryptionConfig import EncryptionConfig
from EnvironmentConfig import EnvironmentConfig
from Responses.SdkResponseCode import SdkResponseCode


class BillPaymentNotificatiion(object):

    def send_payment_notification(self, bill_notification_payload, credentials):
        try:
            get_response = EncryptionConfig()
            if not get_response.credential_available(credentials):
                return get_response.throw_exception(code=get_response.empty_credential_code,
                                                    message=get_response.empty_credential_msg)
            else:
                billing_environment = EnvironmentConfig.set_billing_environment(credentials)
                headers = self.set_header(bill_notification_payload, billing_environment['SECRET_KEY'],
                                          billing_environment['PUBLIC_KEY'])
                time_out = EnvironmentConfig.set_time_out(credentials)
                url = billing_environment['NOTIFICATION_URL']
                payload = {'rrr': bill_notification_payload.rrr,
                           'incomeAccount': bill_notification_payload.incomeAccount,
                           'debittedAccount': bill_notification_payload.debittedAccount,
                           'paymentAuthCode': bill_notification_payload.paymentAuthCode,
                           'paymentChannel': bill_notification_payload.paymentChannel,
                           'tellerName': bill_notification_payload.tellerName,
                           'branchCode': bill_notification_payload.branchCode,
                           'amountDebitted': bill_notification_payload.amountDebitted,
                           'fundingSource': bill_notification_payload.fundingSource
                           }
                print(payload)
                try:
                    response = requests.post(url, headers=headers, json=payload,
                                             timeout=time_out["CONNECTION_TIMEOUT"])
                    print(response.content)
                    get_notification_response = BaseResponse(response.content)
                except ConnectTimeout:
                    return get_response.throw_exception(code=SdkResponseCode.CONNECTION_TIMEOUT_CODE,
                                                        message=SdkResponseCode.CONNECTION_TIMEOUT)
                except ValueError:
                    return get_response.throw_exception(code=SdkResponseCode.ERROR_IN_VALUE_CODE,
                                                        message=SdkResponseCode.ERROR_IN_VALUE)
                except ReadTimeout:
                    return get_response.throw_exception(code=SdkResponseCode.CONNECTION_TIMEOUT_CODE,
                                                        message=SdkResponseCode.CONNECTION_TIMEOUT)
                except ConnectionError as e:  # This is the correct syntax
                    return get_response.throw_exception(code=SdkResponseCode.ERROR_WHILE_CONNECTING_CODE,
                                                        message=SdkResponseCode.ERROR_WHILE_CONNECTING)
            return get_notification_response
        except Exception as e:
            return get_response.throw_exception(code=SdkResponseCode.ERROR_PROCESSING_REQUEST_CODE,
                                                message=SdkResponseCode.ERROR_PROCESSING_REQUEST)

    def set_header(self, bill_payload, secret_key, public_key):

        hash_string = bill_payload.rrr + bill_payload.amountDebitted + bill_payload.fundingSource + \
                      bill_payload.debittedAccount + bill_payload.paymentAuthCode + secret_key
        txn_hash = EncryptionConfig.sha512(hash_string)
        print("SHA512 " + txn_hash)
        headers = {'Content-type': 'application/json', 'publicKey': public_key,
                   'transactionId': bill_payload.transactionId, 'TXN_HASH': txn_hash}
        return headers
