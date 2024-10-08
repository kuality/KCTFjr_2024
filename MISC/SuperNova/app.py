import os
import json
import time
import uuid
from dataclasses import dataclass
from typing import Optional

import aiohttp
from flask import Flask, jsonify, request
from web3 import Web3
from web3.middleware import geth_poa_middleware

app = Flask(__name__)

rpc_url = os.getenv("WEB3_PROVIDER_URI", "http://127.0.0.1:8546")

web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract_abi = [{"inputs":[{"internalType":"address","name":"_wallet","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"solver","type":"address"}],"name":"ChallengeSolved","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"buyer","type":"address"},{"indexed":False,"internalType":"string","name":"letter","type":"string"},{"indexed":False,"internalType":"uint8","name":"quantity","type":"uint8"}],"name":"LetterPurchased","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"string","name":"","type":"string"}],"name":"cart","outputs":[{"internalType":"uint8","name":"quantity","type":"uint8"},{"internalType":"bool","name":"exists","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isChallSolved","outputs":[{"internalType":"bool","name":"solved","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"letter","type":"string"},{"internalType":"bytes32","name":"password","type":"bytes32"}],"name":"purchaseLetter","outputs":[],"stateMutability":"payable","type":"function"}]
contract_bytecode = '60016101a0818152605360f81b6101c05260809081526101e0828152605560f81b6102005260a052610220828152600560fc1b6102405260c052610260828152604560f81b6102805260e0526102a0828152602960f91b6102c052610100526102e0828152602760f91b6103005261012052610320828152604f60f81b6103405261014052610360828152602b60f91b61038052610160526103e06040526103a0918252604160f81b6103c05261018091909152620000c3906004906009620002a7565b50348015620000d157600080fd5b5060405162000d3338038062000d33833981016040819052620000f49162000371565b600380546001600160a01b0319166001600160a01b03831617905560408051605360f81b81526001818101819052825191829003602190810183208054600460ff199182168117909255605560f81b85528484018490528551948590038301852080548216909217909155600560fc1b8452838301839052845193849003820184208054821684179055604560f81b8452838301839052845193849003820184208054821684179055602960f91b8452838301839052845193849003820184208054821684179055602760f91b8452838301839052845193849003820184208054821684179055604f60f81b8452838301839052845193849003820184208054821684179055602b60f91b8452838301839052845193849003820184208054821684179055604160f81b8452838301839052935192839003019091208054909216179055620002426200024c565b600055506200053c565b60004244336200025e600143620003a3565b6040805160208101959095528401929092526001600160601b0319606091821b169083015240607482015260940160405160208183030381529060405280519060200120905090565b8260098101928215620002e5579160200282015b82811115620002e55782518290620002d4908262000470565b5091602001919060010190620002bb565b50620002f3929150620002f7565b5090565b80821115620002f35760006200030e828262000318565b50600101620002f7565b5080546200032690620003e1565b6000825580601f1062000337575050565b601f0160209004906000526020600020908101906200035791906200035a565b50565b5b80821115620002f357600081556001016200035b565b6000602082840312156200038457600080fd5b81516001600160a01b03811681146200039c57600080fd5b9392505050565b81810381811115620003c557634e487b7160e01b600052601160045260246000fd5b92915050565b634e487b7160e01b600052604160045260246000fd5b600181811c90821680620003f657607f821691505b6020821081036200041757634e487b7160e01b600052602260045260246000fd5b50919050565b601f8211156200046b57600081815260208120601f850160051c81016020861015620004465750805b601f850160051c820191505b81811015620004675782815560010162000452565b5050505b505050565b81516001600160401b038111156200048c576200048c620003cb565b620004a4816200049d8454620003e1565b846200041d565b602080601f831160018114620004dc5760008415620004c35750858301515b600019600386901b1c1916600185901b17855562000467565b600085815260208120601f198616915b828110156200050d57888601518255948401946001909101908401620004ec565b50858210156200052c5787850151600019600388901b60f8161c191681555b5050505050600190811b01905550565b6107e7806200054c6000396000f3fe6080604052600436106100345760003560e01c806341ee17971461003957806348eea83a146100ac578063ed7e286b146100c1575b600080fd5b34801561004557600080fd5b5061008e6100543660046105af565b6002602090815260009283526040909220815180830184018051928152908401929093019190912091525460ff8082169161010090041682565b6040805160ff90931683529015156020830152015b60405180910390f35b6100bf6100ba36600461060b565b6100e6565b005b3480156100cd57600080fd5b506100d66102e7565b60405190151581526020016100a3565b6003546001600160a01b031633146101195760405162461bcd60e51b815260040161011090610650565b60405180910390fd5b61012282610473565b61017c5760405162461bcd60e51b815260206004820152602560248201527f496e76616c6964206c65747465722e204f6e6c7920612d7a2c20412d5a20616c6044820152641b1bddd95960da1b6064820152608401610110565b60005481146101c05760405162461bcd60e51b815260206004820152601060248201526f125b9d985b1a59081c185cdcdddbdc9960821b6044820152606401610110565b3360009081526002602052604080822090516101dd9085906106b9565b908152604051908190036020019020805490915060ff6101009091041615610234578054600190829060009061021790849060ff166106eb565b92506101000a81548160ff021916908360ff1602179055506102a0565b6040805180820182526001808252602080830191909152336000908152600290915282902091519091906102699086906106b9565b9081526040516020918190038201902082518154939092015160ff90921661ffff1990931692909217610100911515919091021790555b805460405133917fddec5e1114021679777180db0924ae5367bc273ef9cf998db5da436c7006c047916102da91879160ff9091169061070a565b60405180910390a2505050565b6003546000906001600160a01b031633146103145760405162461bcd60e51b815260040161011090610650565b60005b600981101561046b5760006004826009811061033557610335610748565b0180546103419061075e565b80601f016020809104026020016040519081016040528092919081815260200182805461036d9061075e565b80156103ba5780601f1061038f576101008083540402835291602001916103ba565b820191906000526020600020905b81548152906001019060200180831161039d57829003601f168201915b505033600090815260026020526040808220905195965090949093506103e392508591506106b9565b9081526040805160209281900383018120818301909252905460ff80821683526101009091041615801592820192909252915080610447575060018260405161042c91906106b9565b90815260405190819003602001902054815160ff9182169116105b15610456576000935050505090565b5050808061046390610798565b915050610317565b506001905090565b8051600090829060011461048a5750600092915050565b60008160008151811061049f5761049f610748565b01602001516001600160f81b0319169050604160f81b81108015906104d25750602d60f91b6001600160f81b0319821611155b806105045750606160f81b6001600160f81b03198216108015906105045750603d60f91b6001600160f81b0319821611155b949350505050565b634e487b7160e01b600052604160045260246000fd5b600082601f83011261053357600080fd5b813567ffffffffffffffff8082111561054e5761054e61050c565b604051601f8301601f19908116603f011681019082821181831017156105765761057661050c565b8160405283815286602085880101111561058f57600080fd5b836020870160208301376000602085830101528094505050505092915050565b600080604083850312156105c257600080fd5b82356001600160a01b03811681146105d957600080fd5b9150602083013567ffffffffffffffff8111156105f557600080fd5b61060185828601610522565b9150509250929050565b6000806040838503121561061e57600080fd5b823567ffffffffffffffff81111561063557600080fd5b61064185828601610522565b95602094909401359450505050565b60208082526025908201527f506c6561736520757365207468652077616c6c65742070726f766964656420746040820152646f20796f7560d81b606082015260800190565b60005b838110156106b0578181015183820152602001610698565b50506000910152565b600082516106cb818460208701610695565b9190910192915050565b634e487b7160e01b600052601160045260246000fd5b60ff8181168382160190811115610704576107046106d5565b92915050565b6040815260008351806040840152610729816060850160208801610695565b60ff93909316602083015250601f91909101601f191601606001919050565b634e487b7160e01b600052603260045260246000fd5b600181811c9082168061077257607f821691505b60208210810361079257634e487b7160e01b600052602260045260246000fd5b50919050565b6000600182016107aa576107aa6106d5565b506001019056fea26469706673582212201aa6de5bf8f794712e509439362b1f62d175b8d164cd21dcfdf2ec36a38fb04264736f6c63430008110033'


