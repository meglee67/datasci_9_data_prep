# This code is copied and modified from https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/code/model_dev/scripts/p1_extract.py

import pandas as pd 

## get data 

# original link: https://catalog.data.gov/dataset/chemicals-in-cosmetics-8c29f
# data download link: 
datalink = 'https://data.chhs.ca.gov/dataset/596b5eed-31de-4fd8-a645-249f3f9b19c4/resource/57da6c9a-41a7-44b0-ab8d-815ff2cd5913/download/cscpopendata.csv'

df = pd.read_csv(datalink)
df.size
df.sample(5)

## save as csv to WK9/code/model_dev/data/raw
df.to_csv('../data/raw/cosmetic.csv', index=False)

## save as pickle to WK9/code/model_dev/data/raw
df.to_pickle('../data/raw/cosmetic.pkl',)

# instead of ('model_dev1/data/raw/cosmetic.csv', index=False) I had to replace the model_dev1 part with a ..
# ../ moves up one directory level from the scripts directory and then navigates to model_dev1/data/raw
# because to run the .py file, I needed to cd into /datasci_9_data_prep/model_dev1/scripts, but then I kept getting the message that the data/raw didn't exist even though when I kept doing ls -d */, I could see that the directory did exist 