import json
import csv
import sys

def extract_dependencies(input_filename, output_filename):
    # Load the JSON data
    with open(input_filename, 'r') as file:
        data = json.load(file)

    # Write to CSV
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Dependency Name', 'Dependency Version'])  # CSV header

        # Extract and write each dependency's name and version
        for finding in data.get('all_findings', []):
            spec = finding.get('spec', {})
            name = spec.get('target_dependency_name', '')
            version = spec.get('target_dependency_version', '')
            print(f"Dependancy Name is '{name}'") 
            # Remove leading "https://" if present to match ground truth file.
            if name.startswith("https://"):
                name = name[len("https://"):]
                print(f"leading protocol has been removed from  '{name}' ")

            if name and version:
                writer.writerow([name, version])

    print(f"CSV file '{output_filename}' has been created.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_dependencies.py <input_json_file> <output_csv_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    extract_dependencies(input_filename, output_filename)

