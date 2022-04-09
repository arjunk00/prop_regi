from django.shortcuts import render
from web3 import Web3
import json
from django.shortcuts import render, redirect, get_object_or_404
from app import deploy_smart_contract
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'index.html')

def blockchain(request):
    # ganache_url="http://127.0.0.1:7545"
    # web3=Web3(Web3.HTTPProvider(ganache_url))
    #
    # web3.eth.defaultAccount=web3.eth.accounts[0]
    #
    # abi = json.loads('''[{"inputs": [], "name": "retrieve",
    #                     "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
    #                     "stateMutability": "view", "type": "function"},
    #                    {"inputs": [{"internalType": "uint256", "name": "num", "type": "uint256"}], "name": "store",
    #                     "outputs": [], "stateMutability": "nonpayable", "type": "function"}]''')
    # bytecode = '608060405234801561001057600080fd5b50600436106100365760003560e01c80632e64cec11461003b5780636057361d14610059575b600080fd5b610043610075565b60405161005091906100a1565b60405180910390f35b610073600480360381019061006e91906100ed565b61007e565b005b60008054905090565b8060008190555050565b6000819050919050565b61009b81610088565b82525050565b60006020820190506100b66000830184610092565b92915050565b600080fd5b6100ca81610088565b81146100d557600080fd5b50565b6000813590506100e7816100c1565b92915050565b600060208284031215610103576101026100bc565b5b6000610111848285016100d8565b9150509291505056fea264697066735822122044f0132d3ce474198482cc3f79c22d7ed4cece5e1dcbb2c7cb533a23068c5d6064736f6c634300080d0033'
    #
    # store=web3.eth.contract(abi=abi, bytecode=bytecode)
    #
    # tx_hash=store.constructor().transact()
    # return redirect('/blockchain')


    ##get

    deploy_smart_contract()
