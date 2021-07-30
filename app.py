from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import json

from Model import Model 


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('list', type=list)


model = Model('prod')

@app.route('/')
def hello():
	
	return jsonify('Welcome to Price Segmentation')



@app.route('/features_assessment', methods=['POST'])
def features_assessment():

	ABC = parser.parse_args()
	data_decoded = request.data.decode("utf-8") 

	#convert to json
	data_json = json.loads(data_decoded)


	if 'filepath' in data_json:
		filepath = data_json['filepath']
	else:
		filepath = ''

	if 'features' in  data_json:
		features = data_json['features']
	else:
		features = ''
	
	if 'target_feature' in  data_json:
		target_feature = data_json['target_feature']
	else:
		target_feature = ''

	if filepath!='' and features!='' and target_feature!='':

		output = model.features_assessment(filepath, features , target_feature)
		return jsonify(output)

	else:

		status = 0 
		error = 'There is a problem on the parameters'
		data = None

		output = dict()
		output["status"] = status
		output["error"] = error
		output["data"] = output_json

		output = json.dumps(output)


	return jsonify(output)



@app.route('/segmentation', methods=['POST'])
def segmentation():

	# print('segmentation:', flush=True)

	ABC = parser.parse_args()
	data_decoded = request.data.decode("utf-8") 
	
	#convert to json
	data_json = json.loads(data_decoded)


	if 'filepath' in data_json:
		filepath = data_json['filepath']
	else:
		filepath = ''

	if 'features' in  data_json:
		features = data_json['features']
	else:
		features = ''
	
	if 'target_feature' in  data_json:
		target_feature = data_json['target_feature']
	else:
		target_feature = ''

	if 'index' in  data_json:
		index = data_json['index']
	else:
		index = ''


	if filepath!='' and features!='' and target_feature!='' and index!='':

		output = model.segmentation(filepath, features, target_feature, index)   
		return jsonify(output)

	else:

		status = 0 
		error = 'There is a problem on the parameters'
		data = None

		output = dict()
		output["status"] = status
		output["error"] = error
		output["data"] = output_json

		output = json.dumps(output)


	return jsonify(output)


@app.route('/price_segmentation', methods=['POST'])
def price_segmentation():

	# print('price_segmentation:', flush=True)

	ABC = parser.parse_args()
	data_decoded = request.data.decode("utf-8") 
	
	# #convert to json
	data_json = json.loads(data_decoded)

	if 'price_per_segment' in data_json:
		price_per_segment = data_json['price_per_segment']
	else:
		price_per_segment = ''

	if 'price_threshold' in data_json:
		price_threshold = data_json['price_threshold']
	else:
		price_threshold = ''

	if 'segment' in data_json:
		segment = data_json['segment']
	else:
		segment = ''

	if 'target' in data_json:
		target = data_json['target']
	else:
		target = ''

	if 'is_power_index' in data_json:
		is_power_index = data_json['is_power_index']
	else:
		is_power_index = False

	if price_per_segment!='' and price_threshold!='' and segment!='' and target!='' and is_power_index is not None:		

		output = model.price_segmentation(price_per_segment, price_threshold, segment, target, is_power_index)

	else:

		status = 0 
		error = 'There is a problem on the parameters'
		data = None

		output = dict()
		output["status"] = status
		output["error"] = error
		output["data"] = output_json

		output = json.dumps(output)

	return jsonify(output)


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5050))
	# app.run(host='0.0.0.0', port = port, debug=True)

	# local
	app.run(host='127.0.0.1', port = port, debug=True)
	