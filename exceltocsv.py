import pandas as pd

def excel_to_csv(input_excel_file, output_csv_file):
    try:
        df = pd.read_excel(input_excel_file)

        df.to_csv(output_csv_file, index=False)

        print(f"Conversion successful. Excel file '{input_excel_file}' converted to CSV file '{output_csv_file}'.")
    except Exception as e:
        print(f"Error: {e}")

excel_to_csv('TaskFile.xlsx', 'output_csv_file.csv') 
