import requests
from requests.auth import HTTPBasicAuth

class Wallet():
    def __init__(self):
        self.authKey = f'cqt_rQyqcWHRJhkyTFKqfJjcYYmpdtTP'

    def getAssets(self, walletAddress):
        assets = []
        url = f'https://api.covalenthq.com/v1/eth-mainnet/address/{walletAddress}/balances_v2/?'
        headers = {
            "accept": "application/json",
        }
        basic = HTTPBasicAuth(f'{self.authKey}', '')
        response = requests.get(url, headers=headers, auth=basic)
        success = response.status_code == 200 and response.text.data.chain_name == 'eth-mainnet'
        if success:
            assets = response.text.data.items
            return assets, success
        else:
            return response, success

    def getTransactions(self,walletAddress):
        page = 1
        transactions = []
        while True:
            url = f'https://api.covalenthq.com/v1/eth-mainnet/address/{walletAddress}/transactions_v3/page/{page}/?'
            headers = {
                "accept": "application/json",
            }
            basic = HTTPBasicAuth(f'{self.authKey}', '')
            response = requests.get(url, headers=headers, auth=basic)
            if len(response.text) == 0:
                break
            print(response.text)
            transactions += response.text

        return transactions
