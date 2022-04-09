from django.shortcuts import render
from web3 import Web3
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'index.html')

def blockchain(request):
    ganache_url="http://127.0.0.1:7545"
    web3=Web3(Web3.HTTPProvider(ganache_url))
    success=web3.isConnected()
    if success==1:
        return redirect('/')
    else:
        return redirect('/blockchain')
