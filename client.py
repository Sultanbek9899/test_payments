from abstract_client import AbstractInteractionClient
from models import TransactionResponse

class Client(AbstractInteractionClient):
    URL = "https://api.cloudpayments.ru/"

    def __init__(self, public_token, secret_id):
        self.public_token = public_token
        self.secret_id = secret_id
    
    def charge(self, cryptogram, amount, currency, name, ip_address,
                    invoice_id=None, description=None, account_id=None,
                    email=None, data=None, require_confirmation=False,
                    service_fee=None):
        params = {
            'Amount': amount,
            'Currency': currency,
            'IpAddress': ip_address,
            'Name': name,
            'CardCryptogramPacket': cryptogram

        }
        if invoice_id is not None:
            params['InvoiceId'] = invoice_id
        if description is not None:
            params['Description'] = description
        if account_id is not None:
            params['AccountId'] = account_id
        if email is not None:
            params['Email'] = email
        if service_fee is not None:
            params['PayerServiceFee'] = service_fee
        if data is not None:
            params['JsonData'] = data

        if require_confirmation:
            url = self.URL + 'payments/cards/auth' 
        else:
            url = self.URL + 'payments/cards/charge'
        response = self.post(url=url, data = params)

        if response['Success']:
            return TransactionResponse.dump(response['Model'])
        if response['Message']:
            raise Exception(response["Message"])
        if 'ReasonCode' in response['Model']:
            raise Exception(response['Model']['Reason'])

    