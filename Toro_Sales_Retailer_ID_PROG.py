import pandas as pd

# Read the Excel file
excel_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\RAW_Sales_Nov_2023_POS.xlsx"
df = pd.read_excel(excel_file)

# Replace non-integer values with -1
df['STORE_NUM'] = pd.to_numeric(df['STORE_NUM'], errors='coerce').fillna(-1).astype(int)

# Create a new column "Retailer_ID" by concatenating "ACE" and the values in the "STORE_NUM" column
df['Retailer_ID'] = 'ACE' + df['STORE_NUM'].astype(str)

# Save the modified dataframe to a new Excel file
output_file = r"C:\Users\BryanChacha\OneDrive - Saleslink\Attachments\Desktop\Toro Power Program\November 2023\Sales_Nov_2023_POS_with_Retailer_ID_OUTPUT.xlsx"
df.to_excel(output_file, index=False)

print("Retailer_ID column has been created and saved to", output_file)
