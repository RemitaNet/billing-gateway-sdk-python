import hashlib

from Responses.BaseResponse import BaseResponse

class EncryptionConfig(object):

    empty_credential_msg: str
    empty_credential_code: str

    def sha512(input):
        hashed_input = hashlib.sha512(input.encode('utf-8'))
        hex_dig = hashed_input.hexdigest()
        return hex_dig

    def credential_available(self, credentials):
        if not credentials.public_key:
            self.empty_credential_msg = "Public key not provided"
            self.empty_credential_data = "No available data"
            self.empty_credential_code = "011"
            return False
        elif not credentials.secret_key:
            self.empty_credential_msg = "Secret key not provided"
            self.empty_credential_data = "No available data"
            self.empty_credential_code = "012"
            return False
        elif not credentials.environment:
            credentials.environment = "DEMO"
            return True
        else:
            return True

    def throw_exception(self, code, message):
        response_data = []
        response = '{"responseCode": "' + code + \
                   '", "responseData": "' + str(response_data) + \
                   '", "responseMsg": "' + str(message) + '"}'
        base_response = BaseResponse(response)
        return base_response


