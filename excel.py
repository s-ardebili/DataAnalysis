import pandas as pd
import os

# Where .xlsx files are located
folder_path = r'C:\Users\14042\Downloads\Queries'

# Save multiple sheets
with pd.ExcelWriter(r'C:\Users\14042\Downloads\combined_file.xlsx', engine='openpyxl') as writer:
    # Loop through all the .xlsx files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)

            # Read the Excel file into a dictionary of DataFrames (one per sheet)
            dfs = pd.read_excel(file_path, sheet_name=None)  # sheet_name=None reads all sheets

            # Loop through all sheets and write them to the new Excel file
            for sheet_name, df in dfs.items():
             
                df['Source_File'] = filename

                # Write each sheet to the output Excel file
                sheet_name = f"{filename}_{sheet_name}"[:31] 
                df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Files combined successfully!")