@dataclass
class RPCError:
    code: int
    message: str

PARSE_ERROR = RPCError(code=-32700, message="Parse error")
INVALID_REQUEST = RPCError(code=-32600, message="Invalid request")
METHOD_NOT_SUPPORTED = RPCError(code=-32004, message="Method not supported")
RESULT_UNAVAILABLE = RPCError(code=-32002, message="Resource unavailable")

ALLOWED_METHODS = frozenset(
    [
        "eth_blockNumber",
        "eth_call",
        "eth_chainId",
        "eth_estimateGas",
        "eth_gasPrice",
        "eth_getBalance",
        "eth_getBlockByHash",
        "eth_getBlockByNumber",
        "eth_getCode",
        "eth_getStorageAt",
        "eth_getTransactionByHash",
        "eth_getTransactionCount",
        "eth_getTransactionReceipt",
        "eth_sendRawTransaction",
        "net_version",
        "rpc_modules",
        "web3_clientVersion",
    ]
)

def error_response(error: RPCError, status_code: int, request_id: Optional[int] = None):
    return jsonify({
        "jsonrpc": "2.0",
        "error": {
            "code": error.code,
            "message": error.message,
        },
        "id": request_id,
    }), status_code

async def dispatch_request(provider: str, body: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(provider, json=body) as response:
            return await response.json()

user_data = {}

cnt = 0

def deploy_contract_for_user(user_id):
    global cnt

    while not os.path.exists("/shared/accounts.json"):
        time.sleep(1)

    with open("/shared/accounts.json") as f:
        accounts_data = json.load(f)
    
    ganache_accounts = accounts_data["addresses"]
    private_keys = accounts_data["private_keys"]
    # If you use 'ganache-cli', use the code below
    #ganache_accounts = list(accounts_data["addresses"].keys())
    #private_keys = [bytes(value['secretKey']['data']).hex() for value in accounts_data["addresses"].values()]

    if user_id not in user_data:
        deployer = list(ganache_accounts.keys())[cnt]
        private_key = private_keys[deployer]
        deployer = Web3.to_checksum_address(deployer)

        MirinaeStation = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
        try:
            transaction = MirinaeStation.constructor(deployer).build_transaction({
                'from': deployer,
                'nonce': web3.eth.get_transaction_count(deployer),
                'gas': 2000000,
                'gasPrice': web3.to_wei('20', 'gwei')
            })

            signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

            rpc_url = f"http://3.34.91.236:20101/interact/{user_id}"

            deployment_info = {
                "contractAddress": tx_receipt.contractAddress,
                "walletAddress": deployer,
                "privateKey": private_key,
                "rpcUrl": rpc_url,
                "user_id": user_id
            }

            user_data[user_id] = deployment_info
            cnt += 1

        except Exception as e:
            print(f"Error in transaction: {e}")
            return str(e), deployer, private_key

    return user_data[user_id]

def gen_uuid():
    rand_uuid = str(uuid.uuid4())
    while rand_uuid in user_data:
        rand_uuid = str(uuid.uuid4())
    return rand_uuid


@app.route('/info', methods=['GET'])
def info():
    user_id = gen_uuid()
    deployment_info = deploy_contract_for_user(user_id)
    return jsonify({"user_id": user_id})

@app.route('/info/<user_id>', methods=['GET'])
def info_with_id(user_id):
    if user_id not in user_data:
        return error_response(RESULT_UNAVAILABLE, 400)
    
    deployment_info = user_data[user_id]
    return jsonify(deployment_info)

@app.route('/flag/<user_id>', methods=['GET'])
def flag(user_id):
    if user_id not in user_data:
        return error_response(RESULT_UNAVAILABLE, 400)
    
    deployment_info = deploy_contract_for_user(user_id)
    contract_address = deployment_info['contractAddress']
    wallet_address = deployment_info['walletAddress']

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    solved = contract.functions.isChallSolved().call({'from': wallet_address})

    flag = open("./flag.txt", "r").read()

    result = f"Challenge Solved!! {flag}" if solved else "Challenge Not Solved"
    with open(f'result_{user_id}.txt', 'w') as f:
        f.write(result)

    return result

@app.route('/interact/<user_id>', methods=['POST'])
async def interact(user_id):
    if user_id not in user_data:
        return error_response(RESULT_UNAVAILABLE, 400)

    try:
        body = request.get_json()
    except ValueError:
        return error_response(PARSE_ERROR, 415)

    request_id = body.get("id")
    body_keys = [key.lower() for key in body.keys()]
    if body_keys.count("method") != 1 or not isinstance(body["method"], str):
        return error_response(INVALID_REQUEST, 401, request_id)

    if body["method"] not in ALLOWED_METHODS:
        return error_response(METHOD_NOT_SUPPORTED, 401, request_id)

    try:
        if body["method"] == "eth_sendRawTransaction":
            raw_tx = body["params"][0]
            tx_hash = web3.eth.send_raw_transaction(raw_tx)
            response = {"jsonrpc": "2.0", "result": tx_hash.hex(), "id": request_id}
        else:
            #if body["method"] == "eth_call" or body["method"] == "eth_sendTransaction":
            #    if "gasPrice" not in body["params"][0]:
            #        body["params"][0]["gasPrice"] = web3.to_wei('20', 'gwei')
            response = await dispatch_request(
                os.getenv("WEB3_PROVIDER_URI", rpc_url), body
            )
            if (
                body["method"] in ("eth_getBlockByHash", "eth_getBlockByNumber")
                and "result" in response
            ):
                response["result"]["transactions"] = []
        return jsonify(response)
    except Exception as e:
        print(f"Exception: {e}")
        return error_response(RESULT_UNAVAILABLE, 500, request_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
