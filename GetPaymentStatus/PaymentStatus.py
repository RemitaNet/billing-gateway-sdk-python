import requests
from requests import ConnectTimeout, ReadTimeout

from Responses.BaseResponse import BaseResponse
from EncryptionConfig import EncryptionConfig
from EnvironmentConfig import EnvironmentConfig
from Responses.SdkResponseCode import SdkResponseCode


class PaymentStatus(object):

    def get_payment_status(self, get_payment_status_payload, credentials):
        try:
            get_response = EncryptionConfig()
            if not get_response.credential_available(credentials):
                return get_response.throw_exception(code=get_response.empty_credential_code,
                                                    message=get_response.empty_credential_msg)
            else:
                billing_environment = EnvironmentConfig.set_billing_environment(credentials)
                headers = self.set_header(get_payment_status_payload, billing_environment['PUBLIC_KEY'])
                time_out = EnvironmentConfig.set_time_out(credentials)
                url = billing_environment['GET_URL'] + "payment/status/" + get_payment_status_payload.transaction_id
                try:
                    response = requests.get(url, headers=headers, timeout=time_out["CONNECTION_TIMEOUT"])
                    rrr_detail_response = BaseResponse(response.content)
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
                return rrr_detail_response
        except Exception as e:
            return get_response.throw_exception(code=SdkResponseCode.ERROR_PROCESSING_REQUEST_CODE, message=SdkResponseCode.ERROR_PROCESSING_REQUEST)

    def set_header(self, payment_status_payload, public_key):
        headers = {'content-type': 'application/json', 'publicKey': public_key}
        return headers
