from flask import *
from client import *
app = Flask(__name__)

@app.route("/getAllAssets/<walletAddress>/", methods =['GET'])
def getAllAssets(walletAddress):
    response, success = wallet.getAssets(walletAddress)
    assetsTokens = []
    if success:
        for asset in response:
            assetsTokens.append(asset.tokenId)
        return jsonify(assetsTokens), 200
    else:
        return response.text, 400

@app.route('/getTotalUSDValueOfWallet/<walletAddress>', methods=['GET'])
def getTotalUSDValueOfWallet(walletAddress):
    value = 0
    wallet = Wallet()
    response, success = wallet.getAssets(walletAddress)
    if success:
        for asset in response:
            value += asset.quote
        return jsonify(value), 200
    else:
        return response.text, 400

@app.route('/getAllTransactions/<walletAddress>', methods=['GET'])
def getAllTransactions(walletAddress):
    wallet = Wallet()
    response, success = wallet.getTransactions(walletAddress)
    if success:
        return jsonify(response), 200
    else:
        return response.text, 400

if __name__ == '__main__':
    wallet = Wallet()
    app.run(debug=True)