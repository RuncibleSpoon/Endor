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
    print(f"True Positives: {len(true_positives)}")
    print(f"False Negatives: {len(false_negatives)}")
    print(f"False Positives: {len(false_positives)}\n")

    print(f"{'True Positive':<20}{'False Negative':<20}{'False Positive'}")
    max_length = max(len(true_positives), len(false_negatives), len(false_positives))

    tp_list = list(true_positives)
    fn_list = list(false_negatives)
    fp_list = list(false_positives)

    for i in range(max_length):
        tp = f"{tp_list[i][0]}\t{tp_list[i][1]}" if i < len(tp_list) else ''
        fn = f"{fn_list[i][0]}\t{fn_list[i][1]}" if i < len(fn_list) else ''
        fp = f"{fp_list[i][0]}\t{fp_list[i][1]}" if i < len(fp_list) else ''
        print(f"{tp:<20}{fn:<20}{fp}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_csv.py <truth_file.csv> <results_file.csv>")
        sys.exit(1)

    truth_file = sys.argv[1]
    results_file = sys.argv[2]
    compare_csv_files(truth_file, results_file)

