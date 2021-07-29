#!/bin/bash

# source /home/ubuntu/scripts/religion/env/bin/activate
# cd /home/ubuntu/scripts/religion
python main.py --filepath sample_input_file.csv --features Customer_Type Customer_Industry Grade Country Destination_Port City_State Shipping_Condition Export/Domestic QUANTITY --target Price_Premium --index Index --price_per_segment price_per_segment.json --price_threshold sample_threshold.json --price_threshold_power_index sample_threshold_with_power_index.json
