from web3 import Web3
import json
from views import blockchain

ganache_url='http://127.0.0.1:7545'
web3=Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

web3.eth.defaultAccount=web3.eth.accounts[1]

abi=json.loads('''[
	{
		"inputs": [],
		"name": "getCurrentOwner",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getDetails",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getPreviousOwner",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_input",
				"type": "string"
			}
		],
		"name": "setCurrentOwner",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "CurrentOwner",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "Buyer",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "Price",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "RegId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "LandId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "aadharCurrOwner",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "aadharBuyer",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "OldLandCoord",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "NewLandCoord",
				"type": "string"
			}
		],
		"name": "setDetails",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')
bytecode = '608060405234801561001057600080fd5b50610e1c806100206000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c8063a18a186b1461005c578063be38cd6f1461007a578063cbb8923514610096578063dd135910146100b2578063fbbf93a0146100d0575b600080fd5b6100646100f6565b6040516100719190610b5b565b60405180910390f35b610094600480360381019061008f9190610904565b61018a565b005b6100b060048036038101906100ab919061094d565b6101a6565b005b6100ba6102a4565b6040516100c79190610b5b565b60405180910390f35b6100d8610339565b6040516100ed99989796959493929190610b7d565b60405180910390f35b606060008001805461010790610d00565b80601f016020809104026020016040519081016040528092919081815260200182805461013390610d00565b80156101805780601f1061015557610100808354040283529160200191610180565b820191906000526020600020905b81548152906001019060200180831161016357829003601f168201915b5050505050905090565b806000800190805190602001906101a29291906107f1565b5050565b876000800190805190602001906101be9291906107f1565b5088600060010190805190602001906101d89291906107f1565b5086600060020190805190602001906101f29291906107f1565b50846000600401908051906020019061020c9291906107f1565b5085600060030190805190602001906102269291906107f1565b5083600060050190805190602001906102409291906107f1565b50826000600601908051906020019061025a9291906107f1565b5042600060070181905550816000600801908051906020019061027e9291906107f1565b5080600060090190805190602001906102989291906107f1565b50505050505050505050565b6060600060010180546102b690610d00565b80601f01602080910402602001604051908101604052809291908181526020018280546102e290610d00565b801561032f5780601f106103045761010080835404028352916020019161032f565b820191906000526020600020905b81548152906001019060200180831161031257829003601f168201915b5050505050905090565b606080606080606080606080600080600001600060010160006002016000600401600060050160006006016000600801600060090160006007015488805461038090610d00565b80601f01602080910402602001604051908101604052809291908181526020018280546103ac90610d00565b80156103f95780601f106103ce576101008083540402835291602001916103f9565b820191906000526020600020905b8154815290600101906020018083116103dc57829003601f168201915b5050505050985087805461040c90610d00565b80601f016020809104026020016040519081016040528092919081815260200182805461043890610d00565b80156104855780601f1061045a57610100808354040283529160200191610485565b820191906000526020600020905b81548152906001019060200180831161046857829003601f168201915b5050505050975086805461049890610d00565b80601f01602080910402602001604051908101604052809291908181526020018280546104c490610d00565b80156105115780601f106104e657610100808354040283529160200191610511565b820191906000526020600020905b8154815290600101906020018083116104f457829003601f168201915b5050505050965085805461052490610d00565b80601f016020809104026020016040519081016040528092919081815260200182805461055090610d00565b801561059d5780601f106105725761010080835404028352916020019161059d565b820191906000526020600020905b81548152906001019060200180831161058057829003601f168201915b505050505095508480546105b090610d00565b80601f01602080910402602001604051908101604052809291908181526020018280546105dc90610d00565b80156106295780601f106105fe57610100808354040283529160200191610629565b820191906000526020600020905b81548152906001019060200180831161060c57829003601f168201915b5050505050945083805461063c90610d00565b80601f016020809104026020016040519081016040528092919081815260200182805461066890610d00565b80156106b55780601f1061068a576101008083540402835291602001916106b5565b820191906000526020600020905b81548152906001019060200180831161069857829003601f168201915b505050505093508280546106c890610d00565b80601f01602080910402602001604051908101604052809291908181526020018280546106f490610d00565b80156107415780601f1061071657610100808354040283529160200191610741565b820191906000526020600020905b81548152906001019060200180831161072457829003601f168201915b5050505050925081805461075490610d00565b80601f016020809104026020016040519081016040528092919081815260200182805461078090610d00565b80156107cd5780601f106107a2576101008083540402835291602001916107cd565b820191906000526020600020905b8154815290600101906020018083116107b057829003601f168201915b50505050509150985098509850985098509850985098509850909192939495969798565b8280546107fd90610d00565b90600052602060002090601f01602090048101928261081f5760008555610866565b82601f1061083857805160ff1916838001178555610866565b82800160010185558215610866579182015b8281111561086557825182559160200191906001019061084a565b5b5090506108739190610877565b5090565b5b80821115610890576000816000905550600101610878565b5090565b60006108a76108a284610c67565b610c42565b9050828152602081018484840111156108c3576108c2610dc6565b5b6108ce848285610cbe565b509392505050565b600082601f8301126108eb576108ea610dc1565b5b81356108fb848260208601610894565b91505092915050565b60006020828403121561091a57610919610dd0565b5b600082013567ffffffffffffffff81111561093857610937610dcb565b5b610944848285016108d6565b91505092915050565b60008060008060008060008060006101208a8c0312156109705761096f610dd0565b5b60008a013567ffffffffffffffff81111561098e5761098d610dcb565b5b61099a8c828d016108d6565b99505060208a013567ffffffffffffffff8111156109bb576109ba610dcb565b5b6109c78c828d016108d6565b98505060408a013567ffffffffffffffff8111156109e8576109e7610dcb565b5b6109f48c828d016108d6565b97505060608a013567ffffffffffffffff811115610a1557610a14610dcb565b5b610a218c828d016108d6565b96505060808a013567ffffffffffffffff811115610a4257610a41610dcb565b5b610a4e8c828d016108d6565b95505060a08a013567ffffffffffffffff811115610a6f57610a6e610dcb565b5b610a7b8c828d016108d6565b94505060c08a013567ffffffffffffffff811115610a9c57610a9b610dcb565b5b610aa88c828d016108d6565b93505060e08a013567ffffffffffffffff811115610ac957610ac8610dcb565b5b610ad58c828d016108d6565b9250506101008a013567ffffffffffffffff811115610af757610af6610dcb565b5b610b038c828d016108d6565b9150509295985092959850929598565b6000610b1e82610c98565b610b288185610ca3565b9350610b38818560208601610ccd565b610b4181610dd5565b840191505092915050565b610b5581610cb4565b82525050565b60006020820190508181036000830152610b758184610b13565b905092915050565b6000610120820190508181036000830152610b98818c610b13565b90508181036020830152610bac818b610b13565b90508181036040830152610bc0818a610b13565b90508181036060830152610bd48189610b13565b90508181036080830152610be88188610b13565b905081810360a0830152610bfc8187610b13565b905081810360c0830152610c108186610b13565b905081810360e0830152610c248185610b13565b9050610c34610100830184610b4c565b9a9950505050505050505050565b6000610c4c610c5d565b9050610c588282610d32565b919050565b6000604051905090565b600067ffffffffffffffff821115610c8257610c81610d92565b5b610c8b82610dd5565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b6000819050919050565b82818337600083830152505050565b60005b83811015610ceb578082015181840152602081019050610cd0565b83811115610cfa576000848401525b50505050565b60006002820490506001821680610d1857607f821691505b60208210811415610d2c57610d2b610d63565b5b50919050565b610d3b82610dd5565b810181811067ffffffffffffffff82111715610d5a57610d59610d92565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f830116905091905056fea26469706673582212201f7657a1282ccd5228afce4b0d9ba4a9a9293a798e29441201223e9defc9ba2164736f6c63430008070033'

set=web3.eth.contract(abi=abi, bytecode=bytecode)
setDetails=web3.eth.contract(abi=abi, bytecode=bytecode)

# tx_hash=setDetails.constructor().transact()

# tx_reciept = web3.eth.wait_for_transaction_receipt(tx_hash)

contract = web3.eth.contract(
    address='0xD172BDE953c084Dc998d8eE363745BF503eF5cf9',
    abi=abi
)
current_owner = contract.functions.getCurrentOwner().call()
# if current_owner==

# print(contract.functions.getDetails().call())
# tx_hash = contract.functions.setDetails('Seller','buyer','5000','122345','land id','aadharc','aadharb','oldc','newc').transact()
# tx_reciept = web3.eth.wait_for_transaction_receipt(tx_hash)
# print(contract.functions.getDetails().call())
#
# print(contract.functions.getDetails().call())
# tx_hash = contract.functions.setDetails('Ashish','Ujjwal','50000000','98765','12345','3476978953','439865893467','4985723','4985723').transact()
# tx_reciept = web3.eth.wait_for_transaction_receipt(tx_hash)
# print(contract.functions.getDetails().call())