import requests
import json
import config, utils
import argparse
from pathlib import Path

from Model import Model 

	


if __name__ == '__main__':

	# local url
	url = config.LOCAL_URL
	# url = config.HEROKU_URL

	filepath = 'sample_input_file.csv'
	features = '["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"]'
	target_feature = 'Price_Premium'
	index = 'Index'
	segment = 'segment'
	target = 'Price Premium'
	price_per_segment = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json'
	price_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json'
	price_threshold_power_index = 'sample_threshold_with_power_index.json'


	function = 'features_assessment' 
	url_ = url+function 
	data = '{"filepath" :"'+filepath+'", "features":'+str(features)+', "target_feature":"'+target_feature+'"}'

	print(url_,	data)

	send_request = requests.post(url_, data)	

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')


	print('===================================================================')


	function = 'segmentation' 
	url_ = url+function 
	data = '{"filepath" :"'+filepath+'", "features":'+str(features)+', "target_feature":"'+target_feature+'","index":"'+index+'"}'
	
	print(url_,data)


	send_request = requests.post(url_, data)	

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')

	
	print('===================================================================')


	function = 'price_segmentation' 
	url_ = url+function 
	data = '{"price_per_segment" :"'+price_per_segment+'", "price_threshold":"'+price_threshold+'", "segment":"'+segment+'","target":"'+target+'"}'
	

	print(url_,data)


	send_request = requests.post(url_, data)	

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')


	print('===================================================================')


	function = 'price_segmentation' 
	url_ = url+function 
	data = '{"price_per_segment" :"'+price_per_segment+'", "price_threshold":"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold_with_power_index.json", "segment":"'+segment+'","target":"'+target+'","is_power_index":true}'
	

	print(url_,data)


	send_request = requests.post(url_, data)	

	if send_request.status_code == 200:

		print(send_request.json())
	else:
		print('There is an error occurs')
