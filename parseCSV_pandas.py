import pandas as pd

# Define the headers to be removed
headers_to_remove = ["Admin1 Code", "Admin2 Code", "Admin3 Code", "Admin4 Code", "Modification date", "Feature Class","Feature Code"]

# Input and output file names
input_file = 'geonames-all-cities-with-a-population-1000.csv'
output_file = 'geonames-all-cities-with-a-population-1000_test.csv'

def process_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file, delimiter=';')

    # Remove the specified headers
    df.drop(columns=headers_to_remove, inplace=True)
    
    # Remove rows where Population is not a number, 0, empty, or below 1000
    df['Population'] = pd.to_numeric(df['Population'], errors='coerce')
    df = df[df['Population'].notna() & (df['Population'] >= 1000)]
    
    # Remove rows where 'Country name EN' is empty
    df = df[df['Country name EN'].notna() & (df['Country name EN'].str.strip() != '')]

    # Write the result to a new CSV file
    df.to_csv(output_file, sep=';', index=False)

if __name__ == "__main__":
    process_csv(input_file, output_file)
