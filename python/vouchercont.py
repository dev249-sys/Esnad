from web3 import Web3
web3 = Web3(Web3.HTTPProvider('http://localhost:5000'))
if not web3.isConnected():
    raise Exception('Failed to connect to Ethereum node')
contract_address = '0xYourContractAddress'
contract_abi = [
    {
        'constant': False,
        'inputs': [
            {'name': '_date', 'type': 'string'},
            {'name': '_officiant', 'type': 'string'},
            {'name': '_area', 'type': 'string'},
            {'name': '_husbandName', 'type': 'string'},
            {'name': '_husbandNationalID', 'type': 'string'},
            {'name': '_husbandAgent', 'type': 'string'},
            {'name': '_wifeName', 'type': 'string'},
            {'name': '_wifeNationalID', 'type': 'string'},
            {'name': '_wifeGuardian', 'type': 'string'},
            {'name': '_witness1Name', 'type': 'string'},
            {'name': '_witness1NationalID', 'type': 'string'},
            {'name': '_witness2Name', 'type': 'string'},
            {'name': '_witness2NationalID', 'type': 'string'}
        ],
        'name': 'setCertificate',
        'outputs': [],
        'type': 'function'
    },
    {
        'constant': True,
        'inputs': [],
        'name': 'getCertificate',
        'outputs': [
            {'components': [
                {'name': 'date', 'type': 'string'},
                {'name': 'officiant', 'type': 'string'},
                {'name': 'area', 'type': 'string'},
                {'name': 'husbandName', 'type': 'string'},
                {'name': 'husbandNationalID', 'type': 'string'},
                {'name': 'husbandAgent', 'type': 'string'},
                {'name': 'wifeName', 'type': 'string'},
                {'name': 'wifeNationalID', 'type': 'string'},
                {'name': 'wifeGuardian', 'type': 'string'},
                {'name': 'witness1Name', 'type': 'string'},
                {'name': 'witness1NationalID', 'type': 'string'},
                {'name': 'witness2Name', 'type': 'string'},
                {'name': 'witness2NationalID', 'type': 'string'}
            ], 'name': '', 'type': 'tuple'}
        ],
        'type': 'function'
    }
]
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
account_address = '0xYourAccountAddress'
web3.eth.defaultAccount = account_address
data = {
    'date': '2025-02-02',
    'officiant': 'اسم المأذون',
    'area': 'اسم المنطقة',
    'husbandName': 'اسم الزوج',
    'husbandNationalID': '12345678901',
    'husbandAgent': 'اسم وكيل الزوج',
    'wifeName': 'اسم الزوجة',
    'wifeNationalID': '10987654321',
    'wifeGuardian': 'اسم ولي الزوجة',
    'witness1Name': 'اسم الشاهد الأول',
    'witness1NationalID': '11223344556',
    'witness2Name': 'اسم الشاهد الثاني',
    'witness2NationalID': '66554433221'
}
tx_hash = contract.functions.setCertificate(
    data['date'],
    data['officiant'],
    data['area'],
    data['husbandName'],
    data['husbandNationalID'],
    data['husbandAgent'],
    data['wifeName'],
    data['wifeNationalID'],
    data['wifeGuardian'],
    data['witness1Name'],
    data['witness1NationalID'],
    data['witness2Name'],
    data['witness2NationalID']
).transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print("Data successfully sent to the smart contract!")
