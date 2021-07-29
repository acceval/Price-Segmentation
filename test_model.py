import os
import pytest
from Model import Model 
import json

filepath = 'sample_input_file.csv'
features = ['Customer_Type', 'Customer_Industry', 'Grade', 'Country', 'Destination_Port', 'City_State', 'Shipping_Condition', 'Export/Domestic', 'QUANTITY']
target_feature = 'Price_Premium'
index = 'Index'
price_per_segment = 'price_per_segment.json'
price_threshold = 'sample_threshold.json'
price_threshold_power_index = 'sample_threshold_with_power_index.json'

model = Model()

# happy path

def test_features_assement():

    output = model.features_assement(filepath, features , target_feature)
    assert isinstance(output, str)

    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==1
    assert output_json['error'] is None
    

def test_segmentation():

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
    
    

def test_price_segmentation():

    target = 'Price Premium'
    output = model.price_segmentation(price_per_segment, price_threshold, segment='segment', target=target, is_power_index=False)
    
    output_json = json.loads(output)
    assert isinstance(output_json, dict)

    assert output_json['status']==1
    assert output_json['error'] is None

    # output should has at least 1 data and the type should be a list    
    assert len(output_json['data'])>0
    assert isinstance(output_json['data'], list)

    
    with open(price_threshold) as f:
        price_threshold_json = json.load(f)


    assert isinstance(price_threshold_json, dict)
    assert len(price_threshold_json)==len(output_json['data'][0][target])

    assert len(price_threshold_json.keys()) == len(output_json['data'][0][target])
    assert set(list(price_threshold_json.keys())) == set([k for item in output_json['data'][0][target] for k,v in item.items()]) 


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

    
    with open(price_threshold) as f:
        price_threshold_json = json.load(f)


    assert isinstance(price_threshold_json, dict)
    assert len(price_threshold_json)==len(output_json['data'][0][target])

    assert len(price_threshold_json.keys()) == len(output_json['data'][0][target])
    assert set(list(price_threshold_json.keys())) == set([k for item in output_json['data'][0][target] for k,v in item.items()]) 

