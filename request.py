import requests
import json
import config, utils
import argparse
from pathlib import Path
import curlify
from Model import Model 

	
def curl_request(url,method,headers,payloads):
    # construct the curl command from request
    command = "curl -v -H {headers} {data} -X {method} {uri}"
    data = "" 
    if payloads:
        payload_list = ['"{0}":"{1}"'.format(k,v) for k,v in payloads.items()]
        data = " -d '{" + ", ".join(payload_list) + "}'"
    header_list = ['"{0}: {1}"'.format(k, v) for k, v in headers.items()]
    header = " -H ".join(header_list)
    print(command.format(method=method, headers=header, data=data, uri=url))



if __name__ == '__main__':

	# local url
	url = config.LOCAL_URL
	# url = config.HEROKU_URL

	method = 'POST'
	headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

	filepath = 'sample_input_file.csv'
	features = '["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"]'
	target_feature = 'Price_Premium'
	index = 'Index'
	segment = 'segment'
	target = 'Price Premium'
	price_per_segment = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json'
	# price_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json'
	# price_threshold_power_index = 'sample_threshold_with_power_index.json'
	global_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/global_threshold.json'
	customised_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/customised_threshold_final.json'
	price_power_index_threshold	 = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_power_index_final.json'



	function = 'features_assessment' 
	url_ = url+function 
	data = '{"filepath" :"'+filepath+'", "features":'+str(features)+', "target_feature":"'+target_feature+'"}'
	data_json = json.loads(data)

	print(url_,	data)

	send_request = requests.post(url_, data, headers=headers)

	print(curlify.to_curl(send_request.request))

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')


	print('===================================================================')


	function = 'segmentation' 
	url_ = url+function 
	data = '{"filepath" :"'+filepath+'", "features":'+str(features)+', "target_feature":"'+target_feature+'","index":"'+index+'"}'
	
	print(url_,data)

	send_request = requests.post(url_, data, headers=headers)	

	print(curlify.to_curl(send_request.request))

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')

	
	print('===================================================================')


	function = 'price_segmentation' 
	url_ = url+function 
	data = '{"price_per_segment" :"'+price_per_segment+'", "price_threshold":"'+global_threshold+'", "segment":"'+segment+'","target":"'+target+'"}'
	
	print(url_,data)

	send_request = requests.post(url_, data, headers=headers)

	print(curlify.to_curl(send_request.request))

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')


	print('===================================================================')


	function = 'price_segmentation' 
	url_ = url+function 
	data = '{"price_per_segment" :"'+price_per_segment+'", "price_threshold":"'+customised_threshold+'", "segment":"'+segment+'","target":"'+target+'"}'
	

	print(url_,data)

	send_request = requests.post(url_, data, headers=headers)

	print(curlify.to_curl(send_request.request))

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')

	print('===================================================================')


	function = 'price_segmentation' 
	url_ = url+function 
	data = '{"price_per_segment" :"'+price_per_segment+'", "price_threshold":"'+price_power_index_threshold+'", "segment":"'+segment+'","target":"'+target+'"}'
	

	print(url_,data)

	send_request = requests.post(url_, data, headers=headers)

	print(curlify.to_curl(send_request.request))

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')
