# datasci_9_data_prep
* Due Nov 10
* HHA 507 HW 8
* Assignment details below

<br>

## Dataset Selection
* The 1st dataset was taken from data.gov, [Chemicals in Cosmetics](https://catalog.data.gov/dataset/chemicals-in-cosmetics-8c29f)
  * This dataset reflects information that has been reported to the California Safe Cosmetics Program (CSCP) in the California Department of Public Health (CDPH).
  * This dataset will be used for regression tasks
  * For example, predicting something like the frequency of reporting incidents over time (using 'InitialDateReported' and 'MostRecentDateReported') or predicting the count of reported incidents based on certain company or product characteristics.


* The 2nd dataset was taken from data.gov, [NYPD Shooting Incident Data - Historic](https://catalog.data.gov/dataset/nypd-shooting-incident-data-historic)
  * This dataset reflects shooting data from incidents in NYC.
  * This dataset will be used for classification tasks
  * For example, predicting the number of shooting incidents per month or per year in different boroughs (or precincts) based on historical data.

## Data Cleaning and Transformation Plan

### Extraction
* Initially I copied the p1_extract.py script from the [Week 9 p1_extract.py](https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/code/model_dev/scripts/p1_extract.py), but after modification found that it kept giving me the error that it wasn't able to save my files because the directory was non-existent.
* I had also run into the problem that the .py file didn't exist but to fix that I just cd into the scripts directory under the model_dev folder
* To run the .py file, I needed to cd into /datasci_9_data_prep/model_dev1/scripts, but then I kept getting the message that the data/raw didn't exist even though when I kept doing ls -d */, I could see that the directory did exist 
* Instead of ('model_dev1/data/raw/cosmetic.csv', index=False) I had to replace the model_dev1 part with a ..
* ../ moves up one directory level from the scripts directory and then navigates to model_dev1/data/raw

### Transformation
* First I needed to ``pip install sklearn``
* Copied the code from [Week 9 p2_transform.py](https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/code/model_dev/scripts/p2_transform.py#L71)
* Had to change some datatypes and I droppped some columns from the cosmetic dataset, then saved the mapping and processed dataset in the model_dev1/data/processed folder


## Dataset Splitting
* I copied the [Week 9 p3_compute.py](https://github.com/hantswilliams/HHA_507_2023/blob/86d8439cd2409c649a4d9404e5d9488971e194c2/WK9/code/model_dev/scripts/p3_compute.py)
* Not many modifications made for the splitting, but I did run into several errors with my datatypes
* Standardscaler in p3_compute.py couldn't handle non-numerical data/categorical variables, so I had to perform label encoding for both datasets
* And in both datasets, some dates that I had turned into datetime datatypes ended up needing to be ordinally encoded for standardscaler to be able to handle them


<br>

## **Week 9: Data Preparation for Machine Learning**

### **Objective**: 
Focus on selecting datasets suitable for a machine learning experiment, with an emphasis on data cleaning, encoding, and transformation steps necessary to prepare the data.

### **Instructions**:

#### **1. Dataset Selection:**
- Choose two datasets from healthdata.gov or data.gov that you wish to prepare for a machine learning experiment.
- The datasets can be related to any health or public domain topic but should be suitable for either classification or regression tasks.

#### **2. Data Cleaning and Transformation Plan:**
- Document your plan for data cleaning and transformation in a markdown file. Include the following:
  - A brief description of each dataset.
  - The intended machine learning task for each dataset (classification or regression).
  - The steps needed to clean and transform the data. Consider aspects like missing values, outliers, encoding categorical variables, standardizing or normalizing, etc.
  - Identify the independent (predictors) and dependent (target) variables in each dataset.

#### **3. Data Cleaning Execution (Optional Challenge):**
- If you wish to challenge yourself, perform the actual data cleaning and transformation steps in Python. 
- Use Pandas, NumPy, or other relevant libraries for data manipulation.

#### **4. Dataset Splitting:**
- Create a separate script to split each dataset into three parts:
  - Training data (`train_x`, `train_y`)
  - Validation data (`val_x`, `val_y`)
  - Testing data (`test_x`, `test_y`)
- Follow the standard practices of dataset splitting as discussed in class.

#### **5. Documentation:**
- Document each step of your process. Include screenshots of any errors encountered and how you resolved them.
- Explain your decisions during the data cleaning and transformation process.

#### **6. Submission**:
- Create a new GitHub repository named `datasci_9_data_prep` in your GitHub account.
- Organize your GitHub repository with the following:
  - A "datasets" folder containing the datasets you chose.
  - The markdown file with your data preparation plan.
  - Python scripts used for data cleaning and dataset splitting.
  - Submit the link to your GitHub repository.

---

**Tip**: Proper data preparation is crucial in machine learning. It can significantly impact the performance of your models. Pay attention to the details of each dataset and the specific requirements of the machine learning tasks you plan to perform.

---
