"""
RECORD CHECK  -  my version
===========================

Name  : Rithshika Nallagorla
Lane  :  AI
Date  : 02-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================
count = 0

label = input("Enter the dataset name:")
while label != "quit":
    rows_loaded  = float(input("Enter the rows loaded:"))
    rows_expected = float(input("Enter the rows expected:"))

    
    difference = rows_expected - rows_loaded
    percent = (rows_loaded/rows_expected)*100

    if percent >= 100:
        status = "OVER LIMIT"
        count = count + 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f" Loaded      : {rows_loaded:10.2f}")
    print(f" Expected    : {rows_expected:10.2f}")
    print(f" Difference  : {difference:10.2f}")
    print(f" Percent     : {percent:10.2f} %")
    print(f" Status      : {status:>12}")
    print("=" * 34)

    label = input("Enter the dataset name (or quit): ")

print("OVER LIMIT records:", count)
