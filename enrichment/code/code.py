import pandas as pd 

########################
### load in the data 
########################
patients = pd.read_csv('enrichment/example_data/patients.csv')
patients

medications = pd.read_csv('enrichment/example_data/medications.csv')
medications

patients.columns
medications.columns

patients['Id']
medications['PATIENT']


########################
### merge examples 
# add medications to patients
########################
patients_simple = patients[['Id', 'SSN']]
medications_simple = medications[['PATIENT', 'DESCRIPTION']]

patients_medications = patients_simple.merge(medications_simple, 
            how='left', 
            left_on='Id', right_on='PATIENT')




patients_small = patients[['Id', 'BIRTHDATE', 'DRIVERS', 'SSN']]
print(patients_small.head(5).to_markdown())

patients_medications = patients_medications.drop(columns=['PATIENT'])

########################
### concat examples 
########################

patient_sample_1 = patients.sample(n=10)
patient_sample_2 = patients.sample(n=10)

patients_s1_s2_concat = pd.concat([patient_sample_1, patient_sample_2])


#############
#### below we enrich our medications table with information from patients table ####

df_patients_small = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]
print(df_patients_small.sample(10).to_markdown())

df_medications_small = medications[['PATIENT', 'CODE', 'DESCRIPTION', 'BASE_COST']]
print(df_patients_small.sample(10).to_markdown())

combined_df = df_medications_small.merge(df_patients_small, how='left', left_on='PATIENT', right_on='Id')

combined_df.columns

combined_df.sample

combined_df.shape

combined_df.to_csv('/Users/kevinzhou/Documents/GitHub/HHA-507-2022-ZhouKevin/enrichment/example_data/combined_df.csv')



#### load in payers *****
 
payers_df = pd.read_csv('enrichment/example_data/payers.csv')

payers_df.shape

payers_df.head

payers_df['NAME']

payers_df.columns

payers_df_small = payers_df[['NAME', 'Id', 'AMOUNT_COVERED']]

patients_payers = df_patients_small.merge(payers_df_small, how='left', on='Id') ## they've both got the same column name

print(patients_payers.sample(10).to_markdown())


####

payers = pd.read_csv('enrichment/example_data/payers.csv')

med_df = medications[['PATIENT', 'PAYER']]

pay_df = payers[['Id', 'CITY']]
pay_df.rename(columns={'CITY': 'CITY_PAYER'}, inplace=True)

pat_df = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]

med_pay_df = med_df.merge(pay_df, how='left', left_on='PAYER', right_on='Id')

med_pay_df.columns

med_pay_df = med_pay_df.drop(columns=['Id'])


### for med_pay_df we will drop duplicate rows based on PATIENT

med_pay_df_nodups = med_pay_df.drop_duplicates(subset=['PATIENT'])

med_pay_df_nodups.shape

med_pay_df_nodups = med_pay_df_nodups.drop(columns=(['CODE']))

##final step, we add med_pay_df_nodups to our pat_df dataframe
final_df = pat_df.merge(med_pay_df_nodups, how='left', left_on='Id', right_on='PATIENT')

final_df