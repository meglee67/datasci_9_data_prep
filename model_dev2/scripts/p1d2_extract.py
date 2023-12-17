# This code is copied and modified from https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/code/model_dev/scripts/p1_extract.py

import pandas as pd 

## get data 

# original link: https://catalog.data.gov/dataset/nypd-shooting-incident-data-historic
# data download link: 
datalink = 'https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(datalink)
df.size
df.sample(5)

## save as csv to WK9/code/model_dev/data/raw
df.to_csv('../data/raw/shootings.csv', index=False)

## save as pickle to WK9/code/model_dev/data/raw
df.to_pickle('../data/raw/shootings.pkl',)

# instead of ('model_dev2/data/raw/cosmetic.csv', index=False) I had to replace the model_dev2 part with a ..
# ../ moves up one directory level from the scripts directory and then navigates to model_dev2/data/raw
# because to run the .py file, I needed to cd into /datasci_9_data_prep/model_dev2/scripts, but then I kept getting the message that the data/raw didn't exist even though when I kept doing ls -d */, I could see that the directory did exist 