# this code is copied and modified from https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/code/model_dev/scripts/p2_transform.py

import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## Loading raw data (pickle)
df = pd.read_csv('../data/raw/shootings.csv')

## Getting column names
print(df.columns)

## do some data cleaning of column names, 
## make them all lower case, remove white spaces and replace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')
print(df.columns)


## get data types
df.dtypes 
print(df.dtypes)
# good combo of int64, objects, float64 and bool

# dropping columns
to_drop = [
    'loc_of_occur_desc',
    'loc_classfctn_desc',
    'location_desc',
    'perp_age_group',
    'perp_sex',
    'perp_race',
    'lon_lat',
]
df.drop(to_drop, axis=1, inplace=True, errors='ignore')

# keep columns 
to_keep = [
    'incident_key',
    'occur_date',
    'occur_time',
    'boro',
    'precinct',
    'jurisdiction_code',
    'statistical_murder_flag',
    'vic_age_group',
    'vic_sex',
    'vic_race',
    'x_coord_cd',
    'y_coord_cd',
    'latitude',
    'longitude',
]

# updating the dataframe to only the keep columns 
df = df[to_keep]
print(df)

## perform ordinal encoding on vic_age_group:
enc = OrdinalEncoder()
enc.fit(df[['vic_age_group']])
df['vic_age_group'] = enc.transform(df[['vic_age_group']])

## create dataframe with mapping
df_mapping_date = pd.DataFrame(enc.categories_[0], columns=['vic_age_group:'])
df_mapping_date['vic_age_group_ordinal'] = df_mapping_date.index
df_mapping_date

## save mapping to csv
df_mapping_date.to_csv('../data/processed/mapping_vic_age_group.csv', index=False)

len(df)

#### save a temporary csv file of 1000 rows to test the model
df.head(10000).to_csv('../data/processed/shootings.csv', index=False)