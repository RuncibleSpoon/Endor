import csv
import sys

def read_csv_as_set(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return set(tuple(row) for row in reader)

def compare_csv_files(truth_file, results_file):
    truth_set = read_csv_as_set(truth_file)
    results_set = read_csv_as_set(results_file)

    true_positives = truth_set & results_set
    false_negatives = truth_set - results_set
    false_positives = results_set - truth_set

    print(f"Summary:")
    print("---------")
    print()
    print(f"True Positives: {len(true_positives)}")
    print(f"False Negatives: {len(false_negatives)}")
    print(f"False Positives: {len(false_positives)}\n")

    print("True Positives:")
    print("----------------")
    print()
    for item in sorted(true_positives):
        print(f"{item[0]} {item[1]}")
    print()

    print("False Negatives:")
    print("----------------")
    print()
    for item in sorted(false_negatives):
        print(f"{item[0]} {item[1]}")
    print()

    print("False Positives:")
    print("----------------")
    print()
    for item in sorted(false_positives):
        print(f"{item[0]} {item[1]}")
    print()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_csv.py <truth_file.csv> <results_file.csv>")
        sys.exit(1)

    truth_file = sys.argv[1]
    results_file = sys.argv[2]
    compare_csv_files(truth_file, results_file)

