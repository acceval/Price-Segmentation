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
import importlib
import importlib.util
from import_file import import_file
import requests

from sklearn.feature_selection import f_regression
from sklearn.tree import DecisionTreeRegressor, _tree, export_text
from sklearn.preprocessing import LabelEncoder

class Model:

	def __init__(self, env='local'):
		

		self.log = Log()		

		self.env = env
		
		# tree
		self.max_depth = config.MAX_DEPTH
		self.min_samples_leaf = config.MIN_SAMPLES_LEAF
		self.ccp_alpha = config.CCP_ALPHA
		self.random_state = config.RANDOM_STATE


	def status_check(self,filepath:string,features:list, target, index=None):

		msg = self.__class__.__name__+'.'+utils.get_function_caller()
		self.log.print_(msg)
		print(msg)

		status = 0
		result = None
		error = None

		# check if the file is csv file
		try:

			ext = filepath.split('.')[-1]			

			if ext.lower()=='csv':

				msg = 'File is a csv file'
				self.log.print_(msg)
				print(msg)

				status = 1

			else:

				msg = 'File is not a csv file'
				self.log.print_(msg)
				print(msg)

				error = msg

				return status, error

		except Exception as e:

			msg = 'Error when checking the file extension'
			self.log.print_(msg)
			print(msg)


		if status:

			# check if the all features in the file
			try:

				try:

					data = pd.read_csv(filepath)
					
				except Exception as e:

					msg = 'Cannot read the input file'
					self.log.print_(msg)
					print(msg)

					error = msg

					return status, error

				all_features = data.columns

				# # dataframe size should be >1
				if data.shape[0]:

					msg = 'Dataframe shape:',data.shape
					self.log.print_(msg)
					print(msg)

				else:

					msg = 'DataFrame has no data'
					self.log.print_(msg)
					print(msg)

					status = 0
					error = msg

					return status, error


				# check if index exists and unique
				if index is not None:

					if index in all_features:

						msg = 'Index exists'
						self.log.print_(msg)
						print(msg)

					else: 
						
						msg = 'Index does not exist'
						self.log.print_(msg)
						print(msg)

						status = 0
						error = msg

						return status, error

					if not data[index].is_unique:

						msg = 'Index does not have unique values'
						self.log.print_(msg)
						print(msg)

						status = 0
						error = msg

						return status, error
					

				# check if target exists and type is float
				# print(target)
				# print(all_features)
				if target in all_features:

					msg = 'Target feature exists'
					self.log.print_(msg)
					print(msg)

				else:

					msg = 'Target feature does not exist'
					self.log.print_(msg)
					print(msg)

					status = 0
					error = msg

					return status, error
				
				if 'float' in str(data[target].dtype):

					msg = 'Target feature type is acceptable'
					self.log.print_(msg)
					print(msg)

				else:

					msg = 'Target feature type is not acceptable'
					self.log.print_(msg)
					print(msg)

					status = 0
					error = msg

					return status, error
					
				# check if features sub of all_features
				if not set(features).issubset(set(all_features)):

					msg = 'All or some of the features do not exists'
					self.log.print_(msg)
					print(msg)

					status = 0
					error = msg

					return status, error
				
				status = 1

				return status, error
				

			except Exception as e:

				msg = 'Error when checking the features, target feature and index'
				self.log.print_(msg)
				print(msg)

				status = 0

		return status		


	def feature_engineering(self,dataframe,features,target):

		msg = self.__class__.__name__+'.'+utils.get_function_caller()
		self.log.print_(msg)
		print(msg)

		categorical_features = []
		numerical_features = []

		for col,type_ in zip(dataframe[features].columns,dataframe[features].dtypes):
			
			if str(type_)=='object' and col!=target:        
				categorical_features.append(col)        
			else:
				numerical_features.append(col)

		# handle empty values
		for categorical_feature in categorical_features:

			dataframe[categorical_feature].fillna('No data', inplace=True)

		for numerical_feature in numerical_features:

			dataframe[numerical_feature].fillna(dataframe[numerical_feature].median(), inplace=True)


		# feature engineering
		for categorical_feature in categorical_features:

			dataframe[categorical_feature] = dataframe.groupby(categorical_feature)[target].transform('max')

		return dataframe
			

	def features_assement(self,filepath:string,features:list,target:string):

		msg = self.__class__.__name__+'.'+utils.get_function_caller()
		self.log.print_(msg)
		print(msg)

		# print('target:',target)

		return_ = dict()		

		if isinstance(filepath, str) and isinstance(features, list) and isinstance(target, str):

			target = target.strip()

			status, error = self.status_check(filepath,features,target)

			if status :

				try:

					data = pd.read_csv(filepath)

					# status, target = self.check_target(target)

					if status:

						# handle outliers
						data = data[
									(
										(data[target]>=(data[target].mean() - (3*data[target].std())))
										& (data[target]<=(data[target].mean() + (3*data[target].std())))
									)
									]

						# do the feature assement

						data = self.feature_engineering(data,features,target)

						if len(features)==1:

							freg = f_regression(np.array(data[features].values.reshape(-1, 1),dtype=float), np.array(data[target].values.ravel(),dtype=float))

						else:

							freg = f_regression(np.array(data[features].values,dtype=float), np.array(data[target].values.ravel(),dtype=float))

						p_values = freg[1]

						feature_pval = dict()

						for p_value, feature in zip(p_values,features):
				
							feature_pval[feature] = round(p_value, 3)    

						
						result = json.dumps(feature_pval)

					else:

						msg = 'Error on target feature'
						self.log.print_(msg)
						print(msg)

						status = 0	
						result = None



				except:

					msg = 'Error when doing features_assessment'
					self.log.print_(msg)
					print(msg)

					status = 0	
					result = None



		else:

			msg = 'Parameters type are wrong'
			self.log.print_(msg)
			print(msg)

			status = 0	
			error = msg
			result = None


		return_["status"] = status
		return_["error"] = error

		if status==1:

			return_["data"] = result

		else:

			return_["data"] = None			

		return_json = json.dumps(return_)

		return return_json

	def export_py_code(self, tree, feature_names, max_depth=100, spacing=4):

		if spacing < 2:
			raise ValueError('spacing must be > 1')

		# Clean up feature names (for correctness)
		nums = string.digits
		alnums = string.ascii_letters + nums
		clean = lambda s: ''.join(c if c in alnums else '_' for c in s)
		features = [clean(x) for x in feature_names]
		features = ['_'+x if x[0] in nums else x for x in features if x]
		if len(set(features)) != len(feature_names):
			raise ValueError('invalid feature names')

		# First: export tree to text
		res = export_text(tree, feature_names=features, 
						max_depth=max_depth,
						decimals=6,
						spacing=spacing-1)

		# Second: generate Python code from the text
		skip, dash = ' '*spacing, '-'*(spacing-1)
		code = 'def decision_tree({}):\n'.format(', '.join(features))
		for line in repr(tree).split('\n'):
			code += skip + "# " + line + '\n'
		for line in res.split('\n'):
			line = line.rstrip().replace('|',' ')
			if '<' in line or '>' in line:
				line, val = line.rsplit(maxsplit=1)
				line = line.replace(' ' + dash, 'if')
				line = '{} {:g}:'.format(line, float(val))
			else:
				line = line.replace(' {} class:'.format(dash), 'return')
			code += skip + line + '\n'

		return code.replace('- value:','return').replace('-','')

	def get_func_args(self,f):

		if hasattr(f, 'args'):
			return f.args
		else:
			return list(inspect.signature(f).parameters)


	def segmentation(self,filepath:string,features:list,target:string, index:string, max_depth=None, min_samples_leaf=None, ccp_alpha=None):

		msg = self.__class__.__name__+'.'+utils.get_function_caller()
		self.log.print_(msg)
		print(msg)
		
		# tree
		if max_depth is not None:
			self.max_depth = max_depth

		if min_samples_leaf is not None:
			self.min_samples_leaf = min_samples_leaf

		if ccp_alpha is not None:
			self.ccp_alpha = CCP_ALPHA


		return_ = dict()

		if isinstance(filepath, str) and isinstance(features, list) and isinstance(target, str) or isinstance(filepath, str) and isinstance(features, list) and isinstance(target, str) and isinstance(index, str):

			target = target.strip()

			if index is not None:
				index = index.strip()

			status, error = self.status_check(filepath,features,target,index)		

			if status:

				try:				

					data = pd.read_csv(filepath)
					
					# handle outliers		
					data = data[
								(
									(data[target]>=(data[target].mean() - (3*data[target].std())))
									& (data[target]<=(data[target].mean() + (3*data[target].std())))
								)
								]

					data = self.feature_engineering(data,features,target)

					clf = DecisionTreeRegressor(max_depth=self.max_depth, min_samples_leaf=self.min_samples_leaf, random_state=self.random_state, ccp_alpha=self.ccp_alpha)
					clf.fit(data[features],data[target])		

					# get the tree rules
					res = self.export_py_code(clf, feature_names=features, max_depth=self.max_depth, spacing=4)					

					# save the function as a file
					filename = '_'+utils.get_unique_filename('tree')+'.py'
					
					with open(filename, 'w') as f:
						f.write(res)

					module = import_file(filename)					
					
					# rename column names
					for a,b in zip(features,self.get_func_args(module.decision_tree)): 
						data.rename(columns={a:b},inplace=True)


					data['node'] = data[self.get_func_args(module.decision_tree)].apply(lambda x: module.decision_tree(*x), axis=1)
					data['node'] = data['node'].apply(lambda x:str(x).replace('[','').replace(']',''))
					
					# remove the file
					os.remove(filename)

					# encode the segment
					le = LabelEncoder()
					data['segment'] = le.fit_transform(data['node'])


					output_df = data[[index]+['segment']]
					output_df = output_df.groupby(['segment'])[index].apply(list).reset_index() 
					

					# convert dataframe to json
					# output_json = output_df.to_json(orient ='records')
					outputs = []

					for i, rows in enumerate(output_df.itertuples(),1):

						_str = '{"segment":'+str(rows[1])+', "'+index+'":'+str(rows[2])+'}'
						outputs.append(_str)

					final_output = '['+', '.join(outputs)+']'
					final_output = final_output.replace("'",'"')					
					output_json = json.loads(final_output)



				except Exception as e:

					msg = 'Error on modeling'
					self.log.print_(msg)
					print(msg)

					print(e)

				
			else:

				msg = 'There is problem on the file path, features, target feature, or index'
				self.log.print_(msg)
				print(msg)

		else:

			msg = 'Parameters type are wrong'
			self.log.print_(msg)
			print(msg)

			status = 0	
			error = msg
			result = None


		
		return_["status"] = status
		return_["error"] = error

		if status==1:

			return_["data"] = output_json

		else:

			return_["data"] = None			

		return_ = json.dumps(return_)

		# # save this json for testing purpose
		# with open('sample_json.json', 'w') as f:
		# 	f.write(return_)

		return return_


	def get_threshold(self,price_threshold,is_power_index,segment_field,segment=None):

		msg = self.__class__.__name__+'.'+utils.get_function_caller()
		self.log.print_(msg)
		print(msg)

		try :

			if (is_power_index==True and isinstance(price_threshold, list)):

				threshold = [threshold for threshold in price_threshold if threshold[segment_field]==segment]

				if len(threshold)==1:
					
					threshold = threshold[0]['threshold'][0]
					return threshold

				else:
					raise Exception('There is an error in the JSON threshold file')



			elif (is_power_index==False and isinstance(price_threshold, dict)):

				return price_threshold



		except Exception as e:

			msg = 'There is an error in the JSON threshold file'
			self.log.print_(msg)
			print(msg)

			status = 0	
			error = msg
			result = None							

	def read_json(self,json_file):

		msg = self.__class__.__name__+'.'+utils.get_function_caller()
		self.log.print_(msg)
		print(msg)

		if isinstance(json_file, str):

			try:

				if self.env == 'local':

					with open(json_file) as f:
						json_output = json.load(f)


				elif self.env == 'prod':

					resp = requests.get(json_file)
					json_output = json.loads(resp.text)   

			except Exception as e:

				msg = 'There is an error when reading JSON file'
				self.log.print_(msg)
				print(msg)

			finally:
				
				return json_output





	def price_segmentation(self, price_per_segment, price_threshold, segment, target, is_power_index=False):

		msg = self.__class__.__name__+'.'+utils.get_function_caller()
		self.log.print_(msg)
		print(msg)

		return_ = dict()

		status = 0
		error = None

		if isinstance(price_per_segment, str) and isinstance(price_threshold, str) and isinstance(is_power_index, bool):
			
			try:

				price_per_segment = price_per_segment.strip()
				price_threshold = price_threshold.strip()
				
				# read json 				
				try:

					price_per_segment_json = self.read_json(price_per_segment)
					price_threshold_json = self.read_json(price_threshold)
				
				except Exception as e:

					msg = 'Error on JSON file'
					self.log.print_(msg)
					print(msg)

					print(e)

					status = 0 
					error = msg

				else:

					if (is_power_index==False and isinstance(price_threshold_json, dict)) or (is_power_index==True and isinstance(price_threshold_json, list)):

						price_per_segment_df = pd.DataFrame(price_per_segment_json)

						# check if segment and target exists
						if segment in price_per_segment_df.columns:

							if target in price_per_segment_df.columns:


								output = list()
								for i,segment_ in enumerate(price_per_segment_df[segment].unique()):

									line = list()    
									line.append('"'+segment+'":'+str(segment_))
									  
									sub = price_per_segment_df[price_per_segment_df[segment]==segment_]

									prices = sub[target].values[0]
													

									if is_power_index:
										threshold = self.get_threshold(price_threshold_json,is_power_index,segment_field=segment, segment=segment_)
									else:
										threshold = self.get_threshold(price_threshold_json,is_power_index,segment_field=segment)



									_str = []
									for k,v in threshold.items():
										
										tmp = '{"'+str(k)+'":'+str(np.percentile(prices, v*10))+'}'        
										_str.append(tmp)
										
									
									_str = '"'+target+'":['+','.join(_str)+']'
									

									line.append(_str)
									line = ','.join(line)
									line = "{"+line+"}"
									
									
									output.append(line)					    
									
								output = '['+','.join(output)+']'

								result = json.loads(output)

								status = 1



							else:

								msg = 'Target does not exist'
								self.log.print_(msg)
								print(msg)

								status = 0	
								error = msg
								result = None
						else:

							msg = 'There is an error in the JSON threshold file'
							self.log.print_(msg)
							print(msg)

							status = 0	
							error = msg
							result = None

					else:

						msg = 'Segment does not exist'
						self.log.print_(msg)
						print(msg)

						status = 0	
						error = msg
						result = None

					
			except Exception as e:

				msg = 'Error when do price segmentation!!'
				self.log.print_(msg)
				print(msg)

				print(e)


			




		else:

			msg = 'Parameters type are wrong'
			self.log.print_(msg)
			print(msg)

			status = 0	
			error = msg
			result = None


		return_["status"] = status
		return_["error"] = error

		if status==1:

			return_["data"] = result

		else:

			return_["data"] = None			

		return_ = json.dumps(return_)

		return return_
