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

	parser = argparse.ArgumentParser()	
	parser.add_argument("--filepath", "-p", help="Path to the csv file", required=True)	
	parser.add_argument("--features", "-f", nargs="*", help="Specify all the features name. Use space as a separator. Feature name should not contain space.", required=True)	
	parser.add_argument("--target_feature", "-t", help="Target feature, should not contain space", required=True)	
	parser.add_argument("--index", "-i", help="Set the index", required=True)	
	parser.add_argument("--price_per_segment", "-pp", help="JSON file with prices per segment", required=True)	
	parser.add_argument("--price_threshold", "-pt", help="Tresholds for Floor, Target and Offer", required=True)	
	parser.add_argument("--price_threshold_power_index", "-pi", help="Tresholds for Floor, Target and Offer with Power Index", required=True)	
	args = parser.parse_args()
	

	filepath = None
	if args.filepath is None:
		print("State the filepath!!")
	else:
		filepath = args.filepath

	features = None
	if args.features is None:
		print("State the features!!")
	else:
		features = args.features


	target_feature = None
	if args.target_feature is None:
		print("State the target feature!!")
	else:
		target_feature = args.target_feature 

	index = None
	if args.index is None:
		print("State the index!!")
	else:
		index = args.index 

	price_per_segment = None
	if args.price_per_segment is None:
		print("State the price per segment!!")
	else:
		price_per_segment = args.price_per_segment 

	price_threshold = None
	if args.price_threshold is None:
		print("State the price threshold!!")
	else:
		price_threshold = args.price_threshold 

	price_threshold_power_index = None
	if args.price_threshold_power_index is None:
		print("State the price threshold power index!!")
	else:
		price_threshold_power_index = args.price_threshold_power_index 


	print('filepath:',filepath)
	print('features:',features)
	print('target_feature:',target_feature)
	print('index:',index)
	print('price_per_segment:',price_per_segment)
	print('price_threshold:',price_threshold)
	print('price_threshold_power_index:',price_threshold_power_index)

	print('-------------------------------------------')
	
	log = Log()		

	msg = __name__+'.'+utils.get_function_caller()
	log.print_(msg)

	
	if filepath is not None and features is not None and target_feature is not None:

		model = Model()
		
		output = model.features_assement(filepath, features , target_feature)
		print(output)
		
		output = model.segmentation(filepath, features, target_feature, index)
		print(output)
		
		output = model.price_segmentation(price_per_segment, price_threshold, segment='segment', target='Price Premium', is_power_index=False)
		print(output)

		output = model.price_segmentation(price_per_segment, price_threshold_power_index, segment='segment', target='Price Premium', is_power_index=True)
		print(output)
	
		


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
	