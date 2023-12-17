# this code is copied and modified from https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/code/model_dev/scripts/p2_transform.py

import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## Loading raw data (pickle)
df = pd.read_pickle('../data/raw/cosmetic.pkl')

## Getting column names
print(df.columns)

## do some data cleaning of column names, 
## make them all lower case, remove white spaces and replace with _ 
# df.columns = df.columns.str.lower().str.replace(' ', '_')
# print(df.columns)
# didn't do this part because the way the column names were shown (no spaces, words next to eachother capitalized)

## get data types
df.dtypes 
print(df.dtypes)
# only datatype was object

# Converting column datatypes
columns_to_convert_dates = ['InitialDateReported', 'MostRecentDateReported', 'DiscontinuedDate', 'ChemicalCreatedAt', 'ChemicalUpdatedAt']  

for col in columns_to_convert_dates:
    if df[col].dtype == 'object':
        df[col] = pd.to_datetime(df[col])

columns_to_convert_numbers = ['CDPHId', 'CompanyId', 'PrimaryCategoryId', 'SubCategoryId', 'CasId', 'ChemicalId', 'ChemicalCount']  

for col in columns_to_convert_numbers:
    if df[col].dtype == 'object':
        df[col] = df[col].astype('int64')

## Check data types after conversion
print(df.dtypes)
# now we have a combo of int64, object, datetime64 and some that got turned into float64

# dropping columns
to_drop = [
    'CDPHId',
    'ProductName',
    'CSFId',
    'CSF',
    'CasNumber',
    'DiscontinuedDate',
    'ChemicalCreatedAt',
    'ChemicalUpdatedAt',
    'ChemicalDateRemoved',
]
df.drop(to_drop, axis=1, inplace=True, errors='ignore')

# keep columns 
to_keep = [
    'CompanyId',
    'BrandName',
    'PrimaryCategoryId',
    'PrimaryCategory',
    'SubCategoryId',
    'SubCategory',
    'CasId',
    'ChemicalId',
    'ChemicalName',
    'InitialDateReported',
    'MostRecentDateReported',

]

# updating the dataframe to only the keep columns 
df = df[to_keep]
print(df)

## perform ordinal encoding on MostRecentDateReported
enc = OrdinalEncoder()
enc.fit(df[['MostRecentDateReported']])
df['MostRecentDateReported'] = enc.transform(df[['MostRecentDateReported']])

## create dataframe with mapping
df_mapping_date = pd.DataFrame(enc.categories_[0], columns=['MostRecentDateReported'])
df_mapping_date['MostRecentDateReported_ordinal'] = df_mapping_date.index
df_mapping_date

## save mapping to csv
df_mapping_date.to_csv('../data/processed/mapping_MostRecentDateReported.csv', index=False)

len(df)

#### save a temporary csv file of 1000 rows to test the model
df.head(10000).to_csv('../data/processed/cosmetic.csv', index=False)