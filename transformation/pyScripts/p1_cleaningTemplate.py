import pandas as pd ## focus for the assignment tonight
import datetime as dt ##built in python time library
import uuid as uu ## unique identifiers for rows
import numpy as np ## for missing values


# load in messy data 
df = pd.read_csv('transformation/dataFiles/raw/113243405_StonyBrookUniversityHospital_standardcharges.csv') ##relative path

df

# get a count of the number of rows and columns
df.shape

countRows, countColumns = df.shape ## defining rows and columns of df.shape as variables

tenPercent = int(countRows * 0.1)

sample_df = df.sample(tenPercent)

sample_df

##preview get random sample of 25 rows 
df.sample(25)

## clean the data
# list columns
list(df)

############## COLUMN NAMES ##############
############## COLUMN NAMES ##############
############## COLUMN NAMES ##############

df.columns
column_names = list(df)

## potential problems of default names: capitalization, dashes and special characters, white space
## needs standardization


# remove all special characters and whitespace ' ' from column names
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 
list(df)

# renaming columns
df.columns = df.rename(columns={'code':'codes'}) # rename the column, where the first value is the old name and the second value is the new name

# change all column names to lowercase
df.columns = df.columns.str.lower()

# change all column names to upper case
df.columns = df.columns.str.upper()

# replace all whitespace in column names with an underscore
df.columns = df.columns.str.replace(' ', '_')

# dropping columns
df.drop(['codes'], axis=1, inplace=True) # remember this is CASE SENSITIVE


############## REMOVING WHITESPACE ##############
############## REMOVING WHITESPACE ##############
############## REMOVING WHITESPACE ##############

# remove all whitespace for values within a specific column
df['gross_charge'] = df['gross_charge'].str.strip()
# remove all special characters and whitespace ' ' from a specific column
df['x'] = df['x'].str.replace('[^A-Za-z0-9]+', '_') ## regex # regex tutorial/info: https://www.w3schools.com/python/python_regex.asp;  https://www.regular-expressions.info/refquick.html





############## COLUMN TYPES ##############
############## COLUMN TYPES ##############
############## COLUMN TYPES ##############


# get list of column types 
## want to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans
df.dtypes

# create a list of columns that are strings, and save as strings 
strings = df.select_dtypes(include=['object']).columns
# create a list of columns that are numbers, and save as numbers
numbers = df.select_dtypes(include=['int64', 'float64']).columns
# create a list of columns that are dates, and save as dates
dates = df.select_dtypes(include=['datetime64[ns]']).columns
# create a list of columns that are booleans, and save as booleans
booleans = df.select_dtypes(include=['bool']).columns
# create a list of columns that are objects, and save as objects
objects = df.select_dtypes(include=['object']).columns

## you would then manually go through each of these, and determine if the column 
## type is appropriate for the data model you are creating

df['hospcode'] = df['hospcode'].astype(str)

df.dtypes

########## DATES ##########
########## DATES ##########
########## DATES ##########

# dealing with dates 
# convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])
# convert date column to datetime format like this: '%Y-%m-%d'
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
# convert date column to datetime format like this: '%Y_%M_%D'
df['date'] = pd.to_datetime(df['date'], format='%Y_%M_%D')
# convert date to quarter format
df['date'] = df['date'].dt.quarter
# convert date to year format
df['date'] = df['date'].dt.year
# determine if date is on weekday or weekend
df['date'] = df['date'].dt.dayofweek



########## MISSING DATA ##########
########## MISSING DATA ##########
########## MISSING DATA ##########

# get a count of missing values in each column
df.isnull().sum()

# replacing blank, empty cells with NaN
df.replace(to_replace='', value=np.nan, inplace=True)
df.replace(to_replace=' ', value=np.nan, inplace=True)

# drop rows with missing values
df.dropna(inplace=True) # drop rows with missing values

# droping specific rows 
df.drop([0,1,2,3,4,5,6,7,8,9], axis=0, inplace=True) # example of dropping rows



########## UNIQUE IDs ##########
########## UNIQUE IDs ##########
########## UNIQUE IDs ##########

### Creating UNIQUE IDs 

# Example 1
## create a unique id for each row using uuid
df['id'] = df.apply(lambda row: uuid.uuid4(), axis=1)

## create a unique id for each row using uuid with 8 characters
df['id'] = df.apply(lambda row: uuid.uuid4().hex[8], axis=1)


# Example 2
## create a function that will create a unique id for each row
def create_id():
    return uuid.uuid4()

## create a new column that will have a unique id for each row
df['id'] = df.apply(lambda row: create_id(), axis=1)