"""
RECORD CHECK  -  my version
===========================

Name  :RITHSHIKA
Lane  :  AI & DATA SCIENCE
Date  :23/10/2026

"""

class Record:
    def __init__(self, label, value, limit):
        """Store the record details."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Check whether the record is OK, a warning, or over the limit."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read the file and create a list of records."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")

            record = Record(label, float(value), float(limit))
            records.append(record)

    return records


records = load_records("records.txt")

count = 0
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    status = record.status()
    difference = record.limit - record.value
    percent = (record.value / record.limit) * 100

    print(f"  Rows loaded   : {record.value:10.2f}")
    print(f"  Rows expected : {record.limit:10.2f}")
    print(f"  Remaining     : {difference:10.2f}")
    print(f"  Percent       : {percent:10.2f} %")
    print(f"  Status        : {status:>10}")

    if status == "OVER LIMIT":
        count += 1

    print("=" * 34)

print()
print(f"OVER LIMIT records: {count}")
""" Display the total number of records over the limit."""