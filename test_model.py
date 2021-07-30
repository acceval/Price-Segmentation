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
price_threshold = var[env]['price_threshold']
price_threshold_power_index = var[env]['price_threshold_power_index']
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

    # happy path

    target = 'Price Premium'
    output = model.price_segmentation(price_per_segment, price_threshold, segment='segment', target=target, is_power_index=False)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==1
    assert output_json['error'] is None

    # output should has at least 1 data and the type should be a list    
    assert len(output_json['data'])>0
    assert isinstance(output_json['data'], list)

    try:
    
        if env == 'local':

            with open(price_threshold) as f:
                price_threshold_json = json.load(f)

        elif env == 'prod':

            resp = requests.get(price_threshold)
            price_threshold_json = json.loads(resp.text)   
    
    except Exception as e:

        print(e)        


    assert isinstance(price_threshold_json, dict)
    assert len(price_threshold_json)==len(output_json['data'][0][target])

    assert len(price_threshold_json.keys()) == len(output_json['data'][0][target])
    assert set(list(price_threshold_json.keys())) == set([k for item in output_json['data'][0][target] for k,v in item.items()]) 

    # sad path
    # break the price_per_segment, file does not exist
    random_json = 'random.json'
    output = model.price_segmentation(random_json, price_threshold, segment='segment', target=target, is_power_index=False)
    
    # break the price_per_segment, JSON file does not follow the rules --> key does not exist
    output = model.price_segmentation(bad_price_per_segment, price_threshold, segment='segment', target=target, is_power_index=False)
    
    # break the price_per_segment, JSON file does not follow the rules --> target does not exist
    output = model.price_segmentation(price_per_segment, price_threshold, segment='segment', target='target', is_power_index=False)
    
    # new scenario
    # {"price_per_segment" :"price_per_segment.json", "price_threshold":"sample_threshold.json", "segment":"segment","target":"Price Premium"}
    output = model.price_segmentation('price_per_segment', 'sample_threshold.json', segment='segment', target='Price_Premium', is_power_index=False)
    output_json = json.loads(output)

    print(output_json)


def test_price_segmentation_with_power_index():

    target = 'Price Premium'
    output = model.price_segmentation(price_per_segment, price_threshold_power_index, segment='segment', target=target, is_power_index=True)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==1
    assert output_json['error'] is None

    # output should has at least 1 data and the type should be a list    
    assert len(output_json['data'])>0
    assert isinstance(output_json['data'], list)

    
    if env == 'local':

        with open(price_threshold) as f:
            price_threshold_json = json.load(f)

    elif env == 'prod':

        resp = requests.get(price_threshold)
        price_threshold_json = json.loads(resp.text)   
        

    assert isinstance(price_threshold_json, dict)
    assert len(price_threshold_json)==len(output_json['data'][0][target])

    assert len(price_threshold_json.keys()) == len(output_json['data'][0][target])
    assert set(list(price_threshold_json.keys())) == set([k for item in output_json['data'][0][target] for k,v in item.items()]) 

    # pass number to is_power_index

    print('pass number to is_power_index:')
    output = model.price_segmentation(price_per_segment, price_threshold_power_index, segment='segment', target=target, is_power_index=1)
    output_json = json.loads(output)
    assert output_json['status']==0    
    

    # sad path
    # break the price_per_segment, file does not exist
    random_json = 'random.json'
    output = model.price_segmentation(random_json, price_threshold, segment='segment', target=target, is_power_index=True)
    
    # break the price_per_segment, JSON file does not follow the rules --> key does not exist
    output = model.price_segmentation(bad_price_per_segment, price_threshold, segment='segment', target=target, is_power_index=True)
    
    # break the price_per_segment, JSON file does not follow the rules --> target does not exist
    output = model.price_segmentation(price_per_segment, price_threshold, segment='segment', target='target', is_power_index=True)
    
