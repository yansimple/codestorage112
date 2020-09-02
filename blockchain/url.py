from urllib.request import urlopen
import json


wallet = input("Enter your wallet and press Enter: ")
print(len(wallet))
url = 'https://blockchain.info/rawaddr/' + wallet

url1 = "https://blockchain.info/q/getblockcount"

response = urlopen(url)

response1 = urlopen(url1)

string = response.read().decode('utf-8')

json_obj = json.loads(string)

string1 = response1.read().decode('utf-8')

all_blocks = json.loads(string1)

tx_id = json_obj['txs'][0]['inputs'][0]["prev_out"]['spending_outpoints'][0]['tx_index']

link_tx = "https://blockchain.info/rawtx/" + str(tx_id)


value = json_obj['txs'][1]['inputs'][0]["prev_out"]['value']

#print("VALUE: " , json_obj['txs'][1]['inputs'][0]["prev_out"]['value'])#сумма транзакции
#print("tr_index: ",tx_id)#Индекс транзакции/последняя входящаяя
#print("All blocks: ",all_blocks)
#print(link_tx)

response_tr = urlopen(link_tx)

string_tr = response_tr.read().decode('utf-8')

height_json = json.loads(string_tr)

#print(height_json["block_height"])

try:
	height = height_json["block_height"]

	number_conf = all_blocks - height + 1

	print("\n\n\nBitCoin-адресс ", wallet,"\nКолличество подтверждений на последней транзакции: ",number_conf)

	if number_conf >= 2:
		print("NOTIFICATION")
	
except:
	print("")
