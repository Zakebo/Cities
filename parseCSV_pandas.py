import pandas as pd

# Define the headers to be removed
headers_to_remove = ["Geoname ID", "Admin1 Code", "Admin2 Code", "Admin3 Code", "Admin4 Code", "Modification date"]

# Input and output file names
input_file = 'geonames-all-cities-with-a-population-1000.csv'
output_file = 'geonames-all-cities-with-a-population-1000_OUTPUT2.csv'

def process_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file, delimiter=';')

    # Remove the specified headers
    df.drop(columns=headers_to_remove, inplace=True)
    
    # Remove rows where Population is 0 or empty
    df = df[df['Population'].notna() & (df['Population'] != 0)]

    # Write the result to a new CSV file
    df.to_csv(output_file, sep=';', index=False)

if __name__ == "__main__":
    process_csv(input_file, output_file)
