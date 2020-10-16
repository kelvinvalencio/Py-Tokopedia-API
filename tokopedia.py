#!/usr/lib/python3

import requests, base64, json, os

base_url = 'https://fs.tokopedia.net'
accounts_url = 'https://accounts.tokopedia.com'

# constants you need to fill before executing the script
client_id = b'<your client_id>'
client_secret = b'<your client_secret>'
fs_id = '<your fs_id>'
# global shop_id for testing, if you links multiple shops, implement your own shop_id
shop_id = '<your shop_id>'



def get_token(basic_token):
	print(basic_token)
	url = f'{accounts_url}/token?grant_type=client_credentials'

	header = {
		'Authorization': f'Basic {basic_token}',
		'Content-Length': '0',
		'Content-Type': 'application/json'
	}

	response = requests.post(url, headers=header)
	token = response.json()['access_token']
	print(f'get_token(): response {response.text}')

	return token



def get_product_info(token, sku):
	url = f'{base_url}/inventory/v1/fs/{fs_id}/product/info?sku={sku}'
	
	header = { 
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}

	response = requests.get(url, headers=header)

	return response.json()



def get_all_etalase(token):
	url = f'{base_url}/inventory/v1/fs/{fs_id}/product/etalase?shop_id={shop_id}'

	header = { 
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}

	response = requests.get(url, headers=header)

	return response.json()



def update_stock(token, sku, new_stock):
	url = f'{base_url}/inventory/v1/fs/{fs_id}/stock/update?shop_id={shop_id}'

	header = { 
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}

	data = [
		{
			'sku': sku,
			'new_stock': new_stock
		}
	]

	response = requests.post(url, json=data, headers=header)

	return response.json()



def update_price(token, sku, new_price):
	url = f'{base_url}/inventory/v1/fs/{fs_id}/price/update?shop_id={shop_id}'
	
	header = { 
		'Authorization': f'Bearer {token}',
		'Content-Type': 'application/json'
	}

	data = [
		{
			'sku': sku,
			'new_price': new_price
		}
	]

	response = requests.post(url, json=data, headers=header)

	return response.json()



def main():
	basic_token = base64.b64encode(client_id + b':' + client_secret).decode('utf-8')
	token = ''

	try:
		# Reads token from tokopedia_token.txt if file exists
		f_token = open('tokopedia_token.txt', 'r')
		token = f_token.read().strip()
		print(f'Using token from tokopedia_token.txt, token is {token}')

	except FileNotFoundError:
		# Writes tokopedia_token.txt, generates token, writes to the file
		print('tokopedia_token.txt not found, creating one.')
		f_token = open('tokopedia_token.txt', 'w')
		f_token.write( get_token(basic_token) )
		f_token = open('tokopedia_token.txt', 'r')
		token = f_token.read()

	# example use of get_all_etalase function
	print( json.dumps(get_all_etalase(token), indent=4, sort_keys=True) )



if __name__ == "__main__":
    main()