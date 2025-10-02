import json
import csv
import sys

def process_dependencies(input_filename, output_filename):
    # Load the JSON data
    with open(input_filename, 'r') as file:
        data = json.load(file)

    # Open CSV file for writing
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Navigate to the list of objects
        objects = data.get('list', {}).get('objects', [])

        for obj in objects:
            dependencies = obj.get('spec', {}).get('resolved_dependencies', {}).get('dependencies', [])
            for dep in dependencies:
                name_field = dep.get('name', '')
                if name_field.startswith('c://'):
                    name_field = name_field[len('c://'):]  # Remove 'c://'

                if '@' in name_field:
                    name, version = name_field.split('@', 1)
                    name = name.lower()
                    name = name.rstrip('/')  # Strip any trailing '/' characters
                    version = version.lower()
                    writer.writerow([name, version])

    print(f"Processed data written to '{output_filename}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_dependencies.py <input_json_file> <output_csv_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    process_dependencies(input_filename, output_filename)

