import os,sys,inspect,getopt,io
from pathlib import Path
import argparse

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from log import Log
import config, utils

import pandas as pd
import numpy as np
import json
import string

from Model import Model 


if __name__== '__main__':

	start = utils.get_time()
	print(start)
	
	today = None

	# # --global_threshold global_threshold.json --customised_threshold customised_threshold.json --price_power_index price_power_index.json

	# parser = argparse.ArgumentParser()	
	# parser.add_argument("--env", "-e", help="State the environment", required=True)	
	# parser.add_argument("--filepath", "-p", help="Path to the csv file", required=True)	
	# parser.add_argument("--features", "-f", nargs="*", help="Specify all the features name. Use space as a separator. Feature name should not contain space.", required=True)	
	# parser.add_argument("--target_feature", "-t", help="Target feature, should not contain space", required=True)	
	# parser.add_argument("--index", "-i", help="Set the index", required=True)	
	# parser.add_argument("--price_per_segment", "-pp", help="JSON file with prices per segment", required=True)	
	# parser.add_argument("--global_threshold", "-gt", help="Global tresholds setting for Floor, Target and Offer", required=True)	
	# parser.add_argument("--customised_threshold", "-ct", help="Customised tresholds setting for Floor, Target and Offer", required=True)	
	# parser.add_argument("--price_power_index", "-ppi", help="Power Price Index setting for Floor, Target and Offer", required=True)	
	# args = parser.parse_args()

	# env = None
	# if args.env is None:
	# 	print("State the environment!!")
	# else:
	# 	env = args.env
	
	# filepath = None
	# if args.filepath is None:
	# 	print("State the filepath!!")
	# else:
	# 	filepath = args.filepath

	# features = None
	# if args.features is None:
	# 	print("State the features!!")
	# else:
	# 	features = args.features


	# target_feature = None
	# if args.target_feature is None:
	# 	print("State the target feature!!")
	# else:
	# 	target_feature = args.target_feature 

	# index = None
	# if args.index is None:
	# 	print("State the index!!")
	# else:
	# 	index = args.index 

	# price_per_segment = None
	# if args.price_per_segment is None:
	# 	print("State the price per segment!!")
	# else:
	# 	price_per_segment = args.price_per_segment 

	# global_threshold = None
	# if args.global_threshold is None:
	# 	print("State the global threshold!!")
	# else:
	# 	global_threshold = args.global_threshold 

	# customised_threshold = None
	# if args.customised_threshold is None:
	# 	print("State the customised threshold!!")
	# else:
	# 	customised_threshold = args.customised_threshold 

	# price_power_index = None
	# if args.price_power_index is None:
	# 	print("State the price power index threshold!!")
	# else:
	# 	price_power_index = args.price_power_index 


	# print('env:',env)
	# print('filepath:',filepath)
	# print('features:',features)
	# print('target_feature:',target_feature)
	# print('index:',index)
	# print('price_per_segment:',price_per_segment)
	# print('global_threshold:',global_threshold)
	# print('customised_threshold:',customised_threshold)
	# print('price_power_index:',price_power_index)

	# print('-------------------------------------------')
	env = 'prod'
	filepath = 'sample_input_file.csv'
	features = '["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"]'
	target_feature = 'Price_Premium'
	index = 'Index'
	segment = 'segment'
	target = 'Price Premium'
	price_per_segment = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json'
	# price_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json'
	price_threshold_power_index = 'sample_threshold_with_power_index.json'
	global_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/global_threshold.json'
	customised_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/customised_threshold_final.json'
	price_power_index_threshold	 = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_power_index_final.json'
	price_power_index ='price_power_index.json'

	log = Log()		

	msg = __name__+'.'+utils.get_function_caller()
	log.print_(msg)

	
	if filepath is not None and features is not None and target_feature is not None:

		model = Model(env)
		
		output = model.features_assessment(filepath, features , target_feature)
		print(type(output))
		print(output)
		
		output = model.segmentation(filepath, features, target_feature, index)
		print(type(output))
		print(output)
		
		output = model.price_segmentation(price_per_segment, global_threshold, segment='segment', target='Price Premium')
		print(type(output))
		print(output)

		print('===================================')

		output = model.price_segmentation(price_per_segment, customised_threshold, segment='segment', target='Price Premium')
		print(type(output))
		print(output)

		print('===================================')

		output = model.price_segmentation(price_per_segment, price_power_index, segment='segment', target='Price Premium')
		print(type(output))
		print(output)



		# output = model.price_segmentation(price_per_segment, price_threshold, segment='segment', target='Price Premium', is_power_index=False)
		# print(type(output))
		# print(output)

		# output = model.price_segmentation(price_per_segment, price_threshold_power_index, segment='segment', target='Price Premium', is_power_index=True)
		# print(type(output))
		# print(output)
	
		


	else:
		
		print('Error !!')



	print('-------------------------------------------')

	end = utils.get_time()
	print(end)

	print(end - start)


	msg = 'start:',start
	log.print_(msg)

	msg = 'end:',end
	log.print_(msg)

	msg = 'total:',end-start
	log.print_(msg)	
	