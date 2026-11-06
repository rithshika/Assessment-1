"""
RECORD CHECK  -  my version
===========================

Name  : RITHSHIKA
Lane  : AI & DATA SCIENCE
Date  :6/11/26

"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("survey_data.csv")

df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

# checks percent and assigns status based on the value using a lambda function and the apply method.
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else "WARNING" if x >= 90 else "OK"
)


print("COMPLETE REPORT")
print(df)


print("\nRECORDS THAT NEED ATTENTION")
print(df[df["status"] != "OK"])


print("\nSTATUS COUNTS")
print(df.groupby("status").size())

df.to_csv("survey_report.csv", index=False)

# Creates a bar chart showing the number of records in each status.
df["status"].value_counts().plot(kind="bar")

plt.title("Survey Status Counts")
plt.xlabel("Status")
plt.ylabel("Number of datasets")


plt.tight_layout()


plt.savefig("survey_status.png")


plt.show()


