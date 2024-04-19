import pandas as pd

# Read the main Excel file
main_excel_file = r"RAW SALES DATA PATH/FILE NAME.xlsx"
df_main = pd.read_excel(main_excel_file)

# Read the reference Excel files
reference_file1 = r"REFERENCE DATA FILE PATH/FILE NAME.xlsx"
df_reference1 = pd.read_excel(reference_file1)

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
merged_df['UNIQUE EXTERNAL ID'] = merged_df['Retailer_ID'] + "_MANUFACTURER_NOVEMBER_POS_2023_" + merged_df['Category Abb'] + merged_df['Sub Categories Abb'] + merged_df['Fuel Type Abb']

# Move 'UNIQUE EXTERNAL ID' column to the first position (column A)
unique_external_id_column = merged_df.pop('UNIQUE EXTERNAL ID')
merged_df.insert(0, 'UNIQUE EXTERNAL ID', unique_external_id_column)

# Add Manufacturer ID column and set the value
merged_df['Manufacturer ID'] = '0013Z00001dTu6UQAS'

# Add Manufacturer ID column and set the value
merged_df['Month'] = 'November'

# Save the merged DataFrame to a new Excel file
output_file = r"OUTPUT DIRECTORY/output_file_name.xlsx"
merged_df.to_excel(output_file, index=False)

print("VLOOKUP completed and merged DataFrame saved to", output_file)