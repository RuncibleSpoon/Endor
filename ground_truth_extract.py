import json
import csv
import sys

def extract_library_versions(input_filename, output_filename):
    # Load the JSON data
    with open(input_filename, 'r') as file:
        data = json.load(file)

    # Extract the list of libraries
    libraries = data.get('libs', [])

    # Write to CSV
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Library', 'Actual_version'])  # CSV header

        for lib in libraries:
            library_name = lib.get('Library', '')
          
            # Remove leading "https://" if present to match results file.
            if library_name.startswith("https://"):
                library_name = library_name[len("https://"):]
                print(f"leading protocol has been removed from  '{library_name}' ")
            
            # Remove leading "http://" if present to match results file.
            # I'm sure there is a neater way to do this without using two if statements
            # Fell free to fix that someone! 

            if library_name.startswith("http://"):
                library_name = library_name[len("http://"):]
                print(f"leading protocol has been removed from  '{library_name}' ")
     
            # lowecase the name  

            library_name = library_name.lower()
            library_name  = library_name.rstrip('/')  # Strip any trailing '/' characters

            actual_version = lib.get('Actual_version', '')
    
            if library_name and actual_version:
                writer.writerow([library_name, actual_version])

    print(f"CSV file '{output_filename}' has been created.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_library_versions.py <input_json_file> <output_csv_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    extract_library_versions(input_filename, output_filename)

