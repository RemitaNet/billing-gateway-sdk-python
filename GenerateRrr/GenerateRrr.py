import requests
from requests import ConnectTimeout, ReadTimeout

from Responses.BaseResponse import BaseResponse
from EncryptionConfig import EncryptionConfig
from EnvironmentConfig import EnvironmentConfig
from Responses.SdkResponseCode import SdkResponseCode


class GenerateRrr(object):

    def fetch_rrr(self, get_generate_rrr_payload, credentials):
        try:
            get_response = EncryptionConfig()
            if not get_response.credential_available(credentials):
                return get_response.throw_exception(code=get_response.empty_credential_code,
                                                    message=get_response.empty_credential_msg)
            else:
                billing_environment = EnvironmentConfig.set_billing_environment(credentials)
                headers = self.set_header(get_generate_rrr_payload, billing_environment['PUBLIC_KEY'])
                time_out = EnvironmentConfig.set_time_out(credentials)
                url = billing_environment['GENERATE_RRR_URL']
                generate_rrr_payload_dict = get_generate_rrr_payload.__dict__
                generate_rrr_payload_dict['customFields'] = [{'id': get_each_field.id,
                                                              'values': [get_each_field.__dict__ for get_each_field in
                                                                         get_each_field.values]} for get_each_field in
                                                             get_generate_rrr_payload.customFields]
                try:
                    response = requests.post(url, headers=headers, json=generate_rrr_payload_dict,
                                             timeout=time_out["CONNECTION_TIMEOUT"])
                    generate_rrr_response = BaseResponse(response.content)
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
            return generate_rrr_response
        except Exception as e:
            return get_response.throw_exception(code=SdkResponseCode.ERROR_PROCESSING_REQUEST_CODE,
                                                message=SdkResponseCode.ERROR_PROCESSING_REQUEST)

    def set_header(self, validate_request_payload, public_key):
        headers = {'content-type': 'application/json', 'publicKey': public_key,
                   'transactionId': validate_request_payload.request_id}
        return headers
