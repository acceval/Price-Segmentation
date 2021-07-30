[![Price Segmentation](https://github.com/acceval/Price-Segmentation/actions/workflows/main.yml/badge.svg)](https://github.com/acceval/Price-Segmentation/actions/workflows/main.yml)

# Price-Segmentation

[Link to the presentation](https://docs.google.com/presentation/d/1cbuh-HAZkFPrj3fEssscG-oDuvXqo1a0rcQUDQjdgjo/edit?usp=sharing)

Price Segmentation is a price given to different segment. The key idea in this concept is the </b>segmentation</b>.

In this exercise, we segment the customers (companies) and transaction. Since the dataset is specific for 1 product family, we do not segment the product. We also the minimum segment mumbers to 3. So the final product, we should at least have 9 segmentation (3 segments from customers x 3 segments from transaction). 

![Concept](https://github.com/acceval/Price-Segmentation/blob/main/images/Price%20Segmentation.png)

## Customer Segementation

![Customer Segmentation](https://github.com/acceval/Price-Segmentation/blob/main/images/Customer%20Segmentation_.png)

![Customer Segmentation Featues](https://github.com/acceval/Price-Segmentation/blob/main/images/Customer%20Segmentation%20Radar_.png)

## Transaction Segementation

![Transaction Segmentation](https://github.com/acceval/Price-Segmentation/blob/main/images/Transaction%20Segmentation_.png)

![Transaction Segmentation Featues](https://github.com/acceval/Price-Segmentation/blob/main/images/Transaction%20Segmentation%20Radar_.png)

## Price Segmentation 


![Premium Price Price Segmentation](https://github.com/acceval/Price-Segmentation/blob/main/images/Price%20Segmentation_.png)

![Premium Price Price Segmentation Kde](https://github.com/acceval/Price-Segmentation/blob/main/images/Price%20Segmentation%20Kde_.png)

## Note

- For deployment, please refer to Price Segmentation V.4 - Deployment.ipynb. We use slightly different approach for the segmentation.
 

# Deployment

## Feature Assesment

This is the section where all the features that users pick assessed

Input:

1. filepath: Path to csv file contains all the data
Sample of the input file is [here](https://github.com/acceval/Price-Segmentation/blob/main/sample_input_file.csv). Please note that column names cannot contain space.

2. features: List of features
List of column name that users want to use to segment the data. Each feature should exist as a column name and cannot contain space. Currently, features cannot be date data.

3. target: Target feature
Feature that aim to be used as reference for segmentation. In this sample data, the target feature is "Price Premium".

How to call the API:

To be added later

Output:

To be added later

## Segmentation

This is the section where all the data segmentated

Input:

1. filepath: Path to csv file contains all the data
Sample of the input file is [here](https://github.com/acceval/Price-Segmentation/blob/main/sample_input_file.csv). Please note that column names cannot contain space.

2. features: List of features
List of column name that users want to use to segment the data. Each feature should exist as a column name and cannot contain space. Currently, features cannot be date data.

3. target: Target feature
Feature that aim to be used as reference for segmentation. In this sample data, the target feature is "Price Premium".

4. index: Index column 
Index acts like acts like a primary key in a database table. Values in this column should be unique.  

5. max_depth: not mandatory, default value is 3  
This is the parameter on how far the segmentation goes.

6. min_samples_leaf: not mandatory, default value is 100.  
This is the parameter that ensure minimum number of sample per segment.

7. ccp_alpha: not mandatory, default value is 100.  
This is the parameter that ensure minimum number of sample per segment.

How to call the API:

To be added later

Output:

To be added later

## Price Segmentation

This is the section where the data is calculated and then divided into several cutoffs.

Input:

1. price_per_segment: JSON file
Sample of the input file is [here](https://raw.githubusercontent.com/acceval/Price-Segmentation/main/price_per_segment.json). 

2. price_threshold: JSON file
Sample of the input file is [here](https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold.json) for standard/global setting and [here](https://raw.githubusercontent.com/acceval/Price-Segmentation/main/sample_threshold_with_power_index.json) for setting per each segment. 

3. segment: Key name for the segment
Specify the key name for the segment from price_per_segment file.

4. target: Key name for the target
Specify the target from price_per_segment file.

5. is_power_index: Specify whether each segment has its own threshold. True if it does, and False if it does not.  
The parameter that specify if the price_threshold is a global config or if it config per segment. 

How to call the API:

To be added later

Output:

To be added later







