import os
import pytest
from Model import Model 
import json
import requests
from config import var

env = 'prod'

# default vars
filepath = var[env]['filepath']
features = var[env]['features']
target_feature = var[env]['target_feature']
index = var[env]['index']
price_per_segment = var[env]['price_per_segment']
global_threshold = var[env]['global_threshold']
customised_threshold = var[env]['customised_threshold']
price_power_index_threshold = var[env]['price_power_index_threshold']
bad_price_per_segment = var[env]['bad_price_per_segment']


model = Model(env)


def test_features_assessment():

    # happy path

    output = model.features_assessment(filepath, features , target_feature)
    assert isinstance(output, str)

    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==1
    assert output_json['error'] is None
    

    # sad path

    #if the filepath is a random file
    bad_filepath = 'random.txt'
    output = model.features_assessment(bad_filepath, features , target_feature)
    assert isinstance(output, str)

    #if the filepath is a csv file but does not exist
    bad_filepath = 'random.csv'
    output = model.features_assessment(bad_filepath, features , target_feature)
    assert isinstance(output, str)

    # break the features
    bad_features = ['Customer_Type', 'Customer_Industry', 'Grade', 'Country', 'Destination_Port', 'City_State', 'Shipping_Condition', 'Export/Domestic', 'qty']
    output = model.features_assessment(filepath, bad_features , target_feature)
    assert isinstance(output, str)

    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==0
    assert output_json['error'] is not None
    

    # if the features is string instead of string
    bad_features = 'Customer_Type'
    output = model.features_assessment(filepath, bad_features , target_feature)
    assert isinstance(output, str)

    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==0
    assert output_json['error'] is not None

    # if the target is not string
    bad_target_features = ['Customer_Type']
    output = model.features_assessment(filepath, features , bad_target_features)    
    assert isinstance(output, str)

    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==0
    assert output_json['error'] is not None


def test_segmentation():

    # happy path

    output = model.segmentation(filepath, features, target_feature, index)
    
    assert isinstance(output, str)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==1
    assert output_json['error'] is None
    
    # output should has at least 1 data and the type should be a list    
    assert len(output_json['data'])>0
    assert isinstance(output_json['data'], list)

    assert isinstance(output_json['data'][0], dict)
    assert len(output_json['data'][0][index])>=1

    # sad path

    # break filepath
    bad_filepath = 'random.file'
    output = model.segmentation(bad_filepath, features, target_feature, index)
    assert isinstance(output, str)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==0
    assert output_json['error'] is not None
    
    # if features is a string
    bad_features = 'features'
    output = model.segmentation(filepath, bad_features, target_feature, index)
    assert isinstance(output, str)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==0
    assert output_json['error'] is not None
    
    # if features is a random features
    bad_features = ['features']
    output = model.segmentation(filepath, bad_features, target_feature, index)
    assert isinstance(output, str)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==0
    assert output_json['error'] is not None

    # if index is a random value
    bad_index = 'features'
    output = model.segmentation(filepath, features, target_feature, bad_index)
    assert isinstance(output, str)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==0
    assert output_json['error'] is not None
    

