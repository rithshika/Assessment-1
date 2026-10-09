"""
RECORD CHECK - my version

Name  : Rithshika
Lane  : AI / Data Science
Date  : 09/10/2026
"""

 #FUNCTIONS

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Rows loaded : {value:10.2f}")
    print(f"  Rows expected: {limit:10.2f}")
    print(f"  Remaining   : {difference:10.2f}")
    print(f"  Percent     : {percent:10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


#INPUT
count = 0

while True:
    label = input("Enter dataset name (or quit): ")

    if label == "quit":
        break

    value = float(input("Enter rows loaded: "))
    limit = float(input("Enter rows expected: "))
# PROCESS

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        count += 1

print()
print("Number of OVER LIMIT records:", count)

