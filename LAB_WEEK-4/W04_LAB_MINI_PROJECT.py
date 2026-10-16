"""
RECORD CHECK - my version

Name  : Rithshika
Lane  : AI & Data Science
Date  : 16/10/2026
"""




def check_record(value, limit):
    """Calculate difference, percentage and status."""
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the record report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Rows loaded   : {value:10.2f}")
    print(f"  Rows expected : {limit:10.2f}")
    print(f"  Remaining     : {difference:10.2f}")
    print(f"  Percent       : {percent:10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Load records from a data file."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            records.append(record)

    return records




records = []

try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("Error: records.txt was not found.")
    records = []




count = 0

with open("results.txt", "w") as output_file:

    for record in records:

        difference, percent, status = check_record(
            record["value"],
            record["limit"]
        )

        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        output_file.write(
            f'{record["label"]},{status}\n'
        )

        if status == "OVER LIMIT":
            count += 1


print()
print("Number of OVER LIMIT records:",count)