def test_price_segmentation():

    # # happy path

    target = 'Price Premium'

    #global setting    
    # output = model.price_segmentation(price_per_segment, global_threshold, segment='segment', target=target)
    
    # output_json = json.loads(output)
    # print(output_json)

    # assert isinstance(output_json, dict)
    # assert output_json['status']==1
    # assert output_json['error'] is None

    # # output should has at least 1 data and the type should be a list    
    # assert len(output_json['data'])>0
    # assert isinstance(output_json['data'], list)

    # try:
    
    #     if env == 'local':

    #         with open(global_threshold) as f:
    #             price_threshold_json = json.load(f)

    #     elif env == 'prod':

    #         resp = requests.get(global_threshold)
    #         price_threshold_json = json.loads(resp.text)   
    
    # except Exception as e:

    #     print(e)        

    # assert isinstance(price_threshold_json, dict)
    # # print(len(price_threshold_json))
    # # print(output_json['data'][0][target])

    # # print(len(price_threshold_json))
    # # print(len(output_json['data'][0][target]))
    # assert len(price_threshold_json)==len(output_json['data'][0][target])

    # # print(set(list(price_threshold_json.keys())))
    # # print(set([k for item in output_json['data'][0][target] for k,v in item.items()]))
    # assert set(list(price_threshold_json.keys())) == set([k for item in output_json['data'][0][target] for k,v in item.items()]) 

    #customized setting
    target = 'Price Premium'
    output = model.price_segmentation(price_per_segment, customised_threshold, segment='segment', target=target)
    
    output_json = json.loads(output)
    # print(output_json)

    assert isinstance(output_json, dict)
    assert output_json['status']==1
    assert output_json['error'] is None

    # output should has at least 1 data and the type should be a list    
    assert len(output_json['data'])>0
    assert isinstance(output_json['data'], list)

    try:
    
        if env == 'local':

            with open(customised_threshold) as f:
                price_threshold_json = json.load(f)

        elif env == 'prod':

            resp = requests.get(customised_threshold)
            price_threshold_json = json.loads(resp.text)   
    
    except Exception as e:

        print(e)        

    # print(type(price_threshold_json))
    # print(price_threshold_json)
    # print(output_json)

    assert isinstance(price_threshold_json, list)

    # print(len(output_json['data']))
    # print(len(price_threshold_json))
    assert len(output_json['data'])==len(price_threshold_json)

    for x,y in zip(output_json['data'],price_threshold_json):

        assert x!=y

    # print(price_threshold_json)    

    # print(len(price_threshold_json))
    # print(output_json['data'])

    # print(output_json)

    # print(price_threshold_json)
    # print(len(output_json['data'][0]['threshold']))
    assert len(price_threshold_json)==len(output_json['data'])

    #price_power_index setting
    target = 'Price Premium'
    output = model.price_segmentation(price_per_segment, price_power_index_threshold, segment='segment', target=target)
    
    output_json = json.loads(output)
    # print(output_json)

    assert isinstance(output_json, dict)
    assert output_json['status']==1
    assert output_json['error'] is None

    # output should has at least 1 data and the type should be a list    
    assert len(output_json['data'])>0
    assert isinstance(output_json['data'], list)

    try:
    
        if env == 'local':

            with open(price_power_index_threshold) as f:
                price_threshold_json = json.load(f)

        elif env == 'prod':

            resp = requests.get(price_power_index_threshold)
            price_threshold_json = json.loads(resp.text)   
    
    except Exception as e:

        print(e)        

    # print(type(price_threshold_json))
    # print(price_threshold_json)
    # print(output_json)

    assert isinstance(price_threshold_json, list)

    # print(len(output_json['data']))
    # print(len(price_threshold_json))
    assert len(output_json['data'])==len(price_threshold_json)

    for x,y in zip(output_json['data'],price_threshold_json):

        assert x!=y

    # print(price_threshold_json)    

    # print(len(price_threshold_json))
    # print(output_json['data'])

    # print(output_json)

    # print(price_threshold_json)
    # print(len(output_json['data'][0]['threshold']))
    assert len(price_threshold_json)==len(output_json['data'])

    # sad path
    # break the price_per_segment, file does not exist
    random_json = 'random.json'
    output = model.price_segmentation(random_json, global_threshold, segment='segment', target=target)

    output_json = json.loads(output)
    # print(output_json)

    assert isinstance(output_json, dict)
    assert output_json['status']==0
    assert output_json['error'] is not None


    # break the price_per_segment, JSON file does not follow the rules --> key does not exist
    output = model.price_segmentation(bad_price_per_segment, global_threshold, segment='segment', target=target)
    output_json = json.loads(output)
    # print(output_json)
    
    assert isinstance(output_json, dict)
    assert output_json['status']==0
    assert output_json['error'] is not None

    
    # break the price_per_segment, JSON file does not follow the rules --> target does not exist
    output = model.price_segmentation(price_per_segment, global_threshold, segment='segment', target='target')
    output_json = json.loads(output)
    # print(output_json)
    
    assert isinstance(output_json, dict)
    assert output_json['status']==0
    assert output_json['error'] is not None
    

    # new scenario
    # {"price_per_segment" :"price_per_segment.json", "price_threshold":"sample_threshold.json", "segment":"segment","target":"Price Premium"}
    output = model.price_segmentation('price_per_segment', 'sample_threshold.json', segment='segment', target='Price_Premium')
    output_json = json.loads(output)

    assert isinstance(output_json, dict)
    assert output_json['status']==0
    assert output_json['error'] is not None
    


