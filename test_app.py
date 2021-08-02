import os
import pytest
import json
import requests
import config
from config import var
from Model import Model 
from app import app

env = 'prod'

# default vars
filepath = 'sample_input_file.csv'
features = '["Customer_Type", "Customer_Industry", "Grade", "Country", "Destination_Port", "City_State", "Shipping_Condition", "Export/Domestic", "QUANTITY"]'
target_feature = 'Price_Premium'
index = 'Index'
segment = 'segment'
target = 'Price Premium'
price_per_segment = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json'
price_threshold = 'https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json'
price_threshold_power_index = 'sample_threshold_with_power_index.json'


model = Model(env)
# local url
url = config.LOCAL_URL
# url = config.HEROKU_URL


def test_features_assessment_app(app, client):
            
    function = 'features_assessment' 
    url_ = url+function 
    data = '{"filepath" :"'+filepath+'", "features":'+str(features)+', "target_feature":"'+target_feature+'"}'
    send_request = client.post(url_, data=data, follow_redirects=True)    

    assert send_request.status_code == 200


def test_segmentation_app(app, client):

    function = 'segmentation' 
    url_ = url+function 
    data = '{"filepath" :"'+filepath+'", "features":'+str(features)+', "target_feature":"'+target_feature+'","index":"'+index+'"}'
    send_request = client.post(url_, data=data, follow_redirects=True)    

    assert send_request.status_code == 200


def test_price_segmentation_app(app, client):

    function = 'price_segmentation' 
    url_ = url+function 
    data = '{"price_per_segment" :"'+price_per_segment+'", "price_threshold":"'+price_threshold+'", "segment":"'+segment+'","target":"'+target+'"}'
    send_request = client.post(url_, data=data, follow_redirects=True)    

    assert send_request.status_code == 200


def test_price_segmentation_with_power_index_app(app, client):

    function = 'price_segmentation' 
    url_ = url+function 
    data = '{"price_per_segment" :"'+price_per_segment+'", "price_threshold":"https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold_with_power_index.json", "segment":"'+segment+'","target":"'+target+'","is_power_index":true}'
    send_request = client.post(url_, data=data, follow_redirects=True)    

    assert send_request.status_code == 200
