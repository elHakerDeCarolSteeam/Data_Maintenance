#import pandas as pd
#
## Read the main Excel file
#main_excel_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Data_Maintenance\RAW_Sales_Nov_2023_POS.xlsx"
#df_main = pd.read_excel(main_excel_file)
#
## Read the reference Excel file
#reference_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Data_Maintenance\Ace_Toro_REFERENCE.xlsx"
#df_reference = pd.read_excel(reference_file)
#
## Perform VLOOKUP by merging the two DataFrames on the "Article" column and include Retailer_ID
#merged_df = pd.merge(df_main, df_reference[['Articale #', 'Category Name', 'Category Abb', 'Categories Salesforce', 'Sub Category', 'Sub Categories Abb', 'Sub Categories Salesforce', 'Fuel Type', 'Fuel Type Abb', 'Fuel Type Salesforce']], 
#                      how='left', left_on='Article', right_on='Articale #')
#
## Convert STORE_NUM to integers
#merged_df['STORE_NUM'] = merged_df['STORE_NUM'].fillna(0).astype(int)
#
### Add Retailer_ID column
#merged_df['Retailer_ID'] = 'ACE' + merged_df['STORE_NUM'].astype(str)
##
### Concatenate columns for UNIQUE EXTERNAL ID
##merged_df['UNIQUE EXTERNAL ID'] = merged_df['Retailer_ID'] + "_TORO_NOV_POS_2023_" + merged_df['Category Abb'] + merged_df['Sub Categories Abb'] + merged_df['Fuel Type Abb']
#
## Replace null values with empty strings
#merged_df['Category Abb'] = merged_df['Category Abb'].fillna('')
#merged_df['Sub Categories Abb'] = merged_df['Sub Categories Abb'].fillna('')
#merged_df['Fuel Type Abb'] = merged_df['Fuel Type Abb'].fillna('')
#
## Concatenate columns for UNIQUE EXTERNAL ID
#merged_df['UNIQUE EXTERNAL ID'] = merged_df['Retailer_ID'] + "_TORO_NOV_POS_2023_" + merged_df['Category Abb'] + merged_df['Sub Categories Abb'] + merged_df['Fuel Type Abb']
#
## Save the merged DataFrame to a new Excel file
#output_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Data_Maintenance\Sales_Nov_2023_ID_AND_VLOOKUP_FINAL.xlsx"
#merged_df.to_excel(output_file, index=False)
#
#print("VLOOKUP completed and merged DataFrame saved to", output_file)


import pandas as pd

# Read the main Excel file
main_excel_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Data_Maintenance\RAW_Sales_Nov_2023_POS.xlsx"
df_main = pd.read_excel(main_excel_file)

# Read the reference Excel files
reference_file1 = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Data_Maintenance\Ace_Toro_REFERENCE.xlsx"
df_reference1 = pd.read_excel(reference_file1)

reference_file2 = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Data_Maintenance\Ace_Account_Owner_REFERENCE.xlsx"
df_reference2 = pd.read_excel(reference_file2)

# Perform VLOOKUP to merge the first reference DataFrame based on 'Article'
merged_df = pd.merge(df_main, df_reference1[['Articale #', 'Category Name', 'Category Abb', 'Categories Salesforce', 'Sub Category', 'Sub Categories Abb', 'Sub Categories Salesforce', 'Fuel Type', 'Fuel Type Abb', 'Fuel Type Salesforce']], 
                      how='left', left_on='Article', right_on='Articale #')

# Convert STORE_NUM to integers
merged_df['STORE_NUM'] = merged_df['STORE_NUM'].fillna(0).astype(int)

# Add Retailer_ID column
merged_df['Retailer_ID'] = 'ACE' + merged_df['STORE_NUM'].astype(str)

# Replace null values with empty strings
merged_df['Category Abb'] = merged_df['Category Abb'].fillna('')
merged_df['Sub Categories Abb'] = merged_df['Sub Categories Abb'].fillna('')
merged_df['Fuel Type Abb'] = merged_df['Fuel Type Abb'].fillna('')

# Concatenate columns for UNIQUE EXTERNAL ID
merged_df['UNIQUE EXTERNAL ID'] = merged_df['Retailer_ID'] + "_TORO_NOV_POS_2023_" + merged_df['Category Abb'] + merged_df['Sub Categories Abb'] + merged_df['Fuel Type Abb']

# Perform VLOOKUP to merge the second reference DataFrame based on 'Retailer_ID' from the 'UNIQUE EXTERNAL ID (Account)'
merged_df = pd.merge(merged_df, df_reference2[['Unique_External_ID_(Account)', 'Account_Owner_ID']], 
                     how='left', left_on='Retailer_ID', right_on='Unique_External_ID_(Account)')

# Rename the 'Account_Owner_ID' column to 'Account Owner ID'
merged_df.rename(columns={'Account_Owner_ID': 'Account Owner ID'}, inplace=True)

# Save the merged DataFrame to a new Excel file
output_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Data_Maintenance\Sales_Nov_2023_ID_AND_VLOOKUP_FINALwith_ownerID.xlsx"
merged_df.to_excel(output_file, index=False)

print("VLOOKUP completed and merged DataFrame saved to", output_file)
