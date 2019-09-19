import logging

from Responses.SdkResponseCode import SdkResponseCode
from RemitaBillingService.SetEnvironment import SetEnvironment


class EnvironmentConfig:

    def set_billing_environment(credentials):
        trim_environment = credentials.environment.strip()
        environment_to_upper = trim_environment.upper()
        if environment_to_upper == SetEnvironment.DEMO:
            test_url = "https://remitademo.net/remita/exapp/api/v1/send/api/bgatesvc/billing/"
            billing_environment = {'PUBLIC_KEY': credentials.public_key,
                                   'SECRET_KEY': credentials.secret_key,
                                   'ENVIRONMENT': credentials.environment,
                                   'GET_BILLER_URL': test_url + "billers",
                                   'GET_URL': test_url,
                                   'GET_CUSTOM_FIELD_URL': test_url + "{}/servicetypes/{}",
                                   'GET_RRR_DETAILS_URL': test_url + "lookup/{}",
                                   'GENERATE_RRR_URL': test_url + "generate",
                                   'GET_TXN_STATUS_URL': test_url + "payment/status",
                                   'VALIDATE_REQUEST_URL': test_url + "validate",
                                   'NOTIFICATION_URL': test_url + "payment/notify"
                                   }
            return billing_environment
        elif environment_to_upper == SetEnvironment.LIVE:
            live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/bgatesvc/billing/"
            billing_environment = {'PUBLIC_KEY': credentials.public_key,
                                   'SECRET_KEY': credentials.secret_key,
                                   'ENVIRONMENT': credentials.environment,
                                   'GET_BILLER_URL': live_url + "billers",
                                   'GET_URL': live_url,
                                   'GET_CUSTOM_FIELD_URL': live_url + "{}/servicetypes/{}",
                                   'GET_RRR_DETAILS_URL': live_url + "lookup/{}",
                                   'GENERATE_RRR_URL': live_url + "generate",
                                   'GET_TXN_STATUS_URL': live_url + "payment/status",
                                   'VALIDATE_REQUEST_URL': live_url + "validate",
                                   'NOTIFICATION_URL': live_url + "payment/notify"
                                   }
            return billing_environment
        else:
            logging.error(SdkResponseCode.INVADE_ENVIRONMENT)

    def set_time_out(credentials):
        if not credentials.connection_timeout:
            credentials.connection_timeout = 30000
        if not credentials.read_timeout:
            credentials.read_timeout = 20000
        environment_time_out = {'READ_TIMEOUT': credentials.read_timeout,
                                'CONNECTION_TIMEOUT': credentials.connection_timeout}
        return environment_time_out