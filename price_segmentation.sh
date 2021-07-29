#!/bin/bash

# source /home/ubuntu/scripts/religion/env/bin/activate
# cd /home/ubuntu/scripts/religion

# local
python main.py --filepath sample_input_file.csv --features Customer_Type Customer_Industry Grade Country Destination_Port City_State Shipping_Condition Export/Domestic QUANTITY --target Price_Premium --index Index --price_per_segment price_per_segment.json --price_threshold sample_threshold.json --price_threshold_power_index sample_threshold_with_power_index.json


# filepath = 'https://github.com/acceval/Price-Segmentation/blob/main/sample_input_file.csv'
# features = ['Customer_Type', 'Customer_Industry', 'Grade', 'Country', 'Destination_Port', 'City_State', 'Shipping_Condition', 'Export/Domestic', 'QUANTITY']
# target_feature = 'Price_Premium'
# index = 'Index'
# price_per_segment = 'https://github.com/acceval/Price-Segmentation/blob/main/price_per_segment.json'
# price_threshold = 'https://github.com/acceval/Price-Segmentation/blob/main/sample_threshold.json'
# price_threshold_power_index = 'https://github.com/acceval/Price-Segmentation/blob/main/sample_threshold_with_power_index.json'
#

# python main.py --filepath https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_input_file.csv --features Customer_Type Customer_Industry Grade Country Destination_Port City_State Shipping_Condition Export/Domestic QUANTITY --target Price_Premium --index Index --price_per_segment https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json --price_threshold https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json --price_threshold_power_index https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold_with_power_index.json
